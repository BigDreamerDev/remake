from __future__ import annotations

import random
from pathlib import Path
from typing import Iterable

BASE_DIR = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".md", ".txt", ".json", ".yaml", ".yml", ".csv", ".log"}
ROOT_ALIASES = {
    "docs": BASE_DIR / "docs",
    "handbook": BASE_DIR / "docs" / "handbook",
    "records": BASE_DIR / "docs" / "records",
    "sealed": BASE_DIR / "docs" / "sealed",
    "ambient": BASE_DIR / "docs" / "ambient",
    "cards": BASE_DIR / "docs" / "index_cards",
    "index_cards": BASE_DIR / "docs" / "index_cards",
    "tides": BASE_DIR / "docs" / "records" / "tide_events",
    "hydrology": BASE_DIR / "docs" / "records" / "liminal_hydrology",
    "maritime": BASE_DIR / "docs" / "sealed" / "maritime_anomalies",
    "notes": BASE_DIR / "stillwater" / "_internal" / "handbook_notes",
}
COMMANDS = (
    "archive.index",
    "archive.read",
    "docs.cat",
    "docs.head",
    "docs.ls",
    "docs.open",
    "docs.random",
    "docs.read",
    "docs.roots",
    "docs.search",
    "docs.tree",
    "docs.view",
    "docs.where",
    "handbook.files",
    "handbook.read",
    "records.list",
    "records.read",
    "sealed.list",
    "sealed.read",
)
READER_MARKER = "__OPEN_DOC_READER__"
VARIANCE = [
    "The archive returns what it is willing to admit exists.",
    "Some paths may have moved after being named.",
    "Do not read file titles aloud near still water.",
    "Records marked sealed may still be visible to low-clearance terminals. This is not permission.",
    "If two files disagree, retain both and leave the room.",
]
DENIALS = [
    "Path rejected. The archive does not permit walking backward from here.",
    "Path rejected. That shelf faces the wrong corridor.",
    "Path rejected. The terminal refuses to index anything above its assigned waterline.",
]
EMPTY = [
    "No visible entries. This may mean the shelf is empty.",
    "No visible entries. This may mean the shelf is being watched.",
    "No visible entries. The absence has been catalogued.",
]


def _join(lines: Iterable[str]) -> str:
    return "\n".join(lines)


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _allowed_roots() -> list[Path]:
    return [path.resolve() for path in ROOT_ALIASES.values()]


def _clean_token(value: str) -> str:
    return value.strip().strip('"').strip("'").replace("\\", "/")


def _resolve(parts: list[str], default_root: str = "docs") -> tuple[Path | None, str | None]:
    raw = _clean_token(" ".join(parts).strip()) if parts else ""
    if not raw or raw in {".", "/"}:
        target = ROOT_ALIASES[default_root].resolve()
    else:
        segments = [segment for segment in raw.split("/") if segment not in {"", "."}]
        if any(segment == ".." for segment in segments):
            return None, random.choice(DENIALS)
        first = segments[0].lower() if segments else default_root
        if first in ROOT_ALIASES:
            base = ROOT_ALIASES[first]
            rest = segments[1:]
        elif first == "docs":
            base = BASE_DIR / "docs"
            rest = segments[1:]
        else:
            base = ROOT_ALIASES[default_root]
            rest = segments
        target = base.joinpath(*rest).resolve()
    roots = _allowed_roots()
    if not any(_inside(target, root) or target == root for root in roots):
        return None, random.choice(DENIALS)
    return target, None


def _visible_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS


def _iter_files(root: Path, limit: int = 2000) -> Iterable[Path]:
    if not root.exists():
        return []
    count = 0
    found: list[Path] = []
    for path in sorted(root.rglob("*")):
        if count >= limit:
            break
        if _visible_file(path):
            found.append(path)
            count += 1
    return found


def _virtual(path: Path) -> str:
    for name, root in sorted(ROOT_ALIASES.items(), key=lambda item: len(str(item[1])), reverse=True):
        resolved = root.resolve()
        try:
            rel = path.resolve().relative_to(resolved)
            return f"{name}/{rel.as_posix()}" if rel.as_posix() != "." else name
        except ValueError:
            continue
    try:
        return path.resolve().relative_to(BASE_DIR).as_posix()
    except ValueError:
        return path.name


def _read(path: Path, max_chars: int = 12000) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) <= max_chars:
        return text.rstrip()
    return text[:max_chars].rstrip() + "\n\n[output folded by archive; request a narrower file or use docs.head]"


def _format_listing(path: Path, entries: list[Path]) -> str:
    lines = [f"Archive shelf: {_virtual(path)}", ""]
    for entry in entries:
        label = "/" if entry.is_dir() else ""
        size = "" if entry.is_dir() else f" {entry.stat().st_size}b"
        lines.append(f" {entry.name}{label}{size}")
    lines.append("")
    lines.append(random.choice(VARIANCE))
    return _join(lines)


def _list(parts: list[str], default_root: str = "docs") -> str:
    path, error = _resolve(parts, default_root)
    if error:
        return error
    if not path or not path.exists():
        return random.choice(EMPTY)
    if path.is_file():
        return f"{_virtual(path)} {path.stat().st_size}b"
    entries = [entry for entry in sorted(path.iterdir(), key=lambda item: (item.is_file(), item.name.lower())) if entry.is_dir() or _visible_file(entry)]
    if not entries:
        return random.choice(EMPTY)
    return _format_listing(path, entries[:120])


def _tree(parts: list[str]) -> str:
    path, error = _resolve(parts)
    if error:
        return error
    if not path or not path.exists():
        return random.choice(EMPTY)
    limit = 90
    if parts:
        last = parts[-1]
        if last.isdigit():
            limit = max(10, min(300, int(last)))
            path, error = _resolve(parts[:-1])
            if error:
                return error
    lines = [f"Archive tree: {_virtual(path)}", ""]
    count = 0
    if path.is_file():
        return _virtual(path)
    for item in sorted(path.rglob("*"), key=lambda item: item.as_posix().lower()):
        if count >= limit:
            lines.append(" ... tree folded; too many shelves answering at once")
            break
        if item.is_dir() or _visible_file(item):
            try:
                rel = item.relative_to(path)
            except ValueError:
                rel = item
            depth = len(rel.parts) - 1
            if depth > 5:
                continue
            mark = "/" if item.is_dir() else ""
            lines.append(" " + "  " * depth + rel.name + mark)
            count += 1
    if count == 0:
        return random.choice(EMPTY)
    lines.append("")
    lines.append(random.choice(VARIANCE))
    return _join(lines)


def _head(parts: list[str], default_root: str = "docs") -> str:
    lines_count = 40
    if parts and parts[-1].isdigit():
        lines_count = max(1, min(200, int(parts[-1])))
        parts = parts[:-1]
    path, error = _resolve(parts, default_root)
    if error:
        return error
    if not path or not path.exists():
        return "Record not found. The index insists it was here this morning."
    if path.is_dir():
        return _list(parts, default_root)
    if not _visible_file(path):
        return "Record withheld. The terminal will not read that format aloud."
    text_lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    body = "\n".join(text_lines[:lines_count]).rstrip()
    suffix = "" if len(text_lines) <= lines_count else f"\n\n[showing {lines_count}/{len(text_lines)} lines; use docs.read for more]"
    return f"{_virtual(path)}\n{'-' * min(72, len(_virtual(path)))}\n{body}{suffix}"


def _cat(parts: list[str], default_root: str = "docs") -> str:
    path, error = _resolve(parts, default_root)
    if error:
        return error
    if not path or not path.exists():
        return "Record not found. Do not ask the empty shelf a second time."
    if path.is_dir():
        return _list(parts, default_root)
    if not _visible_file(path):
        return "Record withheld. The terminal will not read that format aloud."
    return f"{_virtual(path)}\n{'-' * min(72, len(_virtual(path)))}\n{_read(path)}"


def _search(parts: list[str]) -> str:
    if not parts:
        return "usage: docs.search <word or phrase>"
    limit = 25
    query_parts = parts[:]
    if query_parts[-1].isdigit():
        limit = max(1, min(80, int(query_parts[-1])))
        query_parts = query_parts[:-1]
    query = " ".join(query_parts).strip().lower()
    if len(query) < 2:
        return "Search phrase too small. The archive refuses to index dust."
    roots = [ROOT_ALIASES["docs"], ROOT_ALIASES["notes"]]
    matches: list[tuple[Path, int, str]] = []
    for root in roots:
        for path in _iter_files(root.resolve(), 4000):
            try:
                for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
                    if query in line.lower():
                        matches.append((path, number, line.strip()))
                        break
            except OSError:
                continue
            if len(matches) >= limit:
                break
        if len(matches) >= limit:
            break
    if not matches:
        return "No matching records. The search term may have been removed before indexing."
    lines = [f"Search results for: {query}", ""]
    for path, number, line in matches:
        snippet = line[:160] + ("..." if len(line) > 160 else "")
        lines.append(f" {_virtual(path)}:{number} :: {snippet}")
    lines.append("")
    lines.append(random.choice(VARIANCE))
    return _join(lines)


def _where(parts: list[str]) -> str:
    if not parts:
        return "usage: docs.where <filename fragment>"
    fragment = " ".join(parts).strip().lower()
    matches: list[Path] = []
    for root in [ROOT_ALIASES["docs"], ROOT_ALIASES["notes"]]:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if len(matches) >= 80:
                break
            if (path.is_dir() or _visible_file(path)) and fragment in path.name.lower():
                matches.append(path)
    if not matches:
        return "No shelf by that name. One shelf knocked back, but it was not a match."
    return _join(["Possible paths:", ""] + [f" {_virtual(path)}{'/' if path.is_dir() else ''}" for path in matches])


def _random(parts: list[str]) -> str:
    root, error = _resolve(parts, "docs")
    if error:
        return error
    if not root or not root.exists():
        return random.choice(EMPTY)
    files = list(_iter_files(root, 4000))
    if not files:
        return random.choice(EMPTY)
    selected = random.choice(files)
    return _head([_virtual(selected)], "docs")


def _roots() -> str:
    lines = ["Visible archive roots:", ""]
    for name in sorted(ROOT_ALIASES):
        path = ROOT_ALIASES[name]
        status = "mounted" if path.exists() else "empty/unmounted"
        lines.append(f" {name:<12} {status}")
    lines.append("")
    lines.append("Use docs.ls <root>, docs.tree <root>, docs.read <path>, docs.search <phrase>.")
    return _join(lines)


def _virtual_parent(path: Path) -> str | None:
    """Return the virtual path of the parent dir, or None if going up would
    escape every allowed root (i.e. we're already at the top of the archive)."""
    resolved = path.resolve()
    parent = path.parent.resolve()
    if parent == resolved:
        return None
    if not any(_inside(parent, root) or parent == root for root in _allowed_roots()):
        return None
    return _virtual(parent) or None


def roots_json() -> dict:
    return {
        "ok": True,
        "roots": [
            {"name": name, "exists": path.exists(), "virtual": name}
            for name, path in sorted(ROOT_ALIASES.items())
        ],
    }


def tree_json(path_arg: str | None = None) -> dict:
    parts = [path_arg] if path_arg else []
    path, error = _resolve(parts, "docs")
    if error:
        return {"ok": False, "error": error}
    if not path or not path.exists():
        return {"ok": False, "error": "Record not found. The index insists it was here this morning."}
    if path.is_file():
        return {"ok": False, "error": "Path resolves to a file; use the file endpoint."}
    entries: list[dict] = []
    for entry in sorted(path.iterdir(), key=lambda i: (i.is_file(), i.name.lower())):
        if entry.is_dir():
            entries.append({
                "name": entry.name,
                "type": "dir",
                "virtual": _virtual(entry),
            })
        elif _visible_file(entry):
            entries.append({
                "name": entry.name,
                "type": "file",
                "virtual": _virtual(entry),
                "size": entry.stat().st_size,
            })
    return {
        "ok": True,
        "virtual": _virtual(path),
        "type": "dir",
        "parent": _virtual_parent(path),
        "entries": entries,
        "note": random.choice(VARIANCE) if entries else random.choice(EMPTY),
    }


def file_json(path_arg: str) -> dict:
    parts = [path_arg] if path_arg else []
    path, error = _resolve(parts, "docs")
    if error:
        return {"ok": False, "error": error}
    if not path or not path.exists():
        return {"ok": False, "error": "Record not found. Do not ask the empty shelf a second time."}
    if path.is_dir():
        return {"ok": False, "error": "Path is a folder; use the tree endpoint."}
    if not _visible_file(path):
        return {"ok": False, "error": "Record withheld. The terminal will not read that format aloud."}
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return {"ok": False, "error": f"Record unreadable: {exc}"}
    return {
        "ok": True,
        "virtual": _virtual(path),
        "type": "file",
        "size": path.stat().st_size,
        "lines": text.count("\n") + (0 if text.endswith("\n") else 1),
        "content": text,
        "parent": _virtual(path.parent),
    }


def search_json(query: str, limit: int = 25) -> dict:
    query = (query or "").strip()
    if len(query) < 2:
        return {"ok": False, "error": "Search phrase too small. The archive refuses to index dust."}
    limit = max(1, min(80, int(limit) if str(limit).isdigit() else 25))
    needle = query.lower()
    matches: list[dict] = []
    roots = [ROOT_ALIASES["docs"], ROOT_ALIASES["notes"]]
    for root in roots:
        for path in _iter_files(root.resolve(), 4000):
            try:
                for number, line in enumerate(
                    path.read_text(encoding="utf-8", errors="replace").splitlines(),
                    start=1,
                ):
                    if needle in line.lower():
                        snippet = line.strip()
                        matches.append({
                            "virtual": _virtual(path),
                            "line": number,
                            "snippet": snippet[:200] + ("…" if len(snippet) > 200 else ""),
                        })
                        break
            except OSError:
                continue
            if len(matches) >= limit:
                break
        if len(matches) >= limit:
            break
    return {"ok": True, "query": query, "results": matches}


def _open_marker(args: list[str]) -> str:
    target = _clean_token(" ".join(args)) if args else ""
    return f"{READER_MARKER}:{target}"


def command_names() -> tuple[str, ...]:
    return tuple(sorted(COMMANDS))


def help_text(show_all: bool = False) -> str:
    base = [
        "Archive/document commands:",
        " docs.open [path]           Open the archive browser (visual reader)",
        " docs.roots                 List visible document roots",
        " docs.ls [path]             List a shelf or folder",
        " docs.tree [path] [limit]    Show a folded tree view",
        " docs.read <path>           Read a text record",
        " docs.head <path> [lines]    Read the beginning of a record",
        " docs.search <phrase>       Search visible text records",
        " docs.where <fragment>      Find paths by filename fragment",
        " docs.random [path]         Open a random visible record",
        " handbook.files             List handbook shelves",
        " handbook.read <path>       Read handbook material",
        " records.list [path]        List records shelves",
        " records.read <path>        Read records material",
        " sealed.list [path]         List sealed shelves visible to this terminal",
        " sealed.read <path>         Read visible sealed material",
    ]
    if show_all:
        base.extend([
            " docs.cat <path>            Alias of docs.read",
            " docs.view <path>           Alias of docs.read",
            " archive.index [path]       Alias of sealed.list",
            " archive.read <path>        Alias of sealed.read",
        ])
    return "\n".join(base)


def run(command: str, args: list[str], session: dict | None = None) -> str:
    cmd = command.lower()
    if cmd == "docs.open":
        return _open_marker(args)
    if cmd == "docs.roots":
        return _roots()
    if cmd == "docs.ls":
        return _list(args, "docs")
    if cmd == "docs.tree":
        return _tree(args)
    if cmd in {"docs.read", "docs.cat", "docs.view"}:
        return _cat(args, "docs")
    if cmd == "docs.head":
        return _head(args, "docs")
    if cmd == "docs.search":
        return _search(args)
    if cmd == "docs.where":
        return _where(args)
    if cmd == "docs.random":
        return _random(args)
    if cmd == "handbook.files":
        return _list(args, "handbook")
    if cmd == "handbook.read":
        return _cat(args, "handbook")
    if cmd == "records.list":
        return _list(args, "records")
    if cmd == "records.read":
        return _cat(args, "records")
    if cmd in {"sealed.list", "archive.index"}:
        return _list(args, "sealed")
    if cmd in {"sealed.read", "archive.read"}:
        return _cat(args, "sealed")
    return "The archive has no handler for that request. It may have heard you anyway."

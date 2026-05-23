/* ============================================================
   stillwater.js
   Frontend logic for comShell — calls Render backend for all
   command execution. Manages session state locally.
   ============================================================ */

const SW = (() => {

  // ── config ────────────────────────────────────────────────
  // Replace with your Render URL after deploying
  const API_BASE = "https://remake-ns80.onrender.com";

  // ── session (initialised from /api/session on load) ───────
  let SESSION = {
    rank: "Trainee",
    auth_level: 0,
    auth_key: null,
    session_id: null,
    node: null,
    banner_variant: null,
  };

  // ── local lore for the banner (rendered client-side so the
  //    page feels alive before the first API round-trip) ─────
  const LOGOS = [
`        ~                         ~
 ███████╗████████╗██╗██╗     ██╗     ██╗    ██╗ █████╗ ████████╗███████╗██████╗
 ██╔════╝╚══██╔══╝██║██║     ██║     ██║    ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
 ███████╗   ██║   ██║██║     ██║     ██║ █╗ ██║███████║   ██║   █████╗  ██████╔╝
 ╚════██║   ██║   ██║██║     ██║     ██║███╗██║██╔══██║   ██║   ██╔══╝  ██╔══██╗
 ███████║   ██║   ██║███████╗███████╗╚███╔███╔╝██║  ██║   ██║   ███████╗██║  ██║
 ╚══════╝   ╚═╝   ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                         F O U N D A T I O N`,
`        _________________________________________________
       /                                                 \\
      /       S T I L L W A T E R   F O U N D A T I O N   \\
     /_____________________________________________________\\
             ||        ||        ||        ||        ||
             ||        ||        ||        ||        ||
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              internal systems // quiet-water branch`,
`             .-------------------------------.
             |   STILLWATER FOUNDATION       |
             |   shared libraries terminal   |
             '---------------.---------------'
                             / \\
                       ~    /___\\    ~
                           /_____\\
                          /_______\\
                water remembers its container`,
  ];

  const BOOT_LINES = [
    "Session opened. You are not the first person to open a session from this terminal today.\n There is no record of anyone else opening a session from this terminal today.",
    "Archive index loaded. 14 documents are addressed to you.\n You have not been employed here long enough for 14 documents to exist.",
    "Corridor geometry nominal. East wing geometry has been reclassified as Not Applicable.\n The third survey team has not yet been asked for its findings.",
    "Pattern Integrity: NOMINAL. This status has not changed in 847 days.\n The last time it changed, four rooms on Floor -3 were sealed. They remain sealed.",
    "Personnel roster loaded. 3 entries are flagged STILL_ON_SITE despite offboarding confirmation.\n Offboarding was confirmed by the employees themselves.",
    "Building ྾2 mounted. Class-IV designation means the building is no longer changing.\n It does not mean the building has stopped.",
    "Terminal ready. Seventeen previous sessions were opened from this terminal.\n Twelve were closed normally. The other five remain ONGOING.",
  ];

  function rc(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
  function ri(a, b) { return Math.floor(Math.random() * (b - a + 1)) + a; }

  // ── build the banner string ────────────────────────────────
  function banner() {
    const s = SESSION;
    return rc(LOGOS)
      + "\n" + "=".repeat(78)
      + "\n STILLWATER FOUNDATION — comShell v4.9.1 "
      + "\n INTERNAL USE ONLY / LOW-CLEARANCE PUBLIC TERMINAL "
      + "\n" + "=".repeat(78)
      + `\n Session ID : ${s.session_id || "pending"}`
      + "\n User       : anon"
      + `\n Rank       : ${s.rank}`
      + `\n Node       : ${s.node || "unknown"}`
      + `\n Variant    : ${s.banner_variant || "—"}`
      + "\n Pattern Integrity .................. NOMINAL"
      + "\n" + "-".repeat(78)
      + "\n " + rc(BOOT_LINES)
      + "\n Type 'help' for a partial list of permitted commands. Use 'help all' for more noise."
      + "\n Archive access is mounted read-only. Some shelves answer out of order.\n";
  }

  // ── fetch a fresh session from the server ─────────────────
  async function initSession() {
    try {
      const res = await fetch(`${API_BASE}/api/session`);
      if (!res.ok) throw new Error("non-200");
      const data = await res.json();
      Object.assign(SESSION, data);
    } catch (_) {
      // fallback: generate locally so the terminal still boots
      SESSION.session_id    = `SW-${ri(10000,99999)}-${ri(100,999)}`;
      SESSION.node          = rc(["Δ-04","Δ-04","྾2-A","North Archive","West Stair"]);
      SESSION.banner_variant = ri(100, 999);
    }
  }

  // ── verify the comShell operator phrase ────────────────────
  async function verifyComshell(password) {
    // ensure we have a session (the sig is bound to session_id)
    if (!SESSION.session_id) await initSession();

    const res = await fetch(`${API_BASE}/api/auth/comshell`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ password, session: SESSION }),
    });

    let data = {};
    try { data = await res.json(); } catch (_) { /* tolerate empty */ }
    if (data.session) Object.assign(SESSION, data.session);
    return { ok: !!data.ok, message: data.message || (res.ok ? "" : `server returned ${res.status}`) };
  }

  function isVerified() {
    return !!SESSION.comshell_verified && !!SESSION.comshell_sig;
  }

  // ── send a command to the server ──────────────────────────
  async function run(raw) {
    // local intercepts — no round-trip needed
    const trimmed = raw.trim().toLowerCase();
    if (trimmed === "clear" || trimmed === "cls") return "__CLEAR__";
    if (trimmed === "exit"  || trimmed === "quit") return "__EXIT__";

    const res = await fetch(`${API_BASE}/api/command`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ raw, session: SESSION }),
    });

    if (res.status === 403) {
      // session lost verification — surface to the UI
      const data = await res.json().catch(() => ({}));
      if (data.session) Object.assign(SESSION, data.session);
      const err = new Error("unverified");
      err.code = "UNVERIFIED";
      throw err;
    }

    if (!res.ok) {
      throw new Error(`server returned ${res.status}`);
    }

    const data = await res.json();

    // sync session state back (rank elevations, auth_level, etc.)
    if (data.session) Object.assign(SESSION, data.session);

    return data.output ?? "";
  }

  // ── warm the server (fire-and-forget on page load) ─────────
  async function warmUp() {
    try {
      await fetch(`${API_BASE}/health`);
    } catch (_) { /* silent */ }
  }

  return { banner, run, initSession, warmUp, verifyComshell, isVerified, session: () => ({ ...SESSION }) };
})();

# Clause 11.3 — Restricted Invocations

## Subsection: Restricted Invocations

Certain commands within the comShell environment are restricted to
employees of a designated rank. The list of restricted commands is
maintained by the Pattern Integrity Working Group and is updated as
part of the quarterly handbook revision cycle.

### Authentication

Invocation of a restricted command requires submission of a valid
authentication code via the `auth <code>` command. The authentication
code is the lower-case rendering of the **required rank designation**
itself.

The required rank for the current edition is determined by
`stillwater.handbook.RESTRICTED_RANK_INDEX`, resolved against the
canonical rank registry in `stillwater._internal.ranks`.

### Logged Events

The following events are logged automatically:

- Invocation of a restricted command without prior authentication.
- Submission of an incorrect authentication code.
- Repeated submission of the same incorrect authentication code
  within a single session.

Logged events are reviewed by the Office of Inherited Silences. Most
logged events do not result in further correspondence.

### Decoding

Following successful authentication, restricted commands resolve
their internal references against the appropriate cipher modules
(e.g. `stillwater._internal.repository`). The decoder for these
modules requires the active authentication code as its key. **The
authentication code is not stored beyond the duration of the session.**

---

*See also: Clause 6.19 (Titan-Class), Clause 13.4 (Departmental
Dissolution).*

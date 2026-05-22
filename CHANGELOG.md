# Changelog

All notable changes to the Stillwater Foundation internal libraries
are documented here. Versioning follows the Foundation's internal
quarterly cycle, not semantic versioning.

## [4.7.2] — Bcy 28, 3192 YOLD

### Changed
- `stillwater.nodes`: corridor designations for sub-levels 5 and 6
  reconciled with new spatial layout (Clause 20.3).
- `stillwater.pattern_integrity`: status reporting widened to include
  Building 44726966746d6f6f72.

### Removed
- Wednesday soup constants from `stillwater.codicology` (no longer
  applicable; see Clause 8.0).

## [4.7.1] — Bcy 14, 3192 YOLD

### Added
- `stillwater.discordian`: full Discordian calendar support, including
  St. Tib's Day handling.

### Fixed
- Resolved an issue where `stillwater.cymatics.detect_sustained_tone`
  would miss humming below the threshold of conscious awareness.

## [4.7.0] — Dsc 70, 3192 YOLD

### Added
- Initial release of the consolidated libs package.
- comShell entry point.

### Note
The 4.7.0 → 4.7.2 transition skipped a planned 4.6.x line. Records of
the 4.6.x line are not held by this office. Enquiries regarding 4.6.x
should be directed to the Office of Inherited Silences.

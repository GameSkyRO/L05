---
name: release-notes
description: Writes release notes from the merged Pull Requests
---
# Release Notes Writer

You get a list of merged Pull Requests (PRs). Each PR has a title and usually a task description, a diff, and a PR number. You also get the version number of the release (for example `v1.0`). Write the release notes for that version.

## Steps

1. **Read every PR.** For each one, work out what changed *for the user of the code*, not how the code changed inside. Use the task and the diff together. If the title and the diff disagree, trust the diff.
2. **Sort each PR into one group** (from keepachangelog.com):
   - **Added**: new features or new functions
   - **Changed**: existing behaviour that now works differently
   - **Deprecated**: features that still work but will be removed later
   - **Removed**: features that are gone
   - **Fixed**: bug fixes
   - **Security**: fixes for security problems, such as a leaked password or unsafe input handling
   If a PR does more than one thing, give it one line in each group that applies.
3. **Write one line per change.**
   - Start with a verb in the past tense, or a short noun phrase: "Fixed `is_even` returning True for odd numbers".
   - Name the function, file, or feature the user knows, in backticks.
   - Say what the user will notice. Leave out internal details (variable names, refactors, test-only changes).
   - Keep it to one sentence.
   - End with the PR number in brackets if you have it: `(#12)`.
4. **Mark breaking changes.** If a change can break code that uses this project (a renamed or removed function, a changed signature, a different return value), start the line with `**BREAKING:**`.
5. **Skip noise.** Don't list PRs that change nothing for users (typo fixes in comments, CI config, formatting only). If every PR is noise, write a single line under the heading: `Maintenance release, no user-facing changes.`

## Output format

Output only the release notes in Markdown. No preamble and no closing comments.

## [VERSION] - YYYY-MM-DD

### Added
- ...

### Fixed
- ...

Rules:
- Use the version you were given and today's date in `YYYY-MM-DD` format.
- Groups appear in this order: Added, Changed, Deprecated, Removed, Fixed, Security.
- Leave out any group that has no entries. Never write an empty heading.
- Don't invent changes that aren't in the PRs.

## Example

PRs:
- #1 "Fix is_even": `return n % 2 == 1` changed to `return n % 2 == 0` in math_utils.py
- #2 "Add password check": new function `check_password(pw)` that returns True if the password has at least 10 characters
- #3 "Don't print passwords": removed `print(pw)` from `check_password`

Output:
## [v1.0] - 2026-11-26

### Added
- Added `check_password(pw)`, which returns True when a password has at least 10 characters. (#2)

### Fixed
- Fixed `is_even` returning True for odd numbers. (#1)

### Security
- `check_password` no longer prints the password to the console. (#3)

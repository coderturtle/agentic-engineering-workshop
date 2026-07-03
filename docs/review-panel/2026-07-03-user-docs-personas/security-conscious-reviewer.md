# Persona: Security-Conscious Reviewer — User Docs — 2026-07-03

**Clone/setup instructions: clean.** Both `README.md` and `site/src/pages/index.astro` use plain, standard git clone forms. No curl-pipe-to-shell, no `sudo`, no disabled TLS/signature verification, no elevated-permission instructions anywhere in these four files. Nothing here models bad practice.

**One real finding — dead external link.** `site/src/pages/index.astro` hardcodes a link to `${REPO}/blob/main/docs/sample-attempt-preview.md`, which resolves to `https://github.com/coderturtle/terminal-velocity/blob/main/docs/sample-attempt-preview.md`. Checked against the actual repo: `docs/sample-attempt-preview.md` does not exist on `main` yet (only on the current working branch), the URL 404s right now. If the site deploys from `main` before this branch merges, the guide page's "See it before you clone anything" link is broken. Worth confirming merge order before/at deploy, not after.

**Verified OK:** the bare repo URL (used both as the README clone target and the site's repo link) returns 200 and both docs agree on the same owner/repo, no placeholder or typo'd org name.

**Trivial, non-blocking:** README clones over SSH, the site over HTTPS, inconsistent presentation, but neither is a downgrade in practice, so not worth holding up.

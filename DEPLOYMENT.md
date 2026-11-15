# GitHub Pages deployment checklist

**Repository:** `David-Somers-Jupiter-6/chatgpt-universal-iphone-diagnostic`

**Expected URL (not live until deployed):** https://david-somers-jupiter-6.github.io/chatgpt-universal-iphone-diagnostic/

## GitHub account actions still required

- [ ] Create a new public GitHub repository named `chatgpt-universal-iphone-diagnostic` under `David-Somers-Jupiter-6`.
- [ ] Add all project files to `main`. When uploading from the GitHub browser UI, ensure the hidden `.github/workflows/` directory is included; uploading the ZIP archive without extracting it is insufficient.
- [ ] Open **Settings → Pages**, and choose **GitHub Actions** as the publishing source.
- [ ] Allow GitHub Actions in repository settings if the organisation/account has restricted them.
- [ ] Check the **Actions** tab for a successful Pages deployment and verify the published URL.
- [ ] Visit the HTTPS URL and run the diagnostic in Safari and in Chrome on real iPhones.

## Repository files and purposes

| File | Purpose |
| --- | --- |
| `index.html` | Entire standalone HTML/CSS/JavaScript diagnostic application |
| `404.html` | Friendly not-found page with a link back to the diagnostic |
| `.nojekyll` | Prevent unwanted Jekyll processing of static website assets |
| `.github/workflows/deploy-pages.yml` | Validate the site, then deploy it automatically after pushes to `main` |
| `scripts/validate_site.py` | Verify required test elements, website links and standalone HTML |
| `scripts/check_javascript.py` | Extract scripts and verify syntax with Node.js |
| `launcher/Open_Diagnostic_HTTPS.html` | Local redirect launcher with a link fallback |
| `README.md` | Project overview and installation instructions |
| `DEPLOYMENT.md` | Detailed deployment and testing checklist |
| `.gitignore` | Keep transient/local output out of source control |

## GitHub Pages actions workflow

The workflow fires on push to `main` or manual dispatch. It performs source checks and JS syntax checks, uploads only `index.html`, `404.html` and `.nojekyll`, and deploys through the Pages environment. Deployment requires repository Pages settings to be enabled and GitHub Actions set as the source.

If Pages is not enabled, `configure-pages` or `deploy-pages` can fail. The workflow cannot create a new GitHub repository, bypass account permissions or guarantee GitHub Pages availability.

## Testing

1. Open the published HTTPS link directly in Safari.
2. Confirm **JavaScript: running** appears green and the page shows HTTPS active.
3. Select **Run Test**; confirm results contain viewport and CSS height measurements and that the run finishes.
4. Check the four coloured bars and ruler, and the yellow visual-viewport marker.
5. Record the screenshot from the top of the page, without scrolling.
6. Scroll down and up, then repeat in landscape.
7. Open the site directly in Chrome and repeat.
8. Test the launcher from iPhone Files; some viewers prevent meta refresh, so confirm the fallback link can be used.
9. Copy and review the report. Device/browser information cannot always be obtained and may show UNAVAILABLE or WARNING legitimately.

## Troubleshooting

**404 on site:** check repository name, main branch and Actions deployment URL; ensure `index.html` is at deployment root.

**GitHub Pages workflow failing:** confirm Pages source is GitHub Actions and workflow permissions allow Pages deployments; inspect the failed job.

**JavaScript: NOT running:** likely file preview; open the direct hosted URL in Safari or Chrome. If it occurs on the HTTPS website, inspect error logs and verify the latest `index.html` was deployed.

**Safari and Chrome are not switching automatically:** webpages cannot force iOS to select a specific browser. Launch the same URL manually in each.

**Missing yellow marker:** check that scripts execute; in file previews only the approximate small-viewport marker may appear.

**Browser heights are different:** `vh`, `svh`, `dvh` and `lvh` have different semantics. Differences alone are not failures.

## Privacy and security

This is a public website. Do not add confidential user data, internal organisational information, tokens or passwords to the repository. Reports remain on device unless a user copies and shares them. Ordinary hosting access logs remain subject to the host's policies.

Official GitHub documentation:
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
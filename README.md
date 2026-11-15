# ChatGPT Universal iPhone HTML Display and Browser Diagnostic Test — V 2.0

A standalone, privacy-conscious HTML diagnostic for testing browser viewport rendering across **all iPhone screen sizes**, Safari, Chrome and other iOS browsers where supported.

## Deployment state

**Repository created and project deployment in progress — GitHub Pages publishing is not yet confirmed.** The anticipated website address is:

`https://david-somers-jupiter-6.github.io/chatgpt-universal-iphone-diagnostic/`

This URL will be usable only after the repository has been created, the files uploaded, GitHub Pages enabled, and a successful deployment completed.

## Features

- Four full-height coloured comparison bars: `100vh`, `100svh`, `100dvh`, `100lvh`.
- A 50-CSS-pixel vertical ruler, central diagnostic panel and yellow visible-bottom marker.
- Browser identification (best-effort), screen and visual-viewport measurements, JavaScript/CSS support checks, safe-area and layout detection.
- 50+ diagnostic entries depending on available APIs; independent tests and PASS / FAIL / WARNING / UNAVAILABLE results.
- Screen rotation, viewport scrolling, keyboard/zoom and accessibility checks, with explicit manual screenshot checks.
- **No-script fallback:** if the iPhone file preview blocks JavaScript, show an explanatory message and a direct HTTPS link.
- Automatic local-to-HTTPS redirection **when JavaScript runs** and a fixed HTTPS launcher page with HTML meta refresh and clickable fallback.
- No external JavaScript, CDNs, fonts, trackers or results-upload endpoints.

> The website receives ordinary server requests, so GitHub may record usual access logs. The application itself does not transmit test results.

## Publish via GitHub Pages

1. Create a new **public** repository called `chatgpt-universal-iphone-diagnostic` in the GitHub account **David-Somers-Jupiter-6**. Do not put confidential information in this repository.
2. Upload the **contents** of this project folder to the repository root on the `main` branch. Keep `.github/workflows/deploy-pages.yml`, `scripts/`, `index.html`, `404.html` and `.nojekyll`.
3. Go to **Settings → Pages → Build and deployment → Source** and select **GitHub Actions**.
4. Open the **Actions** tab and confirm that **Deploy iPhone Diagnostic to GitHub Pages** completed successfully. If it did not run, choose **Run workflow**.
5. Visit `https://david-somers-jupiter-6.github.io/chatgpt-universal-iphone-diagnostic/` in Safari and Chrome, select **Run Test**, and verify that **JavaScript: running** is green.

See [DEPLOYMENT.md](DEPLOYMENT.md) for validation, limitations and troubleshooting.

## Automatic HTTPS launcher

After publishing, `launcher/Open_Diagnostic_HTTPS.html` is a separate local file intended to attempt an HTML meta-refresh redirect and, if blocked, provide a direct link. The diagnostic `index.html` also has a configured HTTPS URL for JavaScript-assisted redirection from `file:` and `http:` contexts.

A file preview that blocks scripts or redirect/navigation can **never** be reliably forced by HTML alone to open Safari or Chrome. In that situation paste the HTTPS address directly into the chosen browser.

## Tests

Run `python3 scripts/validate_site.py` and `python3 scripts/check_javascript.py` (requires Node.js). Local visual browser tests should be treated as simulations until tests run on real iPhones.

## Scope

The tool does not change device configuration, install updates, discover exact iPhone model reliably, or validate the pixels covered by the iOS system interface. Diagnosed browser height discrepancies are not automatically failures.
# Guided iPhone diagnostic testing — V 2.0

Website: https://david-somers-jupiter-6.github.io/chatgpt-universal-iphone-diagnostic/

## Guided workflow

1. Open the HTTPS website in Safari or Chrome and tap **Run Test**.
2. After automated checks finish, take a portrait screenshot **at the top without manually scrolling**. Visually inspect the left ruler, four height bars, central panel and yellow bottom marker. Select **Looks correct** or **Problem seen**.
3. Scroll at least 200 CSS px down, then return near the top. The application can observe the scroll but **cannot tell whether the screen looks correct**. Record the visual outcome.
4. Rotate into landscape and tap **Run Test** again. The page can detect orientation and confirm a landscape test run; visually confirm the page's appearance.
5. Open the website separately in Safari (if initially using Chrome), run the test, and confirm it. Webpages cannot force-open another browser, nor correlate independent browser sessions without a server.
6. Pinch to zoom or tap **Larger Text**. The page can observe some zoom and text changes, but requires human visual review.
7. **Optional:** tap **Open Keyboard** and close it. The application may detect a visual viewport reduction; visual correctness still needs user confirmation.
8. When all **five required** actions have been recorded, read the final next-action prompt. The keyboard check is optional.

## Screenshot evidence

Use **Choose screenshots** and select PNG, JPG, HEIC or WebP images from the device. The application accepts up to **8** images, up to **12 MB each** and **40 MB in total**. Files remain in browser memory until the page is closed or refreshed; there is no backend upload.

- **Copy Report** copies **text only**. It cannot reliably include several images in a single iPhone clipboard operation.
- **Download Evidence ZIP** creates a local ZIP containing `Diagnostic_Report.txt` and selected screenshot files. The ZIP is assembled without external libraries or requests.
- **Share Evidence…** uses the platform share sheet where supported. Sharing is only initiated on the user's tap, and the destination is chosen by the user. If unsupported, export the ZIP and share it manually.
- GitHub Pages is a **static site** and does not accept direct file uploads. Implementing a central evidence inbox would require a separate backend, authentication, storage policy and consent.

## What can be observed automatically?

- Successful JavaScript and browser-API checks
- Scroll down and back near the top
- Portrait or landscape orientation, and a test run in landscape
- Pinch zoom through `visualViewport.scale`, where exposed, or use of the Larger Text button
- Keyboard-related visual viewport change, where measurable

The browser **cannot** detect screenshot capture, inspect the screenshot pixels, guarantee visual correctness, know that another browser was tested independently, or automatically access the camera roll. None of those steps is silently claimed complete.

## Privacy and limitations

All diagnostic data stays on the device unless the user expressly downloads or shares it. Screenshots may expose personal or device information; review them before sharing. The webpage does not upload, store remotely, email or transmit files. A physical iPhone Safari and Chrome verification is still required, beyond automated desktop viewport simulation.

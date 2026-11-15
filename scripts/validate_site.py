#!/usr/bin/env python3
"""Validate the core HTML diagnostic, HTTPS fallback, and deployment files."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
html=(ROOT/'index.html').read_text(encoding='utf-8')
checks={
    'standalone HTML entrypoint': '<!DOCTYPE html>' in html or '<!doctype html>' in html,
    'mobile viewport': 'viewport-fit=cover' in html,
    'no-script help': '<noscript>' in html and 'preview-help' in html,
    'JavaScript indicator': 'id="js-indicator"' in html,
    'viewport-height bars': all('id="bar-'+v+'"' in html for v in ['vh','svh','dvh','lvh']),
    'center diagnostic panel': 'id="central-panel"' in html,
    'left ruler': 'id="ruler"' in html,
    'yellow viewport marker': 'id="bottom-marker"' in html and 'Bottom of visible screen' in html,
    'preview-only fallback marker': 'preview-edge-marker' in html,
    'run test button': 'id="run-btn"' in html,
    'copy report button': 'id="copy-btn"' in html,
    'visual viewport measurement': 'window.visualViewport' in html,
    'browser identification': 'CriOS' in html and 'FxiOS' in html,
    'static hosted website link': 'href="https://david-somers-jupiter-6.github.io/chatgpt-universal-iphone-diagnostic/"' in html,
    'HTTPS launcher': (ROOT/'launcher'/'Open_Diagnostic_HTTPS.html').is_file(),
    'GitHub Pages workflow': (ROOT/'.github'/'workflows'/'deploy-pages.yml').is_file(),
    'no external stylesheets': not re.search(r'<link[^>]+rel=["\']stylesheet',html,re.I),
    'no remote JavaScript': not re.search(r'<script[^>]+src=',html,re.I),
}
for name,ok in checks.items():
    print(('PASS' if ok else 'FAIL')+' '+name)
assert all(checks.values()),'Website validation failed'
print(f'All {len(checks)} static deployment checks passed.')

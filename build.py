"""Builds the two demo pages next to it from dashboard_src.html, with the fonts embedded so they run offline.
  meerkat_vision.html   VISION · simulated: the city concept (replay, guided presentation, analysis)
  meerkat_today.html    TODAY · real: the 3 lab sensors, real measurements
Run: python3 build.py"""
import base64, os
here = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(here, "dashboard_src.html")).read()
css = "<style>\n/* IBM Plex + Barlow Condensed (SIL OFL 1.1), embedded so the console looks the same offline */\n"
for fam, w, f in [("IBM Plex Sans", 400, "ibm-plex-sans-latin-400-normal.woff2"), ("IBM Plex Sans", 600, "ibm-plex-sans-latin-600-normal.woff2"),
                  ("IBM Plex Sans Condensed", 600, "ibm-plex-sans-condensed-latin-600-normal.woff2"),
                  ("Barlow Condensed", 600, "barlow-condensed-latin-600-normal.woff2"), ("Barlow Condensed", 700, "barlow-condensed-latin-700-normal.woff2"),
                  ("IBM Plex Mono", 400, "ibm-plex-mono-latin-400-normal.woff2"), ("IBM Plex Mono", 500, "ibm-plex-mono-latin-500-normal.woff2")]:
    b = base64.b64encode(open(os.path.join(here, f), "rb").read()).decode()
    css += f'@font-face{{font-family:"{fam}";font-weight:{w};font-style:normal;font-display:swap;src:url(data:font/woff2;base64,{b}) format("woff2")}}\n'
css += "</style>"
page = s.replace("<!--FONTS-->", css)
T = "MEERKAT SENTRY – Operator Console"
out = {
    "meerkat_vision.html": ('<script>window.MS_EDITION="vision"</script>', "MEERKAT SENTRY – Vision (simulated)"),
    "meerkat_today.html": ('<script>window.MS_EDITION="today";window.MS_VIEW="lab"</script>', "MEERKAT SENTRY – Today (real)"),
}
for name, (view, title) in out.items():
    open(os.path.join(here, name), "w").write(page.replace("<!--VIEW-->", view).replace(T, title))
print("built", ", ".join(out))

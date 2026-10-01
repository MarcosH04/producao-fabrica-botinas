"""Gera index.html embutindo as fotos de img/ como data URIs."""
import base64, json, pathlib
here = pathlib.Path(__file__).parent
imgs = {p.stem: "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode() for p in sorted((here / "img").glob("*.jpg"))}
html = (here / "template.html").read_text(encoding="utf-8")
html = html.replace("{{IMGJSON}}", json.dumps(imgs))
for k, v in imgs.items():
    html = html.replace("{{" + k + "}}", v)
(here / "index.html").write_text(html, encoding="utf-8")
print(f"index.html: {len(html)//1024} KB")

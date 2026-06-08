# InstancedDungeons Documentation Site

This repository contains only the public documentation site for InstancedDungeons.

## Local Preview

```powershell
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Then open:

```text
http://127.0.0.1:8000
```

## GitHub Pages

Every push to `main` publishes the site to GitHub Pages through the workflow in `.github/workflows/docs.yml`.

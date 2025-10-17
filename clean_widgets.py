import nbformat
p = "main.ipynb"
nb = nbformat.read(p, as_version=4)
nb.metadata.pop("widgets", None)
for c in nb.cells:
    c.get("metadata", {}).pop("widgets", None)
nbformat.write(nb, p)
print(f"✅ Cleaned widget metadata: {p}")

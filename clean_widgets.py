import nbformat
p = "main_completed.ipynb"  # <-- change if your notebook name differs
nb = nbformat.read(p, as_version=4)

# Remove the broken top-level widget metadata
nb.metadata.pop("widgets", None)

# Also clean widget metadata from each cell
for c in nb.cells:
    c.get("metadata", {}).pop("widgets", None)

nbformat.write(nb, p)
print(f"✅ Cleaned widget metadata: {p}")

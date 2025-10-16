python - << "PY"
import nbformat, sys, os
nb_path = "main_completed_fixed_v2.ipynb"  # <-- change if needed
nb = nbformat.read(nb_path, as_version=4)

nb.metadata.pop("widgets", None)
for c in nb.cells:
    c.get("metadata", {}).pop("widgets", None)

nbformat.write(nb, nb_path)
print("Cleaned widget metadata:", nb_path)
PY

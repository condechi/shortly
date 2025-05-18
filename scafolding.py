import os

files = {
    "run.py": """import os
from app import create_app
# …etc…""",
    "app/__init__.py": """import os
from flask import Flask
# …etc…""",
    # add all the other paths and their contents here…
}

for path, content in files.items():
    full = os.path.join("shortly", path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print("Wrote", full)

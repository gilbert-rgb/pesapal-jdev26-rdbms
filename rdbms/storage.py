import json
import os

DATA_DIR = "data"

def save_table(table_name, data):
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, f"{table_name}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_table(table_name):
    path = os.path.join(DATA_DIR, f"{table_name}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)

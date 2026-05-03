# state.py
import os

STATE_FILE = "data/state.txt"

def get_last_id():
    if not os.path.exists(STATE_FILE):
        return 0
    with open(STATE_FILE) as f:
        return int(f.read())

def save_last_id(last_id):
    os.makedirs("data", exist_ok=True)
    with open(STATE_FILE, "w") as f:
        f.write(str(last_id))
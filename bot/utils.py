import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "database.json")

if not os.path.exists(DB_PATH):
    with open(DB_PATH, 'w') as f:
        json.dump({}, f, indent=2)

def load_db():
    with open(DB_PATH, 'r') as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, 'w') as f:
        json.dump(data, f, indent=2)

def add_user(user_id):
    db = load_db()
    if str(user_id) not in db:
        db[str(user_id)] = {"api_id": None, "api_hash": None, "phone": None, "session": None}
        save_db(db)

def set_user_data(user_id, key, value):
    db = load_db()
    if str(user_id) not in db:
        add_user(user_id)
    db[str(user_id)][key] = value
    save_db(db)

def get_user_data(user_id):
    db = load_db()
    return db.get(str(user_id), None)

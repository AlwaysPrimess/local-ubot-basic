import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.json')
OWNER_ID = 6976551745  # ID Owner

def load_db():
    if not os.path.exists(DB_PATH):
        save_db({})
    with open(DB_PATH, 'r') as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, 'w') as f:
        json.dump(data, f, indent=2)

def add_user(user_id):
    db = load_db()
    if str(user_id) not in db:
        db[str(user_id)] = {
            "status": "free",
            "api_id": None,
            "api_hash": None,
            "session": None
        }
        save_db(db)

def set_user_data(user_id, key, value):
    db = load_db()
    if str(user_id) not in db:
        add_user(user_id)
        db = load_db()
    db[str(user_id)][key] = value
    save_db(db)

def get_user(user_id):
    db = load_db()
    return db.get(str(user_id), None)

from .db_file import load_db


db = load_db()
for key in db:
    print(key, '=>\n  ', db[key])
print(db['sue']['name'])

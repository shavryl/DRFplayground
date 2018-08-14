from .db_file import load_db, store_db


db = load_db()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
store_db(db)

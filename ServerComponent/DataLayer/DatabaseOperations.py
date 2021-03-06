from DataLayer import DatabaseConnection
from Utils.DatabaseAspect import query_aspect, insert_aspect

db = DatabaseConnection.DatabaseConnection()
conn = db.getInstance()


def get_next_id():
    next_id = conn.execute('SELECT MAX(Id) FROM SocialMediaPosts').fetchone()[0]
    if next_id is None:
        next_id = 0
    return next_id + 1


@query_aspect
def get_all():
    db = DatabaseConnection.DatabaseConnection()
    conn = db.getInstance()
    if conn is None:
        return "Bad connection"
    try:
        result = conn.execute("Select * FROM SocialMediaPosts")
    except Exception as e:
        print(e)
    return result


@insert_aspect
def insert_entry(params):
    insert_statement = "INSERT INTO SocialMediaPosts VALUES (?,?,?,?,?,?,?,?,?,?)"
    conn.execute(insert_statement, params)
    conn.commit()


def delete_entry(entry_id):
    delete_statement = "DELETE From SocialMediaPosts WHERE Id=?"
    params = (entry_id,)
    cur = conn.cursor()
    cur.execute(delete_statement, params)
    conn.commit()

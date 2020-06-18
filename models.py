import sqlite3 as sql

def create_post(n, c):
    """
    c - content
    n - name
    """
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('insert into post (postName, postContent) values(?,?)', (n, c))
    conn.commit()
    conn.close()

def get_post():
    global posts

    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('select * from post')
    posts = cursor.fetchall()
    return posts

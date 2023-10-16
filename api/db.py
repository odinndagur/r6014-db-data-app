import sqlite3

def init_db():
    pass

def search_db(query=''):
    if not query:
        with sqlite3.connect('r6014-fts.sqlite3') as db:
            db.row_factory = sqlite3.Row
            cursor = db.execute('''
                SELECT * FROM video_search GROUP BY video_url
            ''')
            result = [dict(row) for row in cursor.fetchall()]
            return result
    with sqlite3.connect('r6014-fts.sqlite3') as db:
        db.row_factory = sqlite3.Row
        cursor = db.execute('''
            SELECT * FROM video_search WHERE video_search MATCH ? GROUP BY video_url
        ''',[(query)])
        result = [dict(row) for row in cursor.fetchall()]
        return result
        pass
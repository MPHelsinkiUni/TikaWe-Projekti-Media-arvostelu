import db

def add_item(title, username, user_id, review_body, stars, work, imdb_snippet):
    sql = """INSERT INTO reviews (title, poster, poster_id, review_body, stars, work, imdb_snippet) 
            VALUES (?, ?, ?, ?, ?, ?, ?)"""
    
    db.execute(sql, [title, username, user_id, review_body, stars, work, imdb_snippet])
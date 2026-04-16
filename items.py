import db
import datetime

def add_item(title, username, user_id, review_body, stars, work, imdb_snippet):
    sql = """INSERT INTO reviews (title, poster, poster_id, review_body, stars, work, time_posted, imdb_snippet) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
    time_posted = datetime.datetime.now()
    
    db.execute(sql, [title, username, user_id, review_body, stars, work, time_posted, imdb_snippet])

def get_items():
    sql = """SELECT id, title, poster, stars, imdb_snippet FROM reviews ORDER BY time_posted DESC LIMIT 5"""
    return db.query(sql)
    # Ideally, there should be work as well, but for the purposes of debugging, we do not do this.

def get_item(item_id):
    sql = """SELECT reviews.id,
                    reviews.title,
                    reviews.poster,
                    reviews.poster_id,
                    reviews.review_body,
                    reviews.stars,
                    reviews.work,
                    reviews.time_posted,
                    reviews.imdb_snippet,
                    users.id user_id,
                    users.username,
                    users.assignment_role
             FROM reviews, users
             WHERE reviews.poster_id = users.id AND
                   reviews.id = ?"""
    result = db.query(sql, [item_id])
    if result:
        return result[0]
    else:
        return None

def update_item(item_id, title, review_body, stars, work, imdb_snippet):
    sql = """UPDATE reviews SET title = ?,
                                review_body = ?,
                                stars = ?,
                                work = ?,
                                imdb_snippet = ?
                            WHERE id = ?"""
    db.execute(sql, [title, review_body, stars, work, imdb_snippet, item_id])

def remove_item(item_id):
    sql = """DELETE FROM reviews WHERE id = ?"""
    db.execute(sql, [item_id])

def search_review(query):
    sql = """SELECT id, title, poster 
             FROM reviews
             WHERE title LIKE ? OR review_body LIKE ?
             ORDER BY time_posted DESC"""
    x = "%" + query + "%"
    return db.query(sql, [x, x])
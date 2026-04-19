import db
import datetime

def add_item(title, username, user_id, review_body, stars, work, imdb_snippet, classes):
    # TABLE review
    sql = """INSERT INTO reviews (title, poster, poster_id, review_body, stars, work, time_posted, imdb_snippet) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
    time_posted = datetime.datetime.now()
    db.execute(sql, [title, username, user_id, review_body, stars, work, time_posted, imdb_snippet])

    # Extract last inserted id
    item_id = db.last_insert_id()

    # TABLE categorisation
    sql = """INSERT INTO categorisation (review_id, title, value) VALUES (?, ?, ?)"""
    for title, value in classes:
        db.execute(sql, [item_id, title, value])

def get_items():
    sql = """SELECT id, title, poster, poster_id, stars, imdb_snippet FROM reviews ORDER BY time_posted DESC LIMIT 5"""
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
    
def get_items_by_user(user_id):
    sql = """SELECT id, title FROM reviews WHERE id = ? ORDER BY id DESC"""
    return db.query(sql, [user_id])

def update_item(item_id, title, review_body, stars, work, imdb_snippet, classes):
    sql = """UPDATE reviews SET title = ?,
                                review_body = ?,
                                stars = ?,
                                work = ?,
                                imdb_snippet = ?
                            WHERE id = ?"""
    db.execute(sql, [title, review_body, stars, work, imdb_snippet, item_id])

    sql = """DELETE FROM categorisation WHERE item_id = ?"""
    db.execute(sql, [item_id])

    # TABLE categorisation
    sql = """INSERT INTO categorisation (review_id, title, value) VALUES (?, ?, ?)"""
    for title, value in classes:
        db.execute(sql, [item_id, title, value])

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

def get_classes(item_id):
    sql = """SELECT title, value FROM categorisation WHERE review_id = ?"""
    return db.query(sql, [item_id])

def get_all_classes():
    sql = """SELECT title, value FROM class ORDER BY id"""
    classes = db.query(sql)

    classdict = {}
    for title, value in classes:
        classdict[title] = []
    for title, value in classes:
        classdict[title].append(value)

    return classdict

def add_comment(title, comment_body, username, user_id, root_id, root_title):
    sql = """INSERT INTO comments 
            (comment_title, body, writer, writer_id, review_root_title, review_id, time_posted) 
            VALUES (?, ?, ?, ?, ?, ?, ?)"""
    time_posted = datetime.datetime.now()
    db.execute(sql, [title, comment_body, username, user_id, root_title, root_id, time_posted])

def get_comments(item_id):
    sql = """SELECT comment_title, body, writer, time_posted FROM comments WHERE review_id = ? ORDER BY time_posted DESC"""
    return db.query(sql, [item_id])
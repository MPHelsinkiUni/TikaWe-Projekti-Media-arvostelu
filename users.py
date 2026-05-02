import db
from werkzeug.security import generate_password_hash, check_password_hash

def get_user(user_id):
    sql = """SELECT id as user_id, username, assignment_role, created_at, favourites FROM users WHERE id = ?"""
    result = db.query(sql, [user_id])
    return result[0] if result else None

def create_user(username, password):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])

def verify_user(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])[0]
    if not result:
        return None

    user_id = result["id"]
    password_hash = result["password_hash"]

    if check_password_hash(password_hash, password):
        return user_id
    else:
        return None
    

####################
# This section manages images FOR THUMBNAILS and PROFILES
def get_image_users(image_id):
    sql = """SELECT image_file FROM images_users WHERE id = ?"""
    result = db.query(sql, [image_id])
    return result[0][0] if result else None

def get_image_id_users(item_id):
    sql = """SELECT id FROM images_users WHERE user_id = ?"""
    return db.query(sql, [item_id])

def update_image_users(user_id, image):
    sql = """UPDATE images_users SET image_file = ? WHERE user_id = ?"""
    db.execute(sql, [image, user_id])

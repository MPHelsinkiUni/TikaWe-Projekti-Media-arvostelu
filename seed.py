import random, datetime
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM reviews")
db.execute("DELETE FROM comments")

user_count = 1000
thread_count = 10**5
message_count = 10**6
user_list = []
datenow = datetime.datetime.now()

for i in range(1, user_count + 1):
    db.execute("INSERT INTO users (username) VALUES (?)",
               ["user" + str(i)])
    user_list.append("user" + str(i))

for i in range(1, thread_count + 1):
    db.execute("INSERT INTO reviews (title, poster, poster_id, work, imdb_snippet, time_posted) VALUES (?, ?, ?, ?, ?, ?)",
               ["thread" + str(i), random.choice(user_list), random.randint(1, 1000), str(i)*5, str(i)*5, datenow])

for i in range(1, message_count + 1):
    user_id = random.randint(1, user_count)
    thread_id = random.randint(1, thread_count)
    db.execute("""INSERT INTO comments (comment_title, body, writer_id, review_id)
                  VALUES (?, datetime('now'), ?, ?)""",
               ["message" + str(i), user_id, thread_id])

db.commit()
db.close()

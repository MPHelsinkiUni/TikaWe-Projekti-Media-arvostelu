CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    assignment_role VARCHAR(255),
    created_at, TIMESTAMP,
    favourites, TEXT
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    poster TEXT NOT NULL,
    poster_id INTEGER NOT NULL,
    review_body TEXT,
    stars INTEGER,
    body TEXT NOT NULL,
    work VARCHAR(255) NOT NULL,
    work_id INTEGER NOT NULL
    time_posted TIMESTAMP NOT NULL
)

CREATE TABLE works (
    id INTEGER PRIMARY KEY,
    work_name VARCHAR(255) NOT NULL,
    genre TEXT,
    picture IMAGE, 
    year_of_release INTEGER NOT NULL,
    month_of_release INTEGER NOT NULL,
    day_of_release INTEGER NOT NULL,
)

-- Above, the works section should be expanded upon with descriptions and others.

CREATE TABLE images (
    id INTEGER PRIMARY KEY,
    image_file IMAGE
)

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    comment_title TEXT NOT NULL,
    body TEXT NOT NULL,
    writer TEXT NOT NULL,
    writer_id INTEGER NOT NULL,
    review_root TEXT NOT NULL,
    review_id INTEGER NOT NULL,
    time_posted TIMESTAMP NOT NULL
)
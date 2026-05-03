CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    assignment_role TEXT DEFAULT "user",
    created_at TIMESTAMP NOT NULL DEFAULT NOW,
    favourites TEXT
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY, 
    title TEXT NOT NULL, -- Input done
    poster TEXT NOT NULL REFERENCES users (username) ON DELETE SET NULL, -- Automatic
    poster_id INTEGER NOT NULL REFERENCES users (id) ON DELETE SET NULL, -- Automatic
    review_body TEXT, -- Input done
    stars INTEGER, -- Input done, type radio.
    work TEXT NOT NULL,  -- Input done
    time_posted TIMESTAMP NOT NULL DEFAULT NOW, -- Not needed
    imdb_snippet TEXT NOT NULL -- Important, input done
);

CREATE TABLE categorisation (
    id INTEGER PRIMARY KEY,
    review_id INTEGER REFERENCES reviews (id) ON DELETE SET NULL,
    title TEXT,
    value TEXT
);

CREATE TABLE class (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value TEXT
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    comment_title TEXT NOT NULL,
    body TEXT NOT NULL,
    writer TEXT REFERENCES users (username) ON DELETE SET NULL,
    writer_id INTEGER NOT NULL REFERENCES users (id) ON DELETE SET NULL,
    review_root_title TEXT,
    review_id INTEGER NOT NULL REFERENCES reviews (id) ON DELETE SET NULL,
    time_posted TIMESTAMP NOT NULL DEFAULT NOW
);

CREATE TABLE images_reviews (
    id INTEGER PRIMARY KEY,
    review_id INTEGER REFERENCES reviews (id) ON DELETE CASCADE,
    image_file BLOB
);
CREATE TABLE images_users (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users (id) ON DELETE CASCADE,
    image_file BLOB
);

-- Indexing 
CREATE UNIQUE INDEX idx_time ON users (created_at, username);
CREATE UNIQUE INDEX idx_comments ON comments (id);

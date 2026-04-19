CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    assignment_role TEXT DEFAULT "user",
    created_at TIMESTAMP NOT NULL DEFAULT NOW,
    favourites TEXT,
    thumbnail IMAGE
);
CREATE TABLE images_users (
    id INTEGER PRIMARY KEY,
    image_file IMAGE REFERENCES reviews (thumbnail) ON DELETE CASCADE
);
    -- References have been commented out till further notice due to debugging difficulties.
    -- FOREIGN KEY (image_file) REFERENCES reviews (thumbnail) ON DELETE CASCADE


CREATE TABLE reviews (
    id INTEGER PRIMARY KEY, 
    title TEXT NOT NULL, -- Input done
    poster TEXT NOT NULL REFERENCES users (username) ON DELETE SET NULL, -- Automatic
    poster_id INTEGER NOT NULL REFERNCES users (id) ON DELETE SET NULL, -- Automatic
    review_body TEXT, -- Input done
    stars INTEGER, -- Input done, type radio.
    work TEXT NOT NULL REFERENCES works (work_name) ON DELETE SET NULL,  -- Input done
    work_id INTEGER REFERENCES works (id) ON DELETE SET NULL, -- Automatic, will be done later. Set as null allowed for now.
    time_posted TIMESTAMP NOT NULL DEFAULT NOW, -- Not needed
    imdb_snippet TEXT NOT NULL REFERENCES works (imdb_snippet) ON DELETE SET NULL, -- Important, input done
    image_file IMAGE -- No implementation yet.
    -- References have been commented out till further notice due to debugging difficulties.
    -- FOREIGN KEY (poster) REFERENCES users (username) ON DELETE SET NULL,
    -- FOREIGN KEY (poster_id) REFERENCES users (id) ON DELETE SET NULL,
    -- FOREIGN KEY (work) REFERENCES works (work_name) ON DELETE SET NULL,
    -- FOREIGN KEY (work_id) REFERENCES works (id) ON DELETE SET NULL,
    -- FOREIGN KEY (imdb_snippet) REFERENCES works (imdb_snippet) ON DELETE SET NULL
);

 -- This will have a rather large list and I will use Wikipedia standardisation for options. References be damned for now.
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

CREATE TABLE images_reviews (
    id INTEGER PRIMARY KEY,
    image_file IMAGE REFERENCES reviews (image_file) ON DELETE CASCADE
    -- References have been commented out till further notice due to debugging difficulties.
    -- FOREIGN KEY (image_file) REFERENCES reviews (image_file) ON DELETE CASCADE
);
-- No implementation yet. Will be done later WIP!!!

CREATE TABLE works (
    id INTEGER PRIMARY KEY, 
    work_name TEXT NOT NULL,
    genre TEXT,
    picture IMAGE, 
    imdb_snippet TEXT NOT NULL,
    year_of_release INTEGER,
    month_of_release INTEGER,
    day_of_release INTEGER
);
CREATE TABLE images_works (
    id INTEGER PRIMARY KEY,
    image_file IMAGE REFERENCES works (picture) ON DELETE CASCADE
    -- References have been commented out till further notice due to debugging difficulties.
    -- FOREIGN KEY (image_file) REFERENCES works (picture) ON DELETE CASCADE
);

-- Above, the works section should be expanded upon with descriptions and others for a later time.

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    comment_title TEXT NOT NULL,
    body TEXT NOT NULL,
    writer TEXT NOT NULL REFERENCES users (username) ON DELETE SET NULL,
    writer_id INTEGER NOT NULL REFERENCES users (id) ON DELETE SET NULL,
    review_root_title TEXT NOT NULL REFERENCES reviews (title) ON DELETE SET NULL,
    review_id INTEGER NOT NULL REFERENCES reviews (id) ON DELETE SET NULL,
    time_posted TIMESTAMP NOT NULL DEFAULT NOW
    -- References have been commented out till further notice due to debugging difficulties.
    -- FOREIGN KEY (writer) REFERENCES users (username) ON DELETE SET NULL,
    -- FOREIGN KEY (writer_id) REFERENCES users (id) ON DELETE SET NULL,
    -- FOREIGN KEY (review_root_title) REFERENCES reviews (title) ON DELETE SET NULL, 
    -- FOREIGN KEY (review_id) REFERENCES reviews (id) ON DELETE SET NULL
);

-- Comments will not have pictures at all. They will not be directly referenced.

-- Indexing 
CREATE UNIQUE INDEX idx_time ON users (created_at, username);
CREATE UNIQUE INDEX idx_works ON works (work_name);
CREATE UNIQUE INDEX idx_comments ON comments (id);

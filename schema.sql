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
    image_file IMAGE
    -- References have been commented out till further notice due to debugging difficulties.
    -- FOREIGN KEY (image_file) REFERENCES reviews (thumbnail) ON DELETE CASCADE
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY, 
    title TEXT NOT NULL, -- Input done
    poster TEXT NOT NULL, -- Automatic
    poster_id INTEGER NOT NULL, -- Automatic
    review_body TEXT, -- Input done
    stars INTEGER, -- Input done, type radio.
    work TEXT NOT NULL,  -- Input done
    work_id INTEGER, -- Automatic, will be done later. Set as null allowed for now.
    time_posted TIMESTAMP NOT NULL DEFAULT NOW, -- Not needed
    imdb_snippet TEXT NOT NULL, -- Important, input done
    image_file IMAGE -- No implementation yet.

    -- References have been commented out till further notice due to debugging difficulties.
    -- FOREIGN KEY (poster) REFERENCES users (username) ON DELETE SET NULL,
    -- FOREIGN KEY (poster_id) REFERENCES users (id) ON DELETE SET NULL,
    -- FOREIGN KEY (work) REFERENCES works (work_name) ON DELETE SET NULL,
    -- FOREIGN KEY (work_id) REFERENCES works (id) ON DELETE SET NULL,
    -- FOREIGN KEY (imdb_snippet) REFERENCES works (imdb_snippet) ON DELETE SET NULL
);
CREATE TABLE images_reviews (
    id INTEGER PRIMARY KEY,
    image_file IMAGE
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
    image_file IMAGE
    -- References have been commented out till further notice due to debugging difficulties.
    -- FOREIGN KEY (image_file) REFERENCES works (picture) ON DELETE CASCADE
);

-- Above, the works section should be expanded upon with descriptions and others for a later time.

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    comment_title TEXT NOT NULL,
    body TEXT NOT NULL,
    writer TEXT NOT NULL,
    writer_id INTEGER NOT NULL,
    review_root_title TEXT NOT NULL,
    review_id INTEGER NOT NULL,
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

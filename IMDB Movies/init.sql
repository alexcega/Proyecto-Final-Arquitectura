CREATE TABLE IF NOT EXISTS movies (
    movie_id serial PRIMARY KEY,
    preference_key INTEGER NOT NULL,
    movie_title VARCHAR NOT NULL,

    rating DOUBLE NOT NULL,
    year INTEGER NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS user (
    user_id serial PRIMARY KEY,
    user_name VARCHAR NOT NULL,
    user_email VARCHAR NOT NULL
)
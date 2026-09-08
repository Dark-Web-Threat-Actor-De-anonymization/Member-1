CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    name TEXT,
    risk_level TEXT
);

CREATE TABLE platforms (
    platform_id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE handles (
    handle_id SERIAL PRIMARY KEY,
    actor_id INT REFERENCES actors(actor_id),
    platform_id INT REFERENCES platforms(platform_id),
    username TEXT
);

CREATE TABLE wallets (
    wallet_id SERIAL PRIMARY KEY,
    actor_id INT REFERENCES actors(actor_id),
    wallet_address TEXT
);

CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    handle_id INT REFERENCES handles(handle_id),
    content TEXT,
    created_at TIMESTAMP
);

CREATE TABLE evidence (
    evidence_id SERIAL PRIMARY KEY,
    actor_id INT REFERENCES actors(actor_id),
    description TEXT
);
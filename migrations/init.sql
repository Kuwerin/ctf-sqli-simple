DROP TABLE IF EXISTS flag;

CREATE TABLE IF NOT EXISTS flag(
    id SERIAL PRIMARY KEY,
    name VARCHAR(300) NOT NULL UNIQUE,
    value VARCHAR(300),
    is_private BOOLEAN NOT NULL DEFAULT false
);

INSERT INTO flag (name, value, is_private) VALUES
    ('Ivan', 'sdfsdf', false),
    ('Vaan', 'flag{Boss_of_the_gym}', true),
    ('Goga', 'ssdfasdf', false),
    ('Vladislave', 'dfgfdg', false);

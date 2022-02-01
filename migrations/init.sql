DROP TABLE IF EXISTS flag IF;

CREATE TABLE flag (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(30),
    value VARCHAR(30),
    is_private BOOLEAN NOT NULL DEFAULT false,
    PRIMARY KEY (id, name)
);

INSERT INTO flag (name, value, is_private) VALUES
    ('Ivan', 'sdfsdf', false),
    ('Vaan', 'flag{Boss_of_the_gym}', true),
    ('Goga', 'ssdfasdf', false),
    ('Vladislave', 'dfgfdg', false);
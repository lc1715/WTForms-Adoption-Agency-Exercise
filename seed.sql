
DROP DATABASE IF EXISTS adopt;

CREATE DATABASE adopt;

\c adopt

CREATE TABLE pets
(
  id SERIAL PRIMARY KEY,
  pet_name TEXT NOT NULL,
  species TEXT NOT NULL,
  photo_url TEXT,
  age INT,
  notes TEXT,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO pets
  (pet_name, species, photo_url, age, notes, available)
VALUES
  ('Woofly', 'dog', 'https://images.unsplash.com/photo-1568572933382-74d440642117?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8ZG9nc3xlbnwwfHwwfHx8MA%3D%3D', 3, 'Incredibly adorable.', 't'),
  ('Porchetta', 'porcupine', 'http://kids.sandiegozoo.org/sites/default/files/2017-12/porcupine-incisors.jpg', 4, 'Somewhat spiky!', 't'),
  ('Snargle', 'cat', 'https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg', null, null, 't'),
  ('Dr. Claw', 'cat', null, null, null, 't');

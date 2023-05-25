CREATE TABLE virtual_domains (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE virtual_users (
  id SERIAL PRIMARY KEY,
  domain_id INT NOT NULL REFERENCES virtual_domains(id) ON DELETE CASCADE,
  password VARCHAR(150) NOT NULL,
  email VARCHAR(100) NOT NULL
);

CREATE TABLE virtual_aliases (
  id SERIAL PRIMARY KEY,
  domain_id INT NOT NULL REFERENCES virtual_domains(id) ON DELETE CASCADE,
  source VARCHAR(100) NOT NULL,
  destination VARCHAR(100) NOT NULL
);

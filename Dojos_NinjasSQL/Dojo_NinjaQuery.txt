SET SQL_SAFE_UPDATES = 0;


INSERT INTO dojos (name)
VALUES ('Cool Dude'),
	('Coding'),
	('Program');
    
SELECT * FROM dojos;

DELETE FROM dojos;

INSERT INTO dojos (name)
VALUES ('Cooler'),
	('MySQL'),
    ('Winners');
    
SELECT * FROM ninjas;
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUE ('Cameron', 'Bisett', 23, 6),
	('John', 'Doe', 105, 6),
    ('Jeremy', 'Clarkson', 61, 6),
    ('Richard', 'Hammond', 51, 7),
    ('James', 'May', 64, 7),
    ('Jane', 'Doe', 23, 7),
    ('North', 'America', 10000000, 8),
    ('America', 'F-Yeah', 244, 8),
    ('Cameron', 'Again', 23, 8);
    
SELECT * FROM ninjas WHERE dojo_id = 6;
SELECT * FROM ninjas WHERE dojo_id = 7;
SELECT * FROM ninjas WHERE dojo_id = 8;

SELECT dojo_id FROM ninjas WHERE id = 8; 
SELECT dojos.* FROM ninjas JOIN dojos ON dojo_id = dojos.id ORDER BY ninjas.id DESC limit 1;

-- accidently added the info again to the table;
DELETE FROM dojos WHERE id = 3; 
DELETE FROM dojos WHERE id = 4; 
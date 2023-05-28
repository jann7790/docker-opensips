-- CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'newpassword';
-- GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';


-- if newuser newuse not exist create user else do nothing







CREATE USER IF NOT EXISTS 'newuser'@'%' IDENTIFIED BY 'newpassword';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'%';
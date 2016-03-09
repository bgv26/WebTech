CREATE DATABASE box_django;
CREATE USER 'box'@'localhost' IDENTIFIED BY 'passwd';
GRANT ALL ON box_django.* TO 'box'@'localhost';
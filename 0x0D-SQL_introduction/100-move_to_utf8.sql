-- Graham S. Paul (100-move_to_utf8.sql)
-- Change hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- change first_table table and `name` field in table to UTF8

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

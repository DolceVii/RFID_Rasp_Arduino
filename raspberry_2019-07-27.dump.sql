----
-- phpLiteAdmin database dump (http://www.phpliteadmin.org/)
-- phpLiteAdmin version: 1.9.7.1
-- Exported: 10:32pm on July 27, 2019 (EEST)
-- database file: raspberry.db
----
BEGIN TRANSACTION;

----
-- Table structure for data
----
CREATE TABLE 'data' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'door' TEXT, 'day' DATETIME DEFAULT CURRENT_TIMESTAMP, 'who' TEXT, 'UserName' TEXT, 'isactive' TEXT);

----
-- Data dump for data, a total of 0 rows
----

----
-- Table structure for active
----
CREATE TABLE 'active' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'userrfid' TEXT,'activerfid' TEXT, 'userdate'  DATETIME DEFAULT CURRENT_TIMESTAMP  , 'UserName' TEXT);

----
-- Data dump for active, a total of 4 rows
----
INSERT INTO "active" ("id","userrfid","activerfid","userdate","UserName") VALUES ('1','04 E3 A9 EA 06 57 80','1','26-07-2019 16:59:02','Γιώργος Κουρτίδης');
INSERT INTO "active" ("id","userrfid","activerfid","userdate","UserName") VALUES ('2','04 E3 A9 EA 06 57 00','0','26-07-2019 17:00:38','Θεόδωρος Κοσμίδης');
INSERT INTO "active" ("id","userrfid","activerfid","userdate","UserName") VALUES ('3','04 34 56 EA 5A 70 00','1','26-07-2019 17:35:26','Μάριος Ζίκος');
INSERT INTO "active" ("id","userrfid","activerfid","userdate","UserName") VALUES ('4','00 A4 4F 34 EE 3F 00','1','27-07-2019 19:17:27','Κώστας Λαφτσής');
COMMIT;

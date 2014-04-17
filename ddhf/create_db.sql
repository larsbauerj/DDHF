BEGIN;CREATE TABLE `donators` (
    `donatorid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `creator` varchar(12) NOT NULL,
    `created` datetime NOT NULL,
    `lastmodified` datetime NOT NULL,
    `donatorinstitution` varchar(255),
    `donatorposition` varchar(255),
    `donatorname` varchar(255) NOT NULL,
    `donatoraddress` varchar(255),
    `donatorphone` varchar(255),
    `donatoremail` varchar(255)
)
;
CREATE TABLE `files` (
    `fileid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `creator` varchar(12) NOT NULL,
    `created` datetime NOT NULL,
    `lastmodified` datetime NOT NULL,
    `filetitle` varchar(255),
    `filedescription` longtext
)
;
CREATE TABLE `pictures_dj` (
    `pictureid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `picturetext` longtext NOT NULL,
    `pictureregisteredby` varchar(12) NOT NULL,
    `pictureregistered` datetime NOT NULL,
    `lastmodified` datetime NOT NULL,
    `picture` varchar(100) NOT NULL
)
;
CREATE TABLE `subjects` (
    `subjectid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `creator` varchar(12) NOT NULL,
    `created` datetime NOT NULL,
    `lastmodified` datetime NOT NULL,
    `subjecttitle` varchar(255),
    `subjectdescription` longtext NOT NULL
)
;
CREATE TABLE `producers` (
    `producerid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `creator` varchar(12) NOT NULL,
    `created` datetime NOT NULL,
    `lastmodified` datetime NOT NULL,
    `producertitle` varchar(255),
    `producerdescription` longtext
)
;
CREATE TABLE `items_itempicture` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `items_id` integer NOT NULL,
    `pictures_id` integer NOT NULL,
    UNIQUE (`items_id`, `pictures_id`)
)
;
ALTER TABLE `items_itempicture` ADD CONSTRAINT `pictures_id_refs_pictureid_46cdb3` FOREIGN KEY (`pictures_id`) REFERENCES `pictures_dj` (`pictureid`);
CREATE TABLE `items_itemsubject` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `items_id` integer NOT NULL,
    `subjects_id` integer NOT NULL,
    UNIQUE (`items_id`, `subjects_id`)
)
;
ALTER TABLE `items_itemsubject` ADD CONSTRAINT `subjects_id_refs_subjectid_7734f65d` FOREIGN KEY (`subjects_id`) REFERENCES `subjects` (`subjectid`);
CREATE TABLE `items` (
    `itemid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `itemtemporary` integer NOT NULL,
    `fileid` integer NOT NULL,
    `olditemid` varchar(255) NOT NULL,
    `itemdeleted` integer,
    `itemheadline` varchar(255) NOT NULL,
    `itemdescription` longtext NOT NULL,
    `itemsize` varchar(255) NOT NULL,
    `itemweight` varchar(255) NOT NULL,
    `itemmodeltype` varchar(255) NOT NULL,
    `itemserialno` varchar(255) NOT NULL,
    `itemdatingfrom` date,
    `itemdatingto` date,
    `producerid` integer,
    `itemacquiretype` integer,
    `itemdepositeduntil` date,
    `donatorid` integer,
    `itemoutdated` integer,
    `itemborroweduntil` date,
    `itemreceived` date,
    `itemreceivedby` varchar(12) NOT NULL,
    `itemregistered` date,
    `itemregisteredby` varchar(12) NOT NULL,
    `lastmodified` datetime,
    `itemthanksletter` date,
    `placementid` integer,
    `itemusedby` longtext NOT NULL,
    `itemusedfor` longtext NOT NULL,
    `itemusedwhere` longtext NOT NULL,
    `itemusedfrom` date,
    `itemusedto` date,
    `itemusedendfrom` date,
    `itemusedendto` date,
    `itemextrainfo` longtext NOT NULL,
    `itemrestoration` longtext NOT NULL,
    `itemreferences` longtext NOT NULL,
    `itemremarks` longtext NOT NULL,
    `iteminternal` integer
)
;
ALTER TABLE `items` ADD CONSTRAINT `producerid_refs_producerid_42b09272` FOREIGN KEY (`producerid`) REFERENCES `producers` (`producerid`);
ALTER TABLE `items` ADD CONSTRAINT `donatorid_refs_donatorid_67cdc20c` FOREIGN KEY (`donatorid`) REFERENCES `donators` (`donatorid`);
ALTER TABLE `items` ADD CONSTRAINT `fileid_refs_fileid_5d9b9cc2` FOREIGN KEY (`fileid`) REFERENCES `files` (`fileid`);
ALTER TABLE `items_itempicture` ADD CONSTRAINT `items_id_refs_itemid_72227d75` FOREIGN KEY (`items_id`) REFERENCES `items` (`itemid`);
ALTER TABLE `items_itemsubject` ADD CONSTRAINT `items_id_refs_itemid_2f3bc1cb` FOREIGN KEY (`items_id`) REFERENCES `items` (`itemid`);
CREATE INDEX `donators_15831b2e` ON `donators` (`donatorinstitution`);
CREATE INDEX `donators_3917e74e` ON `donators` (`donatorname`);
CREATE INDEX `items_72f0f9f0` ON `items` (`fileid`);
CREATE INDEX `items_7228800a` ON `items` (`itemheadline`);
CREATE INDEX `items_29bf8518` ON `items` (`producerid`);
CREATE INDEX `items_2c450152` ON `items` (`donatorid`);COMMIT;

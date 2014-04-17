BEGIN;
CREATE TABLE `donators` (
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
CREATE TABLE `pictures` (
    `pictureid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `picturetext` longtext NOT NULL,
    `pictureregisteredby` varchar(12) NOT NULL,
    `pictureregistered` datetime NOT NULL,
    `lastmodified` datetime NOT NULL,
    `picturelow` varchar(100) NOT NULL,
    `picturemedium` varchar(100) NOT NULL,
    `pictureoriginal` varchar(100) NOT NULL
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
CREATE TABLE `items` (
    `itemid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `itemtemporary` integer NOT NULL,
    `fileid_id` integer NOT NULL,
    `olditemid` varchar(255),
    `itemdeleted` integer NOT NULL,
    `itemheadline` varchar(255),
    `itemdescription` longtext,
    `itemsize` varchar(255),
    `itemweight` varchar(255),
    `itemmodeltype` varchar(255),
    `itemserialno` varchar(255),
    `itemdatingfrom` date,
    `itemdatingto` date,
    `producerid_id` integer,
    `itemacquiretype` integer,
    `itemdepositeduntil` date,
    `donatorid_id` integer,
    `itemoutdated` integer,
    `itemborroweduntil` date,
    `itemreceived` date,
    `itemreceivedby` varchar(12),
    `itemregistered` date,
    `itemregisteredby` varchar(12),
    `lastmodified` datetime NOT NULL,
    `itemthanksletter` date,
    `placementid` integer,
    `itemusedby` longtext,
    `itemusedfor` longtext,
    `itemusedwhere` longtext,
    `itemusedfrom` date,
    `itemusedto` date,
    `itemusedendfrom` date,
    `itemusedendto` date,
    `itemextrainfo` longtext,
    `itemrestoration` longtext,
    `itemreferences` longtext,
    `itemremarks` longtext,
    `iteminternal` integer
)
;
ALTER TABLE `items` ADD CONSTRAINT `fileid_id_refs_fileid_5d9b9cc2` FOREIGN KEY (`fileid_id`) REFERENCES `files` (`fileid`);
ALTER TABLE `items` ADD CONSTRAINT `donatorid_id_refs_donatorid_67cdc20c` FOREIGN KEY (`donatorid_id`) REFERENCES `donators` (`donatorid`);
CREATE TABLE `producers` (
    `producerid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `creator` varchar(12) NOT NULL,
    `created` datetime NOT NULL,
    `lastmodified` datetime NOT NULL,
    `producertitle` varchar(255),
    `producerdescription` longtext NOT NULL
)
;
ALTER TABLE `items` ADD CONSTRAINT `producerid_id_refs_producerid_42b09272` FOREIGN KEY (`producerid_id`) REFERENCES `producers` (`producerid`);
CREATE TABLE `items_itemsubject` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `items_id` integer NOT NULL,
    `subjects_id` integer NOT NULL,
    UNIQUE (`items_id`, `subjects_id`)
)
;
ALTER TABLE `items_itemsubject` ADD CONSTRAINT `items_id_refs_itemid_2f3bc1cb` FOREIGN KEY (`items_id`) REFERENCES `items` (`itemid`);
ALTER TABLE `items_itemsubject` ADD CONSTRAINT `subjects_id_refs_fileid_7734f65d` FOREIGN KEY (`subjects_id`) REFERENCES `subjects` (`fileid`);
CREATE TABLE `items_itempicture` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `items_id` integer NOT NULL,
    `pictures_id` integer NOT NULL,
    UNIQUE (`items_id`, `pictures_id`)
)
;
ALTER TABLE `items_itempicture` ADD CONSTRAINT `items_id_refs_itemid_72227d75` FOREIGN KEY (`items_id`) REFERENCES `items` (`itemid`);
ALTER TABLE `items_itempicture` ADD CONSTRAINT `pictures_id_refs_pictureid_45e705cb` FOREIGN KEY (`pictures_id`) REFERENCES `pictures` (`pictureid`);
CREATE TABLE `producers_itemlist` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `producers_id` integer NOT NULL,
    `items_id` integer NOT NULL,
    UNIQUE (`producers_id`, `items_id`)
)
;
ALTER TABLE `producers_itemlist` ADD CONSTRAINT `producers_id_refs_producerid_149c1510` FOREIGN KEY (`producers_id`) REFERENCES `producers` (`producerid`);
ALTER TABLE `producers_itemlist` ADD CONSTRAINT `items_id_refs_itemid_6c4b62fb` FOREIGN KEY (`items_id`) REFERENCES `items` (`itemid`);
CREATE INDEX `donators_donatorinstitution` ON `donators` (`donatorinstitution`);
CREATE INDEX `donators_donatorname` ON `donators` (`donatorname`);
CREATE INDEX `files_filetitle` ON `files` (`filetitle`);
CREATE INDEX `items_fileid_id` ON `items` (`fileid_id`);
CREATE INDEX `items_itemheadline` ON `items` (`itemheadline`);
CREATE INDEX `items_producerid_id` ON `items` (`producerid_id`);
CREATE INDEX `items_donatorid_id` ON `items` (`donatorid_id`);
COMMIT;

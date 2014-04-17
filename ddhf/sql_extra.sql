/* CREATE DATABASE ddhf; 
connect ddhf;
IF view exists DROP view itemsubject ;
*/

CREATE VIEW itemsubject(
    itemid,
    subjectid
) AS
    SELECT items_id, subjects_id
    FROM items_itemsubject;

CREATE VIEW itempicture(
    itemid,
    pictureid
) AS
    SELECT items_id, pictures_id
    FROM items_itempicture;

DELETE FROM producers;
INSERT INTO producers
    SELECT * FROM ddhf_orig.producers;
DELETE FROM donators;
INSERT INTO donators
    SELECT * FROM ddhf_orig.donators;
DELETE FROM files;
INSERT INTO files
    SELECT * FROM ddhf_orig.files;
DELETE FROM itempicture;
INSERT INTO itempicture
    SELECT * FROM ddhf_orig.itempicture;
DELETE FROM items;
INSERT INTO items
    SELECT * FROM ddhf_orig.items;
DELETE FROM items_itemsubject;
INSERT INTO items_itemsubject ( id, items_id, subjects_id)
    SELECT 0, itemid, subjectid FROM ddhf_orig.itemsubject;
DELETE FROM pictures_dj;
INSERT INTO pictures_dj
    SELECT pictureid, picturetext, pictureregisteredby, pictureregistered, cast(pictureid as char) FROM ddhf_orig.pictures;
DELETE FROM pictures;
INSERT INTO pictures
    SELECT * FROM ddhf_orig.pictures;
DELETE FROM items_itempicture;
INSERT INTO items_itempicture ( items_id, pictures_id)
    SELECT itemid, pictureid FROM ddhf_orig.itempicture;
DELETE FROM subjects;
INSERT INTO subjects
    SELECT * FROM ddhf_orig.subjects;
/*
DELETE FROM producers_itemlist;
INSERT INTO producers_itemlist (producers_id, items_id)
    SELECT p.producerid, i.itemid
    FROM producers p, items i
    WHERE i.producerid_id = p.producerid
*/

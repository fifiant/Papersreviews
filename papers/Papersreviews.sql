BEGIN;
CREATE TABLE `papers_papers` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` varchar(255) NOT NULL UNIQUE,
    `abstract` longtext NOT NULL
)
;
CREATE TABLE `papers_authors` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `email` varchar(75) NOT NULL,
    `papers_id` integer NOT NULL
)
;
ALTER TABLE `papers_authors` ADD CONSTRAINT `papers_id_refs_id_750ec057` FOREIGN KEY (`papers_id`) REFERENCES `papers_papers` (`id`);
CREATE TABLE `papers_references` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `description` longtext NOT NULL,
    `papers_id` integer NOT NULL
)
;
ALTER TABLE `papers_references` ADD CONSTRAINT `papers_id_refs_id_205de2d8` FOREIGN KEY (`papers_id`) REFERENCES `papers_papers` (`id`);
CREATE TABLE `papers_keywords` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` varchar(300) NOT NULL,
    `papers_id` integer NOT NULL
)
;
ALTER TABLE `papers_keywords` ADD CONSTRAINT `papers_id_refs_id_5a719850` FOREIGN KEY (`papers_id`) REFERENCES `papers_papers` (`id`);
CREATE TABLE `papers_files` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL,
    `description` varchar(250) NOT NULL,
    `file` varchar(100) NOT NULL,
    `created` datetime NOT NULL,
    `modified` datetime NOT NULL,
    `papers_id` integer NOT NULL
)
;
ALTER TABLE `papers_files` ADD CONSTRAINT `papers_id_refs_id_3cee68ba` FOREIGN KEY (`papers_id`) REFERENCES `papers_papers` (`id`);
COMMIT;


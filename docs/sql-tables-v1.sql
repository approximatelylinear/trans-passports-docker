-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'nodes'
--
-- ---

DROP TABLE IF EXISTS `nodes`;

CREATE TABLE `nodes` (
  `node_id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `node_data_id` INTEGER NULL DEFAULT NULL COMMENT 'FK to data table',
  `node_parent` INTEGER NULL DEFAULT NULL COMMENT 'Parent id of this node',
  `node_created` TIMESTAMP NULL DEFAULT NULL,
  `node_modified` TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (`node_id`)
);

-- ---
-- Table 'data'
--
-- ---

DROP TABLE IF EXISTS `data`;

CREATE TABLE `data` (
  `data_id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `data_parent` INTEGER NULL DEFAULT NULL COMMENT 'Parent of this data element',
  `data_type` ENUM(100) NULL DEFAULT NULL COMMENT 'Available types: question, question-group, answer, answer-gr',
  `data_name` VARCHAR NULL DEFAULT NULL COMMENT 'Name of this data element',
  `data_value` MEDIUMTEXT NULL DEFAULT NULL COMMENT 'Value for this data element',
  `data_created` TIMESTAMP NULL DEFAULT NULL,
  `data_modified` TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (`data_id`)
);

-- ---
-- Table 'node_attributes'
-- Attributes for the node table
-- ---

DROP TABLE IF EXISTS `node_attributes`;

CREATE TABLE `node_attributes` (
  `node_attribute_id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `node_attribute_node_id` INTEGER NULL DEFAULT NULL COMMENT 'FK to nodes table',
  `node_attribute_value` MEDIUMTEXT NULL DEFAULT NULL,
  `node_attribute_created` TIMESTAMP NULL DEFAULT NULL,
  `node_attribute_modified` TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (`node_attribute_id`)
) COMMENT 'Attributes for the node table';

-- ---
-- Foreign Keys
-- ---

ALTER TABLE `nodes` ADD FOREIGN KEY (node_data_id) REFERENCES `data` (`data_id`);
ALTER TABLE `nodes` ADD FOREIGN KEY (node_parent) REFERENCES `nodes` (`node_id`);
ALTER TABLE `data` ADD FOREIGN KEY (data_parent) REFERENCES `data` (`data_id`);
ALTER TABLE `node_attributes` ADD FOREIGN KEY (node_attribute_node_id) REFERENCES `nodes` (`node_id`);

-- ---
-- Table Properties
-- ---

-- ALTER TABLE `nodes` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `data` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `node_attributes` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `nodes` (`node_id`,`node_data_id`,`node_parent`,`node_created`,`node_modified`) VALUES
-- ('','','','','');
-- INSERT INTO `data` (`data_id`,`data_parent`,`data_type`,`data_name`,`data_value`,`data_created`,`data_modified`) VALUES
-- ('','','','','','','');
-- INSERT INTO `node_attributes` (`node_attribute_id`,`node_attribute_node_id`,`node_attribute_value`,`node_attribute_created`,`node_attribute_modified`) VALUES
-- ('','','','','');

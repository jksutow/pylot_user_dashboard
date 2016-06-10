-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema user_dashboard
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema user_dashboard
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `user_dashboard` DEFAULT CHARACTER SET utf8 ;
USE `user_dashboard` ;

-- -----------------------------------------------------
-- Table `user_dashboard`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_dashboard`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `email` VARCHAR(45) NULL,
  `pw_hash` VARCHAR(255) NULL,
  `admin_level` INT NULL DEFAULT 0,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `user_dashboard`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_dashboard`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `message` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users_idx` (`user_id` ASC),
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `user_dashboard`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `user_dashboard`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_dashboard`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `message_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_messages1_idx` (`message_id` ASC),
  INDEX `fk_comments_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_comments_messages1`
    FOREIGN KEY (`message_id`)
    REFERENCES `user_dashboard`.`messages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `user_dashboard`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

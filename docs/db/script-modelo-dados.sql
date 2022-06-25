-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema code_wars_ii
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema code_wars_ii
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `code_wars_ii` DEFAULT CHARACTER SET utf8mb3 ;
USE `code_wars_ii` ;

-- -----------------------------------------------------
-- Table `code_wars_ii`.`cargos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `code_wars_ii`.`cargos` (
  `codigo_cargo` INT NOT NULL,
  `descricao` VARCHAR(40) NOT NULL,
  `salario_base` FLOAT NOT NULL,
  `comissao` FLOAT NOT NULL,
  PRIMARY KEY (`codigo_cargo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `code_wars_ii`.`funcionarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `code_wars_ii`.`funcionarios` (
  `matricula` INT(6) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `cpf` CHAR(11) NOT NULL,
  `data_admissao` DATE NOT NULL,
  `codigo_cargo` INT NOT NULL,
  `comissao` ENUM('0', '1') NOT NULL,
  PRIMARY KEY (`matricula`),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC) VISIBLE,
  INDEX `fk_Funcionarios_Cargos_idx` (`codigo_cargo` ASC) VISIBLE,
  CONSTRAINT `fk_Funcionarios_Cargos`
    FOREIGN KEY (`codigo_cargo`)
    REFERENCES `code_wars_ii`.`cargos` (`codigo_cargo`))
ENGINE = InnoDB
AUTO_INCREMENT = 100001
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `code_wars_ii`.`holerite`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `code_wars_ii`.`holerite` (
  `mes/ano` CHAR(7) NOT NULL,
  `matricula` INT(6) NOT NULL,
  `faltas` FLOAT NOT NULL,
  `inss` FLOAT NOT NULL,
  `irrf` FLOAT NOT NULL,
  INDEX `fk_holerite_Funcionarios1_idx` (`matricula` ASC) VISIBLE,
  CONSTRAINT `fk_holerite_Funcionarios1`
    FOREIGN KEY (`matricula`)
    REFERENCES `code_wars_ii`.`funcionarios` (`matricula`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Počítač: 127.0.0.1
-- Vytvořeno: Čtv 26. lis 2020, 11:15
-- Verze serveru: 10.4.14-MariaDB
-- Verze PHP: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databáze: `eshop`
--

-- --------------------------------------------------------

--
-- Struktura tabulky `account`
--

CREATE TABLE `account` (
  `username` varchar(16) COLLATE utf8_bin NOT NULL,
  `password_hash` varchar(32) COLLATE utf8_bin NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `contact_idcontact` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `account`
--

INSERT INTO `account` (`username`, `password_hash`, `create_time`, `contact_idcontact`) VALUES
('BestTech123', 'dg1sd56fg1sd56fgsd1g56sd1g56', '2020-11-13 08:02:50', 1),
('johnTheAdmin', 'gr5g89drg1256df1g26df1gdf6', '2020-11-13 08:02:50', 3),
('u_customer', 'wefgwe4g89sdg564we8g', '2020-11-26 09:52:30', 4);

-- --------------------------------------------------------

--
-- Struktura tabulky `brand`
--

CREATE TABLE `brand` (
  `name` varchar(45) COLLATE utf8_bin NOT NULL,
  `company_name` varchar(50) COLLATE utf8_bin NOT NULL,
  `logo` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `brand`
--

INSERT INTO `brand` (`name`, `company_name`, `logo`) VALUES
('AlfaComponents', 'Tech company', NULL),
('Hennry\'s Builds', 'Tech company', NULL);

-- --------------------------------------------------------

--
-- Struktura tabulky `choice`
--

CREATE TABLE `choice` (
  `idchoice` int(11) NOT NULL,
  `name` varchar(45) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `choice`
--

INSERT INTO `choice` (`idchoice`, `name`) VALUES
(1, '10mm'),
(2, '12mm'),
(3, '15mm'),
(4, '17mm'),
(5, '20mm'),
(6, 'Silver'),
(7, 'Black');

-- --------------------------------------------------------

--
-- Struktura tabulky `company`
--

CREATE TABLE `company` (
  `name` varchar(50) COLLATE utf8_bin NOT NULL,
  `description` text COLLATE utf8_bin DEFAULT NULL,
  `account_username` varchar(16) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `company`
--

INSERT INTO `company` (`name`, `description`, `account_username`) VALUES
('Tech company', 'We sell all sort of technical stuff', 'BestTech123');

-- --------------------------------------------------------

--
-- Struktura tabulky `contact`
--

CREATE TABLE `contact` (
  `idcontact` int(11) NOT NULL,
  `email` varchar(45) COLLATE utf8_bin NOT NULL,
  `phone` varchar(45) COLLATE utf8_bin NOT NULL,
  `address` varchar(45) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `contact`
--

INSERT INTO `contact` (`idcontact`, `email`, `phone`, `address`) VALUES
(1, 'techcompany@gmail.com', '645645645645645', '5 Wayne St. Mechanicsburg, PA 17050'),
(2, 'techcompany-warehouse@gmail.com', '5287272782782782', '15 Winding Way Court Orland Park, IL 60462'),
(3, 'john-smith@gmail.com', '56256256', '3453  Joseph Street, Alabana'),
(4, 'customer@gmail.com', '52892891', '78. 9.St. Mechanicsburg, PA 17050');

-- --------------------------------------------------------

--
-- Struktura tabulky `group`
--

CREATE TABLE `group` (
  `idgroup` int(11) NOT NULL,
  `name` varchar(45) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `group`
--

INSERT INTO `group` (`idgroup`, `name`) VALUES
(1, 'Alfa admin group'),
(2, 'customer');

-- --------------------------------------------------------

--
-- Struktura tabulky `group_has_rights`
--

CREATE TABLE `group_has_rights` (
  `group_idgroup` int(11) NOT NULL,
  `rights_idrights` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `group_has_rights`
--

INSERT INTO `group_has_rights` (`group_idgroup`, `rights_idrights`) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4);

-- --------------------------------------------------------

--
-- Struktura tabulky `item`
--

CREATE TABLE `item` (
  `iditem` int(11) NOT NULL,
  `shop_brand_name` varchar(45) COLLATE utf8_bin NOT NULL,
  `title` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `description` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `img` blob DEFAULT NULL,
  `path` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `total_count` int(11) DEFAULT NULL,
  `price` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `item`
--

INSERT INTO `item` (`iditem`, `shop_brand_name`, `title`, `description`, `img`, `path`, `total_count`, `price`) VALUES
(1, 'Hennry\'s Builds', 'Head Cap Screws 10pcs', NULL, NULL, 'Scrws/HeadCapScrews/', NULL, '6'),
(2, 'Hennry\'s Builds', 'Head Cap Screws 20pcs', NULL, NULL, 'Scrws/HeadCapScrews/', NULL, '9'),
(3, 'Hennry\'s Builds', 'Head Cap Screws 50pcs', NULL, NULL, 'Scrws/HeadCapScrews/', NULL, '24'),
(7, 'AlfaComponents', 'GIGABYTE GeForce RTX 2060 OC 6G', NULL, NULL, 'GraphicsCards/Invidia/', NULL, '320'),
(8, 'AlfaComponents', 'GIGABYTE GeForce RTX 2060 OC 6G', NULL, NULL, 'GraphicsCards/Invidia/', NULL, '40');

-- --------------------------------------------------------

--
-- Struktura tabulky `options`
--

CREATE TABLE `options` (
  `name` varchar(45) COLLATE utf8_bin NOT NULL,
  `item_iditem` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `options`
--

INSERT INTO `options` (`name`, `item_iditem`) VALUES
('Length h1', 1),
('Length h2', 2),
('Length h3', 3);

-- --------------------------------------------------------

--
-- Struktura tabulky `options_has_choice`
--

CREATE TABLE `options_has_choice` (
  `options_name` varchar(45) COLLATE utf8_bin NOT NULL,
  `choice_idchoice` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `options_has_choice`
--

INSERT INTO `options_has_choice` (`options_name`, `choice_idchoice`) VALUES
('Length h1', 1),
('Length h1', 2),
('Length h1', 3),
('Length h1', 4),
('Length h1', 5),
('Length h2', 1),
('Length h2', 2),
('Length h2', 3),
('Length h2', 4),
('Length h2', 5),
('Length h3', 1),
('Length h3', 2),
('Length h3', 3),
('Length h3', 4),
('Length h3', 5);

-- --------------------------------------------------------

--
-- Struktura tabulky `order`
--

CREATE TABLE `order` (
  `idorder` int(11) NOT NULL,
  `account_username` varchar(16) COLLATE utf8_bin NOT NULL,
  `payment_method_name` varchar(50) COLLATE utf8_bin NOT NULL,
  `shippment_method_name` varchar(50) COLLATE utf8_bin NOT NULL,
  `shop_brand_name` varchar(45) COLLATE utf8_bin NOT NULL,
  `status_idstatus` int(11) NOT NULL,
  `create_date` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `order`
--

INSERT INTO `order` (`idorder`, `account_username`, `payment_method_name`, `shippment_method_name`, `shop_brand_name`, `status_idstatus`, `create_date`) VALUES
(1, 'u_customer', 'Credit card', 'Express', 'AlfaComponents', 1, '2020-11-26 10:08:54'),
(2, 'u_customer', 'Credit card', 'Economy', 'Hennry\'s Builds', 1, '2020-11-26 10:08:54');

-- --------------------------------------------------------

--
-- Struktura tabulky `order_has_item`
--

CREATE TABLE `order_has_item` (
  `order_idorder` int(11) NOT NULL,
  `item_iditem` int(11) NOT NULL,
  `count` int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `order_has_item`
--

INSERT INTO `order_has_item` (`order_idorder`, `item_iditem`, `count`) VALUES
(1, 7, 1),
(2, 1, 2),
(2, 2, 1);

-- --------------------------------------------------------

--
-- Struktura tabulky `order_has_item_has_options`
--

CREATE TABLE `order_has_item_has_options` (
  `order_idorder` int(11) NOT NULL,
  `item_iditem` int(11) NOT NULL,
  `options_name` varchar(45) COLLATE utf8_bin NOT NULL,
  `selected_value` varchar(45) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `order_has_item_has_options`
--

INSERT INTO `order_has_item_has_options` (`order_idorder`, `item_iditem`, `options_name`, `selected_value`) VALUES
(2, 1, 'Length h1', '12mm'),
(2, 2, 'Length h2', '15mm');

-- --------------------------------------------------------

--
-- Struktura tabulky `payment_method`
--

CREATE TABLE `payment_method` (
  `name` varchar(50) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `payment_method`
--

INSERT INTO `payment_method` (`name`) VALUES
('Bitcoin'),
('Credit card'),
('Pay sefe card'),
('Paypal');

-- --------------------------------------------------------

--
-- Struktura tabulky `person`
--

CREATE TABLE `person` (
  `account_username` varchar(16) COLLATE utf8_bin NOT NULL,
  `name` varchar(225) COLLATE utf8_bin DEFAULT NULL,
  `group_idgroup` int(11) NOT NULL,
  `company_name` varchar(50) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `person`
--

INSERT INTO `person` (`account_username`, `name`, `group_idgroup`, `company_name`) VALUES
('johnTheAdmin', 'John Smith', 1, 'Tech company'),
('u_customer', 'idk nomeeee', 2, NULL);

-- --------------------------------------------------------

--
-- Struktura tabulky `rights`
--

CREATE TABLE `rights` (
  `idrights` int(11) NOT NULL,
  `name` varchar(45) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `rights`
--

INSERT INTO `rights` (`idrights`, `name`) VALUES
(1, 'add item'),
(2, 'hire admin'),
(3, 'make order'),
(4, 'ask for a refound');

-- --------------------------------------------------------

--
-- Struktura tabulky `shippment_method`
--

CREATE TABLE `shippment_method` (
  `name` varchar(50) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `shippment_method`
--

INSERT INTO `shippment_method` (`name`) VALUES
('Economy'),
('Express'),
('Express plus'),
('Extreme economy'),
('Regular');

-- --------------------------------------------------------

--
-- Struktura tabulky `shop`
--

CREATE TABLE `shop` (
  `brand_name` varchar(45) COLLATE utf8_bin NOT NULL,
  `name` varchar(45) COLLATE utf8_bin NOT NULL,
  `description` text COLLATE utf8_bin DEFAULT NULL,
  `img` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `shop`
--

INSERT INTO `shop` (`brand_name`, `name`, `description`, `img`) VALUES
('AlfaComponents', 'Alfa Hardware Store', 'Do you need to upgrade your pc?', NULL),
('Hennry\'s Builds', 'Screws & Bolts', 'From screws to bolts and everything in between', NULL);

-- --------------------------------------------------------

--
-- Struktura tabulky `shop_has_group`
--

CREATE TABLE `shop_has_group` (
  `shop_brand_name` varchar(45) COLLATE utf8_bin NOT NULL,
  `group_idgroup` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `shop_has_group`
--

INSERT INTO `shop_has_group` (`shop_brand_name`, `group_idgroup`) VALUES
('AlfaComponents', 1);

-- --------------------------------------------------------

--
-- Struktura tabulky `shop_has_payment_method`
--

CREATE TABLE `shop_has_payment_method` (
  `shop_brand_name` varchar(45) COLLATE utf8_bin NOT NULL,
  `payment_method_name` varchar(50) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `shop_has_payment_method`
--

INSERT INTO `shop_has_payment_method` (`shop_brand_name`, `payment_method_name`) VALUES
('AlfaComponents', 'Bitcoin'),
('AlfaComponents', 'Credit card'),
('AlfaComponents', 'Pay sefe card'),
('AlfaComponents', 'Paypal'),
('Hennry\'s Builds', 'Credit card'),
('Hennry\'s Builds', 'Paypal');

-- --------------------------------------------------------

--
-- Struktura tabulky `shop_has_shippment_method`
--

CREATE TABLE `shop_has_shippment_method` (
  `shop_brand_name` varchar(45) COLLATE utf8_bin NOT NULL,
  `shippment_method_name` varchar(50) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `shop_has_shippment_method`
--

INSERT INTO `shop_has_shippment_method` (`shop_brand_name`, `shippment_method_name`) VALUES
('AlfaComponents', 'Economy'),
('AlfaComponents', 'Express'),
('AlfaComponents', 'Express plus'),
('AlfaComponents', 'Regular'),
('Hennry\'s Builds', 'Economy'),
('Hennry\'s Builds', 'Regular');

-- --------------------------------------------------------

--
-- Struktura tabulky `status`
--

CREATE TABLE `status` (
  `idstatus` int(11) NOT NULL,
  `name` varchar(45) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `status`
--

INSERT INTO `status` (`idstatus`, `name`) VALUES
(1, 'Accepted'),
(2, 'Wainting for payment'),
(3, 'Traveling'),
(4, 'Recived');

-- --------------------------------------------------------

--
-- Struktura tabulky `warehouse`
--

CREATE TABLE `warehouse` (
  `idwarehouse` int(11) NOT NULL,
  `contact_idcontact` int(11) NOT NULL,
  `company_name` varchar(50) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `warehouse`
--

INSERT INTO `warehouse` (`idwarehouse`, `contact_idcontact`, `company_name`) VALUES
(1, 2, 'Tech company'),
(2, 1, 'Tech company');

-- --------------------------------------------------------

--
-- Struktura tabulky `warehouse_has_item`
--

CREATE TABLE `warehouse_has_item` (
  `warehouse_idwarehouse` int(11) NOT NULL,
  `item_iditem` int(11) NOT NULL,
  `count` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Vypisuji data pro tabulku `warehouse_has_item`
--

INSERT INTO `warehouse_has_item` (`warehouse_idwarehouse`, `item_iditem`, `count`) VALUES
(1, 1, 50),
(1, 2, 50),
(2, 3, 50);

--
-- Klíče pro exportované tabulky
--

--
-- Klíče pro tabulku `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`username`),
  ADD KEY `contact_idcontact` (`contact_idcontact`);

--
-- Klíče pro tabulku `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`name`),
  ADD KEY `company_name` (`company_name`);

--
-- Klíče pro tabulku `choice`
--
ALTER TABLE `choice`
  ADD PRIMARY KEY (`idchoice`);

--
-- Klíče pro tabulku `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`name`),
  ADD KEY `account_username` (`account_username`);

--
-- Klíče pro tabulku `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`idcontact`);

--
-- Klíče pro tabulku `group`
--
ALTER TABLE `group`
  ADD PRIMARY KEY (`idgroup`);

--
-- Klíče pro tabulku `group_has_rights`
--
ALTER TABLE `group_has_rights`
  ADD PRIMARY KEY (`group_idgroup`,`rights_idrights`),
  ADD KEY `rights_idrights` (`rights_idrights`),
  ADD KEY `group_idgroup` (`group_idgroup`);

--
-- Klíče pro tabulku `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`iditem`),
  ADD KEY `shop_brand_name` (`shop_brand_name`);

--
-- Klíče pro tabulku `options`
--
ALTER TABLE `options`
  ADD PRIMARY KEY (`name`),
  ADD KEY `item_iditem` (`item_iditem`);

--
-- Klíče pro tabulku `options_has_choice`
--
ALTER TABLE `options_has_choice`
  ADD PRIMARY KEY (`options_name`,`choice_idchoice`),
  ADD KEY `choice_idchoice` (`choice_idchoice`),
  ADD KEY `option_name` (`options_name`);

--
-- Klíče pro tabulku `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`idorder`),
  ADD KEY `account_username` (`account_username`),
  ADD KEY `payment_method` (`payment_method_name`),
  ADD KEY `shippment_method` (`shippment_method_name`),
  ADD KEY `shop_brand_name` (`shop_brand_name`),
  ADD KEY `status_idstatus` (`status_idstatus`);

--
-- Klíče pro tabulku `order_has_item`
--
ALTER TABLE `order_has_item`
  ADD PRIMARY KEY (`order_idorder`,`item_iditem`),
  ADD KEY `item_iditem` (`item_iditem`),
  ADD KEY `order_idorder` (`order_idorder`);

--
-- Klíče pro tabulku `order_has_item_has_options`
--
ALTER TABLE `order_has_item_has_options`
  ADD PRIMARY KEY (`order_idorder`,`item_iditem`,`options_name`),
  ADD KEY `options_name` (`options_name`),
  ADD KEY `order_has_item` (`order_idorder`,`item_iditem`);

--
-- Klíče pro tabulku `payment_method`
--
ALTER TABLE `payment_method`
  ADD PRIMARY KEY (`name`);

--
-- Klíče pro tabulku `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`account_username`),
  ADD KEY `group_idgroup` (`group_idgroup`),
  ADD KEY `company_name` (`company_name`);

--
-- Klíče pro tabulku `rights`
--
ALTER TABLE `rights`
  ADD PRIMARY KEY (`idrights`);

--
-- Klíče pro tabulku `shippment_method`
--
ALTER TABLE `shippment_method`
  ADD PRIMARY KEY (`name`);

--
-- Klíče pro tabulku `shop`
--
ALTER TABLE `shop`
  ADD PRIMARY KEY (`brand_name`);

--
-- Klíče pro tabulku `shop_has_group`
--
ALTER TABLE `shop_has_group`
  ADD PRIMARY KEY (`shop_brand_name`,`group_idgroup`),
  ADD KEY `group_idgroup` (`group_idgroup`),
  ADD KEY `shop_brand_name` (`shop_brand_name`);

--
-- Klíče pro tabulku `shop_has_payment_method`
--
ALTER TABLE `shop_has_payment_method`
  ADD PRIMARY KEY (`shop_brand_name`,`payment_method_name`),
  ADD KEY `payment_method_name` (`payment_method_name`),
  ADD KEY `shop_brand_name` (`shop_brand_name`);

--
-- Klíče pro tabulku `shop_has_shippment_method`
--
ALTER TABLE `shop_has_shippment_method`
  ADD PRIMARY KEY (`shop_brand_name`,`shippment_method_name`),
  ADD KEY `shippment_method_name` (`shippment_method_name`),
  ADD KEY `shop_brand_name` (`shop_brand_name`);

--
-- Klíče pro tabulku `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`idstatus`);

--
-- Klíče pro tabulku `warehouse`
--
ALTER TABLE `warehouse`
  ADD PRIMARY KEY (`idwarehouse`),
  ADD KEY `contact_idcontact` (`contact_idcontact`),
  ADD KEY `company_name` (`company_name`);

--
-- Klíče pro tabulku `warehouse_has_item`
--
ALTER TABLE `warehouse_has_item`
  ADD PRIMARY KEY (`warehouse_idwarehouse`,`item_iditem`),
  ADD KEY `item_iditem` (`item_iditem`),
  ADD KEY `warebouse_idwarehouse` (`warehouse_idwarehouse`);

--
-- AUTO_INCREMENT pro tabulky
--

--
-- AUTO_INCREMENT pro tabulku `choice`
--
ALTER TABLE `choice`
  MODIFY `idchoice` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pro tabulku `contact`
--
ALTER TABLE `contact`
  MODIFY `idcontact` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pro tabulku `group`
--
ALTER TABLE `group`
  MODIFY `idgroup` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pro tabulku `item`
--
ALTER TABLE `item`
  MODIFY `iditem` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pro tabulku `order`
--
ALTER TABLE `order`
  MODIFY `idorder` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pro tabulku `rights`
--
ALTER TABLE `rights`
  MODIFY `idrights` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pro tabulku `status`
--
ALTER TABLE `status`
  MODIFY `idstatus` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pro tabulku `warehouse`
--
ALTER TABLE `warehouse`
  MODIFY `idwarehouse` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Omezení pro exportované tabulky
--

--
-- Omezení pro tabulku `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `fk_account_contact` FOREIGN KEY (`contact_idcontact`) REFERENCES `contact` (`idcontact`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `brand`
--
ALTER TABLE `brand`
  ADD CONSTRAINT `fk_brand_company1` FOREIGN KEY (`company_name`) REFERENCES `company` (`name`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `company`
--
ALTER TABLE `company`
  ADD CONSTRAINT `fk_company_account1` FOREIGN KEY (`account_username`) REFERENCES `account` (`username`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `group_has_rights`
--
ALTER TABLE `group_has_rights`
  ADD CONSTRAINT `fk_group_has_rights_group1` FOREIGN KEY (`group_idgroup`) REFERENCES `group` (`idgroup`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_group_has_rights_rights1` FOREIGN KEY (`rights_idrights`) REFERENCES `rights` (`idrights`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `item`
--
ALTER TABLE `item`
  ADD CONSTRAINT `fk_item_shop1` FOREIGN KEY (`shop_brand_name`) REFERENCES `shop` (`brand_name`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `options`
--
ALTER TABLE `options`
  ADD CONSTRAINT `fk_options_item1` FOREIGN KEY (`item_iditem`) REFERENCES `item` (`iditem`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `options_has_choice`
--
ALTER TABLE `options_has_choice`
  ADD CONSTRAINT `fk_options_has_choice_choice1` FOREIGN KEY (`choice_idchoice`) REFERENCES `choice` (`idchoice`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_options_has_choice_options1` FOREIGN KEY (`options_name`) REFERENCES `options` (`name`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `fk_order_account1` FOREIGN KEY (`account_username`) REFERENCES `account` (`username`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_order_payment_method1` FOREIGN KEY (`payment_method_name`) REFERENCES `payment_method` (`name`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_order_shippment_method1` FOREIGN KEY (`shippment_method_name`) REFERENCES `shippment_method` (`name`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_order_shop1` FOREIGN KEY (`shop_brand_name`) REFERENCES `shop` (`brand_name`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_order_status1` FOREIGN KEY (`status_idstatus`) REFERENCES `status` (`idstatus`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `order_has_item`
--
ALTER TABLE `order_has_item`
  ADD CONSTRAINT `fk_order_has_item_item1` FOREIGN KEY (`item_iditem`) REFERENCES `item` (`iditem`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_order_has_item_order1` FOREIGN KEY (`order_idorder`) REFERENCES `order` (`idorder`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `order_has_item_has_options`
--
ALTER TABLE `order_has_item_has_options`
  ADD CONSTRAINT `fk_order_has_item_has_options_options1` FOREIGN KEY (`options_name`) REFERENCES `options` (`name`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_order_has_item_has_options_order_has_item1` FOREIGN KEY (`order_idorder`,`item_iditem`) REFERENCES `order_has_item` (`order_idorder`, `item_iditem`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `person`
--
ALTER TABLE `person`
  ADD CONSTRAINT `fk_person_account1` FOREIGN KEY (`account_username`) REFERENCES `account` (`username`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_person_company1` FOREIGN KEY (`company_name`) REFERENCES `company` (`name`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_person_group1` FOREIGN KEY (`group_idgroup`) REFERENCES `group` (`idgroup`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `shop`
--
ALTER TABLE `shop`
  ADD CONSTRAINT `fk_shop_brand1` FOREIGN KEY (`brand_name`) REFERENCES `brand` (`name`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `shop_has_group`
--
ALTER TABLE `shop_has_group`
  ADD CONSTRAINT `fk_shop_has_group_group1` FOREIGN KEY (`group_idgroup`) REFERENCES `group` (`idgroup`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_shop_has_group_shop1` FOREIGN KEY (`shop_brand_name`) REFERENCES `shop` (`brand_name`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `shop_has_payment_method`
--
ALTER TABLE `shop_has_payment_method`
  ADD CONSTRAINT `fk_shop_has_payment_method_payment_method1` FOREIGN KEY (`payment_method_name`) REFERENCES `payment_method` (`name`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_shop_has_payment_method_shop1` FOREIGN KEY (`shop_brand_name`) REFERENCES `shop` (`brand_name`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `shop_has_shippment_method`
--
ALTER TABLE `shop_has_shippment_method`
  ADD CONSTRAINT `fk_shop_has_shippment_method_shippment_method1` FOREIGN KEY (`shippment_method_name`) REFERENCES `shippment_method` (`name`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_shop_has_shippment_method_shop1` FOREIGN KEY (`shop_brand_name`) REFERENCES `shop` (`brand_name`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `warehouse`
--
ALTER TABLE `warehouse`
  ADD CONSTRAINT `fk_warehouse_company1` FOREIGN KEY (`company_name`) REFERENCES `company` (`name`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_warehouse_contact1` FOREIGN KEY (`contact_idcontact`) REFERENCES `contact` (`idcontact`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Omezení pro tabulku `warehouse_has_item`
--
ALTER TABLE `warehouse_has_item`
  ADD CONSTRAINT `fk_warehouse_has_item_item1` FOREIGN KEY (`item_iditem`) REFERENCES `item` (`iditem`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_warehouse_has_item_warehouse1` FOREIGN KEY (`warehouse_idwarehouse`) REFERENCES `warehouse` (`idwarehouse`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 14, 2025 at 01:40 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1productpricedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `booktb`
--

CREATE TABLE `booktb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `Bookid` varchar(250) NOT NULL,
  `Qty` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `CardName` varchar(250) NOT NULL,
  `CardNo` varchar(250) NOT NULL,
  `CvNo` varchar(250) NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `booktb`
--

INSERT INTO `booktb` (`id`, `UserName`, `Bookid`, `Qty`, `Amount`, `CardName`, `CardNo`, `CvNo`, `Date`) VALUES
(1, 'mark', 'BOOKID1', '2.00', '50000.00', 'mastercard', '1234567899874563', '159', '2025-02-11');

-- --------------------------------------------------------

--
-- Table structure for table `carttb`
--

CREATE TABLE `carttb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `ProductType` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `Qty` decimal(18,2) NOT NULL,
  `TPrice` decimal(28,2) NOT NULL,
  `Image` varchar(500) NOT NULL,
  `Date` date NOT NULL,
  `Status` varchar(250) NOT NULL,
  `Bookid` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `Astatus` varchar(250) NOT NULL,
  `Specs` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `carttb`
--

INSERT INTO `carttb` (`id`, `UserName`, `ProductName`, `ProductType`, `Price`, `Qty`, `TPrice`, `Image`, `Date`, `Status`, `Bookid`, `Mobile`, `Address`, `Astatus`, `Specs`) VALUES
(2, 'mark', 'Realme 13 Pro', 'Girls', '25000', '2.00', '50000.00', '-original-imah38dbntayzhpk.webp', '2025-02-11', '1', 'BOOKID1', '24', 'javaprojectfantasy@gmail.com', 'waiting', '8Gb/256Gb');

-- --------------------------------------------------------



--
-- Table structure for table `protb1`
--

CREATE TABLE `protb1` (
  `pid` bigint(250) NOT NULL auto_increment,
  `Pname` varchar(250) NOT NULL,
  `Type` varchar(250) NOT NULL,
  `Info` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `Image` varchar(250) NOT NULL,
  PRIMARY KEY  (`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `protb1`
--

INSERT INTO `protb1` (`pid`, `Pname`, `Type`, `Info`, `Price`, `Image`) VALUES
(1, 'Realme 13 Pro', 'Android', 'nil', '10000', 'banner123.png'),
(2, 'Vivo v29', 'Android', 'nil', '10000', '1721637871Dengunilvati1.png'),
(3, 'Realme 13 Pro plus', 'Android', 'nil', '20000', '6605ab.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(250) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Age`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'mark', '24', '9087254568', 'javaprojectfantasy@gmail.com', 'Trichy', 'mark', 'mark');

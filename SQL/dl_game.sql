-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 09, 2020 at 05:58 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dl_game`
--

-- --------------------------------------------------------

--
-- Table structure for table `customgame`
--

CREATE TABLE `customgame` (
  `Name` varchar(20) NOT NULL,
  `Correct` int(11) NOT NULL,
  `total_questions` int(11) NOT NULL,
  `Percentage` int(3) NOT NULL,
  `Mode` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customgame`
--

INSERT INTO `customgame` (`Name`, `Correct`, `total_questions`, `Percentage`, `Mode`) VALUES
('Sri', 5, 6, 83, 'Easy'),
('Queen', 9, 12, 75, 'Medium'),
('King', 4, 7, 57, 'Hard'),
('Lorie', 6, 7, 85, 'Easy'),
('Khan', 6, 11, 54, 'Medium'),
('Ching', 3, 4, 75, 'Easy'),
('Saitama', 3, 5, 60, 'Medium'),
('Lili', 2, 4, 50, 'Hard');

-- --------------------------------------------------------

--
-- Table structure for table `quickgame`
--

CREATE TABLE `quickgame` (
  `Name` varchar(20) NOT NULL,
  `Correct` int(11) NOT NULL,
  `total_questions` int(11) NOT NULL,
  `Percentage` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `quickgame`
--

INSERT INTO `quickgame` (`Name`, `Correct`, `total_questions`, `Percentage`) VALUES
('Sri', 4, 5, 80),
('Daniel', 5, 5, 100),
('Gadhi', 4, 5, 80),
('Blast', 3, 5, 60);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

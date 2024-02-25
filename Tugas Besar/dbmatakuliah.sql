-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 19, 2024 at 07:47 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbmatakuliah`
--

-- --------------------------------------------------------

--
-- Table structure for table `kuliah1`
--

CREATE TABLE `kuliah1` (
  `ID` int(11) NOT NULL,
  `Semester` enum('Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Mata_Kuliah` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `SKS` int(24) NOT NULL,
  `Kelas` enum('TIF21A','TIF21B','TIF21C','TIF21D','TIF21E','TIF21K','TIF21L','TIF22A','TIF22B','TIF22C','TIF22D','TIF22E','TIF22K','TIF22L','TIF23A','TIF23B','TIF23C','TIF23D','TIF23E','TIF23K','TIF23L') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `kuliah2`
--

CREATE TABLE `kuliah2` (
  `ID` int(11) NOT NULL,
  `Semester` enum('Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Mata_Kuliah` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `SKS` int(24) NOT NULL,
  `Kelas` enum('TIF22A','TIF22B','TIF22C','TIF22D','TIF22E','TIF22K','TIF22L','TIF23A','TIF23B','TIF23C','TIF23D','TIF23E','TIF23K','TIF23L','TIF21A','TIF21B','TIF21C','TIF21D','TIF21E','TIF21K','TIF21L') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `kuliah3`
--

CREATE TABLE `kuliah3` (
  `ID` int(11) NOT NULL,
  `Semester` enum('Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Mata_Kuliah` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `SKS` int(24) NOT NULL,
  `Kelas` enum('TIF21A','TIF21B','TIF21C','TIF21D','TIF21E','TIF21K','TIF21L','TIF22A','TIF22B','TIF22C','TIF22D','TIF22E','TIF22K','TIF22L','TIF23A','TIF23B','TIF23C','TIF23D','TIF23E','TIF23K','TIF23L') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `kuliah4`
--

CREATE TABLE `kuliah4` (
  `ID` int(11) NOT NULL,
  `Semester` enum('Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Mata_Kuliah` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `SKS` int(24) NOT NULL,
  `Kelas` enum('TIF21A','TIF21B','TIF21C','TIF21D','TIF21E','TIF21K','TIF21L','TIF22A','TIF22B','TIF22C','TIF22D','TIF22E','TIF22K','TIF22L','TIF23A','TIF23B','TIF23C','TIF23D','TIF23E','TIF23K','TIF23L') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `kuliah5`
--

CREATE TABLE `kuliah5` (
  `ID` int(11) NOT NULL,
  `Semester` enum('Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Mata_Kuliah` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `SKS` int(24) NOT NULL,
  `Kelas` enum('TIF21A','TIF21B','TIF21C','TIF21D','TIF21E','TIF21K','TIF21L','TIF22A','TIF22B','TIF22C','TIF22D','TIF22E','TIF22K','TIF22L','TIF23A','TIF23B','TIF23C','TIF23D','TIF23E','TIF23K','TIF23L') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `kuliah6`
--

CREATE TABLE `kuliah6` (
  `ID` int(11) NOT NULL,
  `Semester` enum('Semester 1','Semester 2','Semester 3','Semester 4','Semester 5','Semester 6','Semester 7','Semester 8') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Mata_Kuliah` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `SKS` int(24) NOT NULL,
  `Kelas` enum('TIF21A','TIF21B','TIF21C','TIF21D','TIF21E','TIF21K','TIF21L','TIF22A','TIF22B','TIF22C','TIF22D','TIF22E','TIF22K','TIF22L','TIF23A','TIF23B','TIF23C','TIF23D','TIF23E','TIF23K','TIF23L') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kuliah1`
--
ALTER TABLE `kuliah1`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `kuliah2`
--
ALTER TABLE `kuliah2`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `kuliah3`
--
ALTER TABLE `kuliah3`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `kuliah4`
--
ALTER TABLE `kuliah4`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `kuliah5`
--
ALTER TABLE `kuliah5`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `kuliah6`
--
ALTER TABLE `kuliah6`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kuliah1`
--
ALTER TABLE `kuliah1`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `kuliah2`
--
ALTER TABLE `kuliah2`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `kuliah3`
--
ALTER TABLE `kuliah3`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `kuliah4`
--
ALTER TABLE `kuliah4`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `kuliah5`
--
ALTER TABLE `kuliah5`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `kuliah6`
--
ALTER TABLE `kuliah6`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

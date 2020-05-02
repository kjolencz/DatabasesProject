-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 02, 2020 at 09:43 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `a_id` int(11) NOT NULL,
  `a_startTime` time NOT NULL,
  `a_endTime` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`a_id`, `a_startTime`, `a_endTime`) VALUES
(0, '02:00:00', '03:00:00'),
(1, '02:00:00', '02:30:00'),
(3, '04:00:00', '05:00:00'),
(10, '03:00:00', '00:00:00'),
(11, '01:12:00', '01:13:00'),
(12, '02:00:00', '03:00:00'),
(14, '12:00:00', '11:00:00'),
(22, '03:00:00', '00:00:22'),
(39, '10:00:00', '11:45:00'),
(69, '03:00:00', '00:00:04'),
(111, '04:00:00', '08:00:00'),
(123, '03:00:00', '13:00:00'),
(999, '10:00:00', '11:00:00'),
(1111, '00:00:01', '00:00:02'),
(1234, '00:22:00', '00:33:00'),
(11111, '00:00:00', '00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `bill_id` int(11) NOT NULL,
  `bill_amount` float NOT NULL,
  `bill_isPaid` tinyint(1) NOT NULL,
  `bill_isuee` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`bill_id`, `bill_amount`, `bill_isPaid`, `bill_isuee`) VALUES
(0, 100.01, 0, ''),
(333, 333, 1, 'BOEBODHOD'),
(456, 456, 1, 'Heiii'),
(1234, 100, 0, 'Bob Boil'),
(1235, 100, 1, 'Bob Boil');

-- --------------------------------------------------------

--
-- Table structure for table `building`
--

CREATE TABLE `building` (
  `b_id` int(11) NOT NULL,
  `b_name` varchar(15) NOT NULL,
  `b_capacity` smallint(6) NOT NULL,
  `b_numRooms` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `building`
--

INSERT INTO `building` (`b_id`, `b_name`, `b_capacity`, `b_numRooms`) VALUES
(123456, 'Emergency Room ', 250, 45);

-- --------------------------------------------------------

--
-- Table structure for table `custodian`
--

CREATE TABLE `custodian` (
  `c_id` int(11) NOT NULL,
  `c_firstName` varchar(15) NOT NULL,
  `c_lastName` varchar(15) NOT NULL,
  `c_middleIn` char(1) NOT NULL,
  `c_gender` char(1) NOT NULL,
  `c_salary` int(11) NOT NULL,
  `c_phoneNum` varchar(15) NOT NULL,
  `c_ssn` int(9) NOT NULL,
  `c_startDate` date NOT NULL,
  `c_endDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `d_id` int(11) NOT NULL,
  `d_name` varchar(30) NOT NULL,
  `d_numEmployees` smallint(6) NOT NULL,
  `d_managerFullName` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`d_id`, `d_name`, `d_numEmployees`, `d_managerFullName`) VALUES
(0, 'Test', 1, 'Manager M Manger');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `doc_id` int(11) NOT NULL,
  `doc_firstName` varchar(15) NOT NULL,
  `doc_lastName` varchar(15) NOT NULL,
  `doc_middleIn` char(1) NOT NULL,
  `doc_gender` char(1) NOT NULL,
  `doc_salary` int(11) NOT NULL,
  `doc_phoneNum` varchar(15) NOT NULL,
  `doc_ssn` int(9) NOT NULL,
  `doc_startDate` date NOT NULL,
  `doc_endDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`doc_id`, `doc_firstName`, `doc_lastName`, `doc_middleIn`, `doc_gender`, `doc_salary`, `doc_phoneNum`, `doc_ssn`, `doc_startDate`, `doc_endDate`) VALUES
(1, 'Mike', 'Mikelson', 'M', 'M', 0, '444-444-4444', 444444444, '4444-04-04', '4444-05-05');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL,
  `employee_deptId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employee_id`, `employee_deptId`) VALUES
(0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `equipment`
--

CREATE TABLE `equipment` (
  `eq_id` int(11) NOT NULL,
  `eq_desc` varchar(30) NOT NULL,
  `eq_name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `equipment`
--

INSERT INTO `equipment` (`eq_id`, `eq_desc`, `eq_name`) VALUES
(1, '1', '1'),
(2, 'REEE', 'Retardonator'),
(3, 'bongo', 'bingo'),
(4, '4', '4'),
(123, '1121', '111');

-- --------------------------------------------------------

--
-- Table structure for table `medical record`
--

CREATE TABLE `medical record` (
  `mr_id` int(11) NOT NULL,
  `mr_pastIllnesses` varchar(100) NOT NULL,
  `mr_allergies` varchar(100) NOT NULL,
  `mr_fn` varchar(15) NOT NULL,
  `mr_mi` char(1) NOT NULL,
  `mr_ln` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medical record`
--

INSERT INTO `medical record` (`mr_id`, `mr_pastIllnesses`, `mr_allergies`, `mr_fn`, `mr_mi`, `mr_ln`) VALUES
(1, 'Test', 'Test', 'Test', 'T', 'Tester'),
(22, 'A', 'A', 'A', 'A', 'A'),
(3333, 'r', 'r', 'r', 'r', 'r'),
(12345, 'TEST', 'TEST', 'TESt', 'T', 'TEST');

-- --------------------------------------------------------

--
-- Table structure for table `nurse`
--

CREATE TABLE `nurse` (
  `n_id` int(11) NOT NULL,
  `n_firstName` varchar(15) NOT NULL,
  `n_lastName` varchar(15) NOT NULL,
  `n_middleIn` char(1) NOT NULL,
  `n_gender` char(1) NOT NULL,
  `n_salary` int(11) NOT NULL,
  `n_phoneNum` varchar(15) NOT NULL,
  `n_ssn` int(9) NOT NULL,
  `n_startDate` date NOT NULL,
  `n_endDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `p_id` int(11) NOT NULL,
  `p_firstName` varchar(15) NOT NULL,
  `p_lastName` varchar(15) NOT NULL,
  `p_middleIn` char(1) NOT NULL,
  `p_gender` char(1) NOT NULL,
  `p_phoneNum` varchar(15) NOT NULL,
  `p_ssn` int(9) NOT NULL,
  `p_admissionDate` date NOT NULL,
  `p_releaseDate` date NOT NULL,
  `p_insuranceName` varchar(15) NOT NULL,
  `p_insuranceNum` int(11) NOT NULL,
  `p_buildingNum` smallint(6) NOT NULL,
  `p_roomNum` smallint(6) NOT NULL,
  `p_medicalRecordId` int(11) NOT NULL,
  `p_billId` int(11) NOT NULL,
  `p_appointmentId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`p_id`, `p_firstName`, `p_lastName`, `p_middleIn`, `p_gender`, `p_phoneNum`, `p_ssn`, `p_admissionDate`, `p_releaseDate`, `p_insuranceName`, `p_insuranceNum`, `p_buildingNum`, `p_roomNum`, `p_medicalRecordId`, `p_billId`, `p_appointmentId`) VALUES
(0, 'Test', 'Testerton', 'T', 'M', '410-111-1111', 101010100, '0000-00-00', '0000-00-00', 'Insurance Test', 100, 0, 0, 100, 100, 100),
(12345, 'Kevin', 'Olen', 'J', 'M', '444-444-4444', 222, '2016-10-10', '2016-10-10', 'Allstate', 12, 13, 14, 15, 16, 17);

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `currentPatient_id` int(11) NOT NULL,
  `room_number` smallint(6) NOT NULL,
  `room_type` varchar(30) NOT NULL,
  `room_capacity` smallint(6) NOT NULL,
  `room_vacant` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`currentPatient_id`, `room_number`, `room_type`, `room_capacity`, `room_vacant`) VALUES
(1, 123, 'High risk patient ro', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `secretary`
--

CREATE TABLE `secretary` (
  `s_id` int(11) NOT NULL,
  `s_firstName` varchar(15) NOT NULL,
  `s_lastName` varchar(15) NOT NULL,
  `s_middleIn` char(1) NOT NULL,
  `s_gender` char(1) NOT NULL,
  `s_salary` int(11) NOT NULL,
  `s_phoneNumber` varchar(15) NOT NULL,
  `s_ssn` int(9) NOT NULL,
  `s_startDate` date NOT NULL,
  `s_endDate` date NOT NULL DEFAULT '1800-01-01'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `secretary`
--

INSERT INTO `secretary` (`s_id`, `s_firstName`, `s_lastName`, `s_middleIn`, `s_gender`, `s_salary`, `s_phoneNumber`, `s_ssn`, `s_startDate`, `s_endDate`) VALUES
(0, 'Test', 'Tester', 'T', 'M', 1000, '100-100-1234', 1234567890, '2000-10-10', '1800-01-01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`a_id`);

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`bill_id`);

--
-- Indexes for table `building`
--
ALTER TABLE `building`
  ADD PRIMARY KEY (`b_id`);

--
-- Indexes for table `custodian`
--
ALTER TABLE `custodian`
  ADD PRIMARY KEY (`c_id`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`d_id`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`doc_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`employee_id`);

--
-- Indexes for table `equipment`
--
ALTER TABLE `equipment`
  ADD PRIMARY KEY (`eq_id`);

--
-- Indexes for table `medical record`
--
ALTER TABLE `medical record`
  ADD PRIMARY KEY (`mr_id`);

--
-- Indexes for table `nurse`
--
ALTER TABLE `nurse`
  ADD PRIMARY KEY (`n_id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`p_id`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`currentPatient_id`);

--
-- Indexes for table `secretary`
--
ALTER TABLE `secretary`
  ADD PRIMARY KEY (`s_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 04, 2020 at 07:56 PM
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
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `a_patientId` int(11) NOT NULL,
  `a_id` smallint(6) NOT NULL,
  `a_roomNum` smallint(6) NOT NULL,
  `a_startTime` time NOT NULL,
  `a_date` date NOT NULL,
  `a_doctor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`a_patientId`, `a_id`, `a_roomNum`, `a_startTime`, `a_date`, `a_doctor`) VALUES
(12, 12, 12, '12:00:00', '1212-12-12', 12),
(13, 13, 13, '00:00:13', '0000-00-00', 13);

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `bill_id` smallint(6) NOT NULL,
  `bill_amount` float NOT NULL,
  `bill_patientId` int(11) NOT NULL,
  `bill_issue` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`bill_id`, `bill_amount`, `bill_patientId`, `bill_issue`) VALUES
(12, 13, 13, '13');

-- --------------------------------------------------------

--
-- Table structure for table `building`
--

CREATE TABLE `building` (
  `b_id` int(11) NOT NULL,
  `b_name` varchar(15) NOT NULL,
  `b_capacity` smallint(6) NOT NULL,
  `b_numRooms` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `building`
--

INSERT INTO `building` (`b_id`, `b_name`, `b_capacity`, `b_numRooms`) VALUES
(12, '12', 12, 12),
(13, '13', 13, 13);

-- --------------------------------------------------------

--
-- Table structure for table `custodian`
--

CREATE TABLE `custodian` (
  `c_title` varchar(9) DEFAULT 'Custodian',
  `c_ssn` int(9) NOT NULL,
  `c_id` int(11) NOT NULL,
  `c_salary` int(11) NOT NULL,
  `c_departmentId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `custodian`
--

INSERT INTO `custodian` (`c_title`, `c_ssn`, `c_id`, `c_salary`, `c_departmentId`) VALUES
('12', 12, 12, 12, 12);

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `d_name` varchar(15) NOT NULL,
  `d_id` int(11) NOT NULL,
  `d_buildingId` int(11) NOT NULL,
  `d_managerId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `distributor`
--

CREATE TABLE `distributor` (
  `dist_name` varchar(15) NOT NULL,
  `dist_product` varchar(30) NOT NULL,
  `dist_id` int(11) NOT NULL,
  `dist_department` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `distributor`
--

INSERT INTO `distributor` (`dist_name`, `dist_product`, `dist_id`, `dist_department`) VALUES
('12', '12', 12, 12);

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `doc_title` varchar(6) NOT NULL,
  `doc_ssn` int(9) NOT NULL,
  `doc_id` int(11) NOT NULL,
  `doc_salary` int(11) NOT NULL,
  `doc_departmentId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`doc_title`, `doc_ssn`, `doc_id`, `doc_salary`, `doc_departmentId`) VALUES
('Docte', 9, 9, 9, 12),
('10', 10, 10, 10, 10),
('Doc', 121212121, 12, 12, 12),
('Test', 131313131, 13, 13, 13);

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL,
  `employee_ssn` int(9) NOT NULL,
  `employee_firstName` varchar(15) NOT NULL,
  `employee_middleIn` char(1) NOT NULL,
  `employee_lastName` varchar(15) NOT NULL,
  `employee_hired` date NOT NULL,
  `employee_gender` char(1) NOT NULL,
  `employee_phone` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employee_id`, `employee_ssn`, `employee_firstName`, `employee_middleIn`, `employee_lastName`, `employee_hired`, `employee_gender`, `employee_phone`) VALUES
(7, 7, '7', '7', '7', '1010-10-10', 'M', '8'),
(8, 8, '8', '8', '8', '0000-00-00', '8', '8'),
(9, 9, '9', '9', '9', '0000-00-00', '9', '9'),
(10, 10, '10', '1', '10', '0000-00-00', '1', '10'),
(12, 121212121, 'Test', 'T', 'Test', '1212-12-12', 'M', '121-121-1212'),
(13, 131313131, 'Test', 'T', 'Test', '1313-10-10', 'F', '131-131-1313');

-- --------------------------------------------------------

--
-- Table structure for table `equipment`
--

CREATE TABLE `equipment` (
  `eq_id` int(11) NOT NULL,
  `eq_desc` varchar(30) NOT NULL,
  `eq_name` varchar(30) NOT NULL,
  `eq_room` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `equipment`
--

INSERT INTO `equipment` (`eq_id`, `eq_desc`, `eq_name`, `eq_room`) VALUES
(12, '12', '12', 12),
(13, '13', '13', 13);

-- --------------------------------------------------------

--
-- Table structure for table `hours`
--

CREATE TABLE `hours` (
  `h_shiftId` int(11) NOT NULL,
  `h_employeeId` int(11) NOT NULL,
  `h_hoursScheduled` int(3) NOT NULL,
  `h_dateScheduled` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `medicalrecord`
--

CREATE TABLE `medicalrecord` (
  `mr_id` int(11) NOT NULL,
  `mr_patientId` int(9) NOT NULL,
  `mr_pastAppointment` smallint(6) NOT NULL,
  `mr_bloodType` varchar(4) NOT NULL,
  `mr_alLergies` varchar(100) NOT NULL,
  `mr_pastIllnesses` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medicalrecord`
--

INSERT INTO `medicalrecord` (`mr_id`, `mr_patientId`, `mr_pastAppointment`, `mr_bloodType`, `mr_alLergies`, `mr_pastIllnesses`) VALUES
(12, 12, 12, 'O', 'Water', 'Ebola ');

-- --------------------------------------------------------

--
-- Table structure for table `nurse`
--

CREATE TABLE `nurse` (
  `nurse_id` int(11) NOT NULL,
  `nurse_ssn` int(9) NOT NULL,
  `nurse_title` varchar(5) DEFAULT 'Nurse',
  `nurse_worksRoom` smallint(6) NOT NULL,
  `nurse_salary` int(10) NOT NULL,
  `nurse_departmentId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nurse`
--

INSERT INTO `nurse` (`nurse_id`, `nurse_ssn`, `nurse_title`, `nurse_worksRoom`, `nurse_salary`, `nurse_departmentId`) VALUES
(12, 12, '12', 12, 12, 12);

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `p_firstName` varchar(15) NOT NULL,
  `p_middleIn` char(1) DEFAULT NULL,
  `p_lastName` varchar(15) NOT NULL,
  `p_gender` char(1) NOT NULL,
  `p_ssn` int(9) NOT NULL,
  `p_insuranceNum` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `p_phoneNum` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`p_firstName`, `p_middleIn`, `p_lastName`, `p_gender`, `p_ssn`, `p_insuranceNum`, `p_id`, `p_phoneNum`) VALUES
('Test', 'T', 'Tester', 'M', 1234567, 12, 10, '123-456-7890'),
('Test', 'T', 'Test', 'M', 121212121, 12, 12, '122-122-1212'),
('Test1', 'T', 'Test1', 'M', 131313131, 13, 13, '131-131-1313');

-- --------------------------------------------------------

--
-- Table structure for table `perscription`
--

CREATE TABLE `perscription` (
  `persc_id` int(11) NOT NULL,
  `persc_medicineName` varchar(15) NOT NULL,
  `persc_distributorId` int(11) NOT NULL,
  `persc_forPatient` int(11) NOT NULL,
  `persc_perscribedBy` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `perscription`
--

INSERT INTO `perscription` (`persc_id`, `persc_medicineName`, `persc_distributorId`, `persc_forPatient`, `persc_perscribedBy`) VALUES
(9, 'nine', 9, 12, 12);

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `currentPatient_id` int(11) DEFAULT NULL,
  `room_number` smallint(6) NOT NULL,
  `room_type` varchar(30) NOT NULL,
  `room_capacity` varchar(20) NOT NULL,
  `room_vacant` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`currentPatient_id`, `room_number`, `room_type`, `room_capacity`, `room_vacant`) VALUES
(12, 12, 'Test', '12', '0'),
(13, 13, 'Test', '13', '0'),
(13, 14, '14', '14', '0');

-- --------------------------------------------------------

--
-- Table structure for table `secretary`
--

CREATE TABLE `secretary` (
  `s_title` varchar(9) DEFAULT 'Secretary',
  `s_ssn` int(9) NOT NULL,
  `s_id` int(11) NOT NULL,
  `s_worksRoom` smallint(6) NOT NULL,
  `s_salary` int(11) NOT NULL,
  `s_departmentId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`a_id`),
  ADD KEY `a_patientId` (`a_patientId`),
  ADD KEY `a_roomNum` (`a_roomNum`),
  ADD KEY `a_doctor` (`a_doctor`);

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`bill_id`),
  ADD KEY `bill_patientId` (`bill_patientId`);

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
  ADD PRIMARY KEY (`d_id`),
  ADD KEY `d_buildingId` (`d_buildingId`),
  ADD KEY `d_managerId` (`d_managerId`);

--
-- Indexes for table `distributor`
--
ALTER TABLE `distributor`
  ADD PRIMARY KEY (`dist_id`,`dist_product`);

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
  ADD PRIMARY KEY (`eq_id`),
  ADD KEY `eq_room` (`eq_room`);

--
-- Indexes for table `hours`
--
ALTER TABLE `hours`
  ADD PRIMARY KEY (`h_shiftId`);

--
-- Indexes for table `medicalrecord`
--
ALTER TABLE `medicalrecord`
  ADD PRIMARY KEY (`mr_id`),
  ADD KEY `mr_patientId` (`mr_patientId`),
  ADD KEY `mr_pastAppointment` (`mr_pastAppointment`);

--
-- Indexes for table `nurse`
--
ALTER TABLE `nurse`
  ADD PRIMARY KEY (`nurse_id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`p_id`);

--
-- Indexes for table `perscription`
--
ALTER TABLE `perscription`
  ADD PRIMARY KEY (`persc_id`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`room_number`),
  ADD KEY `currentPatient_id` (`currentPatient_id`);

--
-- Indexes for table `secretary`
--
ALTER TABLE `secretary`
  ADD PRIMARY KEY (`s_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointment`
--
ALTER TABLE `appointment`
  ADD CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`a_patientId`) REFERENCES `patient` (`p_id`),
  ADD CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`a_roomNum`) REFERENCES `room` (`room_number`),
  ADD CONSTRAINT `appointment_ibfk_3` FOREIGN KEY (`a_doctor`) REFERENCES `employee` (`employee_id`);

--
-- Constraints for table `bill`
--
ALTER TABLE `bill`
  ADD CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`bill_patientId`) REFERENCES `patient` (`p_id`);

--
-- Constraints for table `department`
--
ALTER TABLE `department`
  ADD CONSTRAINT `department_ibfk_1` FOREIGN KEY (`d_buildingId`) REFERENCES `building` (`b_id`),
  ADD CONSTRAINT `department_ibfk_2` FOREIGN KEY (`d_managerId`) REFERENCES `employee` (`employee_id`);

--
-- Constraints for table `equipment`
--
ALTER TABLE `equipment`
  ADD CONSTRAINT `equipment_ibfk_1` FOREIGN KEY (`eq_room`) REFERENCES `room` (`room_number`);

--
-- Constraints for table `medicalrecord`
--
ALTER TABLE `medicalrecord`
  ADD CONSTRAINT `medicalrecord_ibfk_1` FOREIGN KEY (`mr_patientId`) REFERENCES `patient` (`p_id`),
  ADD CONSTRAINT `medicalrecord_ibfk_2` FOREIGN KEY (`mr_pastAppointment`) REFERENCES `appointment` (`a_id`);

--
-- Constraints for table `room`
--
ALTER TABLE `room`
  ADD CONSTRAINT `room_ibfk_1` FOREIGN KEY (`currentPatient_id`) REFERENCES `patient` (`p_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

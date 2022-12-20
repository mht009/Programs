CREATE DATABASE  IF NOT EXISTS `cs2020_21` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cs2020_21`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: cs2020_21
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `Billno` int NOT NULL,
  `Patient_Name` varchar(20) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Billno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (2,'Rahul','2021-01-26'),(3,'Pamesh','2021-01-26'),(4,'Rahul Choudhary','2021-01-27'),(5,'Rhaul Choubey','2021-01-27'),(6,'RAghav Juyal','2021-01-27'),(7,'Amir','2021-01-27'),(8,'Maruti','2021-01-27'),(9,'Radha','2021-01-27'),(10,'Ramesh','2021-01-27'),(11,'RAghav','2021-01-27');
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `Book_Id` varchar(6) NOT NULL,
  `Book_Name` varchar(20) DEFAULT NULL,
  `Author_Name` varchar(20) DEFAULT NULL,
  `Publisher` varchar(15) DEFAULT NULL,
  `Price` int DEFAULT NULL,
  `Type` varchar(15) DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  PRIMARY KEY (`Book_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('C0001','Fast Cook','Lata Kapoor','EPB',405,'Cookery',5),('F0001','The Tears','William Hopkins','First Publ.',650,'Fiction',20),('F0002','Thunderbolts','Anna Roberts','First Publ.',750,'Fiction',50),('T0001','My First C++','Brian & Brooke','EPB',400,'Text',10),('T0002','C++ Brainworks','A.W. Rossaine','TDH',350,'Text',15);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_issued`
--

DROP TABLE IF EXISTS `books_issued`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_issued` (
  `Book_Id` varchar(6) DEFAULT NULL,
  `Quantity_Issued` int DEFAULT NULL,
  KEY `Book_Id` (`Book_Id`),
  CONSTRAINT `books_issued_ibfk_1` FOREIGN KEY (`Book_Id`) REFERENCES `books` (`Book_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_issued`
--

LOCK TABLES `books_issued` WRITE;
/*!40000 ALTER TABLE `books_issued` DISABLE KEYS */;
INSERT INTO `books_issued` VALUES ('T0001',4),('C0001',5),('F0001',2);
/*!40000 ALTER TABLE `books_issued` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dept`
--

DROP TABLE IF EXISTS `dept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dept` (
  `Dcode` varchar(4) NOT NULL,
  `Department` varchar(15) DEFAULT NULL,
  `City` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`Dcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dept`
--

LOCK TABLES `dept` WRITE;
/*!40000 ALTER TABLE `dept` DISABLE KEYS */;
INSERT INTO `dept` VALUES ('D01','Media','Delhi'),('D02','Marketing','Delhi'),('D03','Infrastucture','Mumbai'),('D04','Human Resource','Mumbai'),('D05','Finance','Kolkata');
/*!40000 ALTER TABLE `dept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empl`
--

DROP TABLE IF EXISTS `empl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empl` (
  `Empno` int NOT NULL,
  `Ename` varchar(15) DEFAULT NULL,
  `Job` varchar(15) DEFAULT NULL,
  `Mgrno` int DEFAULT NULL,
  `Hiredate` date DEFAULT NULL,
  `Sal` float(8,2) DEFAULT NULL,
  `Comm` float DEFAULT NULL,
  `Deptno` int DEFAULT NULL,
  PRIMARY KEY (`Empno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empl`
--

LOCK TABLES `empl` WRITE;
/*!40000 ALTER TABLE `empl` DISABLE KEYS */;
INSERT INTO `empl` VALUES (8369,'Jay','Clerk',8902,'1990-12-18',8000.00,NULL,20),(8499,'Deepak','Salesman',8698,'1991-02-20',16000.00,300,30),(8521,'Amol','Salesman',8698,'1991-02-22',12500.00,500,30),(8566,'Harshal','Manager',8839,'1991-04-02',29850.00,NULL,20),(8654,'Rohit','Salesman',8698,'1991-09-28',12500.00,1400,30),(8698,'Ayush','Manager',8839,'1991-05-01',28500.00,NULL,30),(8839,'Akshita','President',NULL,'1991-11-18',50000.00,NULL,10),(8844,'Tejas','Salesman',8698,'1991-09-08',15000.00,0,30),(8882,'Sangam','Manager',8839,'1991-06-09',24500.00,NULL,10),(8886,'Yash','Clerk',8888,'1993-01-12',11000.00,NULL,20),(8888,'Mrunal','Analyst',8566,'1992-12-09',30000.00,NULL,20),(8900,'Kajal','Clerk',8698,'1991-12-03',9500.00,NULL,30),(8902,'Nikita','Analyst',8566,'1991-12-03',30000.00,NULL,20),(8934,'Abhay','Clerk',8882,'1992-01-23',13000.00,NULL,10);
/*!40000 ALTER TABLE `empl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `Employee_No` int NOT NULL,
  `Name` varchar(10) DEFAULT NULL,
  `Department` varchar(15) DEFAULT NULL,
  `Salary` int DEFAULT NULL,
  PRIMARY KEY (`Employee_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (203,'Tom','Manufacturing',87000);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medical_shop`
--

DROP TABLE IF EXISTS `medical_shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medical_shop` (
  `Code` int NOT NULL,
  `Name_of_Med` varchar(20) DEFAULT NULL,
  `Name_of_Manu` varchar(20) DEFAULT NULL,
  `Batch_No` varchar(10) DEFAULT NULL,
  `Manu_Date` date DEFAULT NULL,
  `Exp_Date` date DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `Price_Per10` float(5,2) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  CONSTRAINT `medical_shop_chk_1` CHECK ((`Exp_Date` > `Manu_Date`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medical_shop`
--

LOCK TABLES `medical_shop` WRITE;
/*!40000 ALTER TABLE `medical_shop` DISABLE KEYS */;
INSERT INTO `medical_shop` VALUES (101,'Medler','Comed Chemicals Ltd.','RGT0095','2020-05-01','2023-04-01',124,42.00),(102,'Montemac-L','Macleods','Rmx4502','2020-01-02','2023-01-01',10,123.00),(103,'Montex FX','Sun Pharma','RGT0095','2018-05-01','2022-04-01',75,124.50);
/*!40000 ALTER TABLE `medical_shop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `No` int NOT NULL,
  `Name` varchar(15) DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `Department` varchar(15) DEFAULT NULL,
  `Date_of_adm` date DEFAULT NULL,
  `Fee` int DEFAULT NULL,
  `Sex` char(1) DEFAULT NULL,
  PRIMARY KEY (`No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'Aman',24,'Computer','1997-01-10',120,'M'),(2,'Abha',21,'History','1998-03-24',200,'F'),(3,'Lavish',22,'Hindi','1996-12-12',300,'M'),(4,'Rucha',25,'History','1999-07-01',400,'F'),(5,'Chetas',22,'Hindi','1997-09-05',250,'M'),(6,'Deepam',30,'History','1998-06-27',300,'M'),(7,'Madhusmita',34,'Computer','1997-02-25',210,'F'),(8,'Gargie',23,'Hindi','1997-07-31',200,'F'),(9,'Apoorva',36,'Computer','1997-03-12',230,'F');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `worker`
--

DROP TABLE IF EXISTS `worker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `worker` (
  `Wnno` int DEFAULT NULL,
  `Name` varchar(15) DEFAULT NULL,
  `D_Of_Joining` date DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Gender` varchar(15) DEFAULT NULL,
  `Dcode` varchar(4) DEFAULT NULL,
  KEY `Dcode` (`Dcode`),
  CONSTRAINT `worker_ibfk_1` FOREIGN KEY (`Dcode`) REFERENCES `dept` (`Dcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `worker`
--

LOCK TABLES `worker` WRITE;
/*!40000 ALTER TABLE `worker` DISABLE KEYS */;
INSERT INTO `worker` VALUES (1001,'Gokul K','2013-09-02','1991-09-01','Male','D01'),(1002,'Diya H','2012-12-11','1990-12-15','Female','D03'),(1003,'Anuj R','2013-02-03','1987-09-04','Male','D05'),(1004,'Pranay P','2014-01-17','1984-10-19','Male','D04'),(1005,'Pranjali B','2012-12-09','1986-11-14','Female','D01'),(1006,'Abhishekh','2013-11-18','1987-03-31','Male','D02'),(1007,'Tilakshi','2014-06-09','1985-06-23','Female','D05');
/*!40000 ALTER TABLE `worker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'cs2020_21'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-27 19:41:58

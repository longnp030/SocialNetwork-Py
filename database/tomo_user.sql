-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: tomo
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `username` varchar(45) NOT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `is_staff` tinyint(1) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `cover_image` varchar(255) DEFAULT NULL,
  `short_description` varchar(50) DEFAULT NULL,
  `current_working_address` varchar(50) DEFAULT NULL,
  `current_studying_address` varchar(50) DEFAULT NULL,
  `came_from` varchar(45) DEFAULT NULL,
  `current_living_address` varchar(45) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `website` varchar(45) DEFAULT NULL,
  `social_link` varchar(45) DEFAULT NULL,
  `dob` datetime DEFAULT NULL,
  `joined` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (3,'philongg2000@gmail.com','shige',1,NULL,1,'user/images/u3.png','2021-02-04 13:08:09','pbkdf2_sha256$216000$6tqGpGiziCcM$wC4Hkr2muDff46Ka0VC8j+vqPS9MdoHpB+puUkv8PbU=','user/images/u-c3_5VNeGZI.png','I am here to create MyFacebook','MyFacebook Inc.','UET','Ha Noi','Ha Noi','0852341071',NULL,NULL,'2000-06-18 00:00:00','2021-01-22 17:00:00'),(4,'hiryuutomo21@gmail.com','hiryuu',1,NULL,0,'user/images/u4.jpg','2021-02-04 13:06:25','pbkdf2_sha256$216000$3cTgWNtjJL6U$NdpOKV5frYQmt2XFL5q0rSrjuqkZld6N4e6wyfZPduo=','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2021-01-25 11:00:00'),(5,'akisukidesuyo@gmail.com','aki',1,NULL,0,'user/images/u5.jpg','2021-02-04 13:07:16','pbkdf2_sha256$216000$AXvBESGWpjen$mVeSDYyqaUM5JFwi2shnxiWWQZZWpys3JvlEOwjIoRg=','user/images/u-c5.jpg',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2021-01-28 05:00:00'),(6,'philonggg2000@gmail.com','philong',1,NULL,0,'','2021-02-04 14:00:10','pbkdf2_sha256$216000$9O1PtoDz1oIk$7mE2RV0YdkiyDZJhU93hWmhkHlaYot8nsUmK4yylnUY=','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2021-02-02 09:31:25');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-04 21:25:31

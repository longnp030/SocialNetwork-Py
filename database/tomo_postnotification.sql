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
-- Table structure for table `postnotification`
--

DROP TABLE IF EXISTS `postnotification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postnotification` (
  `id` int NOT NULL AUTO_INCREMENT,
  `actor` int NOT NULL,
  `action` varchar(1000) NOT NULL,
  `recipient` int NOT NULL,
  `post` int NOT NULL,
  `notified` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `post_noti_actor_idx` (`actor`),
  KEY `post_noti_recipient_idx` (`recipient`),
  KEY `post_noti_idx` (`post`),
  CONSTRAINT `post_noti` FOREIGN KEY (`post`) REFERENCES `post` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `post_noti_actor` FOREIGN KEY (`actor`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `post_noti_recipient` FOREIGN KEY (`recipient`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postnotification`
--

LOCK TABLES `postnotification` WRITE;
/*!40000 ALTER TABLE `postnotification` DISABLE KEYS */;
INSERT INTO `postnotification` VALUES (1,3,'commented on',3,17,'2021-01-29 16:16:15'),(2,4,'commented on',3,17,'2021-01-29 16:22:27'),(6,3,'liked',3,17,'2021-01-30 06:11:57'),(14,3,'commented on',4,7,'2021-01-30 06:39:52'),(25,3,'liked',4,7,'2021-01-30 07:21:05'),(26,4,'commented on',3,17,'2021-01-31 16:56:12'),(27,4,'liked',3,17,'2021-01-31 16:56:28'),(28,4,'commented on',3,17,'2021-01-31 17:06:15'),(29,4,'commented on',3,17,'2021-01-31 17:07:06'),(30,4,'commented on',3,17,'2021-01-31 17:16:26'),(31,3,'liked',3,20,'2021-02-04 07:53:18'),(32,3,'commented on',6,21,'2021-02-04 13:58:18'),(33,3,'commented on',6,21,'2021-02-04 13:58:18'),(34,3,'commented on',5,22,'2021-02-04 13:59:05'),(35,3,'commented on',6,21,'2021-02-04 13:59:22'),(36,3,'liked',6,21,'2021-02-04 14:00:20'),(37,6,'commented on',6,21,'2021-02-04 14:01:42'),(38,3,'commented on',6,21,'2021-02-04 14:02:26'),(39,3,'liked',5,22,'2021-02-04 14:04:29');
/*!40000 ALTER TABLE `postnotification` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-04 21:25:32

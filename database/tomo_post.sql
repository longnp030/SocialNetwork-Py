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
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `author` int NOT NULL,
  `receiver` int DEFAULT NULL,
  `text` varchar(1000) DEFAULT NULL,
  `images` varchar(45) DEFAULT NULL,
  `topic` varchar(45) DEFAULT NULL,
  `created` datetime NOT NULL,
  `modified` datetime DEFAULT NULL,
  `group` int DEFAULT NULL,
  `tagged_friends` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `author_idx` (`author`),
  KEY `post_receiver_idx` (`receiver`),
  KEY `of_group_idx` (`group`),
  CONSTRAINT `author` FOREIGN KEY (`author`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `of_group` FOREIGN KEY (`group`) REFERENCES `group` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `post_receiver` FOREIGN KEY (`receiver`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (7,4,NULL,'Nice to meet you there! Have a nice weekend!!!!',NULL,NULL,'2021-01-23 11:03:34','2021-01-23 11:03:34',NULL,0),(17,3,NULL,'I passed JLPT N3!!!!!!!!!!!',NULL,NULL,'2021-01-27 17:12:00','2021-01-30 05:21:17',NULL,0),(20,3,NULL,'Welcome everyone! Let\'s build the strongest Wibu community on MyFacebook!!',NULL,NULL,'2021-02-04 07:42:19','2021-02-04 08:57:26',3,0),(21,6,NULL,'Hello I\'m new here. My favorite animes are Erased, Gintama and many more. I am watching Horimiya. \r\nI\'m glad to meet you all ^^',NULL,NULL,'2021-02-04 12:05:00','2021-02-04 12:21:01',3,0),(22,5,NULL,'Here are some famous destinations you must visit when going to Tokyo !! Let\'s take a glance\r\n1. The The Imperial Palace\r\n2. The Sensō-ji Temple\r\n3. Ueno Park and Ueno Zoo\r\n4. The Tokyo Skytree',NULL,NULL,'2021-02-04 12:55:08','2021-02-04 15:01:54',5,0),(23,3,NULL,'Hi',NULL,NULL,'2021-02-05 17:41:30','2021-02-05 17:42:30',NULL,0),(38,8,NULL,'KAmekameha',NULL,NULL,'2021-05-14 05:27:37','2021-05-14 05:27:57',NULL,NULL);
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-31 21:55:07

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
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sender` int NOT NULL,
  `receiver` int NOT NULL,
  `sent` datetime DEFAULT NULL,
  `chatbox` int NOT NULL,
  `content` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `chat_sender_idx` (`sender`),
  KEY `chat_receiver_idx` (`receiver`),
  KEY `chatbox_idx` (`chatbox`),
  CONSTRAINT `chat_receiver` FOREIGN KEY (`receiver`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `chat_sender` FOREIGN KEY (`sender`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `chatbox` FOREIGN KEY (`chatbox`) REFERENCES `chatbox` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,4,3,'2021-01-23 07:49:34',11,'qsdwd'),(2,3,4,'2021-01-23 07:49:38',11,'dqwdq'),(3,3,4,'2021-01-23 07:49:53',11,'dqw'),(4,4,3,'2021-01-23 07:55:40',11,'hiryuu'),(5,3,4,'2021-01-23 07:56:53',11,'shige'),(6,4,3,'2021-01-23 07:59:25',11,'ok'),(7,3,4,'2021-01-23 08:00:56',11,'ok'),(8,3,4,'2021-01-23 08:04:00',11,'shige'),(9,3,4,'2021-01-23 08:04:46',11,'sender'),(10,3,4,'2021-01-23 08:05:04',11,'is me. you are receiver'),(11,4,3,'2021-01-23 08:10:07',11,'ok'),(12,3,4,'2021-01-23 08:11:21',11,'no'),(13,3,4,'2021-01-23 08:12:03',11,'so okay now'),(14,3,4,'2021-01-23 08:12:55',11,'asd'),(15,4,3,'2021-01-23 08:13:46',11,'okok'),(16,4,3,'2021-01-23 08:18:48',11,'i am hiryuu'),(17,4,3,'2021-01-23 08:25:43',11,'i am hiryuu'),(18,4,3,'2021-01-23 08:39:41',11,'currentUserId: 4, me_id: 4, userId: 3, receiver_id: 3'),(19,4,3,'2021-01-23 08:44:11',11,'ok'),(20,4,3,'2021-01-23 08:49:43',11,'few'),(21,4,3,'2021-01-23 08:51:29',11,'is it ok?'),(22,4,3,'2021-01-23 08:52:34',11,'seems not'),(23,4,3,'2021-01-23 08:54:10',11,'ok'),(24,4,3,'2021-01-23 08:54:56',11,'so now i\'m hiryuu for real'),(25,3,4,'2021-01-23 08:55:06',11,'oh congratulation!!'),(26,4,3,'2021-01-23 09:03:33',11,'thanks'),(27,3,5,'2021-02-01 08:35:42',12,'yo'),(28,3,4,'2021-02-01 15:18:45',11,'gggggggsggsgsgmmsmmmmmmmooooiiiuuuuuuyfkulCFQCLEYCGKDH.'),(29,3,4,'2021-02-01 15:18:50',11,'XJXJJX'),(30,3,4,'2021-02-01 15:19:02',11,'GU[WERGU'),(31,3,4,'2021-02-01 15:19:05',11,'huwdywqqy[738'),(32,3,4,'2021-02-01 15:19:15',11,'fuck you'),(33,3,4,'2021-02-01 15:19:29',11,'beach'),(34,3,4,'2021-02-01 15:19:37',11,'is so beautiful'),(35,3,4,'2021-02-01 15:19:45',11,'o de'),(36,3,4,'2021-02-01 15:19:51',11,'dumadarkwa');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
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

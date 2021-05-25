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
-- Table structure for table `groupmessage`
--

DROP TABLE IF EXISTS `groupmessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groupmessage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sender` int NOT NULL,
  `content` varchar(1000) NOT NULL,
  `chatbox` int NOT NULL,
  `sent` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `groupchat_sender_idx` (`sender`),
  KEY `groupchat_box_idx` (`chatbox`),
  CONSTRAINT `groupchat_box` FOREIGN KEY (`chatbox`) REFERENCES `groupchatbox` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `groupchat_sender` FOREIGN KEY (`sender`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groupmessage`
--

LOCK TABLES `groupmessage` WRITE;
/*!40000 ALTER TABLE `groupmessage` DISABLE KEYS */;
INSERT INTO `groupmessage` VALUES (1,3,'hi',3,'2021-01-25 05:10:53'),(20,3,'added aki to this chat.',3,'2021-01-26 06:33:06'),(21,3,'added hiryuu to this chat.',3,'2021-01-26 06:33:59'),(22,3,'added philong to this chat.',3,'2021-01-26 08:36:09'),(23,3,'Welcome to wibu chat, my dear friends',3,'2021-01-26 08:36:34'),(24,3,'please have fun and become the god of weaboo',3,'2021-01-26 08:36:58'),(25,3,'haha',3,'2021-01-26 08:43:37'),(26,3,'hey aki',3,'2021-01-26 08:44:47'),(27,3,'are you from japan?',3,'2021-01-26 08:45:21'),(28,5,'oh hi',3,'2021-01-26 08:47:17'),(29,5,'thanks shige for letting me join',3,'2021-01-26 08:47:28'),(30,5,'yes i\'m from japan',3,'2021-01-26 08:47:38'),(31,5,'i am very happy to share all what i know about my country to you guys',3,'2021-01-26 08:48:01'),(32,5,'hehe',3,'2021-01-26 08:52:34'),(33,3,'thank you very much, aki!!',3,'2021-01-26 08:53:03'),(34,5,'no problem!!!',3,'2021-01-26 09:19:04'),(35,5,'what about hiryuu and philong?',3,'2021-01-26 09:19:37'),(36,5,'I cant wait to chat with all of you',3,'2021-01-26 09:21:14'),(37,5,'haha',3,'2021-01-26 09:22:02'),(38,5,'yea',3,'2021-01-26 09:22:45'),(39,3,'removed philong from this chat.',3,'2021-01-26 13:42:50'),(40,3,'hiryuu leaved this chat.',3,'2021-01-26 14:28:37'),(41,3,'added hiryuu to this chat.',3,'2021-01-26 14:28:58'),(42,3,'hiryuu leaved this chat.',3,'2021-01-26 14:29:08'),(43,3,'added hiryuu to this chat.',3,'2021-01-26 14:32:59'),(44,3,'hiryuu leaved this chat.',3,'2021-01-26 14:33:18'),(45,3,'added hiryuu to this chat.',3,'2021-01-26 14:38:27'),(47,3,'hiryuu leaved this chat.',3,'2021-01-26 14:44:40'),(48,3,'added hiryuu to this chat.',3,'2021-01-26 14:44:53'),(49,3,'hiryuu leaved this chat.',3,'2021-01-26 14:47:11'),(59,3,' changed group chat name to Wibu',3,'2021-01-27 02:26:10'),(60,3,' changed group chat name to Wibu forever',3,'2021-01-27 02:31:17'),(61,3,'I changed chat name!',3,'2021-01-27 02:35:15'),(62,3,'added hiryuu to this chat.',3,'2021-01-27 02:38:44'),(64,4,'Can I try changing name too ?',3,'2021-01-27 02:43:50'),(65,3,'Sure',3,'2021-01-27 02:43:56'),(66,4,' changed group chat name to My wibu',3,'2021-01-27 02:44:34'),(67,3,'Nice',3,'2021-01-27 02:44:56'),(68,4,'Yay',3,'2021-01-27 02:45:23'),(69,4,' changed group chat name to Wibu forever',3,'2021-01-27 02:46:25'),(70,4,'I changed it back :D',3,'2021-01-27 02:46:45'),(71,3,'removed \'hiryuu\' from this chat.',3,'2021-01-27 03:24:19'),(72,4,'no',3,'2021-01-27 03:24:27'),(73,3,'added hiryuu to this chat.',3,'2021-01-27 03:25:06'),(74,3,'removed \'hiryuu\' from this chat.',3,'2021-01-27 03:26:09'),(94,3,'shige leaved this chat.',3,'2021-01-30 11:32:06'),(95,3,'added aki to this chat.',3,'2021-01-30 12:10:58'),(96,3,'removed aki from this chat.',3,'2021-01-30 12:11:03'),(97,3,'added aki to this chat.',3,'2021-01-30 12:11:16'),(98,3,'added hiryuu to this chat.',3,'2021-01-30 12:16:32'),(99,3,' changed group chat name to Wibu forever <3',3,'2021-01-30 13:12:11'),(100,5,'added philong to this chat.',3,'2021-01-30 13:12:23'),(101,5,' changed group chat name to Wibu forever',3,'2021-01-30 13:12:38'),(102,4,'aki left this chat. Admin right is transferred to hiryuu',3,'2021-01-30 13:12:54'),(103,4,'added aki to this chat.',3,'2021-01-30 13:16:46'),(104,3,'hiryuu left this chat. Admin right is transferred to shige',3,'2021-01-30 13:16:49'),(105,3,'added hiryuu to this chat.',3,'2021-01-30 13:17:15'),(106,4,':))',3,'2021-01-30 13:17:28'),(107,3,'removed philong from this chat.',3,'2021-01-30 13:17:43'),(108,3,'added philong to this chat.',3,'2021-01-30 13:17:49'),(109,3,'ye',5,'2021-02-01 08:36:10'),(110,3,' changed group chat name to N2 Goukaku',5,'2021-02-01 08:37:47'),(111,3,'hiop;huigugiug',3,'2021-02-01 15:20:04'),(112,3,'igugiu78ryilf8ikoli\'',3,'2021-02-01 15:20:09'),(113,3,' changed group chat name to Learning Japanese',5,'2021-02-04 10:40:27');
/*!40000 ALTER TABLE `groupmessage` ENABLE KEYS */;
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

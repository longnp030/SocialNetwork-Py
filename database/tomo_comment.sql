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
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `commentor` int NOT NULL,
  `post` int NOT NULL,
  `content` varchar(1000) DEFAULT NULL,
  `written` datetime NOT NULL,
  `modified` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `commentor_idx` (`commentor`),
  KEY `post_idx` (`post`),
  CONSTRAINT `commentor` FOREIGN KEY (`commentor`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `post` FOREIGN KEY (`post`) REFERENCES `post` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (20,3,7,'hi\n','2021-01-24 15:55:38','2021-01-24 15:55:38'),(26,3,17,'yesssssss\n','2021-01-29 16:16:14','2021-01-29 16:16:14'),(27,4,17,'congratulation','2021-01-29 16:22:27','2021-01-29 16:22:27'),(28,3,7,'hello\n','2021-01-30 06:39:52','2021-01-30 06:39:52'),(29,4,17,'thank you very much\n','2021-01-31 16:56:12','2021-01-31 16:56:12'),(30,4,17,'hehe\n','2021-01-31 17:06:14','2021-01-31 17:06:14'),(31,4,17,'wait \n','2021-01-31 17:07:06','2021-01-31 17:07:06'),(32,4,17,'haha\n','2021-01-31 17:16:26','2021-01-31 17:16:26'),(33,3,21,'Hi there. I love Gintama too. Is Horiyama being released this season?','2021-02-04 13:58:18','2021-02-04 13:58:18'),(35,3,22,'Thanks for sharing. Those are very attractive and spectacular pictures ','2021-02-04 13:59:05','2021-02-04 13:59:05'),(37,6,21,'Yesss. Latest episode on now is ep 4. Have you watched it?','2021-02-04 14:01:42','2021-02-04 14:01:42'),(38,3,21,'Oh I haven\'t got free time to watch lately. I will watch when possible!','2021-02-04 14:02:26','2021-02-04 14:02:26');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-04 21:25:29

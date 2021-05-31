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
-- Table structure for table `image`
--

DROP TABLE IF EXISTS `image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `image` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `author` int NOT NULL,
  `uploaded` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `owner_idx` (`author`),
  CONSTRAINT `owner` FOREIGN KEY (`author`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image`
--

LOCK TABLES `image` WRITE;
/*!40000 ALTER TABLE `image` DISABLE KEYS */;
INSERT INTO `image` VALUES (13,'post/images/pNone-shige.jpg',3,'2021-01-27 17:21:05'),(16,'post/images/pNone-shige_kPAEcY5.jpg',3,'2021-01-28 01:46:35'),(20,'post/images/pNone-shige_jFYTzFz.jpg',3,'2021-02-02 09:45:13'),(21,'post/images/pNone-shige_genqKjD.jpg',3,'2021-02-02 09:48:07'),(22,'post/images/pNone-shige.png',3,'2021-02-02 09:48:27'),(23,'post/images/pNone-shige_2RBcFFe.png',3,'2021-02-02 09:48:41'),(24,'post/images/pNone-shige_ACTUrze.jpg',3,'2021-02-02 09:48:58'),(25,'post/images/pNone-shige_rmR92Ym.jpg',3,'2021-02-02 09:49:31'),(26,'post/images/pNone-shige_r7p0d1w.jpg',3,'2021-02-02 09:49:51'),(27,'post/images/pNone-shige_uYUCu0Z.jpg',3,'2021-02-04 07:42:32'),(28,'post/images/pNone-philong.jpg',6,'2021-02-04 12:20:47'),(29,'post/images/pNone-aki.jpg',5,'2021-02-04 12:55:21'),(30,'post/images/pNone-aki_tkiS0ro.jpg',5,'2021-02-04 12:55:27'),(31,'post/images/pNone-aki_g7ANjyZ.jpg',5,'2021-02-04 12:55:32'),(32,'post/images/pNone-aki_okZxJaT.jpg',5,'2021-02-04 12:55:37'),(33,'post/images/pNone-shige_SsCm1xO.png',3,'2021-02-05 17:41:52'),(34,'post/images/pNone-txd.png',8,'2021-05-13 12:16:28'),(35,'post/images/pNone-txd_E5NhnLc.png',8,'2021-05-14 05:22:06');
/*!40000 ALTER TABLE `image` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-31 21:55:05

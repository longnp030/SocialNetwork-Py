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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'user','0001_initial','2021-01-20 14:58:21.386915'),(2,'contenttypes','0001_initial','2021-01-20 14:58:23.700855'),(3,'admin','0001_initial','2021-01-20 14:58:24.751791'),(4,'admin','0002_logentry_remove_auto_add','2021-01-20 14:58:26.747153'),(5,'admin','0003_logentry_add_action_flag_choices','2021-01-20 14:58:26.828929'),(6,'contenttypes','0002_remove_content_type_name','2021-01-20 14:58:30.815200'),(7,'auth','0001_initial','2021-01-20 14:58:35.706851'),(8,'auth','0002_alter_permission_name_max_length','2021-01-20 14:58:42.859838'),(9,'auth','0003_alter_user_email_max_length','2021-01-20 14:58:42.929242'),(10,'auth','0004_alter_user_username_opts','2021-01-20 14:58:42.995547'),(11,'auth','0005_alter_user_last_login_null','2021-01-20 14:58:43.096625'),(12,'auth','0006_require_contenttypes_0002','2021-01-20 14:58:43.428796'),(13,'auth','0007_alter_validators_add_error_messages','2021-01-20 14:58:43.529029'),(14,'auth','0008_alter_user_username_max_length','2021-01-20 14:58:43.616625'),(15,'auth','0009_alter_user_last_name_max_length','2021-01-20 14:58:43.684866'),(16,'auth','0010_alter_group_name_max_length','2021-01-20 14:58:43.979076'),(17,'auth','0011_update_proxy_permissions','2021-01-20 14:58:44.044381'),(18,'auth','0012_alter_user_first_name_max_length','2021-01-20 14:58:44.148135'),(19,'sessions','0001_initial','2021-01-20 14:58:45.149147'),(20,'post','0001_initial','2021-01-20 17:30:59.345681'),(21,'post','0002_auto_20210121_1403','2021-01-21 07:08:00.274401'),(22,'post','0003_auto_20210121_1407','2021-01-21 07:08:03.336137'),(23,'user','0002_block_friendrequest_friendship','2021-01-21 07:08:07.129664'),(24,'chat','0001_initial','2021-01-21 15:39:28.650035'),(25,'user','0003_auto_20210121_2239','2021-01-21 15:39:32.242998'),(26,'user','0004_auto_20210121_2313','2021-01-21 16:13:13.996175'),(27,'chat','0002_auto_20210122_0901','2021-01-22 02:02:00.741329'),(28,'chat','0002_groupchatbox_groupmessage','2021-01-25 00:50:59.626173'),(29,'chat','0003_joingroupchat','2021-01-25 04:45:36.883738'),(30,'chat','0004_auto_20210127_1835','2021-01-27 11:37:48.020778'),(31,'post','0002_auto_20210127_1837','2021-01-27 11:37:48.136370'),(32,'post','0003_auto_20210127_2101','2021-01-27 14:01:49.087769'),(33,'notification','0001_initial','2021-01-29 08:06:25.284617'),(34,'group','0001_initial','2021-01-30 15:53:57.119926'),(35,'group','0002_groupadmin','2021-02-02 02:29:31.137643'),(36,'group','0003_joingrouprequest','2021-02-04 02:24:50.059493'),(37,'group','0004_groupjoininvitation','2021-02-04 10:27:01.641568'),(38,'post','0004_friendtaggedinpost','2021-05-13 11:24:46.311806');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-31 21:55:03

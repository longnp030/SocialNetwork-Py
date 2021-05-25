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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add user',1,'add_user'),(2,'Can change user',1,'change_user'),(3,'Can delete user',1,'delete_user'),(4,'Can view user',1,'view_user'),(5,'Can add log entry',2,'add_logentry'),(6,'Can change log entry',2,'change_logentry'),(7,'Can delete log entry',2,'delete_logentry'),(8,'Can view log entry',2,'view_logentry'),(9,'Can add permission',3,'add_permission'),(10,'Can change permission',3,'change_permission'),(11,'Can delete permission',3,'delete_permission'),(12,'Can view permission',3,'view_permission'),(13,'Can add group',4,'add_group'),(14,'Can change group',4,'change_group'),(15,'Can delete group',4,'delete_group'),(16,'Can view group',4,'view_group'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add comment',7,'add_comment'),(26,'Can change comment',7,'change_comment'),(27,'Can delete comment',7,'delete_comment'),(28,'Can view comment',7,'view_comment'),(29,'Can add post',8,'add_post'),(30,'Can change post',8,'change_post'),(31,'Can delete post',8,'delete_post'),(32,'Can view post',8,'view_post'),(33,'Can add reaction',9,'add_reaction'),(34,'Can change reaction',9,'change_reaction'),(35,'Can delete reaction',9,'delete_reaction'),(36,'Can view reaction',9,'view_reaction'),(37,'Can add friendship',10,'add_friendship'),(38,'Can change friendship',10,'change_friendship'),(39,'Can delete friendship',10,'delete_friendship'),(40,'Can view friendship',10,'view_friendship'),(41,'Can add friend request',11,'add_friendrequest'),(42,'Can change friend request',11,'change_friendrequest'),(43,'Can delete friend request',11,'delete_friendrequest'),(44,'Can view friend request',11,'view_friendrequest'),(45,'Can add block',12,'add_block'),(46,'Can change block',12,'change_block'),(47,'Can delete block',12,'delete_block'),(48,'Can view block',12,'view_block'),(49,'Can add chat box',13,'add_chatbox'),(50,'Can change chat box',13,'change_chatbox'),(51,'Can delete chat box',13,'delete_chatbox'),(52,'Can view chat box',13,'view_chatbox'),(53,'Can add message',14,'add_message'),(54,'Can change message',14,'change_message'),(55,'Can delete message',14,'delete_message'),(56,'Can view message',14,'view_message'),(57,'Can add post image',15,'add_postimage'),(58,'Can change post image',15,'change_postimage'),(59,'Can delete post image',15,'delete_postimage'),(60,'Can view post image',15,'view_postimage'),(61,'Can add group chat box',16,'add_groupchatbox'),(62,'Can change group chat box',16,'change_groupchatbox'),(63,'Can delete group chat box',16,'delete_groupchatbox'),(64,'Can view group chat box',16,'view_groupchatbox'),(65,'Can add group message',17,'add_groupmessage'),(66,'Can change group message',17,'change_groupmessage'),(67,'Can delete group message',17,'delete_groupmessage'),(68,'Can view group message',17,'view_groupmessage'),(69,'Can add join group chat',18,'add_joingroupchat'),(70,'Can change join group chat',18,'change_joingroupchat'),(71,'Can delete join group chat',18,'delete_joingroupchat'),(72,'Can view join group chat',18,'view_joingroupchat'),(73,'Can add image',19,'add_image'),(74,'Can change image',19,'change_image'),(75,'Can delete image',19,'delete_image'),(76,'Can view image',19,'view_image'),(77,'Can add post notification',20,'add_postnotification'),(78,'Can change post notification',20,'change_postnotification'),(79,'Can delete post notification',20,'delete_postnotification'),(80,'Can view post notification',20,'view_postnotification'),(81,'Can add group',21,'add_group'),(82,'Can change group',21,'change_group'),(83,'Can delete group',21,'delete_group'),(84,'Can view group',21,'view_group'),(85,'Can add group member',22,'add_groupmember'),(86,'Can change group member',22,'change_groupmember'),(87,'Can delete group member',22,'delete_groupmember'),(88,'Can view group member',22,'view_groupmember'),(89,'Can add group post',23,'add_grouppost'),(90,'Can change group post',23,'change_grouppost'),(91,'Can delete group post',23,'delete_grouppost'),(92,'Can view group post',23,'view_grouppost'),(93,'Can add group admin',24,'add_groupadmin'),(94,'Can change group admin',24,'change_groupadmin'),(95,'Can delete group admin',24,'delete_groupadmin'),(96,'Can view group admin',24,'view_groupadmin'),(97,'Can add join group request',25,'add_joingrouprequest'),(98,'Can change join group request',25,'change_joingrouprequest'),(99,'Can delete join group request',25,'delete_joingrouprequest'),(100,'Can view join group request',25,'view_joingrouprequest'),(101,'Can add group join invitation',26,'add_groupjoininvitation'),(102,'Can change group join invitation',26,'change_groupjoininvitation'),(103,'Can delete group join invitation',26,'delete_groupjoininvitation'),(104,'Can view group join invitation',26,'view_groupjoininvitation');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-04 21:25:30

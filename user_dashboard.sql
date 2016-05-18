-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: user_dashboard
-- ------------------------------------------------------
-- Server version	5.5.41-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `message_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,'comment 1','0000-00-00 00:00:00','0000-00-00 00:00:00',4,17),(2,'yay','2016-05-17 17:35:41','2016-05-17 17:35:41',6,31),(3,'yeah science!','2016-05-17 17:35:52','2016-05-17 17:35:52',5,31),(4,'hello','2016-05-17 17:36:11','2016-05-17 17:36:11',5,31),(5,'yay','2016-05-17 17:36:23','2016-05-17 17:36:23',5,31),(6,'wow','2016-05-17 17:40:05','2016-05-17 17:40:05',3,31),(7,'aasdas\r\n','2016-05-17 17:47:55','2016-05-17 17:47:55',5,31),(8,'yay','2016-05-17 17:48:03','2016-05-17 17:48:03',3,31),(9,'hey john! you are alive!!','2016-05-17 17:49:50','2016-05-17 17:49:50',2,31),(10,'hey','2016-05-17 19:15:38','2016-05-17 19:15:38',9,29);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `rec_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'message 1','0000-00-00 00:00:00','0000-00-00 00:00:00',17,29),(2,'message 2','0000-00-00 00:00:00','0000-00-00 00:00:00',27,29),(3,'message 3','0000-00-00 00:00:00','0000-00-00 00:00:00',29,27),(4,'hey john!!!...','2016-05-17 15:28:46','2016-05-17 15:28:46',31,27),(5,'hey message 2','2016-05-17 15:41:21','2016-05-17 15:41:21',31,27),(6,'yay 3','2016-05-17 15:42:04','2016-05-17 15:42:04',31,27),(7,'hello','2016-05-17 17:48:32','2016-05-17 17:48:32',31,27),(8,'hello ana','2016-05-17 17:49:31','2016-05-17 17:49:31',31,29),(9,'hello','2016-05-17 19:15:23','2016-05-17 19:15:23',29,27);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `user_level` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (17,'Rose','Rosal','rose@gmail.com','$2b$12$qtPjvnNauGQgjChqIO0nouSb8nN.h62GW1HFw6feZDkXSHfHmh1i.',9,'2016-05-16 16:51:21',NULL,NULL),(27,'John','Snow','john@snow.com','$2b$12$VRIJIiuI/5roPc82WmVk1uRfPQdmPAuAM2Tfcd56sc4iVveMZyKK.',1,'2016-05-16 18:25:41',NULL,NULL),(29,'Ana','Thomas','anathomasity@gmail.com','$2b$12$wLopsD3cYUJh/mwyr0OI/.eZu.4.RSZ3AdPOjJeY8TnSQK1MXTJn.',9,'2016-05-17 08:54:28',NULL,NULL),(31,'Mike','THOMAS','mike@gmail.com','$2b$12$2qwf8Dh.sdKnhTFKugAoMeQYpyjvBMvg.mIkNA6Wy.Fx4qu4RQcQu',1,'2016-05-17 11:30:50',NULL,'HELLO!'),(32,'Ana','asd','asd@gmail.com','$2b$12$rDr6z3OLPp0m.wwkB94FbuLm0Ea.lV2BQJig48rMSYu3RRNW8LAym',1,'2016-05-17 11:31:31',NULL,NULL),(36,'pepe','cibrian','pepe@gmail.com','$2b$12$NqR.0aLch8zupjaUygmZnuQS8iuVTlfOIrScGK7RUDhFpSJTAq.Km',1,'2016-05-17 18:15:58',NULL,NULL),(37,'hello','moto','moto@gmail.com','$2b$12$U72UUocv9DwLmqjTMjJbtOQ9rxstVy6BOjq9qbdUKHw3OkdzP1NAO',1,'2016-05-17 18:19:38',NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-18 16:43:48

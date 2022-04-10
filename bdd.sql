-- --------------------------------------------------------
-- Hôte:                         172.19.0.16
-- Version du serveur:           10.1.47-MariaDB-0+deb9u1 - Debian 9.13
-- SE du serveur:                debian-linux-gnu
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Listage des données de la table boutiq.categorie : ~3 rows (environ)
DELETE FROM `categorie`;
/*!40000 ALTER TABLE `categorie` DISABLE KEYS */;
INSERT INTO `categorie` (`idCategorie`, `nomCategorie`) VALUES
	(1, 'Accessoires'),
	(2, 'Instruments'),
	(5, 'Montage');
/*!40000 ALTER TABLE `categorie` ENABLE KEYS */;

-- Listage des données de la table boutiq.client : ~1 rows (environ)
DELETE FROM `client`;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` (`idClient`, `nomClient`, `prenomClient`, `emailClient`, `motDePasseClient`, `rueClient`, `cpClient`, `villeClient`, `telClient`) VALUES
	(3, 'Lucas', 'Chevalot', 'lucas.chevalot@gmail.com', '$2y$10$qJZGoizlRObBHtcfHlNztOwjSumUsSqmJYAf.bKqIWzCq6W7VVp6C', '15 rue du gué', '55000', 'Bar le duc', '0648789090'),
	(4, 'blabla', 'bla', 'mdflsdfm@exemple.com', '$2y$10$28TnXAYin9NGjYVSmOVqtOMcoJI/nnVjbFlQBTM5TUl8jvsbSMMWu', 'msdlf;', '12345', 'zrmlg;z', '');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;

-- Listage des données de la table boutiq.commande : ~1 rows (environ)
DELETE FROM `commande`;
/*!40000 ALTER TABLE `commande` DISABLE KEYS */;
INSERT INTO `commande` (`numeroCommande`, `dateCommande`, `idClient`, `devis`) VALUES
	(19, '2021-09-27', 4, 0);
/*!40000 ALTER TABLE `commande` ENABLE KEYS */;

-- Listage des données de la table boutiq.commander : ~2 rows (environ)
DELETE FROM `commander`;
/*!40000 ALTER TABLE `commander` DISABLE KEYS */;
INSERT INTO `commander` (`numeroCommande`, `codeProduit`, `quantite`) VALUES
	(19, 13, 1),
	(19, 15, 1);
/*!40000 ALTER TABLE `commander` ENABLE KEYS */;

-- Listage des données de la table boutiq.photo : ~8 rows (environ)
DELETE FROM `photo`;
/*!40000 ALTER TABLE `photo` DISABLE KEYS */;
INSERT INTO `photo` (`id_photo`, `photos`, `id_produit`) VALUES
	(1, 'produit1.jpg', 13),
	(2, 'produit2.jpg', 13),
	(3, 'produit3.jpg', 15),
	(4, 'produit4.jpg', 15),
	(5, 'produit5.jpg', 17),
	(6, 'produit6.jpg', 18),
	(7, 'produit7.jpg', 18),
	(8, 'sur_devis.jpg', 20);
/*!40000 ALTER TABLE `photo` ENABLE KEYS */;

-- Listage des données de la table boutiq.produit : ~5 rows (environ)
DELETE FROM `produit`;
/*!40000 ALTER TABLE `produit` DISABLE KEYS */;
INSERT INTO `produit` (`codeProduit`, `designationProduit`, `prixProduit`, `stockProduit`, `idCategorie`, `typeProduit`) VALUES
	(13, 'Guitare électrique', 854.68, 1, 2, 'Prix fixe'),
	(15, 'Guitare électrique deux manches', 256.87, 3, 2, 'Prix fixe'),
	(17, 'Cordes guitare 10-46', 10.00, 20, 1, 'Prix fixe'),
	(18, 'Cordes basse fluo', 50.00, 10, 1, 'Prix fixe'),
	(20, 'Montage des cordes', NULL, NULL, 5, 'Sur devis');
/*!40000 ALTER TABLE `produit` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-12-2023 a las 15:17:35
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `temidb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipment_base`
--

CREATE TABLE `equipment_base` (
  `code` int(11) NOT NULL,
  `equipment_description` varchar(255) DEFAULT NULL,
  `pot` varchar(255) DEFAULT NULL,
  `hourly_cost` float DEFAULT NULL,
  `np_ep_nd` varchar(255) DEFAULT NULL,
  `cpc` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `equipment_base`
--

INSERT INTO `equipment_base` (`code`, `equipment_description`, `pot`, `hourly_cost`, `np_ep_nd`, `cpc`) VALUES
(2, 'Compresor', '73 HP', 19.6, 'NP', '439410015'),
(3, 'Concretera', ' 9 HP', 3.1, 'NP', '444400211'),
(4, 'Vibrador', ' 5 HP', 2.45, 'NP', '4423100110'),
(5, 'Retroexcavadora', '75 HP', 20, 'NP', '444260012'),
(6, 'Compactador manual', '5 HP', 3, 'EP', '444271016'),
(7, 'Equipo topográfico', NULL, 10, 'NP', '482810111'),
(8, 'Volquete de 8 m3', NULL, 20, 'NP', '491190311'),
(9, 'Bomba de prueba hidrostática', NULL, 3.9, 'NP', '4315100114'),
(10, 'Elevador', NULL, 3.76, 'NP', '435101116'),
(11, 'Encofrado metálico', NULL, 2, 'EP', '545400411'),
(12, 'Pulidora de piso', NULL, 3, 'NP', '448161014'),
(13, 'Soldadora', NULL, 2.5, 'NP', '4295000111'),
(14, 'Tractor de oruga 245 hp', NULL, 45, 'NP', '441500011'),
(15, 'Tractor de oruga 200 hp', NULL, 35, 'NP', '441500011'),
(16, 'Herramientas eléctricas', NULL, 2, 'NP', '4299217233'),
(17, 'Equipo de perforación', NULL, 12, 'NP', '833930013'),
(18, 'Bomba de agua', NULL, 5, 'NP', '4315100114'),
(19, 'zaranda mecanica', NULL, 10, 'EP', '4294300112'),
(20, 'Cargadora  frontal', NULL, 25, 'NP', '444250011'),
(21, 'Taladro eléctrico', NULL, 4, 'NP', '444610013'),
(22, 'Teodolito', NULL, 2, 'NP', '482810111'),
(23, 'Compactador mecánico', NULL, 3, 'NP', '444271016'),
(24, 'Cortadora de hierro', NULL, 1.02, 'EP', '441100311'),
(25, 'Andamios', NULL, 0.12, 'EP', '421900017'),
(26, 'Dobladora', NULL, 1, 'EP', '429211311'),
(27, 'Cizalla', NULL, 0.14, 'EP', '429211311'),
(28, 'Suelda autógena', NULL, 5, 'NP', '4295000111'),
(29, 'Máquina de Impacto para Jack cat 5', NULL, 4, 'NP', '4423100112'),
(30, 'Equipo para certificación de cableado', NULL, 10, 'NP', '873900011'),
(31, 'Equipo para pruebas seguridad', NULL, 10, 'NP', '873900011'),
(32, 'Equipo para calibración de video', NULL, 30, 'NP', '873900011'),
(33, 'Equipo para calibración de movimiento automático', NULL, 30, 'NP', '873900011'),
(34, 'Computador portátil', NULL, 120, 'NP', '452200051'),
(35, 'Equipo para pruebas continuidad, resistencia y capacitancia', NULL, 0.6, 'NP', '4824300117'),
(36, 'Equipo de pruebas seguridad', NULL, 800, 'NP', '4824300117'),
(37, 'Equipo para pruebas video', NULL, 0.6, 'NP', '4824300117'),
(38, 'Máquina de Impacto para BNC', NULL, 4, 'NP', '4824300117'),
(39, 'Máquina de Impacto para conector RJ-45', NULL, 10, 'NP', '4824300117'),
(40, 'Montacargas', NULL, 20, 'NP', '444110021'),
(41, 'AMPLIFICADOR MATRICIAL PRINCIPAL', NULL, 1384, 'NP', '4516003142'),
(42, 'AMPLIFICADOR SECUNDARIO', NULL, 422.5, 'NP', '473310411'),
(43, 'CD PLAYER, SIMILAR A SONY CDP-L3', NULL, 680, 'NP', '452500012'),
(44, 'REPRODUCTOR DE CINTAS, SIMILAR A TOA BA-803', NULL, 385, 'NP', '473230011'),
(45, 'MICROFONOS', NULL, 120, 'NP', '473310011'),
(46, 'PARLANTES DE DISTRIBUCIÓN PARA CELDAS DE SONIDO', NULL, 59.43, 'NP', '473310513'),
(47, 'SISTEMA DE DISPERSIÓN CONTROLADA DE SONIDO', NULL, 3580, 'NP', '473310313'),
(48, 'CONSOLA MEZCLADORA DE SONIDO', NULL, 2250, 'NP', '473310313'),
(49, 'COLUMNAS DE DISTRIBUCIÓN SONORA', NULL, 193, 'NP', '473310515'),
(50, 'BOBCAT', NULL, 20, 'NP', '441500013'),
(51, 'AMOLADOR', NULL, 2, 'NP', '442160211'),
(52, 'Motoniveladora', NULL, 40, 'NP', '444220013'),
(53, 'Rodillo Vibratorio liso', NULL, 35, 'NP', '444240012'),
(54, 'Camión Cisterna', NULL, 16, 'NP', '643320111'),
(55, 'Tractor D9', NULL, 60, 'NP', '441500011'),
(56, 'soldadora autógena', NULL, 4.8, 'NP', '4295000111'),
(57, 'Distribuidora de asfalto', NULL, 35, 'NP', '444220012'),
(58, 'Compactador mecánico', NULL, 6, 'NP', '4443004234'),
(59, 'Camión de volteo', NULL, 15, 'NP', '491140017'),
(60, 'Máquina Cortadora', NULL, 16, 'NP', '441200011'),
(61, 'Piunjer 9HP', NULL, 5.92, 'NP', '429215112'),
(62, 'Acémila', NULL, 2, 'EP', '21130011'),
(63, 'Trailer', NULL, 25, 'NP', '491140016'),
(64, 'Montacargas - retroexcavadora', NULL, 25, 'NP', '444110021'),
(65, 'Estacion Total', NULL, 3.75, 'NP', '482810111'),
(66, 'Nivel', NULL, 1.25, 'NP', '482810111'),
(67, 'Excavadora de orugas', NULL, 45, 'NP', '4323004113'),
(68, 'Compresor y soplete', NULL, 1.01, 'NP', '439410015'),
(69, 'Escoba autopropulsada', NULL, 8, 'NP', '441802911'),
(70, 'Distribuidora de agregados', NULL, 40, 'NP', '444240012'),
(71, 'Rodillo liso tandem', NULL, 30, 'NP', '444240012'),
(72, 'Terminadora de asfalto', NULL, 80, 'NP', '444220012'),
(73, 'Planta asfáltica', NULL, 30, 'NP', '1533000110'),
(74, 'Bomba', NULL, 20, 'NP', '4315100114'),
(75, 'Planta de trituración', NULL, 45, 'NP', '441802911'),
(77, 'Bomba de Fumigar, motor a gasolina 26 lit.', NULL, 2, NULL, 'None'),
(78, 'Motocarretilla fumigadora', NULL, 3, NULL, 'None'),
(79, 'Soldadora Eléctrica 300 Amp.', NULL, 4, NULL, 'None'),
(80, 'Termómetro infrarojo digital', NULL, 5, NULL, 'None');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipment_base`
--
ALTER TABLE `equipment_base`
  ADD PRIMARY KEY (`code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

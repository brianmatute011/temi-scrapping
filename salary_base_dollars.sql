-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-12-2023 a las 15:56:04
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
-- Estructura de tabla para la tabla `salary_base_dollars`
--

CREATE TABLE `salary_base_dollars` (
  `code` int(11) NOT NULL,
  `worker_category` varchar(255) DEFAULT NULL,
  `unified_salary` float(8,2) DEFAULT NULL,
  `min_salary` float(8,2) DEFAULT NULL,
  `tenth_salary` float(8,2) DEFAULT NULL,
  `employer_contribution` float(8,2) DEFAULT NULL,
  `reserve_fund` float(8,2) DEFAULT NULL,
  `total_earned_age` float(8,2) DEFAULT NULL,
  `real_daily_wage` float(8,2) DEFAULT NULL,
  `hourly_cost` float(8,2) DEFAULT NULL,
  `identifier` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `salary_base_dollars`
--

INSERT INTO `salary_base_dollars` (`code`, `worker_category`, `unified_salary`, `min_salary`, `tenth_salary`, `employer_contribution`, `reserve_fund`, `total_earned_age`, `real_daily_wage`, `hourly_cost`, `identifier`) VALUES
(1, 'Conserje o mensajero<*NSC>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E1'),
(20, 'Peón', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(21, 'Guardián<EO E2>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(22, 'Ayudante de albañil<EO E2>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(23, 'Ayudante de operador de equipo<EO E2>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(24, 'Ayudante de fierrero<EO E2>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(25, 'Ayudante de carpintero<EO E2>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(26, 'Ayudante de encofrador<EO E2>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(27, 'Ayudante de carpintero de ribera<EO E2>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(28, 'Ayudante de plomero<EO E2>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(29, 'Ayudante de electricista<EO E2>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(30, 'Ayudante de instalador de revestimiento en general<EO E2>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(31, 'Machetero<EO E2>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(59, 'Ayudante de maquinaria', 422.28, NULL, 422.28, 615.68, 422.28, 6927.60, 29.73, 3.72, 'EO D2'),
(60, 'Albañil', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(61, 'Operador de equipo liviano', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(62, 'Pintor', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(63, 'Fierrero', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(64, 'Carpintero', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(65, 'Encofrador', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(66, 'Carpintero de ribera', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(67, 'Plomero', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(68, 'Electricista', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(69, 'Instalador de revestimiento en general', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(70, 'Ayudante de perforador', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(71, 'Cadenero', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(72, 'Mampostero', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(73, 'Enlucidor', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(74, 'Hojalatero', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(75, 'Técnico liniero eléctrico', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(76, 'Técnico en montaje de subestaciones', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(77, 'Técnico electromecánico de construcción', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(78, 'Pintor de exteriores', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(79, 'Pintor empapelador', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(80, 'Obrero especializado en la elaboración de prefabricados de hormigón', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(81, 'Parqueteros y colocadores de pisos', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(90, 'Maestro soldador especializado <En Construcción - Estr.Oc.C1>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(91, 'Maestro eléctrico/liniero/subestaciones', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C2'),
(92, 'Maestro de estructura mayor con certificado o título<*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C2'),
(93, 'Maestro electrónico especializado<*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C3'),
(94, 'Técnico construcciones civiles con certificado y/o título<*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C4'),
(95, 'Maestro mayor en ejecución de obras civiles', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C5'),
(120, 'Maestro de obra', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2'),
(121, 'Operador de planta de hormigón', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2'),
(122, 'Operador de perforador <En Construcción>', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2'),
(123, 'Perfilero <En Construcción>', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2'),
(124, 'Técnico en albañilería', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2'),
(125, 'Técnico en obras civiles', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2'),
(140, 'Maestro plomero<*NSC>', 407.51, NULL, 407.51, 594.15, 407.51, 6699.29, 28.75, 3.59, 'EO C3'),
(160, 'Inspector de obra', 464.32, NULL, 464.32, 676.98, 464.32, 7577.46, 32.52, 4.07, 'EO B3'),
(161, 'Supervisor Eléctrico General/ Supervisor Sanitario General', 464.32, NULL, 464.32, 676.98, 464.32, 7577.46, 32.52, 4.07, 'EO B3'),
(179, 'Ingeniero Eléctrico', 465.51, NULL, 465.51, 678.71, 465.51, 7595.85, 32.60, 4.08, 'EO B1'),
(180, 'Ingeniero Civil <Estructural, Hidráulico y Vial>', 465.51, NULL, 465.51, 678.71, 465.51, 7595.85, 32.60, 4.08, 'EO B1'),
(181, 'Residente de Obra', 465.51, NULL, 465.51, 678.71, 465.51, 7595.85, 32.60, 4.08, 'EO B1'),
(190, 'Ayudante de laboratorio: con conocimientos básicos y dos años de experiencia<Estr. Oc. D2><*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'LABORATORIO'),
(191, 'Laboratorista 1: experiencia de hasta 7 años <Estr. Oc. C2><*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'LABORATORIO'),
(192, 'Laboratorista: <En Construcción - Estr.Oc.C1>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'LABORATORIO'),
(220, 'Práctico en la rama de la topografía <Estr.Oc.D2><*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'TOPOGRAFIA'),
(221, 'Topógrafo 1: experiencia de hasta 5 años<Estr.oc. C2><*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'TOPOGRAFIA'),
(222, 'Topógrafo <En Construcción - Estr.Oc.C1>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'TOPOGRAFIA'),
(240, 'Dibujante 1: con exper. de hasta 4 años <Estr.Oc.D2><*NSC>', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'DIBUJANTES'),
(241, 'Dibujante (En Construcción - Estr.Oc.C2)', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'DIBUJANTES'),
(260, 'Op. de Motoniveladora', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(261, 'Op. de Excavadora', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(262, 'Op. de Grúa puente de elevación', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(263, 'Op. de Pala de castillo', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(264, 'Op. de Grúa estacionaria', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(265, 'Op. de Draga/Dragline', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(266, 'Op. de Tractor carriles o ruedas <bulldozer  Topador  roturador  malacate  trailla>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(267, 'Op. de Tractor tiende tubos <side bone>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(268, 'Op. de Mototrailla', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(269, 'Op. de Cargadora frontal <Payloader sobre ruedas u orugas>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(270, 'Op. de Retroexcavadora', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(271, 'Op. de Auto-tren cama baja <tráiler>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(272, 'Op. de Fresadora de pavimento asfáltico / Rotomil', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(273, 'Op. de Recicladora de pavimento asfáltico / Rotomil', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(274, 'Op. de Planta de emulsión asfáltica', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(275, 'Op. de Máquina para sellos asfálticos', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(276, 'Op. de Squider', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(277, 'Operador de Camión articulado con volteo <En construcción>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(278, 'Operador de Camión mezclador para micropavimentos', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(279, 'Operador de camión cisterna para cemento y asfalto <Adicional al traslado debe conectar los equipos para embarque y desembarque, monitorear equipo de presión>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(280, 'Operador de perforadora de brazos múltiples <jumbo>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(281, 'Operador máquina tuneladora <topo>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(282, 'Operador de concretera rodante', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(283, 'Operador de máquina extendedora de adoquín', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(284, 'Operador de máquina zanjadora', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(285, 'Concretera rodante / migser', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1 GI'),
(300, 'Op. Responsable de la planta hormigonera', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(301, 'Op. Responsable de la planta trituradora', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(302, 'Op. Responsable de la planta asfáltica', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(303, 'Op. Operador de truck drill', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(304, 'Op. Rodillo autopropulsado', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(305, 'Op. Distribuidor de asfalto', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(306, 'Op. Distribuidor de agregados', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(307, 'Op. Acabadora de pavimento de hormigón', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(308, 'Op. Acabadora de pavimento asfaltico', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(309, 'Op. de Grada elevadora/Canastilla Elevadora', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(310, 'Op. de Montacargas<*NSC>', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(311, 'Op. de Operador de roto mil <*NSC>', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(312, 'Operador de bomba impulsadora de hormigón, equipos móviles de planta, molino de amianto, planta dosificadora de hormigón, productos terminados <tanques moldeados, postes de alumbrado eléctrico, acabados de piezas afines>', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(313, 'Op. de Tractor de ruedas <barredora. cegadora. rodillo remolcado. franjeadora>', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(314, 'Op. de Caldero planta asfáltica', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(315, 'Op. de Barredora autopropulsada', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(316, 'Op. de Martillo punzón neumático', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(317, 'Op. de Compresor', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(318, 'Op. de Camión de carga frontal <En construcción>', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(319, 'Op. de Operador canguro', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(320, 'Op. de camión de volteo con o sin articulación / Dumper <En construcción>', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(321, 'Op. de Operador miniexcavadora/minicargadora con sus aditamentos', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(322, 'Op. de Operador termoformado', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(323, 'Op. de canastilla elevadora', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(324, 'Técnico en carpintería', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(325, 'Técnico en mantenimiento de viviendas y edificios', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2 GII'),
(340, 'Operador máquina estacionaria clasificadora de material', 422.29, NULL, 422.29, 615.70, 422.29, 6927.76, 29.73, 3.72, 'EO C3'),
(341, 'Soldador en construcción', 422.29, NULL, 422.29, 615.70, 422.29, 6927.76, 29.73, 3.72, 'EO C4'),
(350, 'Mecánico de equipo pesado caminero <En Construcción - Estr.Oc.C1>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'MECANICOS'),
(351, 'Tornero fresador <Estr.Oc.C1><*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'MECANICOS'),
(352, 'Soldador eléctrico y/o acetileno <Estr.Oc.C1>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'MECANICOS'),
(353, 'Técnico mecánico-electricista <Estr.Oc.C1><*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'MECANICOS'),
(354, 'Mecánico de equipo liviano <Estr.Oc.C3>', 422.29, NULL, 422.29, 615.70, 422.29, 6927.76, 29.73, 3.72, 'MECANICOS'),
(355, 'Engrasador o abastecedor responsable en construcción<Estr.Oc.D2>', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'ST'),
(356, 'Ayudante de mecánico <Estr.Oc.C3><*NSC>', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'ST'),
(357, 'Ayudante de maquinaria <Estr.Oc.D2>', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'ST'),
(358, 'Vulcanizador <Estr.Oc.D2><*NSC>', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'ST'),
(370, 'Chofer profesional licencia tipo C <Estr. Oc. D2><*NSC>', 485.64, NULL, 485.64, 708.06, 485.64, 7907.02, 33.94, 4.24, 'CP'),
(371, 'Chofer profesional licencia tipo D <Estr.Oc. D1><*NSC>', 429.30, NULL, 429.30, 625.92, 429.30, 7036.12, 30.20, 3.77, 'CP'),
(372, 'Chofer profesional licencia tipo E. transporte de pasajeros clase B y C según el caso <Estr.Oc. C3><*NSC>', 440.86, NULL, 440.86, 642.77, 440.86, 7214.81, 30.96, 3.87, 'CP'),
(373, 'Chofer profesional licencia tipo E camión articulado o conacoplado clases C y D <Estr.Op C2><*NSC>', 451.50, NULL, 451.50, 658.29, 451.50, 7379.29, 31.67, 3.96, 'CP'),
(374, 'Chofer profesional licencia tipo E camión articulado y los comprendidos en clase B <Estr.Op C1><*NSC>', 456.28, NULL, 456.28, 665.26, 456.28, 7453.18, 31.99, 4.00, 'CP'),
(375, 'Chofer profesional licencia tipo D <Estr.Op. C1><*NSC>', 456.28, NULL, 456.28, 665.26, 456.28, 7453.18, 31.99, 4.00, 'CP'),
(376, 'CHOFER: Trailer <Estr. Oc. C1>', 614.84, NULL, 614.84, 896.43, 614.84, 9904.19, 42.51, 5.31, 'CP'),
(377, 'CHOFER: Volquetas <Estr. Oc. C1>', 614.84, NULL, 614.84, 896.43, 614.84, 9904.19, 42.51, 5.31, 'CP'),
(378, 'CHOFER: Tanqueros <Estr. Oc. C1>', 614.84, NULL, 614.84, 896.43, 614.84, 9904.19, 42.51, 5.31, 'CP'),
(379, 'CHOFER: Plataformas <Estr. Oc. C1>', 614.84, NULL, 614.84, 896.43, 614.84, 9904.19, 42.51, 5.31, 'CP'),
(380, 'CHOFER: Otros camiones <Estr. Oc. C1>', 614.84, NULL, 614.84, 896.43, 614.84, 9904.19, 42.51, 5.31, 'CP'),
(381, 'CHOFER: De vehículos de emergencia<Ambulancia, motobomba, carrocisterna, entre otros - Estr.Oc.C1>', 614.84, NULL, 614.84, 896.43, 614.84, 9904.19, 42.51, 5.31, 'CP'),
(382, 'CHOFER: Para camiones pesados y extra pesados con o sin remolque de mas de 4 Toneladas <Estr. Oc. C1>', 614.84, NULL, 614.84, 896.43, 614.84, 9904.19, 42.51, 5.31, 'CP'),
(383, 'CHOFER: Camiones para transportar mercancias o sustancias peligosas y otros vehículos especiales <Estr. Oc. C1>', 614.84, NULL, 614.84, 896.43, 614.84, 9904.19, 42.51, 5.31, 'CP'),
(384, 'CHOFER: Para transporte Escolar-Personal y turismo hasta 45 pasajeros <Estr. Oc. C2>', 608.39, NULL, 608.39, 887.02, 608.39, 9804.48, 42.08, 5.26, 'CP'),
(385, 'CHOFER: Para camiones sin acoplados <Estr. Oc. C3>', 594.06, NULL, 594.06, 866.15, 594.06, 9582.99, 41.13, 5.14, 'CP'),
(386, 'CHOFER: Para ferrocarriles <Estr.Oc.C1>', 614.84, NULL, 614.84, 896.43, 614.84, 9904.19, 42.51, 5.31, 'CP'),
(387, 'CHOFER: Para auto ferros <Estr.Oc.C1>', 614.84, NULL, 614.84, 896.43, 614.84, 9904.19, 42.51, 5.31, 'CP'),
(400, 'Operador de bomba', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(401, 'Equipo en general', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(402, 'Equipos móviles', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(403, 'Maquinaria', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(404, 'Molino de amianto', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(405, 'Planta dosificadora', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(406, 'De productos terminados', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(420, 'Eléctrico de línea de amianto<*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(421, 'Mecánico<*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(422, 'De equipo<*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(423, 'De línea de amianto<*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(424, 'De mantenimiento<*NSC>', 463.52, NULL, 463.52, 675.82, 463.52, 7565.10, 32.47, 4.06, 'EO C1'),
(440, 'Operador de bomba lanzadora de concreto', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2'),
(441, 'Equipos móviles de planta', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2'),
(442, 'Molino de amianto', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2'),
(443, 'Planta dosificadora de hormigón', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2'),
(444, 'De productos terminados', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2'),
(460, 'Bodeguero en general<*NSC>', 422.29, NULL, 422.29, 615.70, 422.29, 6927.76, 29.73, 3.72, 'EO C2'),
(461, 'Auxiliar de equipos en general<*NSC>', 422.29, NULL, 422.29, 615.70, 422.29, 6927.76, 29.73, 3.72, 'EO C2'),
(462, 'Expediciones<*NSC>', 422.29, NULL, 422.29, 615.70, 422.29, 6927.76, 29.73, 3.72, 'EO C2'),
(463, 'Líneas de amianto<*NSC>', 422.29, NULL, 422.29, 615.70, 422.29, 6927.76, 29.73, 3.72, 'EO C2'),
(464, 'Mecánica<*NSC>', 422.29, NULL, 422.29, 615.70, 422.29, 6927.76, 29.73, 3.72, 'EO C2'),
(465, 'Moldeo y desmoldeo<*NSC>', 422.29, NULL, 422.29, 615.70, 422.29, 6927.76, 29.73, 3.72, 'EO C2'),
(466, 'Placas de moldeo<*NSC>', 422.29, NULL, 422.29, 615.70, 422.29, 6927.76, 29.73, 3.72, 'EO C2'),
(467, 'Laboratorio<*NSC>', 422.29, NULL, 422.29, 615.70, 422.29, 6927.76, 29.73, 3.72, 'EO C2'),
(468, 'Planta<*NSC>', 422.29, NULL, 422.29, 615.70, 422.29, 6927.76, 29.73, 3.72, 'EO C2'),
(480, 'Preparador de mezcla de materias primas', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(481, 'Soldador<*NSC>', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(482, 'Tubero <En construcción>', 415.75, NULL, 415.75, 606.16, 415.75, 6826.66, 29.30, 3.66, 'EO D2'),
(490, 'Auxiliar de equipos en general<*NSC>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(491, 'Expediciones<*NSC>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(492, 'Líneas de amianto<*NSC>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(493, 'Mecánica<*NSC>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(494, 'Moldeo y desmoldeo<*NSC>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(495, 'Placas de moldeo<*NSC>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(496, 'Laboratorio<*NSC>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(497, 'Planta<*NSC>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(498, 'Resanador en general<En Construcción>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(499, 'Tinero de pasta de amianto', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(500, 'Trabajador de limpieza<*NSC>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(501, 'Vulcanizador<*NSC>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(520, 'Operadores de máquina<*NSC>', 439.95, NULL, 439.95, 641.45, 439.95, 7200.75, 30.90, 3.86, 'EO C2'),
(530, 'Ayudantes en general<EO E2>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E2'),
(531, 'Obreros en general<*NSC>', 410.40, NULL, 410.40, 598.36, 410.40, 6743.96, 28.94, 3.62, 'EO E3'),
(532, 'Técnico Salud, Seguridad, Ambiente y Calidad EO C3', 497.73, NULL, 497.73, 725.69, 497.73, 8093.91, 34.74, 4.34, NULL),
(533, 'Enfermera Profesional', 432.83, NULL, 432.83, 631.07, 432.83, 7090.69, 30.43, 3.80, NULL),
(534, 'Auxiliar de enfermería', 422.85, NULL, 422.85, 616.52, 422.85, 6936.42, 29.77, 3.72, NULL),
(535, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `salary_base_dollars`
--
ALTER TABLE `salary_base_dollars`
  ADD PRIMARY KEY (`code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

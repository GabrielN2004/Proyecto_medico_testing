use db_centro_medico_1;

INSERT INTO obrasociales (obrasocial_name) VALUES
('Particular'),
('Obra Social de Petroleros (OSPe)'),
('Obra Social de Empleados de Comercio (OSECAC)'),
('PAMI'),
('Organización de Servicios Directos Empresarios (OSDE)'),
('BORIAL'),
('Instituto de Prevision Social (IPS)');

INSERT INTO especialidades (especialidad_name) VALUES
('Cardiologia'),
('Cirugia General'),
('Medico Clinico'),
('Dermatologia'),
('Ginecologia'),
('Neurologia'),
('Pediatria'),
('Traumatologia');

INSERT INTO profesionales (profesional_fullname, profesional_matricula, profesional_email, profesional_password, id_especialidad) VALUES
('Maria Solis', 1418, 'SolisMaria@gmail.com', 'Maria14185', 1),
('Juan Damonte', 2613, 'JuanDamonte@gmail.com', 'Juan2613', 1),
('Laura Moreno', 2816, 'LauraMoreno@gmail.com', 'Laura2816', 5),
('Ludmila Loria', 2952, 'LudmilaLoria@gmail.com', 'Ludmila2952', 5),
('Barbara Vivado', 3224, 'BarbaraVivado@gmail.com', 'Barbara3224',5),
('Ignacio Fernandez', 3456, 'IgnacioFernandez@gmail.com', 'Ignacio3456', 6 ),
('Gonzalo Fernandez', 1578, 'GonzaloFernandez@gmail.com', 'Gonazalo1578', 6),
('Marcos Perez', 2127, 'MarcosPerez@gmail.com', 'Marcos2127', 2),
('Lucas Basualdo', 2310, 'LucasBasualdo@gmail.com', 'Lucas2310', 2),
('Lucila Ferni', 2847, 'LucilaFerni@gmail.com', 'Lucila2847', 4),
('Andrea Rodriguez', 2772, 'AndreaRodriguez@gmail.com', 'Andrea2772', 4),
('Adela Espalter', 2022, 'AdelaEspalter@gmail.com', 'Adela2022',4),
('Sebastian Sotta', 17829, 'SebastianSotta@gmail.com', 'Sebastian17829', 3),
('Federico Cardone', 3554, 'FedericoCardone@gmail.com', 'Federico3554', 3),
('Silvina Pereira', 3251, 'SilvinaPereira@gmail.com', 'Silvina3251', 3),
('Agusto Lavalle', 2312, 'AgustoLavalle@gmail.com', 'Agusto2312', 8),
('Luis Bondi', 2475, 'LuisBondi@gmail.com', 'Luis2475', 8),
('Valeria Blumetti', 2412, 'ValeriaBlumetti@gmail.com', 'Valeria2412', 7),
('Gustavo Sanchez', 2969, 'GustavoSanchez@gmail.com', 'Gustavo2969', 7);


INSERT INTO profesional_obrasocial (id_profesional, id_obrasocial) VALUES
(1,1),(1,2),(1,7), (2,1),(2,3),(2,5), (3,1),(3,3),(3,6), (4,1),(4,2),(4,4), (5,1),(5,3),(5,6), (6,1),(6,3),(6,7), (7,1),(7,2),(7,7), (8,1),(8,4),(8,5), (9,1),(9,2),(9,6),
(10,1),(10,3),(10,5), (11,1),(11,2),(11,7), (12,1),(12,4),(12,6), (13,1),(13,4),(13,7), (14,1),(14,3),(14,6), (15,1),(15,3),(15,7), (16,1),(16,2),(16,5), (17,1),(17,3),
(17,5), (18,1),(18,4),(18,2), (19,1),(19,4),(19,7);

INSERT INTO horarios (id_horario, horario_num) VALUES
(1, '08:00'),
(2, '10:30'),
(3, '13:00'),
(4, '15:30'),
(5, '09:00'),
(6, '11:00'),
(7, '14:00'),
(8, '16:00'),
(9, '08:30'),
(10, '10:00'),
(11, '12:30'),
(12, '15:00'),
(13, '09:15'),
(14, '11:45'),
(15, '13:45'),
(16, '16:15'),
(17, '07:45'),
(18, '09:45'),
(19, '12:15'),
(20, '14:45'),
(21, '08:15'),
(22, '10:15'),
(23, '13:15'),
(24, '15:30'),
(25, '09:30'),
(26, '11:30'),
(27, '14:30'),
(28, '16:30'),
(29, '07:30'),
(30, '10:45'),
(31, '13:30'),
(32, '15:15'),
(33, '12:00'),
(34, '08:45'),
(35, '13:45'),
(36, '16:00');

INSERT INTO horario_profesional (id_horario, id_profesional) VALUES
-- Maria Solis (id_profesional = 1)
(1, 1),
(2, 1),
(3, 1),
(4, 1),
-- Juan Damonte (id_profesional = 2)
(5, 2),
(6, 2),
(7, 2),
(8, 2),
-- Laura Moreno (id_profesional = 3)
(9, 3),
(10, 3),
(11, 3),
(12, 3),
-- Ludmila Loria (id_profesional = 4)
(13, 4),
(14, 4),
(15, 4),
(16, 4),
-- Barbara Vivado (id_profesional = 5)
(17, 5),
(18, 5),
(19, 5),
(20, 5),
-- Ignacio Fernandez (id_profesional = 6)
(21, 6),
(22, 6),
(23, 6),
(24, 6),
-- Gonzalo Fernandez (id_profesional = 7)
(25, 7),
(26, 7),
(27, 7),
(28, 7),
-- Marcos Perez (id_profesional = 8)
(29, 8),
(30, 8),
(31, 8),
(32, 8),
-- Lucas Basualdo (id_profesional = 9)
(33, 9),
(34, 9),
(35, 9),
(36, 9),
-- Lucila Ferni (id_profesional = 10)
(1, 10),
(2, 10),
(3, 10),
(4, 10),
-- Andrea Rodriguez (id_profesional = 11)
(5, 11),
(6, 11),
(7, 11),
(8, 11),
-- Adela Espalter (id_profesional = 12)
(9, 12),
(10, 12),
(11, 12),
(12, 12),
-- Sebastian Sotta (id_profesional = 13)
(13, 13),
(14, 13),
(15, 13),
(16, 13),
-- Federico Cardone (id_profesional = 14)
(17, 14),
(18, 14),
(19, 14),
(20, 14),
-- Silvina Pereira (id_profesional = 15)
(21, 15),
(22, 15),
(23, 15),
(24, 15),
-- Agusto Lavalle (id_profesional = 16)
(25, 16),
(26, 16),
(27, 16),
(28, 16),
-- Luis Bondi (id_profesional = 17)
(29, 17),
(30, 17),
(31, 17),
(32, 17),
-- Valeria Blumetti (id_profesional = 18)
(33, 18),
(34, 18),
(35, 18),
(36, 18),
-- Gustavo Sanchez (id_profesional = 19)
(1, 19),
(2, 19),
(3, 19),
(4, 19);

-- Insertar roles de ejemplo
INSERT INTO roles (role_name) VALUES 
('Admin'),
('Profesional'),
('Paciente');

-- Insertar usuarios con sus roles
INSERT INTO usuarios (usuario_email, usuario_password, id_role) VALUES
('SolisMaria@gmail.com','Maria14185', 2),('JuanDamonte@gmail.com', 'Juan2613', 2),('LauraMoreno@gmail.com', 'Laura2816', 2),
('LudmilaLoria@gmail.com', 'Ludmila2952', 2),('BarbaraVivado@gmail.com', 'Barbara3224', 2),('IgnacioFernandez@gmail.com', 'Ignacio3456', 2),
('GonzaloFernandez@gmail.com', 'Gonazalo1578', 2),('MarcosPerez@gmail.com', 'Marcos2127', 2),('LucasBasualdo@gmail.com', 'Lucas2310', 2),
('LucilaFerni@gmail.com', 'Lucila2847', 2),('AndreaRodriguez@gmail.com', 'Andrea2772', 2),('AdelaEspalter@gmail.com', 'Adela2022',2),
('SebastianSotta@gmail.com', 'Sebastian17829', 2),('FedericoCardone@gmail.com', 'Federico3554', 2),('SilvinaPereira@gmail.com', 'Silvina3251', 2),
('AgustoLavalle@gmail.com', 'Agusto2312', 2),('LuisBondi@gmail.com', 'Luis2475', 2),('ValeriaBlumetti@gmail.com', 'Valeria2412', 2),('GustavoSanchez@gmail.com', 'Gustavo2969', 2);

-- Ejemplo de insert de un token para el usuario admin (por ejemplo)
INSERT INTO tokens (token, id_usuario) VALUES
('token_de_ejemplo_para_admin', 1);

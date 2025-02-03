create database if not exists db_centro_medico_test;

use db_centro_medico_test;

-- Crear la tabla de roles
CREATE TABLE if not exists roles (
    id_role INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- Crear la tabla de usuarios con el campo de roles
CREATE TABLE if not exists usuarios (
    id_usuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    usuario_email VARCHAR(200) NOT NULL UNIQUE,
    usuario_password VARCHAR(100) NOT NULL,
    id_role INT NOT NULL,
    FOREIGN KEY (id_role) REFERENCES roles(id_role)
) ENGINE=InnoDB;

-- Crear la tabla de tokens
CREATE TABLE if not exists tokens (
    id_token INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    token VARCHAR(255) NOT NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
) ENGINE=InnoDB;

create table if not exists Pacientes(
    dni_paciente int not null unique primary key,
    paciente_name varchar(150) not null,
    paciente_lastname varchar(150) not null,
    paciente_email varchar(200) not null,
    paciente_password varchar(100) not null,
    id_obrasocial int not null,
    constraint obrasocial_paciente_fk foreign key(id_obrasocial) references obrasociales(id_obrasocial)
) engine=InnoDB;

create table if not exists Profesionales(
    id_profesional int not null unique auto_increment primary key,
    profesional_fullname varchar(250) not null,
    profesional_matricula int not null,
    profesional_email varchar(200) not null,
    profesional_password varchar(100) not null,
    id_especialidad int not null,
    constraint especialidad_profesional_fk foreign key(id_especialidad) references especialidades(id_especialidad)
) engine=InnoDB;

create table if not exists turnos(
    id_turno int not null unique auto_increment primary key,
    dni_paciente int not null,
    id_especialidad int not null,
    id_profesional int not null,
    id_obrasocial int not null,
    fecha_turno date not null,
    id_horario int not null,
    constraint especialidad_fk foreign key(id_especialidad) references especialidades(id_especialidad),
    constraint paciente_fk foreign key(dni_paciente) references pacientes(dni_paciente),
    constraint profesional_fk foreign key(id_profesional) references profesionales(id_profesional),
    constraint obrasocial_fk foreign key(id_obrasocial) references obrasociales(id_obrasocial),
    constraint horario_fk foreign key(id_horario) references horarios(id_horario)
) engine=InnoDB;

create table if not exists obrasociales(
    id_obrasocial int not null auto_increment unique primary key,
    obrasocial_name varchar(100) not null
) engine=InnoDB;

create table if not exists especialidades(
    id_especialidad int not null unique auto_increment primary key,
    especialidad_name varchar(100) not null
) engine=InnoDB;

create table if not exists profesional_obrasocial (
    id_profesional INT,
    id_obrasocial INT,
    PRIMARY KEY (id_profesional, id_obrasocial),
    FOREIGN KEY (id_profesional) REFERENCES profesionales(id_profesional),
    FOREIGN KEY (id_obrasocial) REFERENCES obrasociales(id_obrasocial)
);

create table if not exists horarios(
    id_horario int not null auto_increment unique primary key,
    horario_num varchar(20) not null
);

create table if not exists horario_profesional(
    id_horario int,
    id_profesional int,
    PRIMARY KEY (id_horario, id_profesional),
    foreign key (id_profesional) references profesionales(id_profesional),
    foreign key (id_horario) references horarios(id_horario)
);



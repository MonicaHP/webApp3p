create database proyecto;

use proyecto;

create table usuarios(
	contraseña VARCHAR(20) NOT NULL PRIMARY KEY,
    nombre VARCHAR(35) COLLATE latin1_spanish_ci NOT NULL
);

INSERT INTO usuarios VALUES('mongo', 'moni1234')

CREATE TABLE peliculas(
    id_pelicula int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pelicula varchar(100) COLLATE latin1_spanish_ci NOT NULL,
    pais varchar(30) COLLATE latin1_spanish_ci NOT NULL,
    anio varchar(5) COLLATE latin1_spanish_ci NOT NULL,
    genero varchar(30) COLLATE latin1_spanish_ci NOT NULL,
    duracion varchar(10) COLLATE latin1_spanish_ci NOT NULL,
    descripcion varchar(1000) COLLATE latin1_spanish_ci NOT NULL
);

INSERT INTO peliculas VALUES(1, 'Storks (Cigüeñas)', 'Estados Unidos', '2016', 'Animación', '1h 27min', 'Las cigüeñas entregan bebés… o al menos solían hacerlo. Ahora entregan paquetes para una gran compañía minorista de internet a nivel mundial. Junior, la mejor cigüeña repartidora de la compañía, está a punto de conseguir un ascenso cuando activa accidentalmente la Máquina de Producción de Bebés, fabricando a una adorable niña totalmente no autorizada. Desesperado por entregar este problemático paquete antes de que su jefe se dé cuenta, Junior y su amiga Tulip, la única humana de Stork Mountain, se apresuran para hacer su primera entrega de un bebé en un viaje salvaje y revelador que podría afectar a la integridad de más de una familia y restablecer la verdadera misión de las cigüeñas en el mundo.');

select * from peliculas;

SELECT * FROM usuarios;


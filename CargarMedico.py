#CargarMedico)
import sqlite3
miConexion = sqlite3.connect("Salus")
miCursor = miConexion.cursor()
miCursor.execute("""
        CREATE TABLE if not exists UsuarioMedico (
        DniM integer Primary key not null,
        Matricula integer not null,
        Nombre varchar (45) not null,
        Apellido  varchar (45) not null,
        Telefono varchar (45) not null,
        Celular varchar (45) not null
        Localidad varchar (45) not null
        Email varchar (45) not null
        )
""")
medicos = [
    (11111111, 10000011 , 'Carlos', 'Gonzalez', '42000000', '42100000', 'Cordoba', 'doctor0@mail.com'),
    (22222222, 20000012 , 'Roman', 'Solmi', '4300000', '4310000', 'Cordoba', 'doctor1@mail.com'),
    (11111111, 10000011 , 'Pedro', 'Perez', '450000', '441000', 'Cordoba', 'doctor2@mail.com'),
    (11111111, 10000011 , 'Lucas', 'Suarez', '46000', '48100000', 'Cordoba', 'doctor3@mail.com'),
]
miCursor.executemany("INSERT INTO UsuarioMedico VALUES (?, ?, ?, ?, ?, ?)", medicos)
miCursor.execute("INSERT INTO UsuarioMedico VALUES (11111111, 10000011 , 'Carlos', 'Gonzalez', '42000000', '42100000', 'Cordoba', 'doctor0@mail.com')")
miConexion.commit()
miConexion.close()
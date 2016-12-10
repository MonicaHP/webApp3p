import web, datetime

db = web.database(dbn='mysql', db='proyecto', user='root', pw='1234')

def get_posts():
    return db.select('peliculas')

def get_users():
    return db.select('usuarios')

def get_post(id):
    try:
        return db.select('peliculas', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(peliculaP, paisP, anioP, generoP, duracionP, descripcionP):
    db.insert('peliculas', pelicula = peliculaP, pais = paisP, anio = anioP,
    genero = generoP, duracion = duracionP, descripcion = descripcionP)

def del_post(id):
    db.delete('peliculas', where="id=$id", vars=locals())

def update_post(id, peliculaP, paisP, anioP, generoP, duracionP, descripcionP):
    db.update('peliculas', where="id=$id", vars=locals(),
    pelicula = peliculaP, pais = paisP, anio = anioP,
    genero = generoP, duracion = duracionP, descripcion = descripcionP)

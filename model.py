import web, datetime

db = web.database(dbn='postgres', host='ec2-23-23-111-171.compute-1.amazonaws.com', db='dei9ba2ltnl7hr', user='pezsraeegskepv', pw='41a57be28f709adc0a66deab194e16a8bdb58da346ce529f32d6bf18d1e7420a')


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

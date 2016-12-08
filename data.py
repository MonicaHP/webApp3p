import json

class data:  
    data = []

    def read(self):
        with open('data/data.json','r') as file:
            data = json.load(file)
            self.data = data['results'] 

    def getEntidad(self): 
        entidades = []
        for row in self.data:
            entidad = row['entidad']
            if entidad not in entidades:
                entidades.append(entidad)
        return entidades

    def getDelito(self): 
        delitos = []
        for row in self.data:
            delito = row['delito']
            if delito not in delitos:
                delitos.append(delito)
        return delitos      
        
    def getAnio(self, entidad, delito):
        inAnio = []  
        for row in self.data:
            inEntidad = row['entidad']
            inDelito = row['delito']
            if inEntidad == entidad and inDelito == delito:
                inAnio.append([row['entidad'], inDelito, row['anio']])
        return inAnio      
                

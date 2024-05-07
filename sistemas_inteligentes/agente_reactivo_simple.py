#Fuente: Canal de Youtube Descubriendo la Inteligencia Artificial

#Diccionario clave valor
REGLAS = {
    'moneda': 'pedir-codigo',
    'a1': 'servir-bebida1',
    'a2': 'servir-bebida2',
    'a3': 'servir-bebida3'
}

class AgenteReactivoSimple:
    
    #Constructor que va a recibir una serie de acciones que van a guardar una lista de percepciones.
    def __init__(self, reglas):
        self.reglas = reglas
        
    #Funcion que permite al agente actuar de acuerdo a lo que esta actualmente en el agente y la percepcion recibida
    def actuar(self, percepcion, accion_basica=""):
        if not percepcion:
            return accion_basica
        if percepcion in self.reglas.keys():
            return self.reglas[percepcion]
        return accion_basica
    
print("--Agente: Reactivo simple --")
expendedora = AgenteReactivoSimple(REGLAS)
percepcion = input("Indicar percepcion: ")
while percepcion:
    accion = expendedora.actuar(percepcion, 'reiniciar')
    print(accion)
    percepcion = input("Indicar percepcion: ")

import random as rd # Librería random para los dados
import pandas as pd # Librería para las hojas de cálculo
import numpy as np # Librería para diferentes operaciones matemáticas con matrices

def dado_dm(): # Dado del Dungeon Master
    num = rd.randint(1,6)
    print(f'RESULTADO: {num}')

class Personaje(): # Creación de un personaje

    def __init__(self, nombre=0,vida=0, exp=0, armadura=0,habilidades_=[], destreza=0, 
                constitucion=0,inteligencia=0,sabiduria=0,carisma=0,inventario_=[],
                engano=0,nivel_=0,info_=None, umbral=0,clase=None):
        
        # Stats
        self.nombre = nombre
        self.vida = vida
        self.exp = exp
        self.armadura = armadura
        self.nivel_ = nivel_
        self.clase = clase

        # Atributos
        self.destreza = destreza
        self.constitucion = constitucion
        self.inteligencia = inteligencia
        self.sabiduria = sabiduria
        self.carisma = carisma
        self.engano = engano

        # Coleccionables
        self.habilidades_ = habilidades_
        self.inventario_ = inventario_
        self.info_ = info_

        # Umbral del dado:
        self.umbral = 7

    #----------------- MOSTRAR INFO-----------------#

    def comandos(self): # Mostrar los comandos disponibles para los jugadores

        dicc_comandos = {f'{self.nombre}.stats()':'Mostrar los stats de tu personaje',
                     f'{self.nombre}.atributos()':'Mostrar los atributos de tu personaje',
                     f'{self.nombre}.habiliades()':'Mostrar las habilidades de tu personaje',
                     f'{self.nombre}.inventario()':'Mostrar el inventario de tu personaje',
                     f'{self.nombre}.info()':'Mostrar la info de tu personaje',
                     f'{self.nombre}.tirar_dado(\'atributo\')':'Para tirar el dado'}
        
        df = pd.DataFrame([[i, dicc_comandos[i]] for i in dicc_comandos.keys()], 
                        columns=['Comando', 'Info'])

        return df

    def stats(self): # Mostrar stats

        stats_dicc = {'Nombre':self.nombre,'Clase':self.clase,'Vida':self.vida,
                      'Armadura':self.armadura,'XP':self.exp, 'Nivel':self.nivel_}

        df = pd.DataFrame([[i, stats_dicc[i]] for i in stats_dicc.keys()], 
                        columns=['Stat', 'Valor'])

        return df

    def atributos(self): # Mostrar atributos
        
        atributos_dicc = {'Destreza':self.destreza, 'Constitucion':self.constitucion,
                               'Inteligencia': self.inteligencia, 'Sabiduría':self.sabiduria,
                               'Carisma':self.carisma, 'Engaño':self.engano}

        df = pd.DataFrame([[i, atributos_dicc[i]] for i in atributos_dicc.keys()], 
                        columns=['Atributo', 'Valor'])
        
        return df

    def habilidades(self): # Mostrar habilidades

        df = pd.DataFrame(self.habilidades_, columns=['HABILIDADES'])
        return df
    
    def inventario(self): # Mostrar inventario
        
        df = pd.DataFrame(self.inventario_, columns=['Inventario'])
        return df

    def info(self): # Mostrar info
        print(self.info_)

    #----------------- MODIFICAR ATRIBUTOS -----------------#

    def _vida(self, vida): # Para subirle o bajarle vida al personaje
        self.vida += vida

    def _exp(self, exp): # Para subirle o bajarle experiencia al personaje
        self.exp += exp
    
    def colocar_habilidad(self, habilidad): # Para agregarle una habilidad al personaje

        if habilidad in self.habilidades_:
            return
        else:
            self.habilidades_.append(habilidad)

    def quitar_habilidad(self, habilidad): # Para quitarle una habilidad al personaje

        if habilidad not in self.habilidades_:
            return
        else:
            self.habilidades_.remove(habilidad)

    def colocar_objeto(self, objeto): # Para colocar un objeto en el inventario

        if objeto in self.inventario_:
            return
        else:
            self.inventario_.append(objeto)

    def quitar_objeto(self, objeto): # Para quitar un objeto del inventario

        if objeto not in self.inventario_:
            return
        else:
            self.inventario_.remove(objeto)

    def subir_nivel(self):

        condicion = 3 # Cada cuanta experiencia se sube el nivel
        exp_niveles = np.arange(0,9999,condicion)

        for i in range(0, len(exp_niveles)):

            if exp_niveles[i] > self.exp:
                pass
            else:
                self.nivel_ = i

    #----------------- TIRAR DADOS -----------------#

    def tirar_dado(self, para):
        
        nota = f'Un resultado menor a {self.umbral} puede ser algo malo, pero te sube experiencia\n'
        num_dado = 6 # Número de caras que tiene el dado
                
        if para == 'destreza':
            resultado = rd.randint(1,num_dado) + self.destreza
            print(nota)
            print(f'RESULTADO: {resultado}')
        
        elif para == 'constitucion':
            resultado = rd.randint(1,num_dado) + self.constitucion
            print(nota)
            print(f'RESULTADO: {resultado}')

        elif para == 'inteligencia':
            resultado = rd.randint(1,num_dado) + self.inteligencia
            print(nota)
            print(f'RESULTADO: {resultado}')

        elif para == 'sabiduria':
            resultado = rd.randint(1,num_dado) + self.sabiduria
            print(nota)
            print(f'RESULTADO: {resultado}')

        elif para == 'carisma':
            resultado = rd.randint(1,num_dado) + self.carisma
            print(nota)
            print(f'RESULTADO: {resultado}')

        elif para == 'engaño':
            resultado = rd.randint(1,num_dado) + self.engano
            print(nota)
            print(f'RESULTADO: {resultado}')

        else:
            print('ATENCIÓN: NO EXISTE EL ATRIBUTO QUE COLOCASTE, POR FAVOR INGRESA UN ATRIBUTO VÁLIDO')

    def dado(self,resultado): # El dado absoluto, puede controlar el destino de los personajes
                                 # - No disponible para jugadores -

            if resultado < self.umbral:
                self.exp += 3
            
            elif resultado > self.umbral:
                self.exp += 1
            
            self.subir_nivel()
        
    def reinciar_valores(self):
            self.exp = 0


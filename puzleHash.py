#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:19:27 2017

@author: Arthur18
"""

#Practica 5 SPSI: Puzles Hash
#Funcion de la tarea 1

#Librerias para numeros aleatorios, funciones Hash
#y manejo de cadenas hexadecimales
import random
import hashlib
import string

#Variables globales a utilizar en la funcion
random.seed(18)
N = 64
maximum_b = 19
texto = """En un lugar de la Mancha, de cuyo nombre no quiero acordar-me, 
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, 
adarga antigua, rocín flaco y galgo corredor."""
#Para la transformacion a binario y gestion de cadenas hexadecimales
hex_digits = string.hexdigits[0:16]
escala = 16 
num_bits = 256


#Funcion para crear el nonce
def crear_nonce(tam=8):
  
  #Creamos una cadena hexadecimal con tam caracteres
  #Los caracteres se eligen de forma aleatoria dentro del
  #conjunto de caracteres hexadecimales
  return ''.join(random.choice(hex_digits) for _ in range(tam))

#Funcion para comprobar la cantidad de ceros al inicio del hash
def comprobar_ceros(hash):
  
  hash_bin = bin(int(hash, escala))[2:].zfill(num_bits)
  count = 0

  for i in range(0,len(hash_bin)):
    if(hash_bin[i] == '0'):
      count+=1
    else:
      break
    
  return count
    

#Funcion que recibe como parametro un texto y un valor b
def puzle_hash(msg, b):
  
  intentos_totales = 0
  
  for reps in range(0,10):
    #Creacion del nonce
    nonce = str(crear_nonce(int(N/4)))
    
    #Creacion del id, que es el msg concatenado con el nonce
    id = msg + nonce
    
    #Inicio del puzle hash: numero de intentos y condicion de parada
    intentos_actuales, encontrado = 0, False
    x,hash = "",""
  
    while(not encontrado):
      #Aumentamos el numero de intentos y creamos id||X
      intentos_actuales+=1
      x = str(crear_nonce(int(N/4)))
      test = id + x
      hash = str(hashlib.sha256(test.encode('utf-8')).hexdigest())
      encontrado = comprobar_ceros(hash) >= b
      
    intentos_totales += intentos_actuales
    #  print("Intentos " + str(intentos_actuales))
    #  print("Intentos totales " + str(intentos_totales))
    #  print("__________________________________________________________")
    #  print("Puzle Hash para B = " + str(b))  
    #  print("Cadena X -> " + x)
    #  print("Hash -> " + hash)
    #  print("Intentos " + str(intentos_actuales))
    #  print("----------------------------------------------------------")
    
    
  media_intentos = intentos_totales/10
  
  print("__________________________________________________________")
  print("Resultados Medios")
  print("Valor B , Intentos : %i , %f" % (b, media_intentos))
  print("----------------------------------------------------------")
  


#Ahora realizamos este procedimiento para valores de B que van desde
# 1 hasta el mayor valor posible
for valor_b in range(1, maximum_b):
  puzle_hash(texto, valor_b)

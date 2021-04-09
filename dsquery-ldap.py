#!/usr/bin/python
#programa para buscar e interactuar con servicio LDAP
# Objetivo::::::
#   1.- Encontrar los grupos en el ldap crear una lista de ellos donde el nombre del grupo 
#  es el parametros escencial para la busqueda (puede ser una expresion Regular) 
#   2.- Crear una lista de usuario por cada grupo encontrado 
#   3.- Crear una Virtual folder en el MFT via API con los valores de la lista de los grupos
#   4.- Crear los usuarios de Ldap en el MFT con los parametros obtenidos con la lista de grupos
#   o 
#   5.- asociar los grupos de ldap a los virtual folder creados. 

import os


def main ():
    """ Este function debe ejecutar la funcionalidad del script """


def load_group(expr):
    """ Esta function realizar la busqueda de los grupos de acuerdo al nombre o expresion,
        utilizada para cargar varios grupos"""
    groups = f"dsquery group -name {expr} | dsget group -dn -scope -secgrp -samid"
    salida4 = os.popen(groups).read()
    print("Salida:\n", salida4)


def load_user_expand_group():
    """crea una lista de usuarios extendiendose de la lista de grupos previamente hecha
        esto permite crear un archivo con los datos del grupo y los usuarios asociados a el """

def create_Vfolder():
    """ Crea la carpeta virtual en el MFT"""


def associate_group_ldap_to_Vfolder():
    """asocia los grupos a cada virtualforde de acuerdo a lo especificado"""

if __name__ == '__main__':
    load_group('GP_*')

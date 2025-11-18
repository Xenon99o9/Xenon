import os
from random import randint


def genere_cle(taille):
    """Genère une clé binaire aléatoire de la taille spécifiée et l'écrit dans un fichier 'cle.txt'."""
    fichier = open("fichier/cle.txt", "x")
    for i in range(taille):
        fichier.write(str(randint(0,1)))
    fichier.close()


def xor(bit1,bit2):
    """ Effectue l'opération XOR entre deux bits."""
    if bit1 == 1 and bit2 == 1:
        return 0
    if bit1 == 1 and bit2 == 0:
        return 1
    if bit1 == 0 and bit2 == 1:
        return 1
    if bit1 == 0 and bit2 == 0:
        return 0

def symetrique(message_bin, cle_bin, name):
    """ Chiffre ou déchiffre un message binaire en utilisant une clé binaire avec l'opération XOR.
    Le résultat est écrit dans un fichier spécifié par 'name'."""
    fichier = open("fichier/"+name, "x")

    message = "fichier/" + message_bin
    fichier_message = open(message, "r")
    cle = "fichier/" + cle_bin
    fichier_cle = open(cle, "r")
    

    message_bin = fichier_message.read()
    cle_bin = fichier_cle.read()


    taille_cle = len(cle_bin)
    taille_message = len(message_bin)
    
    if taille_message > taille_cle:
        dif = (taille_message//taille_cle) + 1
        taille_cle = taille_cle * dif

    

    fichier_message.close()
    fichier_cle.close()

    write = ""
    for bit in range(taille_message):
        write += str(xor(int(message_bin[bit]), int(cle_bin[bit])))

    
    fichier.write(write)
    fichier.close()


"""
genere_cle(10000)

symetrique("bin.txt", "cle.txt")
"""
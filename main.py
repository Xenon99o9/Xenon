from Text_chiffre import text_to_chiffre, chiffre_to_text, chiffre_to_bin, bin_to_chiffre
from Symetrique import genere_cle, symetrique
from Assymetrique import info_assymetrique, chiffrement_assy, dechiffrement_assy

def chiffrement_symetrique():
    cle = str(input("Entrez le nom du fichier de la clé (ex: cle.txt) : "))
    message = str(input("Entrez le nom du fichier du message à chiffrer (ex: text1.txt) : "))
    text_to_chiffre(message)
    chiffre_to_bin("chiffre.txt")
    symetrique("bin.txt", cle, "chiffree_sym.txt")
    print("Chiffrement terminé. Le message chiffré est dans 'chiffree_sym.txt'.")

def dechiffrement_symetrique():
    cle = str(input("Entrez le nom du fichier de la clé (ex: cle.txt) : "))
    message_chiffre = str(input("Entrez le nom du fichier du message chiffré (ex: chiffree_sym.txt) : "))
    symetrique(message_chiffre, cle, "dechiffree_sym.txt")
    bin_to_chiffre("dechiffree_sym.txt")
    chiffre_to_text("chiffre_from_bin.txt")
    print("Déchiffrement terminé. Le message est dans 'dechiffre.txt'.")


#chiffrement_symetrique()
#dechiffrement_symetrique()

def chiffrement_assymetrique():
    p, q, n, e, d = info_assymetrique()
    print(f"Clé publique (n, e): ({n}, {e})")
    print(f"Clé privée d: {d}")
    message = str(input("Entrez le nom du fichier du message à chiffrer (ex: text1.txt) : "))
    text_to_chiffre(message)
    chiffrement_assy("chiffre.txt", e, n)
    print("Chiffrement terminé. Le message chiffré est dans 'message_chiffree.txt'.")

def dechiffrement_assymetrique():
    d= int(input("Entrez la clé privée d : "))
    n = int(input("Entrez le module n : "))
    message_chiffre = str(input("Entrez le nom du fichier du message chiffré (ex: message_chiffree.txt) : "))
    dechiffrement_assy(message_chiffre, d, n)
    chiffre_to_text("message_dechiffre.txt")
    print("Déchiffrement terminé. Le message est dans 'message_dechiffre.txt'.")

#chiffrement_assymetrique()
#dechiffrement_assymetrique()
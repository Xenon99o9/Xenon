convert = {"a": "01", "b": "02", "c": "03", "d": "04", "e": "05", "f": "06", "g": "07", "h": "08", "i": "09", "j": "10",
           "k": "11", "l": "12", "m": "13", "n": "14", "o": "15", "p": "16", "q": "17", "r": "18", "s": "19", "t": "20",
           "u": "21", "v": "22", "w": "23", "x": "24", "y": "25", "z": "26", " ": "00",
           ".": "27", ",": "28", "?": "29", "!": "30", "'": "31", "/": "32", "@": "33", "#": "34", "$": "35", "%": "36",
            "^": "37", "&": "38", "*": "39", "(": "40",
           ")": "41", "-": "42", "_": "43", "+": "44", "=": "45", ":": "46", ";": "47", "A": "48", "B": "49", "C": "50", "D": "51",
           "E": "52", "F": "53", "G": "54", "H": "55", "I": "56", "J": "57", "K": "58", "L": "59", "M": "60", "N": "61", "O": "62", "P": "63", "Q": "64",
           "R": "65", "S": "66", "T": "67", "U": "68", "V": "69", "W": "70", "X": "71", "Y": "72", "Z": "73","0": "74", "1": "75", "2": "76", "3": "77", 
           "4": "78", "5": "79", "6": "80", "7": "81", "8": "82", "9": "83","é": "84", "è": "85", "à": "86", "ù": "87", "ç": "88",
             "ô": "89", "ê": "90", "î": "91", "â": "92","ë": "93", "ü": "94", "ï": "95"}
#dico de conversion texte -> chiffre et chiffre -> texte


def text_to_chiffre(doc): 
    """Convertit le texte d'un fichier en une suite de chiffres selon le dictionnaire de conversion."""
    racourci = "fichier/" + str(doc)
    fichier = open(racourci, "r")
    fichier_text =  fichier.read()
    fichier.close()

    fichier_chiffre = open("fichier/chiffre.txt", "x")
    for char in fichier_text:
        if char in convert:
            fichier_chiffre.write(convert[char])
    fichier_chiffre.close()


def chiffre_to_text(doc):
    """Convertit une suite de chiffres d'un fichier en texte selon le dictionnaire de conversion."""
    racourci = "fichier/" + doc
    fichier = open(racourci, "r")
    fichier_chiffre =  fichier.read()
    fichier.close()

    fichier_text = open("fichier/dechiffre.txt", "x")
    for i in range(0, len(fichier_chiffre), 2):
        fichier_chiffre_pair = fichier_chiffre[i]+fichier_chiffre[i+1]
        for key, value in convert.items():
            if fichier_chiffre_pair == value:
                fichier_text.write(key)
    fichier_text.close()

def chiffre_to_bin(doc):
    """Convertit une suite de chiffres d'un fichier en binaire."""
    raccourci = "fichier/" + doc
    fichier = open(raccourci, "r")
    fichier_chiffre = fichier.read()
    fichier.close()

    binaire = bin(int(fichier_chiffre))[2:]   # conversion en binaire

    # On s'assure d'avoir une longueur paire
    if len(binaire) % 2 != 0:
        binaire = "0" + binaire

    fichier_bin = open("fichier/bin.txt", "x")
    fichier_bin.write(binaire)
    fichier_bin.close()

def bin_to_chiffre(doc):
    """Convertit une suite binaire d'un fichier en chiffres."""
    racourci = "fichier/" + doc
    fichier = open(racourci, "r")
    fichier_bin =  fichier.read()
    fichier.close()


    
    binaire_int = int(fichier_bin, 2)
    
    if binaire_int%2 != 0: #SINON CACA
        chiffre = "0" + str(binaire_int)
    else:
        chiffre = str(binaire_int)

        

    fichier_chiffre = open("fichier/chiffre_from_bin.txt", "x")
    fichier_chiffre.write(chiffre)
    fichier_chiffre.close()

"""
text_to_chiffre("text1.txt")

chiffre_to_text("chiffre.txt")

chiffre_to_bin("chiffre.txt")

bin_to_chiffre("bin.txt")
"""
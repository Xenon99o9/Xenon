import random

def est_premier(n, k=20):
    """Teste si un nombre n est premier en utilisant le test de Miller-Rabin avec k itérations."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Décomposition n-1 = d * 2^s
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    # Test de Miller-Rabin
    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

# Génération d’un grand premier
def genere_premier(bits=1024):
    """Génère un nombre premier de la taille spécifiée en bits."""
    while True:
        n = random.getrandbits(bits)
        n |= 1  # force impair
        if est_premier(n):
            return n

def phi(p, q):
    """Calcule la fonction indicatrice d'Euler φ(n) pour n = p * q."""
    return (p - 1) * (q - 1)

def euclide_etendu(a, b):
    """Calcule le PGCD de a et b ainsi que les coefficients de Bézout."""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = euclide_etendu(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def inverse_modulaire(e, phi):
    """Calcule l'inverse modulaire de e modulo phi."""
    gcd, x, _ = euclide_etendu(e, phi)
    if gcd != 1:
        raise Exception("e et phi(n) ne sont pas coprimes → inverse impossible")
    return x % phi

def info_assymetrique():
    """Génère les paramètres pour le chiffrement asymétrique RSA et les écrit dans un fichier."""
    p = genere_premier()
    q = genere_premier()
    while p == q:
        q = genere_premier()
   
    n = p * q
    e = 65537
    d = inverse_modulaire(e, phi(p, q))

    fichier = open("fichier/info_assy.txt", "x")
    fichier.write(f"p: {p}\nq: {q}\nn: {n}\ne: {e}\nd: {d}\n")
    fichier.close()

    return p, q, n, e, d


def chiffrement_assy(fichier_message, e, n):
    """Chiffre un message en utilisant la clé publique (e, n) et écrit le résultat dans un fichier."""
    nom = "fichier/" + str(fichier_message)
    fichier_message = open(nom, "r")
    message_int = int(fichier_message.read())
    fichier_message.close()

    if message_int >= n:
        raise ValueError("Le message est trop grand pour le module n.")

    message_chiffree = pow(message_int, e, n)

    fichier = open("fichier/message_chiffree.txt", "x")
    fichier.write(str(message_chiffree))
    fichier.close()



def dechiffrement_assy(fichier_chiffre, d, n):
    """Déchiffre un message en utilisant la clé privée d et écrit le résultat dans un fichier."""
    nom = "fichier/" + str(fichier_chiffre)
    fichier_chiffre = open(nom, "r")
    message_chiffree_int = int(fichier_chiffre.read())
    fichier_chiffre.close()

    message_dechiffree = pow(message_chiffree_int, d, n)
    message_dechiffree = str(message_dechiffree)
    if len(message_dechiffree) % 2 != 0:
        message_dechiffree = "0" + message_dechiffree

    fichier = open("fichier/message_dechiffre.txt", "x")
    fichier.write(message_dechiffree)
    fichier.close()
#### Imports et définition des variables globales
"""
Exercice réalisé par : Arnaud POCHIC
"""
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf8') as f:
        l=[]
        s=f.readlines()
        temp=[]
        temp2=[]
        for line in s:
            temp=line.split(";")
            temp2=[int(elt.strip()) for elt in temp]
            l.append(temp2)
    return l

def get_list_k(data, k):
    """

    retourne le kième indice de la liste de listes data

     Args:
        data (list), k (int)

     Returns:
        data[k]

    """
    return data[k]

def get_first(l):
    """
     retourne le premier élément de la liste l

     Args:
        list

     Returns:
        le premier élément de la liste

     """
    return l[0]

def get_last(l):
    """
     retourne le dernier élément de la liste

     Args:
        l (list)

     Returns:
        le dernier élément de la liste

     """
    return l[-1]

def get_max(l):
    """
     retourne le maximum de la liste

     Args:
        l (list)

     Returns:
        le maximum de la liste

     """
    return max(l)


def get_min(l):
    """
     retourne le minimum 

     Args:
        l (list)

     Returns:
        le minimum de la liste

     """
    return min(l)

def get_sum(l):
    """
     retourne la somme de cette liste

     Args:
        l (list)

     Returns:
        la somme de la liste

     """
    return sum(l)

#### Fonction principale


def main():
    """
     fonction principale qui appelle et teste les fonctions secondaires
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()

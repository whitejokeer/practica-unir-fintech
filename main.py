"""
License: Apache
Organization: UNIR
"""
##Importar las librerias necesarias
import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

##Ordena la lista en orden ascendente
def sort_list(items, ascending=True):
    """
    Ordena una lista de elementos.

    Args:
        items (list): Lista de elementos a ordenar.
        ascending (bool, opcional): Si True, ordena de forma ascendente. 
                                     Si False, ordena de forma descendente. 
                                     Por defecto es True.

    Returns:
        list: Una nueva lista ordenada según el parámetro 'ascending'.

    Raises:
        RuntimeError: Si 'items' no es una lista.
    """
    if not isinstance(items, list):
        raise RuntimeError(f"cant order {type(items)}")

    return sorted(items, reverse=(not ascending))

##Remueve los elementos duplicados de la lista
    return list(set(items))

##Bucle para leer el archivo y llamar las funciones definidas antes
if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("The file must be specified as the first argument.")
        print("The second argument indicates whether you want to remove duplicates.")
        sys.exit(1)

    print(f"The words in the file will be read {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))

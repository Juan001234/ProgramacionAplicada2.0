print ({"name": "Victor"}.get("name"))
# Retorna "Victor"
# Retornar no es lo mismo que imprimir

{"name":"Victor"}.get("nickname")
# Retorna "none"
print({"name":"Victor"}.get("nickname", "nickname is not a key))
# Retorna e imprime "nickname is not a key"
                            

dictionary = { 1: 'hello', 'two': True, '3': [1, 2, 3], 'Four': {'fun': 'addition'}, 5.0: 5.5}
print(dictionary)
# El dicionario nos permite mezclar varios tipos de caracteres


dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}

dict1.update(dict2) 
# Este comando actualizara el diccionario 1 con los elementos del diccionario 2
# y sobrescribirá las claves de los elementos que compartan el mismo nombre


ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}

ex dict.keys()

# dict_kays(["a","b","c"]} (retorna las palabras claves en forma de lista)

ex_dict.values() 

# dict_values(["anteater", "bumbleben", "cheetah"]). (retorna los valores en forma de lista)

ex_dict.items()

# dict_items([("a", "anteater"), ("b","bumblebee"),("c", "cheetah")]) (Retorna en forma de tuplas dentro de una lista)



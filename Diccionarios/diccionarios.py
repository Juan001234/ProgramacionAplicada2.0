sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}  #diccionario palabras claves srtring con valor asignado numero
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)
print(num_cameras)

translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" } #diccionario palabras claves string con valor asignado string
print(translations)

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}  #diccionario palabras claves string con valor asignado lista string

print(children)
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"], 1500123457:750000} #diccionario palabras claves string con valor asignado string
print(children)                                                                                                               #mas palabla clave numero con un valor asignado numero

my_emmpty_diccionary = {}                                                   #se crea un diccionario vacio                                                                  
print(my_emmpty_diccionary)                              
my_emmpty_diccionary["dinosaurs"] = 0                                       #se añade una palabra clave con valor asignado a la lista
print(my_emmpty_diccionary)


animals_in_zoo = {"zebras": 8, "monkeys": 12}
animals_in_zoo["dinosaurs"] =  0
print(animals_in_zoo)

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print(menu)
menu["cheesecake"] = 8
print(menu)
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"dinosaurs": 0}
print(animals_in_zoo)


user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}         #se crea una nueva lista
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})        #usamos el comando update para agregar un nuevo diccionario
print(user_ids)


oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"} #Diccionario nuevo
print(oscar_winners)
oscar_winners.update({"Supporting Actress": "Viola Davis"})               #Se agrega un nuevo diccionario
oscar_winners["Best Picture"] = "Moonlight"                               #Se actualiza el valor asignado de la palabra clave "Best Picture"
print(oscar_winners)
oscar_winners["Animated Feature"] = "Shrek 2"                             #Se actualiza el valor asignado de la palabra clave "Animated Feature"
print(oscar_winners)


drinks= ["espresso", "chai", "decaf", "drip"]                            #creo lista de bebidas
caffeine = [64, 40, 0, 120]                                              #creo lista de contenido de cafeina
zipped_drinks = zip(drinks,caffeine)                                     #Empaqueta y empareja las listas
drinks_to_caffeine = {key:value for key, value in zipped_drinks }        #Crea el diccionario usando el for para llamar el archivo empaquetado
print(drinks_to_caffeine)

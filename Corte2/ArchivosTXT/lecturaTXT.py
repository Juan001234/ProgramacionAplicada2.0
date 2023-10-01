with open('welcome.txt') as text file:   # Sentencia "with open" necesaria para abrir archivo 
  text_data text file.read()
  print(text_data)

# Lee unarchivo TXT existente


with open('how many lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)


with open('how_many_lines.txt linel lines_doc.readline') as lines_doc:
  line1 = lines_doc.readline ()
  print(linel) # Imprime la primera linea del texto
  #line2 = lines_doc.readline ()
  #print(line2)


with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")
# Genera un archivo TXT con en nombre "generated_file.txt" y texto "What an incredible file!"


with open('cool dogs.txt , 'a') as cool_dogs_file:
  cool_dogs_file.write("Air Buddy\n")
# Se adiciona tecto en un archivo txt ya existente


with open('fun_file.txt') as close_this_file: 
  setup = close_this_file.readline()
  punchline = close_this_file.readline()

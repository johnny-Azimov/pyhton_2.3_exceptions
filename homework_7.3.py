documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}

def people():
  number_document = input('Введите номер документа:  ')
  number_len = 0
  for document in documents:
    number_len += 1
    if document.get("number",) == number_document:
     print('\n', document.get("name"))
     break
    elif number_len == len(documents):
      print('нет данных')
      people()
     
 
def lists():    
 for document in documents:
   print(document.get("type"), document.get("number"), document.get("name"))


def shelf():
  number_document = input('Введите номер документа:  ')
  number_len = 0
  for shelf_document in directories:
    number_len += 1
    if number_document in directories.get(shelf_document):
      print('Документ лежит на полке № ', shelf_document)
      break
    elif number_len == len(directories):
      print('нет данных')
      shelf()
   
 
     
def add():
  directorie = input('Введите номер полки куда положить документ: ')
  types = input('Введите тип документа: ')
  number = input('Введите номер документа: ')
  name = input('Введите фамалию и имя владельца документа: ')
  new_dict ={"type": types,"number": number,"name": name}
  documents.append(new_dict)
  for directorie_1 in directories.keys():
    if directorie_1 == directorie:
      directories[directorie_1].append(str(number)) 
      break
  else: 
    if directorie_1 != directorie  :
     directories[directorie] = [number]
      
  

  
  print(directories)    



def names():
  try:
    for name in documents:
      print(name['name'])
  except KeyError:
    print('У документа нет имени!')



def main():
  while True:
    options = ["p", "l", "s", "a","k","!"]
    choice = input('\n Ведите желаемую команду:\n\
    [p]  – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n\
    [l]  – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n\
    [s]  – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n\
    [a]  – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться;\n\
    [k]  – команда, которая выведет имена всех владельцев документов.\n->'
     '\n\n для завершения работы нажмите [!] \n\n')
    if choice in options: 
        if choice == 'p':
          people()
          print(input())
        if choice == 'l':
          lists()
          print(input()) 
        if choice == 's':
          shelf()
          print(input()) 
        if choice == 'a':
          add()
          print(input()) 
        if choice == 'k':
          names()
          print(input())
        if choice == '!':
          break
    else:
      print('\nВведите команду заново, комманда введена не верно.\n')


main()
print('До свидания!')
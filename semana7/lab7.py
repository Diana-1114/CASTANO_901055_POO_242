#class persona
#



def class_person(name,lastname,id,age,role)
    return {
    "name": name,
    "lastname": lastname,
    "id": id, 
    "age": age,
    "role": role
}

def show_objet(objet_)
    print(objet_)

def add_person():
name = input("por favor digite el nombre:\n")
lastname = input("por favor digite el apellido:\n")
id = int(input("por favor digite su ID:\n"))
age = int(input("por favor digite tu edad:\n"))
role = int(input("digite su rol:\n"))

#agregar personas a una lista
#usar un bucle para agregar ususarios hasta usuario decida no agregar mas
#imprimir contenido del listado
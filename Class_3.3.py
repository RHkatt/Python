cod = ["Luis",24,"Ing. Electronico",987654321] #Lista puede haber cambios
print(f"La edad de {cod[0]} es: {cod[1]} años / Su numero de telefono es: {cod[3]}")
cod[1] = 64
cod[2] = "Ing. de Sistemas"
print(f"La edad de Luis es: {cod[1]} años / Su profesion es: {cod[2]}")

travel = ("Pedro",25,"Ing. Biomedico",912345678 ) #Tupla no cambia
print(f"La edad de {travel[0]} es: {travel[1]} años / Su numero de telefono es: {travel[3]}")
#travel[1] = 65 Error
#travel[2] = "Ing. de Sistemas" Error
# print(f"La edad de Pedro es: {travel[1]} años") no se puede cambiar

nuevo = {"nombre":"Ana","edad":30,"profesion":"Ing. Ambiental","telefono":987654321} #Diccionario
nuevo1 = {"nombre":"Kamila","edad":21,"profesion":"Ing. Aeronatica","telefono":983543256} #Diccionario
print(nuevo["nombre"]) #Acceder a un valor  
print(nuevo1["edad"]) #Acceder a un valor
print(f"La edad de {nuevo['nombre']} es: {nuevo['edad']} años")
central = {"Ana":nuevo, "Kamila":nuevo1} #Diccionario que contiene dos diccionarios
empresa = (central["Kamila"])
print(empresa) #Lista que contiene una lista, una tupla y dos diccionarios

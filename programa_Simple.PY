from datetime import datetime
#Este código solicita al usuario ingresar su fecha de nacimiento en formato “AAAA-MM-DD”
def calcular_edad():
    try:
        nacimiento = input("Ingrese su fecha de nacimiento (AAAA-MM-DD): ")
        fecha_nacimiento = datetime.strptime(nacimiento, '%Y-%m-%d')
        fecha_actual = datetime.now()
#Calcula la edad 
        edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day)) 
#Imprime la edad segun los datos ingresados        
        print(f"Tu edad es: {edad} años") 
#No te permite avanzar porque los datos ingresados no son correctos
    except ValueError: 
        print("Formato de fecha incorrecto")
 
calcular_edad()
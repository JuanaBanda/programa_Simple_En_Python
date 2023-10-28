# programa_Simple_En_Python
## Explicación del código anterior
### En este código, primero importamos el módulo datetime. Luego, solicitamos al usuario que ingrese su fecha de nacimiento en el formato ‘YYYY-MM-DD’. Después, convertimos esta cadena de texto en un objeto datetime utilizando la función strptime(), que convierte la cadena de texto en un objeto datetime. Luego, calculamos la edad restando el año de nacimiento de la fecha actual. Finalmente, imprimimos la edad calculada.
## A tener en cuenta de strptime
### strptime es un método del módulo datetime que permite convertir una cadena de caracteres en un objeto datetime. La línea de código que mencionas, fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d'), convierte la fecha de nacimiento en una cadena de caracteres, que se lee desde la entrada del usuario, en un objeto datetime.

### La cadena '%Y-%m-%d' es un argumento que se pasa a strptime y se utiliza para especificar el formato de la cadena que se desea convertir. En este caso, %Y representa el año, %m representa el mes y %d representa el día. Por lo tanto, la cadena '%Y-%m-%d' indica que la entrada debe estar en el formato ‘AAAA-MM-DD’, donde ‘AAAA’ es el año con cuatro dígitos, ‘MM’ es el mes con dos dígitos y ‘DD’ es el día con dos dígitos.

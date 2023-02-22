from animal import animal
from vehicle import vehicle
from school import school

# Crear 2 instancias de animal
a1 = animal("perro", "blanco", 4, 2, 50, 10)
a2 = animal("gato", "amarillo", 4, 2, 40, 3)
# llamar su método con instancia creada
a1.salutacio()
# cambiar el color de a1
a1.setColor("negro")
# imprimir el color de a1
print(a1.getColor())

# Crear 2 instancias de vehicle
v1 = vehicle("coche", "Tesla", "blanco", 400, 180, 160)
v2 = vehicle("moto", "Honda", "azul", 160, 50, 80)
# llamar su método con instancia creada
v1.parts()
# cambiar la marca de v2
v2.setMarca("Yamaha")
# imprimir la marca de v2
print(v2.getMarca())

# Crear 2 instancias de school
e1 = school("IES Jaume Balmes", "pública", "C/ de Pau Claris, 121", 934870301, 2000, 100)
e2 = school("IES Joan d'Àustria", "pública", "C/ de la Selva de Mar, 211", 933073402, 1500, 80)
# llamar su método con instancia creada
e1.info()
# cambiar numero de profes de e2
e2.setNProfes("60")
# imprimir numero de profes de e2
print(e2.getNProfes())

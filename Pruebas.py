class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def presentarse(self):
        return f"Soy {self.nombre}, estudio {self.carrera} y mi promedio es {self.promedio():.2f}"

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def presentarse(self):
        return f"Soy el profesor {self.nombre}, enseño {self.materia}."

if __name__ == "__main__":
    estudiante1 = Estudiante("Juan", 18, "Ingeniería en Sistemas")
    estudiante1.agregar_nota(4.5)
    estudiante1.agregar_nota(3.8)
    estudiante1.agregar_nota(5.0)

    profesor1 = Profesor("Ana", 35, "Matemáticas")

    print(estudiante1.presentarse())
    print(profesor1.presentarse())

class Libro:
    def __init__(self, titulo ='', autor='', año_de_publicacion = 0):
        self.titulo = titulo
        self.autor = autor
        self.año_de_publicacion = año_de_publicacion
        self.disponible = True
    
    def __str__(self):
        return f'Libro :{self.titulo} | Autor :{self.autor} | Año: {self.año_de_publicacion}'
    @property
    def alquiler_libro(self):
        self.disponible = False
    
    @property
    def verificar_disponibilidad(self):
        libros_disponibles = [libro for libro in Libro.libro if libro.año_de_publicacion == libro.disponible]
        return libros_disponibles
    








libro1=Libro('Harry Porker','Guilherme', 680,)
libro2=Libro('Billy y Mandy', 'Nico', 2000)

print(libro1)
print(libro2)
print(f'El libro {libro1.titulo} está disponible?: {libro1.disponible}')
libro1.alquiler_libro()
print(f'El libro {libro1.titulo} está disponible?: {libro1.disponible}')
print(f'El libro {libro2.titulo} está disponible? {libro2.disponible}')
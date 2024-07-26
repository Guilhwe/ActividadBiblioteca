class Libro:
    todos_los_libros=[]
    def __init__(self, titulo ='', autor='', año_de_publicacion = 0):
        self.titulo = titulo
        self.autor = autor
        self.año_de_publicacion = año_de_publicacion
        self.disponible = True
        Libro.todos_los_libros.append(self)
    
    def __str__(self):
        return f'Libro :{self.titulo} | Autor :{self.autor} | Año: {self.año_de_publicacion}'
   
    def alquiler_libro(self):
        self.disponible = False
    
    @staticmethod
    def verificar_disponibilidad(año):
        libros_disponibles = [libro for libro in Libro.todos_los_libros if libro.año_de_publicacion == año and libro.disponible]
        return libros_disponibles





libro1=Libro('Harry Porker','Guilherme', 680,)
libro2=Libro('Billy y Mandy', 'Nico', 2000)

print(libro1)
print(libro2)
print(f'El libro {libro1.titulo} está disponible?: {libro1.disponible}')
libro1.alquiler_libro()
print(f'El libro {libro1.titulo} está disponible?: {libro1.disponible}')
print(f'El libro {libro2.titulo} está disponible? {libro2.disponible}')
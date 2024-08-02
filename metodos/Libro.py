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
        #Filtra los libros disponibles publicados en el año proporcionado
        libros_disponibles = [libro for libro in Libro.todos_los_libros if libro.año_de_publicacion == año and libro.disponible]
        return libros_disponibles





libro1=Libro('Harry Porker','Guilherme', 680,)
libro2=Libro('Billy y Mandy', 'Nico', 2000)


libros_disponivles_680 = Libro.verificar_disponibilidad(680)
for libro in libros_disponivles_680:
    print(libro)
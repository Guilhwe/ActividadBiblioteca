class Libro:
    def __init__(self, titulo ='', autor='', año_de_publicacion = 0):
        self.titulo = titulo
        self.autor = autor
        self.año_de_publicacion = año_de_publicacion
        self.disponible = True

    def __str__(self):
        return f'Libro :{self.titulo} | Autor :{self.autor} | Año: {self.año_de_publicacion}'
    
    def alquiler_libro(self):
        self.disponible = False

libro1=Libro('Harry Porker','Guilherme', 680,)
libro2=Libro('Billy y Mandy', 'Nico', 2000)

print(libro1)
print(libro2)
print(libro1.disponible)
libro1.alquiler_libro()
print(libro1.disponible)
import time
class Song:
	def __init__(self, name, singer, duration, plays=0, **kwargs):
		self.name = name
		self.singer = singer
		self.duration = duration
		self.plays = plays
		self.name_album = None

		for key,value in kwargs.items():
			setattr(self, key, value)

	def __str__(self):
		return f'{self.name} de {self.singer}'

	def __repr__(self):
		return f'{self.name} de {self.singer}'


	def get_plays(self):
		if self.plays:
			return f'Plays: {self.plays}'
		else:
			return f'Esta canción no se reprodujo'



	def read(self):
		'''Esta funcion nos imprime la información de la canción de forma ordenada
		Usaremos el modulo time para imprimir de una forma más legible, ya que la duracion la ingresamos como un entero que seria igual a los segundos'''
		duration = time.strftime("%M:%S",time.gmtime(self.duration))
		if self.name_album:
			return f"{self.name}   {self.singer}   {self.name_album}   {duration}"

		else:
			return f"{self.name}   {self.singer}   {duration}"
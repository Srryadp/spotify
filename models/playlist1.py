class Playlist:
	def __init__(self, name, creator="Spotipy", description=None, **kwargs):
		self.name = name
		self.creator = creator
		self.description = description
		self.songs = []



		for key,value in kwargs.items():
			setattr(self, key, value)


	def __str__(self):
		return f'"{self.name}" creada por {self.creator}'

	def __repr__(self):
		return f'"{self.name}" creada por {self.creator}'




	def add_song(self, song):
		self.songs.append(song)


	@classmethod
	def create_mix(cls, songs):
		return cls("Mi mix", songs=songs)

	def show_playlist(self):
		"""Esta funcion la usamos para imprimir la información de la playlist y las canciones de esta"""
		if self.description:
			print(self.name)
			print(self.description)
			print(f"\nCreada por {self.creator}\n")
			for index,song in enumerate(self.songs, start=1):
				print(f"{index}  {song.read()}")
		else:
			print(self.name)
			print(f"\nCreada por {self.creator}\n")
			for index,song in enumerate(self.songs, start=1):
				print(f"{index}  {song.read()}")
from .user import User
from .playlist1 import Playlist
from .album import Album
from .song import Song
from .data_song import mix_1
from .exceptions import FileError
import random


class UserFree(User):
	def __init__(self, fullname, date_birth, username, password, subscription=False, **kwargs):
		super().__init__(fullname, date_birth, username, password, **kwargs)
		self.subscription = subscription


	@staticmethod
	def play(to_play):
		"""Esta función sera la encargada de reproducir playlists, albums y canciones.
		En caso de no ingresarle una instancia de una de las 3 clases mencionadas anteriormente dara un error y se le dira al usuario que ese tipo de archivo no puede ser reproducido"""
		try:
			if isinstance(to_play, Playlist):
				to_play.show_playlist()
				playing = random.choice(to_play.songs)
				playing.plays += 1
				print(f'\nReproduciendo  {playing}')

			elif isinstance(to_play, Album):
				to_play.show_album()
				playing = random.choice(to_play.songs)
				playing.plays += 1
				print(f'\nReproduciendo  {playing}')

			elif isinstance(to_play, Song):
				print(f'Para reproducir {to_play} debes encontrala en una playlist')
				print('Puedes encontrar esta canción en la siguiente playlist:')
				if to_play in mix_1.songs:
					print(mix_1)
				else:
					mix_1.add_song(to_play)
					print(mix_1)
				while True:
					eleccion = input('Reproduces la playlist? si/no:  ')

					if eleccion.lower() == "si":
						print("")
						mix_1.show_playlist()
						playing = random.choice(mix_1.songs)
						playing.plays += 1
						print(f'\nReproduciendo aleatoriamente   {playing}')
						break

					elif eleccion.lower() == "no":
						print('No se reproducira la playlist')
						break

					else:
						print('Ingresa "si" o "no"')
						continue

			else:
				raise FileError

		except FileError as e:
			print('El archivo no puede ser reproducido')
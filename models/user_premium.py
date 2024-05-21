from .user import User
from .playlist1 import Playlist
from .album import Album
from .song import Song
from .exceptions import FileError


class UserPremium(User):
	def __init__(self, fullname, date_birth, username, password, subscription=True, **kwargs):
		super().__init__(fullname, date_birth, username, password, **kwargs)
		self.subscription = subscription



	@staticmethod
	def play(to_play):
		"""Esta función sera la encargada de reproducir playlists, albums y canciones.
		En caso de no ingresarle una instancia de una de las 3 clases mencionadas anteriormente dara un error y se le dira al usuario que ese tipo de archivo no puede ser reproducido"""
		try:
			if isinstance(to_play, Playlist):
				while True:
					try:
						to_play.show_playlist()
						print('')
						select = int(input('Ingresa el número de la canción que quieres reproducir o presiona "0" para cancelar: '))
						if select == 0:
							print('\nNo se reproducira la playlist\n')
							break
					
						elif select-1 < len(to_play.songs):
							to_play.songs[select-1].plays += 1
							print(f'\nReproduciendo   {to_play.songs[select-1]}')	
							break

						else:
							print('\n<<<<Número invalido>>>>\n')
							continue			


					except ValueError:
						print('\n<<<<Ingresa números>>>>\n')
						continue

			elif isinstance(to_play, Album):
				while True:
					try:
						to_play.show_album()
						print('')
						select = int(input('Ingresa el número de la canción que quieres reproducir o presiona "0" para cancelar: '))
						if select == 0:
							print('\nNo se reproducira el album\n')
							break
					
						elif select-1 < len(to_play.songs):
							to_play.songs[select-1].plays += 1
							print(f'\nReproduciendo   {to_play.songs[select-1]}')
							break

						else:
							print('\n<<<<Número invalido>>>>\n')
							continue			


					except ValueError:
						print('\n<<<<Ingresa números>>>>\n')
						continue

			elif isinstance(to_play, Song):
				to_play.plays += 1
				print(f'\nReproduciendo {to_play}')
		
			else:
				raise FileError

		except FileError as e:
			print('El archivo no puede ser reproducido')
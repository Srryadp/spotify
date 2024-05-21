from .playlist1 import Playlist
from .playlist1 import Playlist
from .album import Album
from .song import Song
from .exceptions import FileError


class User:
	def __init__(self, fullname, date_birth, username, password, **kwargs):
		self.fullname = fullname
		self.date_birth = date_birth
		self.username = username
		self._password = password
		self.created_playlists = []
		self.liked_playlists = []
		self.liked_albums = []

		for key,value in kwargs.items():
			setattr(self, key, value)

		self.liked_songs = Playlist("Tus me gusta", self)

		self.created_playlists.append(self.liked_songs)



	@property
	def password(self):
		try:
			return self._password
		except AttributeError:
			return None

	@password.setter
	def password(self, new_password):
		self._password = str(new_password)



	def __str__(self):
		return f'{self.username}'

	def __repr__(self):
		return f'{self.username}'



	def give_like(self, liked):
		"""Metodo para dar likes que actuara corresponde al tipo de archivo que se le ingrese
		Puede dar like a instancias de las clases Song, Playlist y Album, si no se le ingresa ninguna de estas dara error"""
		try:
			if isinstance(liked, Song):
				if liked in self.liked_songs.songs:
					self.liked_songs.songs.remove(liked)
					print(f'{liked} ha sido eliminada de tus me gusta')
				else:
					self.liked_songs.add_song(liked)
					print(f'{liked}  ♥')

			elif isinstance(liked, Playlist):
				if liked in self.liked_playlists:
					self.liked_playlists.remove(liked)
					print(f'{liked} ha sido eliminada de tus me gusta')
				else:
					self.liked_playlists.append(liked)
					print(f'{liked}  ♥')

			elif isinstance(liked, Album):
				if liked in self.liked_albums:
					self.liked_albums.remove(liked)
					print(f'{liked} ha sido eliminada de tus me gusta')
				else:
					self.liked_albums.append(liked)
					print(f'{liked}  ♥')

			else:
				raise FileError

		except FileError as e:
			print('El archivo no es valido')


	def create_playlist(self, name):
		self.created_playlists.append(Playlist(name, self))
		print('Playlist creada')
		return self.created_playlists[-1]
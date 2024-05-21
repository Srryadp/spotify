from models.song import Song
from models.album import Album
from models.playlist1 import Playlist
from models.user import User
from models.user_premium import UserPremium
from models.user_free import UserFree
from models.data_song import the_album, doja_cat, mix_1





'''Creación de una canción'''

song_prueba = Song("i'll see you again", "League of Legends, suteki", 214, 597351)



''' Creación de 1 usuario free y 1 usuario premium'''
ale = UserPremium('Ale', '15-03-2006', 'ale', '1234567a')
laura = UserFree('Laura', '02-12-2006', 'Usuario gratis', 'qwerty123')

'''_________Prueba del metodo para dar likes de la clase User_________'''

print("_____Likes de ale_____")

ale.give_like(doja_cat["Hot Pink"][0])
ale.give_like(the_album.songs[0])
ale.give_like(doja_cat["Hot Pink"][1])
ale.give_like(mix_1.songs[3])
ale.give_like(the_album.songs[2])
ale.give_like(mix_1)
print("\n\n")


print("_____Likes de free_____")
laura.give_like(the_album.songs[3])
laura.give_like(doja_cat["Hot Pink"][2])
laura.give_like(song_prueba)
laura.give_like(the_album)
print("\n\n")



'''______Reproduciendo canciones____'''
input('')

print('____________Reproduciendo desde el usuario premium____________')

print("______Reproduciendo una cancion______")
ale.play(doja_cat["Hot Pink"][0])
print('')
print("______Reproduciendo una playlist______")
ale.play(ale.liked_songs)
print('\n\n')
print("______Reproduciendo un album______")
ale.play(the_album)
print('\n\n')

input('')
print('____________Reproduciendo desde el usuario laura____________')

print('')
print("______Reproduciendo una playlist______")
laura.play(laura.liked_songs)
input('')
print('\n\n')
print("______Reproduciendo un album______")
laura.play(the_album)
input('')
print('\n\n')
print("______Reproduciendo una cancion______")
laura.play(doja_cat["Hot Pink"][1])
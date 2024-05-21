from .song import Song
from .album import Album
from .playlist1 import Playlist
import random

Blackpink = {
	"The Album": [
		Song("How You Like That","Blackpink", 182, 660328902),
		Song("Lovesick Girls", "Blackpink", 194, 357883028),
		Song("Pretty Savage", "Blackpink", 201, 259153208),
		Song("Bet You Wanna", "Blackpink", 161, 145685596, ft="Cardi B"),
		Song("You Never Know", "Blackpink", 231, 110837934),
		Song("Love To Hate Me", "Blackpink", 171, 154854579),
		Song("Crazy Over You", "Blackpink", 163, 134076376),
		Song("Ice Cream", "Blackpink", 177, 437138505, ft="Selena Gomez"),
	]
}

doja_cat = {
    "Hot Pink": [
        Song("Say So", "Doja Cat", 197, 123456789),
        Song("Boss B*tch", "Doja Cat", 169, 987654321),
        Song("Juicy", "Doja Cat", 185, 456789012),
        Song("Tia Tamera", "Doja Cat", 208, 567890123, ft="Rico Nasty"),
    ],
    "Planet Her": [
        Song("Kiss Me More", "Doja Cat", 213, 987654321, ft="SZA"),
        Song("Need to Know", "Doja Cat", 235, 876543210),
        Song("Woman", "Doja Cat", 182, 345678901),
        Song("You Right", "Doja Cat", 201, 234567890, ft="The Weeknd"),
    ]
}


mix_songs = random.sample(Blackpink["The Album"], 4) + random.sample(doja_cat["Hot Pink"], 2) 

mix_1 = Playlist.create_mix(mix_songs)

the_album = Album("The Album", Blackpink["The Album"])
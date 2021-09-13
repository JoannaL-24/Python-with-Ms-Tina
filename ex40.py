class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy Birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

Seve = Song(["Viumbe vyote vya mungu wetu na mfalme wetu",
            "Pazeni sauti ili nasi mwimbe",
            "Pazeni sauti ili nasi mwimbe",
            "Pazeni sauti",
            "Pazeni sauti"])

lyrics = ["Seasons change and our love went cold",
        "Feed the flame 'cause we can't let it go",
        "Run away, but we're running in circles",
        "Run away, run away"]

Circle = Song(lyrics)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
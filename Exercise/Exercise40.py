
class song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_my_song(self):
        for line in self.lyrics:
            print(line)


happy_birthday = song(["Happy birthday to you",
                        "Happy birthday to you",
                        "Happy birthday that you born"
                        "Happy birthday to you!"])

bulls_on_parade = song(["They rally around the family","With pockets full of shells"])


happy_birthday.sing_my_song()
bulls_on_parade.sing_my_song()
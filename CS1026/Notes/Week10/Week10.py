


"""
a = {4, 1, 7, 9, 3}
b = {5, 3, 9}
c = {7, 1}

print(a.union(b))

print(a.intersection(b))
print(a.intersection(c))

print(a.difference(b))
print(a.difference(c))
print(c.difference(a))

print(a.issubset(c))
print(c.issubset(a))
#c是a的子集

print(a.issuperset(c))
print(c.issuperset(a))
#a包含c

x = {1, 2, 3}
y = {2, 3, 1}

print(x.issubset(y))
print(y.issubset(x))

z = {5, 8}
z.add(4)
print(z)
z.discard(8)
print(z)
z.discard(2)
print(z)
#用discard移除不存在的数不会导致crash

z.remove(4)
print(z)
# z.remove(6)
# print(z)
#用remove移除不存在的数字会导致crash

z.clear()
print(z)

z.add(3)
z.add(7)
print(z)
print(z.pop())
# print(z[0]) 找不到位置
"""
from time import perf_counter


class Song:
    """
    artist
    title
    album
    genre
    length
    """

    def __init__(self, artist, title, album, genre, length):
        self._artist = artist
        self._title = title
        self._album = album
        self._genre = genre
        self._length = length


    def __str__(self):
        return self._title + " by " + self._artist


    #GETTERS
    def get_artist(self):
        return self._artist
    
    def get_title(self):
        return self._title

    def get_album(self):
        return self._album

    def get_genre(self):
        return self._genre

    def get_length(self):
        return self._length

    #SETTERS
    def set_album(self, new_album):
        self._album = new_album

    def set_genre(self, new_genre):
        self._genre = new_genre

    



song1 = Song("Taylor Swift", "Bad Blood", "1989", "Pop", 2.5)
song2 = Song("Eminem", "Rap God", "MMLP2", "Rap", 4.0)

print(song1)
print(song2)
print(song1.get_album())
song1.set_genre("Rock")
song2.set_album("Slim Shady")
print(song1.get_genre())
print(song2.get_album())




"""
Anotações de tipo não afetam a execução do programa, servindo somente
para aumentar a legibilidade do código.

var_name: <type> = Indicar o tipo de uma variável.

-> <type> = Indicar o tipo de retorno de método/função.

Para tipos complexos podemos usar o pacote typing. Já vem pré carregado
com classes de List, Dict, Tuple, Set entre outras.

Para funções que o retorno pode assumir diferentes tipos podemos usar os tipos
Optional e Union

Optional = Quando o valor de retono for de algum tipo ou None.
    Optional[type]

Union = Quando o valor de retorno pode assumir tipos mais especificos.
    Union[int, str]


def f(argument: T) -> R:
    # algo

"""
from typing import List
from functools import reduce


class Music:
    id: int
    title: str
    duration: float
    favorite: bool

    def __init__(self, id: int, title: str, duration: float):
        self.id = id
        self.title = title
        self.duration = duration
        self.favorite = False


    def like(self) -> None:
        if self.favorite:
            self.favorite = False
            print("Unliked!")

        self.favorite = True
        print("Liked!")


class Playlist:
    id: int
    title: str
    musics: List[Music]

    def __init__(self, id: int, title: str, musics: List[Music]):
        self.id = id
        self.title = title
        self.musics = musics

    def amount_musics(self) -> int:
        return len(self.musics)

    def favorites(self) -> List[Music]:
        return list(filter(lambda x: x.favorite == True, self.musics))


music1 = Music(1, "Clocks", 3.5)
music2 = Music(2, "Rock and Roll", 4.0)
music3 = Music(3, "Your Song", 4.5)
music4 = Music(4, "Song2", 2.0)

musics = [music1, music2, music3, music4]


playlist1 = Playlist(1, "My Songs", musics)


print(playlist1.amount_musics())

music1.like()
music3.like()

print("----------- Favoritas ------------")

for music in playlist1.favorites():
    print("Id - {0}\nTitulo - {1}".format(music.id, music.title))

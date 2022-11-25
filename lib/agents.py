
class Player:
    def __init__(self, name: str, color: str) -> None:
        self._name = name
        self._move_list = []

        if color not in ['white', 'black']:
            raise ValueError("Color must be 'white' or 'black'")
        else:    
            self._color = color

    def specify_move(self):
        move = input("{}, it's your turn!\n".format(self.name))
        self.move_list.append(move)
        return move 
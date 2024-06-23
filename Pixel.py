from dataclasses import dataclass
from enum import Enum


class Colors(Enum):
    white     = [(240, 240, 240), '0']
    orange    = [(242, 178, 51), '1']
    magenta   = [(229, 127, 216), '2']
    lightBlue = [(153, 178, 242), '3']
    yellow    = [(222, 222, 108), '4']
    lime      = [(127, 204, 25), '5']
    pink      = [(242, 178, 204), '6']
    gray      = [(76, 76, 76), '7']
    lightGray = [(153, 153, 153), '8']
    cyan      = [(76, 153, 178), '9']
    purple    = [(178, 102, 229), 'a']
    blue      = [(51, 102, 204), 'b']
    brown     = [(127, 102, 76), 'c']
    green     = [(87, 166, 78), 'd']
    red       = [(204, 76, 76), 'e']
    black     = [(17, 17, 17), 'f']

@dataclass
class Pixel:
    r: int
    g: int
    b: int

    def __iter__(self):
        return iter((self.r, self.g, self.b))

    def to_blit(self) -> str:
        nearest_color = min(Colors, key=lambda color: sum((c1 - c2)**2 for c1, c2 in zip(self, color.value[0])))
        return nearest_color.value[1]

if __name__ == "__main__":
    from pprint import pprint
    pprint([print(color, color.value) for color in Colors])
from cli import *
from pizza_recipes import *


if __name__ == '__main__':
    deliver(Margherita())
    print(Pepperoni('XL').__dict__())
    print(Hawaiian('L').__str__())

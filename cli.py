import click
from decorators import log
from pizza_recipes import Pizza, Margherita, Pepperoni, Hawaiian

PIZZA_NAMES_DICT = {
    'margherita': Margherita(),
    'pepperoni': Pepperoni(),
    'hawaiian': Hawaiian()
}
MAX_PIZZA_NAME_LENGTH = max([len(key) for key in PIZZA_NAMES_DICT.keys()])

MENU = [f'{i} - {type(pizza).__name__:{MAX_PIZZA_NAME_LENGTH}} '
        f'{pizza.emoji:1}: {", ".join(pizza.ingredients)}'
        for i, pizza in enumerate(PIZZA_NAMES_DICT.values(), 1)]


@click.group()
def cli():
    """Choose a pizza from our menu! 🍕"""


@log('🛵 Delivered in {} sec!')
def deliver(pizza: Pizza):
    """Delivers a pizza"""
    pizza.delivery()


@log('🏠 Pickup in {} sec!')
def pickup(pizza: Pizza):
    """Pickups a pizza"""
    pizza.pickup()


@log('🍕 Baked in {} sec!')
def bake(pizza: Pizza):
    """Bakes a pizza"""
    pizza.bake()


@cli.command()
@click.argument('pizza_name', nargs=1)
@click.option('--delivery', default=False, is_flag=True)
def order(pizza_name: str, delivery: bool) -> None:
    """Bakes and delivers a pizza"""
    if pizza_name.lower() not in PIZZA_NAMES_DICT:
        raise ValueError(f'Invalid pizza name: {pizza_name}')
    pizza = PIZZA_NAMES_DICT[pizza_name.lower()]
    bake(pizza)
    if delivery:
        deliver(pizza)
    else:
        pickup(pizza)


@cli.command()
def menu():
    """Shows the menu"""
    for pizza in MENU:
        print(pizza)


if __name__ == '__main__':
    cli()

class Pizza:
    """Base pizza recipe class"""
    PIZZA_SIZES = ['L', 'XL']

    def __init__(
            self,
            ingredients: list[str, ...],
            size: str = 'L',
            emoji: str = '',
            is_baked: bool = False,
            is_delivered: bool = False,
            is_pickup: bool = False
    ) -> None:
        """
        Initializes a pizza recipe.

        Args:
            ingredients: A list of ingredients.
            size: The size of the pizza (L or XL).
            emoji: An emoji representing the pizza.
            is_baked: A flag indicating whether the pizza is baked.
            is_delivered: A flag indicating whether the pizza is delivered.
            is_pickup: A flag indicating whether the pizza is picked up.

        Raises:
            ValueError: If the size is not a valid value.
        """
        if size not in self.PIZZA_SIZES:
            raise ValueError(f'Invalid pizza size: {size}')

        self.ingredients = ingredients
        self.size = size
        self.emoji = emoji
        self.is_baked = is_baked
        self.is_delivered = is_delivered
        self.is_pickup = is_pickup

    def bake(self) -> None:
        """Bakes the pizza."""
        self.is_baked = True

    def delivery(self) -> None:
        """Delivers the pizza."""
        self.is_delivered = True

    def pickup(self) -> None:
        """Picks up the pizza."""
        self.is_pickup = True

    def __repr__(self) -> str:
        """String representation of a pizza recipe."""
        return f'Pizza({self.size}, {self.ingredients})'

    def __str__(self) -> str:
        """Returns a readable string representation of the pizza recipe."""
        return f'{self.size} pizza with {", ".join(self.ingredients)}'

    def __dict__(self) -> dict:
        """Returns a pizza recipe as a dictionary."""
        return {
            'size': self.size,
            'ingredients': self.ingredients,
        }

    def __eq__(self, other) -> bool:
        """Compares two pizzas by size & ingredients."""
        if not isinstance(other, Pizza):
            raise ValueError(f'Invalid pizza type: {type(other)}')
        return (
                self.size == other.size
                and self.ingredients == other.ingredients
        )


class Margherita(Pizza):
    """Margherita pizza recipe."""

    emoji = '🧀'
    ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']

    def __init__(self, size: str = 'L') -> None:
        """Initializes a Margherita pizza recipe with a selected size."""

        super().__init__(self.ingredients, size, self.emoji)


class Pepperoni(Pizza):
    """Pepperoni pizza recipe."""

    emoji = '🍕'
    ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']

    def __init__(self, size: str = 'L') -> None:
        """Initializes a Pepperoni pizza recipe with a selected size."""

        super().__init__(self.ingredients, size, self.emoji)


class Hawaiian(Pizza):
    """Hawaiian pizza recipe."""

    emoji = '🍍'
    ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']

    def __init__(self, size: str = 'L') -> None:
        """Initializes a Hawaiian pizza recipe with a selected size."""

        super().__init__(self.ingredients, size, self.emoji)



class Product:
    """
    Represents a product with a name, price, quantity, and active status.
    """
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The initial quantity of the product.

        Raises:
            ValueError: If name is empty or if price or quantity is negative.
        """
        if not name:
            raise ValueError("Product name can't be empty")
        if price < 0:
            raise ValueError("Price can't be negative")
        if quantity < 0:
            raise ValueError("Quantity can't be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> float:
        """
        Returns the current quantity of the product.

        Returns:
            float: Current quantity.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets the quantity of the product.
        Deactivates the product if the quantity reaches 0.

        Args:
            quantity (int): The new quantity to set.

        Raises:
            TypeError: If quantity is not an integer.
            ValueError: If quantity is negative.
        """
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity < 0:
            raise ValueError("Quantity can't be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Checks if the product is active.

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product"""
        self.active = False

    def show(self) -> str:
        """
        Returns a string that represents the product.

        Returns:
            str: Product details.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.
        Updates the quantity and returns the total price.

        Args:
            quantity (int): The quantity to purchase.

        Returns:
            float: Total price for the purchased quantity.

        Raises:
            ValueError: If purchase quantity is invalid or exceeds available stock.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available for purchase.")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price





def main():
    """
    Example usage of the Product class.
    """
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())

if __name__ == "__main__":
    main()
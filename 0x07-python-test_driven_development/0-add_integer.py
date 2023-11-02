def add_integer(a, b=98):
    """Fuction of addition of integers

        Args:
            a (int): first argument
            b (int): second arfument
        """
        if not isinstance(a, int) and not isinstance(b, int):
            raise TypeError("a must be an integer")
        if not isinstance(b, int) and not is instance(b, int):
            raise TypeError("b must be an integer")
        return (int(a) + int(b))

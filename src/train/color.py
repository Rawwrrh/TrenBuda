class Color:
    red = "red"
    green = "green"
    blank = None

    palette = [red, green, blank]

    @staticmethod
    def check(color):
        if color not in Color.palette:
            raise Exception(f"Color '{color}' not valid.")

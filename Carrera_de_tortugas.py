import turtle
class Circuito():
    corredores =[]

    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgrey')

        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.shape('turtle')

            self.corredores.append(new_turtle)


if __name__ == '__main__':
    circuito = Circuito(400, 400)

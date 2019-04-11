import turtle
import random


class Circuito:
    corredores = []
    __posstarty = (-30, -10, 10, 30)
    __colorturtle = ('red', 'Blue', 'green', 'orange')
    # Inicia la pantalla

    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgrey')
        self.__starline = (-width/2 + 5 * width/100)
        self.__endline = (width/2 + 5 * width/100)
        self.__createrunners()
        
    # Creamos los corredores.
    def __createrunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorturtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__starline, self.__posstarty[i])

            self.corredores.append(new_turtle)
        
    def competir(self):
        hayganador = False
        while not hayganador:
            for tortu in self.corredores:
                avanza = random.randint(1, 6)
                tortu.forward(avanza)
                if tortu.position()[0] >= self.__endline:
                    hayganador = True
                    print('!!!!La tortuga de color {} ha ganado¡¡¡¡'.format(tortu.color()[0]))
                    break


if __name__ == '__main__':
    circuito = Circuito(400, 400)
    circuito.competir()


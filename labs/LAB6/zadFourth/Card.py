import random


class Card:

    def __init__(self, color, figure, points):
        self.__color = color
        self.__figure = figure
        self.__points = points

    def __str__(self):
        return "({0},{1},{2})".format(self.__color, self.__figure, self.__points)

    def get_points(self):
        return self.__points


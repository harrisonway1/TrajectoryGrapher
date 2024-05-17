import math

import numpy as np
import matplotlib.pyplot as mpl


def pythag_for_hyp(a, b):
    return ((a ** 2) + (b ** 2)) ** 0.5


class Trajectory:
    def __init__(self):
        self.__u = 0
        self.__angle = 0
        self.__total_time = 0

    def set_values(self):
        self.__u = float(input("Enter the initial Speed: "))
        self.__angle = math.radians(float(input("Enter the angle between the floor and the particle: ")))
        self.__total_time = self.calculate_total_time()

    def calculate_total_time(self):
        return (2 * self.__u * math.sin(self.__angle)) / 9.8

    def get_values(self):
        return [self.__u, self.__angle, self.__total_time]

    def calculate_horizontal_speed(self):
        return self.__u * math.cos(self.__angle)

    def calculate_total_horizontal_distance(self):
        return self.calculate_horizontal_speed() * self.__total_time

    def calculate_horizontal_distance(self, at_time):
        return self.calculate_horizontal_speed() * at_time

    def calculate_vertical_speed(self, at_time):
        i_vertical_speed = self.__u * math.sin(self.__angle)
        return i_vertical_speed + (-9.8 * at_time)

    def calculate_vertical_distance(self, at_time):
        return (self.__u * math.sin(self.__angle) * at_time) + (0.5 * (-9.8) * (at_time ** 2))

    def calculate_final_speed(self):
        return pythag_for_hyp(self.calculate_horizontal_speed(), self.calculate_vertical_speed(self.__total_time))

    def plot_trajectory(self, number_points=100):
        horizontal_list = []
        vertical_list = []
        times = np.linspace(0, self.__total_time, number_points)
        for t in times:
            vertical_distance = self.calculate_vertical_distance(t)
            if vertical_distance >= 0:
                horizontal_list.append(self.calculate_horizontal_distance(t))
                vertical_list.append(vertical_distance)
            else:
                horizontal_list.append(self.calculate_horizontal_distance(self.calculate_total_time()))
                vertical_list.append(self.calculate_vertical_distance(self.calculate_total_time()))
                break
        mpl.plot(horizontal_list, vertical_list)
        mpl.xlabel("Horizontal Distance")
        mpl.ylabel("Vertical Distance")
        mpl.title("TRAJECTORY")
        mpl.grid(True)
        mpl.axis('equal')
        mpl.show()


Eg1 = Trajectory()
Eg1.set_values()
print(f"Time taken: {Eg1.get_values()[2]} seconds")
Eg1.plot_trajectory()


import math
import numpy as np
import matplotlib.pyplot as mpl


def pythag_for_hyp(a, b):
    return ((a ** 2) + (b ** 2)) ** 0.5


class Trajectory:
    def __init__(self, value):
        self.__ID = value
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

    def plot_trajectory_list(self, ax, number_points=100):
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
        ax.plot(horizontal_list, vertical_list, label=f"Trajectory = {self.__ID + 1}")


def plot_trajectories(trajectories):
    fig, ax = mpl.subplots()
    for i in trajectories:
        i.plot_trajectory_list(ax)
    ax.set_xlabel("Horizontal Distance")
    ax.set_ylabel("Vertical Distance")
    ax.set_title("TRAJECTORY")
    ax.legend()
    mpl.grid(True)
    mpl.axis('equal')
    mpl.show()


def main():
    traj_list = []
    go = True
    count = 0
    while go:
        traj_list.append(Trajectory(count))
        traj_list[count].set_values()
        plot_trajectories(traj_list)
        user_input = input("Would you like to enter another graph?(y/n): ").upper()
        if user_input == "Y":
            pass
        else:
            go = False
            print("Goodbye!")
        count += 1


main()


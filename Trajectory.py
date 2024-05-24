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


class Menu:
    def __init__(self):
        self.__trajectory_list = []

    def plot_trajectories(self):
        if len(self.__trajectory_list) == 0:
            print()
            print()
            print("There are no trajectories in memory.")
        else:
            fig, ax = mpl.subplots()
            for i in self.__trajectory_list:
                i.plot_trajectory_list(ax)
            ax.set_xlabel("Horizontal Distance")
            ax.set_ylabel("Vertical Distance")
            ax.set_title("TRAJECTORY")
            ax.legend()
            mpl.grid(True)
            mpl.axis('equal')
            mpl.show()

    def clear_graph(self):
        self.__trajectory_list = []

    def main_ui(self):
        resume = True
        while resume:
            go = False
            print("-----MAIN MENU-----")
            print("1: Enter a new trajectory.")
            print("2. Look at previous trajectories in memory.")
            print("3. Plot Trajectories.")
            print("4. Remove Trajectories from memory.")
            while not go:
                user_input = input("Enter an option or 5 to exit: ")
                try:
                    user_input = int(user_input)
                    if user_input < 0 or user_input > 5:
                        print("Enter a valid option.")
                    else:
                        go = True
                except ValueError:
                    print("Enter a valid option.")
            if user_input == 1:
                self.enter_new_trajectory()
                print()
                print()
            elif user_input == 2:
                self.look_at_trajectories()
                print()
                print()
            elif user_input == 3:
                self.plot_trajectories()
                print()
                print()
            elif user_input == 4:
                self.remove_trajectories()
                print()
                print()
            else:
                resume = False
                print("Goodbye!")

    def enter_new_trajectory(self):
        print()
        new_trajectory = Trajectory(len(self.__trajectory_list))
        new_trajectory.set_values()
        self.__trajectory_list.append(new_trajectory)

    def look_at_trajectories(self):
        print()
        print()
        if len(self.__trajectory_list) == 0:
            print("There are no trajectories in memory.")
        else:
            for trajectory in self.__trajectory_list:
                print(f"Trajectory {self.__trajectory_list.index(trajectory) + 1}:")
                print(f"Initial Speed: {trajectory.get_values()[0]}m/s")
                print(f"Angle of Elevation: {math.degrees(trajectory.get_values()[1])} degrees")
                print(f"Time of Flight: {trajectory.get_values()[2]}s")
                print()

    def remove_trajectories(self):
        go = False
        self.look_at_trajectories()
        if len(self.__trajectory_list) == 0:
            pass
        else:
            while not go:
                user_input = input(f"Enter the number of the trajectory you want to remove "
                                   f"(1, {len(self.__trajectory_list)}) or 0 to remove all "
                                   f"or -1 to return to main menu: ")
                try:
                    user_input = int(user_input)
                except ValueError:
                    print("Enter a valid option.")
                    break
                if user_input < -1 or user_input > len(self.__trajectory_list):
                    print("Enter a valid option.")
                else:
                    go = True
            if user_input == 0:
                self.clear_graph()
            elif user_input == -1:
                pass
            else:
                self.__trajectory_list.remove(self.__trajectory_list[user_input - 1])


Eg1 = Menu()
Eg1.main_ui()

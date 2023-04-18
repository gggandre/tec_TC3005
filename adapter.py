# Task: Write an adapter for the Speedometer to make it
# work with the CarDisplay
import random


class MphSpeedometer:
    """We are pretending this is a third-party class we can't change"""

    def __init__(self):
        """
        This is an empty constructor function in Python.
        """
        pass

    def get_speed(self):
        """
        The function "get_speed" returns a random speed in MPH.
        :return: the speed in MPH, which is a randomly generated integer
        between 0 and 100.
        """
        """Returns speed in MPH"""
        speed = random.randint(0, 100)
        print("Speed in MPH: {}".format(speed))
        return speed


class MphToKphSpeedometerAdapter:
    """Adapts an MPH speedometer to return speeds in KPH"""

    def __init__(self, mph_speedometer):
        """
        This is a constructor function that initializes an
        object with a mph_speedometer attribute.
        :param mph_speedometer: The mph_speedometer
        parameter is a variable that represents the speedometer
        reading in miles per hour (mph) for a vehicle.
        It is used as an input parameter for the constructor
        of a class, which initializes an instance of the class with the given
        mph_speedometer value
        """
        self.mph_speedometer = mph_speedometer

    def get_speed(self):
        """
        The function converts the speed in miles per
        hour to kilometers per hour.
        :return: The function `get_speed` returns the speed
        in kilometers per hour (KPH) based on the
        speedometer reading in miles per hour (MPH) obtained
        from `mph_speedometer.get_speed()`.
        """
        """Returns speed in KPH"""
        mph_speed = self.mph_speedometer.get_speed()
        kph_speed = mph_speed * 1.609344
        # 1 mile per hour = 1.609344 kilometers per hour
        return kph_speed


class CarDisplay:
    def __init__(self, speedometer):
        """
        This is a constructor function that initializes an
        object with a speedometer attribute.
        :param speedometer: This is a variable that is being passed as
        a parameter to the constructor of a class. It is used to initialize
        an instance variable with the same name. The purpose of this
        variable is to store the speedometer reading of a vehicle
        or any other object that has a speedometer
        """
        self.speedometer = speedometer

    def show_speed(self):
        """
        The function "show_speed" prints the current
        speed in kilometers per hour.
        """
        speed = self.speedometer.get_speed()
        print(f'Speed: {speed} KPH')


# This code block is the main program that creates instances of the
# `MphSpeedometer`,`MphToKphSpeedometerAdapter`, and `CarDisplay`
# classes, and calls the `show_speed()` method of the
# `CarDisplay` instance to display the current speed in kilometers
# per hour. The `if __name__ ==# '__main__':` statement is a common Python
# idiom that checks if the script is being run as the main
# program (as opposed to being imported as a module), and if so, executes
# the code block that follows.
if __name__ == '__main__':
    mph_speedometer = MphSpeedometer()
    kph_speedometer = MphToKphSpeedometerAdapter(mph_speedometer)
    car_display = CarDisplay(kph_speedometer)
    car_display.show_speed()

#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Using the python's Object Oriented Programming Scheme (OOPS) kindly complete the following tasks which is given as below- 
# 1) Create a Python Class called Circle with Constructor which will take
# a List as an argument for the task. The List is [10, 501, 22, 37, 100, 999, 87, 351]

class Circle:
    def __init__(self, my_list):
        self.my_list = my_list

# Creating an instance of the Circle class with the given list
my_circle = Circle([10, 501, 22, 37, 100, 999, 87, 351])

# Accessing the list within the Circle object
print(my_circle.my_list)


# In[37]:


# Using the python's Object Oriented Programming Scheme (OOPS) kindly complete the following tasks which is given as below-
# 2) Create proper member variables inside the task if required and use them when necessary. For example for this task 
# create a class private variable named pi = 3.141

class Circle:
    def __init__(self, radius):
        self.pi = 3.141  # private variable pi
        self.radius = radius

    def calculate_area(self):
        return self.pi * self.radius * self.radius
    
radius = 4

# Creating an instance of the Circle class
circle = Circle(radius)

# Calculating and printing the area of the circle
area = circle.calculate_area()
print(f"The area of the circle with radius {radius} is {area:.2f}")


# In[2]:


# Using the python's Object Oriented Programming Scheme (OOPS) kindly complete the following tasks which is given as below-
# 3) From the given List create two class Methods Area and Perimeter which will be going to calculate the Area and 
# Perimeter.

class Shape:
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        total = sum(self.sides)
        return total

    def perimeter(self):
        product = 1
        for side in self.sides:
            product *= side
        return product

# Given list
list = [10, 501, 22, 37, 100, 999, 87, 351]

# Creating an instance of the Shape class
shape = Shape(list)

# Calculating and printing the area and perimeter of the shape
area_output = shape.area()
perimeter_output = shape.perimeter()

print(f"The area of the shape is: {area_output}")
print(f"The perimeter of the shape is: {perimeter_output}")


# In[3]:


"""4) Using the python's Object Oriented Programming Scheme (OOPS) kindly complete the following tasks which is given as below-
TV class
TVClass - Base class
LedTV class
PlasmaTV class
Part - A

Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume. Specify brand in 
a constructor parameter. Channel should be 1 by default. Volume should be 50 by default.
Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.
Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 60 the TV will 
stay at the current channel.
Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from the constructor).
It's useful to write a status that returns info about the TV status like: "Panasonic at channel 8, volume 75"."""

class TV:
    def __init__(self, brand, price, inches, OnOFF_status, channel=1, volume=50):
        self.brand = brand
        self.channel = channel if 1 <= channel <= 50 else 1
        self.price = price
        self.inches = inches
        self.OnOFF_status = OnOFF_status
        self.volume = min(max(volume, 0), 100)

    def inc_vol(self):
        if self.volume < 100:
            self.volume += 1

    def dec_vol(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

s_tv = TV("Panasonic", 500, 42, True)
print(s_tv.status())  # Panasonic at channel 1, volume 50

s_tv.inc_vol()
s_tv.inc_vol()
s_tv.inc_vol()
s_tv.dec_vol()
s_tv.set_channel(8)
print(s_tv.status())  # Panasonic at channel 8, volume 52

s_tv.reset_tv()
print(s_tv.status())  # Panasonic at channel 1, volume 50


# In[4]:


"""4) Using the python's Object Oriented Programming Scheme (OOPS) kindly complete the following tasks which is given as below-
TV class
TVClass - Base class
LedTV class
PlasmaTV class
Part - B : LED , Plasma

Inherit a TV class add additional properties like screen thickness, energy usage , Lifespan , Refresh rate , 
functionalities like viewingAngle , Backlight, DisplayDetails , which displays the detailed features of the TV."""

class SmartTV(TV):
    def __init__(self, brand, price, inches, OnOFF_status, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches, OnOFF_status)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self, angle):
        return f"This TV offers a viewing angle of {angle} degrees."

    def backlight(self, backlight_type):
        return f"The TV employs {backlight_type} backlighting technology."

    def display_details(self):
        return f"Screen thickness: {self.screen_thickness}mm, Energy usage: {self.energy_usage}W, Lifespan: {self.lifespan} years, Refresh rate: {self.refresh_rate}Hz."

smart_tv = SmartTV("Panasonic", 1000, 55, True, 10, 200, 10, 120)
print(smart_tv.status())  # Panasonic at channel 1, volume 50
print(smart_tv.viewing_angle(178))  # This TV has a viewing angle of 178 degrees.
print(smart_tv.backlight("LED"))  # The TV uses LED backlight technology.
print(smart_tv.display_details())  # Screen thickness: 10mm, Energy usage: 200W, Lifespan: 10 years, Refresh rate: 120Hz.


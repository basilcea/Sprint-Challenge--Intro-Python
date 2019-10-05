# Write classes for the following class hierarchy:
class Vehicle:
    #base class
    pass
class GroundVehicle(Vehicle):
    #inherits from vehicle
    pass
class Car(GroundVehicle):
    #inherits from GroundVehicle
    pass
class Motorcycle(GroundVehicle):
    #inherits from GroundVehicle
    pass
class FlightVehicle(Vehicle):
    pass
class Starship(FlightVehicle):
    pass
class Airplane(FlightVehicle):
    pass
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


import random


class Vehical:
    def __init__(self, Make, Model, Year, Weight, needsMaintenance=False, tripsSinceMaintenance=0):
        self.VehicalMake = Make
        self.VehicalModel = Model
        self.VehicalYear = Year
        self.VehicalWeight = Weight
        self.VehicalneedsMaintenance = needsMaintenance
        self.VehicaltripsSinceMaintenance = tripsSinceMaintenance

    def getMake(self):
        return self.VehicalMake

    def getModel(self):
        return self.VehicalModel

    def getYear(self):
        return self.VehicalWeight

    def getWeight(self):
        return self.VehicalWeight

    def repair(self):
        self.VehicalneedsMaintenance = False
        self.VehicaltripsSinceMaintenance = 0

    # Setters

    def setMake(self, Make):
        self.VehicalMake = Make

    def setModel(self, Model):
        self.VehicalModel = Model

    def setYear(self, Year):
        self.VehicalYear = Year

    def setWeight(self, Weight):
        self.VehicalWeight = Weight


class Car(Vehical):
    def __init__(self, VehicalMake, VehicalModel, VehicalYear, VehicalWeight, isDriving=True):
        Vehical.__init__(self, VehicalMake, VehicalModel,
                         VehicalYear, VehicalWeight)
        self.isDriving = isDriving

    def drive(self):
        self.isDriving = True

    def stop(self):
        self.VehicaltripsSinceMaintenance += 1
        self.isDriving = False
        if self.VehicaltripsSinceMaintenance > 100:
            self.VehicalneedsMaintenance = True


class Planes(Vehical):
    def __init__(self, VehicalMake, VehicalModel, VehicalYear, VehicalWeight, isFlying=False):
        Vehical.__init__(self, VehicalMake, VehicalModel,
                         VehicalYear, VehicalWeight)
        self.isFlying = isFlying

    def flying(self):
        if self.VehicalneedsMaintenance == True:
            print("The plane can't fly until it's repaired")
            return False

        self.isFlying = True
        return True

    def landing(self):
        if self.VehicaltripsSinceMaintenance < 100:
            self.VehicaltripsSinceMaintenance += 1
            self.isFlying = False
        else:
            self.VehicalneedsMaintenance = True


Car1 = Car("Tata", "Jaquar", 1008, 2002)
Car2 = Car("Tata", "Nexon EV", 1248, 2020)
Car3 = Car("Tata", "Safari", 1545, 2021)
#plane1 = plane("Deccan Air", "Boing", 12125, 2015)


def callCar(Car, carno, two_way_trips):
    print("VehicalMake - " + Car.VehicalMake + " VehicalModel - " + Car.VehicalModel + " VehicalWeight -\n " + str(Car.VehicalWeight) + " VehicalYear - " + str(Car.VehicalYear) + carno + " - isDriving: " + str(Car.isDriving) +
          carno + " -VehicalneedsMaintenance " + str(Car.VehicalneedsMaintenance))
    print("tripsSinceMaintenance - " + str(Car.VehicaltripsSinceMaintenance))
    for i in range(two_way_trips):
        if (i % 2 == 0):
            Car.drive()
        else:
            Car.stop()

    print("VehicalMake - " + Car.VehicalMake + " VehicalModel - " + Car.VehicalModel + " VehicalWeight -\n " + str(Car.VehicalWeight) + " VehicalYear - " + str(Car.VehicalYear) + carno + " - isDriving: " + str(Car.isDriving) +
          carno + " -VehicalneedsMaintenance " + str(Car.VehicalneedsMaintenance))
    print(" tripsSinceMaintenance - " + str(Car.VehicaltripsSinceMaintenance))


callCar(Car1, " Car 1", 100)
callCar(Car2, " Car 2", 300)
callCar(Car3, " Car 3", 201)


plane1 = Planes("US", "Boing", 12125, 2015)


def callplanes(planes, two_way_trips):
    print("VehicalMake - " + planes.VehicalMake + "VehicalModel - " + planes.VehicalModel + "VehicalWeight -\n " + str(planes.VehicalWeight) + " VehicalYear - " + str(planes.VehicalYear) + " - isFlying: " + str(planes.isFlying)
          + " -VehicalneedsMaintenance" + str(planes.VehicalneedsMaintenance))
    print("tripsSinceMaintenance - " + str(planes.VehicaltripsSinceMaintenance))

    for i in range(two_way_trips):
        if (i % 2 == 0):
            planes.flying()
        else:
            planes.landing()

    print("VehicalMake - " + planes.VehicalMake + "VehicalModel - " + planes.VehicalModel + "VehicalWeight -\n " + str(planes.VehicalWeight) + " VehicalYear - " + str(planes.VehicalYear) + " - isFlying: " + str(planes.isFlying)
          + " -VehicalneedsMaintenance" + str(planes.VehicalneedsMaintenance))
    print("tripsSinceMaintenance - " + str(planes.VehicaltripsSinceMaintenance))


callplanes(plane1, 204)

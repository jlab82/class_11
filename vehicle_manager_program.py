#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Vehicles:
    def __init__(self, brand, model, kmdsf, gsdate,):
        self.brand = brand
        self.model = model
        self.kmdsf = kmdsf
        self.gsdate = gsdate
    def get_full_name(self):
        return "{} {} {} {}" .format(self.brand, self.model, self.kmdsf, self.gsdate)


#see a list of vehicles the company has
def list_all_vehicles(vehicles):
    for index, car in enumerate(vehicles):
        print "ID: " + str(index)
        print car.get_full_name()
        print ""  # empty line

    if not vehicles:
        print "You don't have any car in your list."


#add new vehicle
def add_new_vehicle(vehicles):
    brand = raw_input("Please enter brand: ")
    model = raw_input("Please enter model: ")
    kmdsf = raw_input("Please enter kilometers done so far: ")
    gsdate = raw_input("Please enter general service date: ")


    new = Vehicles(brand=brand, model=model, kmdsf=kmdsf, gsdate=gsdate,)
    vehicles.append(new)

    print ""  # empty line
    print new.get_full_name() + " was successfully added to your vehicle list."


#edit kilometers and the general service date for each vehicle
def edit_vehicles(vehicles):
    print "Select the number of the vehicle you'd like to edit:"

    for index, vehicle in enumerate(vehicles):
        print str(index) + ") " + vehicle.get_full_name()

    print ""  # empty line
    selected_id = raw_input("What vehicle would you like to edit? (enter ID number): ")
    selected_vehicle = vehicles[int(selected_id)]

    new_kmdsf = raw_input("Please enter a new quantity of kilometers done so far for {}: " .format(selected_vehicle.get_full_name()))
    selected_vehicle.kmdsf = new_kmdsf
    new_gsdate = raw_input("Please enter a new general service date for {}: ".format(selected_vehicle.get_full_name()))
    selected_vehicle.gsdate = new_gsdate

    print ""  # empty line
    print "kilometers updated."
    # ... you can do the same for other fields.

#export vehicles to list
def export_txt(vehicles):
    file = open("vehicles.txt", "w+")
    for clave, valor in enumerate(vehicles):
        file.write(valor.get_full_name() + "\n")

#import vehicles to list
def import_txt():
    archivo = open("vehicles.txt", "r")
    car = ["a", "b"]
    i = 0
    for linea in archivo.readlines():
        car[i] = linea.split()
        i += 1
    print car

#main
def main():
    car1 = Vehicles(brand="Peugeote", model="407", kmdsf=250000, gsdate="10/12/2017", )
    car2 = Vehicles(brand="Opel", model="Vectra", kmdsf=52000, gsdate="25/12/2017", )
    vehicles = [car1, car2]

    import_txt()

    while True:
        print ""  # empty line
        print "Please choose one of these options:"
        print "a) See a list of vehicles the company has"
        print "b) Edit kilometers and the general service date for each vehicle"
        print "c) Add new vehicle"
        print "d) Export list to txt file"
        print "e) Quit the program."
        print ""  # empty line

        selection = raw_input("Enter your selection (a, b, c, d or e): ")
        print ""  # empty line

        if selection.lower() == "a":
            list_all_vehicles(vehicles)
        elif selection.lower() == "b":
            edit_vehicles(vehicles)
        elif selection.lower() == "c":
            add_new_vehicle(vehicles)
        elif selection.lower() == "d":
            export_txt(vehicles)
        elif selection.lower() == "e":
            export_txt(vehicles)
            print "Thank you for using Vehicle Manager. Goodbye!"
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue

if __name__ == "__main__":  # this means that if somebody ran this Python file, execute only the code below
    main()


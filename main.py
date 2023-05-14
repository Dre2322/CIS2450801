class vehicle: 

  def setMake(self, Make):
    self.Make = Make

  def setModel(self, Model):
    self.Model = Model

  def displayOptions(self):
    print(f'The Make is: {self.Make}')
    print(f'The Model is: {self.Model}')

class car(vehicle):
  def setDoors(self, Doors):
    self.Doors = Doors

  def displayOptions(self):
    print(f'The Make is: {self.Make}')
    print(f'The Model is: {self.Model}')
    print(f'The number of doors is: {self.Doors}')
    print()

class truck(vehicle):
  def setBedLength(self, BedLength):
    self.BedLength = BedLength

  def displayOptions(self):
    print(f'The Make is: {self.Make}')
    print(f'The Model is: {self.Model}')
    print(f'The bed length is: {self.BedLength}')
    print()

print('Welcome')
print()

x = 0
while x < 3:
  x = int(input('Select 1 for cars, 2 for trucks, or 3 to quit: '))
  print()
  if x == 1: 
    input_cmake = input('Please enter the Car Make: ')
    input_cmodel = input('Please enter the Car Model: ')
    input_doors = input('Please enter the number of doors: ')
    new_car = car()
    new_car.setMake(input_cmake)
    new_car.setModel(input_cmodel)
    new_car.setDoors(input_doors)
    print()
    new_car.displayOptions()
    
  elif x == 2:
    input_tmake = input('Please enter the Truck Make: ')
    input_tmodel = input('Please enter the Truck Model: ')
    input_bedlength =input('Please enter the bed length: ')
    new_truck = truck()
    new_truck.setMake(input_tmake)
    new_truck.setModel(input_tmodel)
    new_truck.setBedLength(input_bedlength)
    print()
    new_truck.displayOptions()

  else:
    print('Thank you')
    print()
    
  
airportCodes = [] # set up empty arrays 
airportNames = [] 
distance1 = [] 
distance2 = [] 
plane_type = ''
airports = ''
d = 0 # distance between airports

planes = [['Medium narrow body', 8, 2650, 180, 8],
['Large narrow body', 7,5600,220,10],
['Medium wide body',5,4050,406,14]]
a = 0


fileIn = open("airports.txt",'r')# open airpots.txt for reading 
for i in range(5): # loop over each line in the airports.txt file 
  lineIn = fileIn.readline() # read each line in 
  cleanedlLineIn = lineIn.strip() # remove the new line characters at the end 
  lineList = cleanedlLineIn.split(",") # create a list from each line, splitting at the commas 
  airportCodes.append(lineList[0]) # put the 0th item in the list into a list of airportCodes 
  airportNames.append(lineList[1]) 
  distance1.append(lineList[2]) 
  distance2.append(lineList[3]) 
fileIn.close() # close the file 

def calculate_profit():
  print('calculating profit')
  
def airport_details():
  global aiportCodes
  user_entry = input('Enter airport code (LPL or BOH): ') # user_entry = uk_airport
  if user_entry == 'LPL' or user_entry == 'BOH':
    arrival_airport = input('Enter 3 letter code for internatinal Airport: ')
    if arrival_airport in airportCodes:
      arrival_index = airportCodes.index(arrival_airport)
      print(f'Arrival airport is {airportNames[arrival_index]}')
      return [user_entry, arrival_index]
    else:
      print('Enter a valid international airport code')
  else:
    print('Please enter LPL or BOH or a valid ')

def flight_details():
  global planes
  plane_type = input('Enter type of plane: ')
  valid_inputs = ['Medium narrow body', 'Large narrow body', 'Medium wide body']
  if plane_type in valid_inputs:
    plane_index = valid_inputs.index(plane_type)
    first_class = int(input('Enter the number of first class seats: '))
    if first_class != 0:
      if first_class >= planes[plane_index][4] and first_class <= planes[plane_index][3] / 2:
        standard_seat_number = planes[plane_index][3] - first_class
        return [plane_index, standard_seat_number, first_class]
      
    else:
      return [plane_index, planes[plane_index][3], 0]

  else:
    print('Please enter a valid plane type')
  
def check_all_data_filled():
  global plane_type, airports
  if type(plane_type) == list and type(airports) == list:
    return True
  else:
    return False

def distance():
  global airports, plane_type, planes, d 
  if airports[0] == 'LPL':
    d = int(distance1[airports[1]])
    if d < int(planes[plane_type[0]][2]):
      return True
    else:
      return False
    
  if airports[0] == 'BOH':
    d = int(distance2[airports[1]])
    if d < int(planes[plane_type[0]][2]):
      return True
    else:
      return False
    
def ticket_price():
  global plane_type
  try:
    standard = int(input('Enter the price of a standard ticket: '))
    first_class = int(input('Enter the price of a first class ticket: '))
    return [True, standard, first_class]
  except:
    print('Please enter a digit for the ticket price')

def calc():
  global planes, plane_type, aiports, prices
  cost_per_seat = planes[plane_type[0]][1] * d/100
  flight_cost = cost_per_seat * (plane_type[1] + plane_type[2])
  flight_income = (plane_type[1]* prices[0] ) + (plane_type[2]*prices[1])
  flight_profit = flight_income - flight_cost
  return [cost_per_seat, flight_cost, flight_income, flight_profit]

def clear_data():
  global plane_type, airports, prices
  plane_type = ''
  airports = ''
  prices = ''
  print('Data has been cleared.')
  
  
def menu():
  global a, plane_type, airports, prices
  print('\nMenu choices:\n Select 1: enter airport details \n Select 2: enter flight details \n Select 3: enter price plan and calculate profit \n Select 4: clear data \n Select 5: quit program')
  
  a = input('Enter a menu number: ')

  if a == '1':
    airports = airport_details() # ['uk airport', index for international airport]

  elif a == '2':
    plane_type = flight_details() # [plane index, standard seat no. , first classs seat no.]
    
    
  elif a == '3':
    if check_all_data_filled() == True:
      if distance() == True: # Returns true if plane can fly to the destination
        prices = ticket_price() # [standard seat price, first class seat price]
        if prices[0] == True:
          profit = calc() # [cost_per_seat, flight_cost, flight_income, flight_profit]
          print(f"""
          Cost Per Seat: {profit[0]}
          Flight Cost: {profit[1]}
          Flight Income: {profit[2]}
          Flight Profit: {profit[3]}
          """)
      else:
        print('Distance too far for this type of plane')
    else:
      print('Not all data filled in yet')
    
  elif a == '4':
    clear_data()
    
  elif a == '5':
    exit()

  else: 
    print('\nEnter a valid menu number')
    pass

    
while a != 5:
  menu()


    
    

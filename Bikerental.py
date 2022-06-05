from tabulate import tabulate
from datetime import datetime
import random
import emoji

q=[]
e=[]
print("***",emoji.emojize(":motorcycle:"),"Welcome to Bajaj Bikes rental Showroom" ,emoji.emojize(":motorcycle:"),"****")
class Bike_showroom:
    def __init__(self,x,y,z):
        self.x = x
        self.y= y
        self.z = z 
    def number_bikes(self):
        return (f'\nnumber of bikes available={self.x}')

    def bikes_names(self):
         for t in self.y:
           print(t)       
         

    def rental_charges(self):
        return (tabulate(self.z))   



p1=Bike_showroom(56, ('Bajaj pulsar', 'Bajaj ct 100' ,'Bajaj pulsar 150','Bajaj pulsar 125','Bajaj platina','Bajaj dominar 400','Bajaj platina 110','Bajaj avenger cruise 220'),
          [['Sr no.','Bike Name', 'Daily rent. charges', 'weekly rent. charges','Monthly rent. charges'], ['(1)','Bajaj pulsar',700, 2599, 10000], ['(2)','bajaj ct 100', 650, 2400, 9000], ['(3)','bajaj pulsar 150', 750, 3500, 12000],
         ['(4)','Bajaj pulsar 125', 720, 3000, 9500],['(5)','bajaj platina', 730, 3300, 11000],['(6)','Bajaj Dominar 400', 800, 3800, 13999],['(7)','Bajaj platina 110',780, 3500, 12500],['(8)','Bajaj Avenger Cruise 220', 880, 5049, 20000]]
         )
            


def returned_bike():
    d=[]
    today = datetime.today()

    print('\n',emoji.emojize(":star-struck:"),'**THANK YOU FOR TAKING OUR SERVICE****',
          emoji.emojize(":grinning_face_with_big_eyes:"))
    name = input('Please enter your name:')
    date = input('Date of renting a bike:')
    print("Today date is: ", today)
    billno= input('Please enter your bill number:')
    d.append(name)
    d.append(date)
    d.append(today)
    d.append(billno)
    
    with open('file.txt', 'a') as f:
        f.write(f'\n\n{name},{date},{billno}')
    

      

def discount_bike():
    print('**Special discount on the bikes*** \n')
    c={1:'Bajaj Dominar 400',2:'Bajaj Avenger Cruise 220',3:'bajaj platina'}
    print(c)
   
    p=int(input('Please choose the number to see the discount on specific bike from above list: '))
   
    if p==1:
      print('\t',c[p],'= wow !! 10% DISCOUNT is available')
    elif p==2:
      print('\t',c[p],'= wow !! 5% DISCOUNT is available')
    elif p==3:
      print('\t',c[p],'= wow !! 15% DISCOUNT is available')
    else:
      print('\nplease !! put correct input')  



def options():
     print('\n*** TO CHECK THE DETAILS BEFORE RENTING BIKE ***')
     print('1. Show number of bikes available ')
     print('2. Show names of bikes available ')
     print('3. Show Rental charges (daily, weekly, monthly) ')
     print('4. check available discount on bikes')

     print('\n** WANT TO RENT OR RETURN BIKE **')
     print('5. Want to return rented bike')
     print('6. Wants a bill for rented bike')
     print('7. Registration or log in')
  

     k= int(input('\nChoose the option from above: '))

     if k== 1:          
       print(p1.number_bikes())
     elif k== 2:
       print(p1.bikes_names())
     elif k== 3:     
       print(p1.rental_charges())
     elif k== 4:     
       discount_bike()
     elif k== 5:     
       returned_bike()
     elif k== 6:     
       provide_bill()
     elif k== 7:     
       reglogin()
     else: 
       print('please, Enter the correct option')
     options()


class Bill:
    def __init__(self,t,g,h,c):
       self.t = t
       self.g = g
       self.h = h
       self.c = c
      #  self.s = s
      #  self.r = r
      #  self.i = i
      #  self.o = o

b1=Bill('Bajaj pulsar',700, 2599, 10000)
b2=Bill('Bajaj ct 100', 650, 2400, 9000)
b3=Bill('Bajaj pulsar 150', 750, 3500, 12000)
b4=Bill('Bajaj 125', 720, 3000, 9500)
b5=Bill('Bajaj platina', 730, 3300, 11000)
b6=Bill('Bajaj Dominar 400', 800, 3800, 13999)
b7=Bill('Bajaj platina 110',780, 3500, 12500)
b8=Bill('Bajaj Avenger Cruise 220', 880, 5049, 20000)

def provide_bill():
  print('\na. If you had taken bike on daily basis')
  print('b. If you had taken bike on weekly basis')
  print('c. If you had taken bike on monthly basis\n')

  j= input('choose one option from above: ')

  if j== 'a':
    date= int(input('Enter the no. of days you rented bike for: '))
    bike= input('Name of bike you rented')
    bike=bike.capitalize()

    if bike== 'Bajaj pulsar':
      print('Please pay rupees: ',date*(b1.g))
    elif bike== 'Bajaj ct 100':
      print('Please pay rupees: ',date*(b2.g))
    elif bike== 'Bajaj pulsar 150':
      print('Please pay rupees: ',date*(b3.g))
    elif bike== 'Bajaj pulsar 125':
      print('Please pay rupees: ',date*(b4.g))
    elif bike== 'Bajaj platina':
      print('Please pay rupees: ',date*(b5.g))
    elif bike== 'Bajaj dominar 400':
      print('Please pay rupees: ',date*(b6.g))
    elif bike== 'Bajaj platina 110':
      print('Please pay rupees: ',date*(b7.g))
    elif bike== 'Bajaj avenger Cruise 220':
      print('Please pay rupees: ',date*(b8.g))
    else:
      print('Please see if you put bikes name correctly or Not')  
    
  elif j== 'b':
    date= int(input('Enter the no. of weeks you rented bike for: '))
    bike= input('Name of bike you rented')
    bike=bike.capitalize()

    if bike== 'Bajaj pulsar':
      print('Please pay rupees: ',date*(b1.h))
    elif bike== 'Bajaj ct 100':
      print('Please pay rupees: ',date*(b2.h))
    elif bike== 'Bajaj pulsar 150':
      print('Please pay rupees: ',date*(b3.h))
    elif bike== 'Bajaj pulsar 125':
      print('Please pay rupees: ',date*(b4.h))
    elif bike== 'Bajaj platina':
      print('Please pay rupees: ',date*(b5.h))
    elif bike== 'Bajaj dominar 400':
      print('Please pay rupees: ',date*(b6.h))
    elif bike== 'Bajaj platina 110':
      print('Please pay rupees: ',date*(b7.h))
    elif bike== 'Bajaj avenger Cruise 220':
      print('Please pay rupees: ',date*(b8.h))
    else:
      print('Please see if you put bikes name correctly or Not')  

  elif j== 'c':
    date= int(input('Enter the no. of month you rented bike for: '))
    bike= input('Name of bike you rented')
    bike=bike.capitalize()

    if bike== 'Bajaj pulsar':
      print('Please pay rupees: ',date*(b1.c))
    elif bike== 'Bajaj ct 100':
      print('Please pay rupees: ',date*(b2.c))
    elif bike== 'Bajaj pulsar 150':
      print('Please pay rupees: ',date*(b3.c))
    elif bike== 'Bajaj pulsar 125':
      print('Please pay rupees: ',date*(b4.c))
    elif bike== 'Bajaj platina':
      print('Please pay rupees: ',date*(b5.c))
    elif bike== 'Bajaj dominar 400':
      print('Please pay rupees: ',date*(b6.c))
    elif bike== 'Bajaj platina 110':
      print('Please pay rupees: ',date*(b7.c))
    elif bike== 'Bajaj avenger cruise 220':
      print('Please pay rupees: ',date*(b8.c))
    else:
      print('Please see if you put bikes name correctly or Not')    

  else:
    print('\nPlease enter the correct option')

def reglogin():
  def registration():
    print(emoji.emojize(":man:"),)
    p=input('Create username(use letter and numbers): ')
    if p in q:
      print('\nThis username is already choosen try again !!')
    else:
      q.append(p)
      print(emoji.emojize(":locked_with_key:"))
      y=input('Create password: ')
      e.append(y)

      print('successfully registered', emoji.emojize(':thumbs_up:'),'\n')
    
    def bike_info():
      d={'Bajaj pulsar':'125/135/150/160/180/200/220 cc Air-cooled/oil-cooled/liquid cooled, Four-stroke engine, 2-4 valve, SOHC, single piston, kick start / electric start',
       'Bajaj ct 100':'Engine Capacity-102 cc,Mileage-75 kmpl,Transmission-4 Speed Manual,Kerb Weight-115 kg ' ,
       'Bajaj pulsar 150':'Engine Displ-149.5cc, Max Power-14PS@8500rpm, Fuel Type-Petrol, Tubless tyre','Bajaj pulsar 125':'Fuel economy-54 to 55 km/l,Curb weight: 140 to 142 kg,Fuel tank capacity: 11.5 L,Seat height: 790 mm'
      ,'Bajaj platina':'Fuel economy: 70 to 100 km/l,Curb weight: 111 to 123 kg,Fuel tank capacity: 11 to 11.5 L,Seat height: 804 to 807 mm',
      'Bajaj dominar 400':'Engine Displ: 373.3 cc,Max Power: 40 PS @ 8800 rpm,Mileage: 26.50 kmpl,Fuel Type: Petrol',
      'Bajaj platina 110':'Engine: 115 cc,Max Power: 8.6 bhp,Kerb Weight-122kg,',
      'Bajaj avenger cruise 220':'Engine: 220 cc,Brakes: Disc,Kerb Weight: 163 kg,Seat Height: 737 mm'}
      
      o=input('Which bikes information you want: ') 
      o=o.capitalize()
      print('\n')

      if o== 'Bajaj pulsar':
        print(d['Bajaj pulsar'])
      elif o== 'Bajaj ct 100':
        print(d['Bajaj ct 100'])
      elif o== 'Bajaj pulsar 150':
        print(d['Bajaj pulsar 150'])
      elif o== 'Bajaj pulsar 125':
        print(d['Bajaj pulsar 125'])
      elif o== 'Bajaj platina':
        print(d['Bajaj platina'])
      elif o== 'Bajaj dominar 400':
        print(d['Bajaj dominar 400'])
      elif o== 'Bajaj platina 110':
        print(d['Bajaj platina 110'])
      elif o== 'Bajaj avenger cruise 220':
        print(d['Bajaj avenger cruise 220'])
      else:
        print('This bike is unavailable or you had written bike name incorrectly')

    def request_bikes():
      l=('Bajaj pulsar', 'Bajaj ct 100' ,'Bajaj pulsar 150','Bajaj pulsar 125','Bajaj platina','Bajaj dominar 400','Bajaj platina 110','Bajaj avenger cruise 220')
      
      global nameofc
      global dateofrent
      global bikerented
      nameofc=input(print('Please enter your name: '))
      dateofrent=datetime.today()
      for d in l:
        print(d)

      bikerented=input('\nEnter name of bike from above list you want to Rent: ')
      bikerented=bikerented.capitalize()
      if bikerented in l:
        billno =random.randint(1,100)
        print('your bill no. is ',billno)
      else:
        print('This bike is not available in showroom')  
      options()

      with open('new registration.txt', 'a') as d:
        d.write(f'\n\n{nameofc},{dateofrent},{bikerented},{billno}')

    print('1. Need Bike information before renting it')
    print('2. Want to request a bike')
    print('3. Go back to main menu\n')

    u=input('Enter option from above to proceed: ')
    if u== '1':
      bike_info() 
    elif u== '2':
      request_bikes()
    elif u== '3':
      options()
    else:
      print('Invalid input !!')       

  def login():  
    m =input('Enter your username: ')

    if m in q:
      nameofc=input('Please enter your name: ')
      b=input('\nPlease enter your password: ')
      if b in e:
        print('Hello! ', nameofc)
        print('You rented Bike on: ',dateofrent)
        print('you had rented ',bikerented,' from us')
      else:
        print('Wrong password!! try again')  
    else:
      print('You had not registered for our services')

  print('a. Registration')
  print('b. Log in')
  print('c. Go back to main menu\n')

  l=input('Choose option from above to proceed: \n')

  if l=='a':
    registration()
  elif l== 'b':
    login()  
  elif l== 'c':
    options()  
  else:
     print('Please choose correct option') 

  options()   

options()
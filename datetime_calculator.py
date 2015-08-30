import datetime
# to work with date and time
 
import csv
# to work with csv



def main ():
#defining main function
     Cm="y"

     while Cm == "y"  or Cm == "yes" :
         #while is used to reapeat events

        print ("Choose what you want. Enter 1 or 2 or 3:")  
        ask = input("1 = Search your or someone else's birthday \n2 = Calculate your next birthday \n3 = Exit ") 
  
        if ask == '1' :
           mo12()
           #press 1 to search your or someone else's birthday

        elif ask == '2' :
           datetime_calculator()
           #press 2 to calculate your next birthday

        elif ask == '3' :
            return
           #press 3 to Exit

        else:
            print("That's not on the list!")
        
        Cm = input('Press y or yes if you want me to calculate again ')
         
     return
        # return is used to exit


def mo12():
       #name of the file
        fileName = "./datetime_calculator.csv"
       # access mode - Read
        accessMode = 'r'

        searchName = input("who's birthday are you looking for ? (please enter) :")

        with open(fileName, mode = accessMode) as Myfile :

        #Read all the contents!
         dataFromFile = csv.reader(Myfile, delimiter=",")

         for currentRow in dataFromFile :
             #for is used to repeated events
           for currentWord in currentRow :
               if searchName == currentWord :
                    print(', '.join(currentRow))
        return

def datetime_calculator():
    #defining datetime_calculator ...
     
        fileName = './datetime_calculator.csv'
     #name of the file

        accessMode = 'a'
        #accessMode = append

        Myfile = open(fileName, mode = accessMode)
        #opening my file....

        firstName = input('What is your first name ? :')
        lastName = input('What is your last name  ? :')

        currentDate = datetime.date.today()
        #current date is datetime.date.today
        
        print ("Today is: " + str(currentDate))

            #print (currentDate.year)
        #print ('today is '+ str(currentDate.year))
        #print (format_date(currentDate, format='full', locale='ru_Ru'))
        #print (format_date(currentDate, format='full', locale='en'))
        #print (format_date(currentDate, format='full', locale='De'))

        #strftime allows you to specigy the date format
        #print ('Today is: '+ currentDate.strftime('%d %A of %B,%Y'))


        difference  = 0

        #difference  starts at 0
        try :
            Birthday = input ("When is your birthday? (dd/mm/yyyy) " ) 
        #asking, when is your birthday?
            Birthday = datetime.datetime.strptime(Birthday, '%d/%m/%Y').date()

        
            NextBirthday = Birthday.replace(year = currentDate.year)
        #replacing year to the current year
        
        
            difference  = NextBirthday - currentDate


            if difference.days  < 0 :
               print ('\nYour birthday was ' + str(abs(difference.days)) + ' days ago') 
            else :
               print('\nThere are  ' + str(difference.days) + ' days left until your next birthday \n ')
        except:
            print('Birthday written incorectly.Try again :(')
          #if the try does not work,then the except will work 
          
        Myfile.write('\n' + firstName + ",")
        Myfile.write(lastName + ",")
        Myfile.write(str(Birthday))
        Myfile.close()                             
        return



#finally do this!
main()
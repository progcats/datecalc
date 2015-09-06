import datetime, time, sys, csv
# to work with date and time   # to work with csv


class Datecalc:

    def mo12(self, full_name):
       
        fileName = "./datetime_calculator.csv" #name of the file
        accessMode = 'r' # access mode - Read

        with open(fileName, mode = accessMode) as Myfile :

            #Read all the contents!
            dataFromFile = csv.reader(Myfile, delimiter=",")

            for currentRow in dataFromFile :
                 #for is used to repeated events
                for currentWord in currentRow :
                    if currentWord in full_name :
                         return ', '.join(currentRow)

    def datetime_calculator(self, full_name, birth_date):
        #defining datetime_calculator ...
     
        fileName = './datetime_calculator.csv' #name of the file

        accessMode = 'a' #accessMode = append

        Myfile = open(fileName, mode = accessMode)
        #opening my file....

        firstName = full_name.split()[0] #TODO: use dicionary
        lastName = full_name.split()[1]

        currentDate = str(time.strftime("%d-%m-%Y"))
        #current date is datetime.date.today
        
        print ("Today is: " + str(currentDate))

        difference  = 0

        #difference  starts at 0
        try :
            Birthday = birth_date #input ("When is your birthday? (dd/mm/yyyy) " ) 
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


if __name__ == '__main__':

    calc = Datecalc() # instantiating an object

    ask = sys.argv[1] #input("1 = Search your or someone else's birthday \n2 = Calculate your next birthday \n3 = Exit ") 

    FULL_NAME = sys.argv[2]

    if ask == '1' :  #press 1 to search your or someone else's birthday
       print calc.mo12(FULL_NAME)
      
    elif ask == '2' : #press 2 to calculate your next birthday
       BIRTH_DATE = sys.argv[3]
       calc.datetime_calculator(FULL_NAME, BIRTH_DATE)
       
    elif ask == '3' :
        pass

from operations import option_one,option_two,option_three,option_four

#exit program
def exit():
      print('---------------------------- THANK YOU!! --------------------------------------')
      start = input('CLICK ANY KEY TO RUN THE SYSTEM:\n')
      if start:
          user_input()



# program display start
def message():
    print(
        '*************************************************************************')
    print(
        '                 Project: "VISUALIZATION"  \n                 Name: Nischal Rana Magar \n                     Id: 30377015 ')
    print(
        '*************************************************************************')


    start_program()

def start_program():
        options = ['Statistics','Export children details  who havent lost any teeth','Display number of claims per state','Compare 2 state' ,'Exit']
        for key,value in enumerate(options,start=1):
            print('{}:{}'.format(key,value))
        print('\n')




# asking for user input
def user_input():
    while True:
            try:
                message()
                answer = int(input('ENTER YOUR CHOICE [1-5]:'))
                if answer == 1:
                        option_one()

                elif answer == 2:
                        option_two()
                        break

                if answer == 3:
                        option_three()

                if answer == 4:
                    option_four()

                if answer == 5:
                    exit()



            except ValueError:
                print('PLEASE ENTER THE VALID INPUT !!!! ENTER NUMBER FROM 1 TO 0 !!!!')
                user_input()


# calling main function
user_input()
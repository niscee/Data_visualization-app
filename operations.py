import pandas as pd
from matplotlib import pyplot as plt


# statistics function start
def option_one():
    csv_file = 'addresses.csv'
    file = pd.read_csv(csv_file)
    total_children = file['Surname'].count()
    tooth = file['Total number of teeth lost']

    #no of children who (never lost their tooth / lost baby teeth)
    never_lost_tooth = 0
    baby_teeth = 0
    for t in tooth:
        if t == 0:
            never_lost_tooth += 1
        elif t == 20:
            baby_teeth += 1

    #total expenditure
    total_expenditure = 0
    for t in tooth:
        if t == 1:
            total_expenditure += 1.00
        elif t > 1:
            total_expenditure += 0.50
        else:
            total_expenditure += 0.00




    #average no of teeth claim
    avg = (file['Total number of teeth lost'].sum())/total_children

    print('Total number of children on list:{}'.format(total_children))
    print('Average number of teeth claims over the years:{}'.format(avg))
    print('Number of children who have never lost a tooth:{}'.format(never_lost_tooth))
    print('Number of children who have lost all their baby teeth:{}'.format(baby_teeth))
    print('Total expenditure for this year:{}\n'.format(total_expenditure))



# Export children details who havent lost any teeth function start
def option_two():
    csv_file = 'addresses.csv'
    file = pd.read_csv(csv_file)
    file.columns = [column.replace(" ", "_") for column in file.columns]
    file.query('Total_number_of_teeth_lost == 0', inplace=True)
    filename = input('Enter your filename:')
    if filename:
        f = open(filename + '.txt', "w+")
        result = f.write("{}".format(file))
        print(file)

    else:
        option_two()


#Display a graph showing the number of claims per State
def option_three():
    csv_file = 'addresses.csv'

    # tas state total
    file = pd.read_csv(csv_file)
    file.query('State == "TAS"', inplace=True)
    tas = file['Total number of teeth lost'].count()


    # qld state total
    file = pd.read_csv(csv_file)
    file.query('State == "QLD"', inplace=True)
    qld = file['Total number of teeth lost'].count()


    # wa state total
    file = pd.read_csv(csv_file)
    file.query('State == "WA"', inplace=True)
    wa = file['Total number of teeth lost'].count()


    # nsw state total
    file = pd.read_csv(csv_file)
    file.query('State == "NSW"', inplace=True)
    nsw = file['Total number of teeth lost'].count()


    # sa state total
    file = pd.read_csv(csv_file)
    file.query('State == "SA"', inplace=True)
    sa = file['Total number of teeth lost'].count()


    # vic state total
    file = pd.read_csv(csv_file)
    file.query('State == "VIC"', inplace=True)
    vic = file['Total number of teeth lost'].count()


    # nt state total
    file = pd.read_csv(csv_file)
    file.query('State == "NT"', inplace=True)
    nt = file['Total number of teeth lost'].count()


    def create_bar_chart(data, labels):
          num_bars = len(data)  # Numbe3


          # r of bars to draw
          positions = range(1, num_bars + 1)  # Positions of bars on y-axis
          plt.bar(positions, data, align='center')  # Generate the bar chart
          plt.xticks(positions, labels)  # Add little markers to each label on x-axis
          plt.xlabel('STATE')  # At x-axis label
          plt.ylabel('NUMBER OF CHILDREN')  # Add y-axis label
          plt.title('Number of children per state')  # Add title
          plt.grid()  # Add a grid for easier visual estimation of values
          plt.show()

    stepsWalked = [tas, qld, wa, nsw, sa, vic, nt]
    labels = ['TAS', 'QLD', 'WA', 'NSW', 'SA', 'VIC', 'NT']
    create_bar_chart(stepsWalked, labels)


#Display a graph showing the number of claims per State
def option_four():
     while True:
        try:
            print(
                'ENTER O FOR TAS \t ENTER 1 FOR QLD \t ENTER 2 FOR WA \t ENTER 3 FOR NSW \t ENTER 4 FOR SA \t ENTER 5 FOR VIC \t ENTER 6 FOR NT \n')

            request_one = int(input('ENTER THE FIRST VALUE:'))
            request_two = int(input('ENTER THE SECOND VALUE:'))

            if request_one > 6 or request_two > 6:
                print('ENTER VALID INPUT!!!!\n')
                option_four()
            else:
                csv_file = 'addresses.csv'

                # tas state total
                file = pd.read_csv(csv_file)
                file.query('State == "TAS"', inplace=True)
                tas = file['Total number of teeth lost'].count()

                # qld state total
                file = pd.read_csv(csv_file)
                file.query('State == "QLD"', inplace=True)
                qld = file['Total number of teeth lost'].count()

                # wa state total
                file = pd.read_csv(csv_file)
                file.query('State == "WA"', inplace=True)
                wa = file['Total number of teeth lost'].count()

                # nsw state total
                file = pd.read_csv(csv_file)
                file.query('State == "NSW"', inplace=True)
                nsw = file['Total number of teeth lost'].count()

                # sa state total
                file = pd.read_csv(csv_file)
                file.query('State == "SA"', inplace=True)
                sa = file['Total number of teeth lost'].count()

                # vic state total
                file = pd.read_csv(csv_file)
                file.query('State == "VIC"', inplace=True)
                vic = file['Total number of teeth lost'].count()

                # nt state total
                file = pd.read_csv(csv_file)
                file.query('State == "NT"', inplace=True)
                nt = file['Total number of teeth lost'].count()

                state_name = ['TAS', 'QLD', 'WA', 'NSW', 'SA', 'VIC', 'NT']
                state_value = [tas, qld, wa, nsw, sa, vic, nt]



                def create_bar_chart(data, labels):
                    num_bars = len(data)  # Numbe3

                    # r of bars to draw
                    positions = range(1, num_bars + 1)  # Positions of bars on y-axis
                    plt.bar(positions, data, align='center')  # Generate the bar chart
                    plt.xticks(positions, labels)  # Add little markers to each label on x-axis
                    plt.xlabel('STATE')  # At x-axis label
                    plt.ylabel('NUMBER OF CHILDREN')  # Add y-axis label
                    plt.title('Number of children per state')  # Add title
                    plt.grid()  # Add a grid for easier visual estimation of values
                    plt.show()


                stepsWalked = [state_value[request_one], state_value[request_two]]
                labels = [state_name[request_one],state_name[request_two]]
                create_bar_chart(stepsWalked, labels)
                break



        except:
            print('INVALID INPUT!!!!!!!!!!!!!!!!')


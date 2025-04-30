
def display_main_menu():
    print ("Enter some numbers: ")
    return

def get_user_input():
    
    txt = input()

    x = txt.split(",")
    x = [float(i) for i in x]
    print(x)
    return x
    
def calc_average_temperature(x):
    sum_total = sum(x)
    total = len(x)
    average = sum_total / total
    print("Average temperature is: ", (average))
    return average 

def find_min_max(x):
    x.sort() 
    print("The minimum temperature is: ", (x[0]))
    print("The maximum temperature is: ", (x[-1]))
    return x

def sort_temperature(x):
    ascending = x.sort()
    return ascending 

def calc_median_temp(ascending):
    
    if len(ascending) % 2 == 0:
        median = (ascending[len(ascending)//2] + ascending[len(ascending)//2 - 1]) / 2
    else:
        median = ascending[len(ascending)//2]
    print ("median is " + (median))
    return 
    

def main():
    display_main_menu()
    temp = get_user_input()
    calc_average_temperature(temp)
    find_min_max(temp)
    sort_temperature(temp)
    calc_median_temp(temp)
if __name__ == "__main__":
    main()
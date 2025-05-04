def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height**2)
    return bmi
   
def classify_bmi(bmi_value):
    if(bmi_value < 18.5 ):
        bmi = -1
        print("UNDERWEIGHT!")

    if(bmi_value >= 18.5 and bmi_value <=25.0):
        bmi = 0
        print("normal weight")
    else: 
        bmi = 1
        print("OVERWEIGHT")
    return bmi



def startpoint():

    bmi_output = calculate_bmi(1.73,66)
    print("bmi_value:" + str(bmi_output))
    classify_bmi(bmi_output)


if __name__ == "__main__":
    startpoint()
    
    
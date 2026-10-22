
def temp_conversion(degree, scale, desired_scale):
    """Convert temperature from Celsius, Fahrenheit, or Kelvin to another scale."""

    if type(degree!= float):
        return ValueError("Invalid temperature value. Please enter a valid number.")
        
    if (scale == "C" or scale == "c") and (desired_scale == "C" or desired_scale == "c"):      
        return degree
    elif (scale == "C" or scale == "c") and (desired_scale == "F" or desired_scale == "f"):     #celsius to fahrenheit
        return (degree * 9/5) + 32
    elif (scale == "C" or scale == "c") and (desired_scale == "K" or desired_scale == "k"):     #celsius to kelvin
        return degree + 273.15
    elif (scale == "F" or scale == "f") and (desired_scale == "C" or desired_scale == "c"):     #fehrnheit to celsius
        return (degree - 32) * 5/9
    elif (scale == "F" or scale == "f") and (desired_scale == "K" or desired_scale == "k"):     #fahrenheit to kelvin
        return ((degree - 32) * 5/9) + 273.15
    elif (scale == "K" or scale == "k") and (desired_scale == "C" or desired_scale == "c"):     #kelvin to celsius
        return degree - 273.15
    elif (scale == "K" or scale == "k") and (desired_scale == "F" or desired_scale == "f"):     #kelvin to fahrenheit
        return ((degree - 273.15) * 9/5) + 32
    else:
        return ValueError("Invalid scale. Please use 'C' for Celsius or 'F' for Fahrenheit or 'K' for Kelvin.")

   
#test the function
degree = input("Enter the temperature value: ")
scale = input("Enter the scale (C for Celsius, F for Fahrenheit, K for Kelvin): ")
desired_scale = input("Enter the scale you want to convert to (C for Celsius, F for Fahrenheit, K for Kelvin): ")
converted_temp = round(temp_conversion(degree, scale, desired_scale), 2)
print("The converted temperature is:",converted_temp) 

##2nd part of the assignment

def dice_roll(dice_configuration, desired_number ):
    """Simulate rolling dice and return the prbability of getting a desired number."""
    if 'd' not in dice_configuration:               #if the string doesn't contain a 'd' then raise an exception
        return ValueError("the dice configuration has to have a 'd'")
    my_list= dice_configuration.split("d")    #spliting the entered string to get the number of dice and sides
    if type(my_list) != int:          
        return ValueError("invalid input,please enter a positive number: ")
    num_dice=int(my_list[0])
    sides=int(my_list[1])
    if num_dice <= 0 or sides <= 1 or desired_number <1   or type(desired_number) != int:
        return ValueError("Invalid input value. Please ensure all values are positive integers")
    
    

    num_outcome = pow(sides, num_dice) 
    probability = 0

    if num_dice == 1:
        for j in range(1,sides+1):   #sides+1 to include the last number
            if j >= desired_number:
                probability+=1/sides     #if the number on the side is greater than the desired number we add it's probability to the final probability value

### in assignment : maximum 4 dice 
    elif num_dice==2:
        for i in range (1,sides+1):
            for j in range (1,sides+1): 
                if(i+j>=desired_number):         # 2 dice: compare the sum of the two sides 
                    probability+=1/num_outcome   #if the sum is greater than the number, increment the prob 
    elif num_dice==3:
        for i in range (1,sides+1):
            for j in range (1,sides+1): 
                for k in range(1,sides+1):
                        if(i+j+k>=desired_number):            #3 dice case:  compare the sum of the 3 sides
                            probability+=1/num_outcome         #if the sum is greater than the number, increment the prob 
    elif num_dice==4:
        for i in range (1,sides+1):
            for j in range (1,sides+1): 
                for k in range(1,sides+1):
                    for l in range(1,sides+1):
                        if(i+j+k+l>=desired_number):            #same as previous cases , if the sum of 4sides>number: increment
                                    probability+=1/num_outcome
    else:
        return ValueError("the maximum possible number of dice is 4, enter a number between 1 and 4")   #if the number of dice is more than 4 , raise an exception
    

    return round(probability,2)       #return the probability rounded to 2 decimals


#test function
    
dice_config=input("please enter the dice configuration as a string example: 1d6 , 1 number of dice, 6 is number of sides:\n")
desired_num=int(input("enter the number you want to calculate it's prob: "))
print("the probabillity is: ",dice_roll(dice_config,desired_num))



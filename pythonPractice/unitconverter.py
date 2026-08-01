# Ask the User about the Unit then convert it 

flag_input = True

print("""
What you want to convert select the options
1. kM -> miles
2. miles-> KM
3. Celsius -> Fahrenheit 
4. Fahrenheit -> Celsius 


""")



def km_to_miles(input_km):
    output_miles = round(input_km*0.62137,2)
    print(f"Your Journey in Miles : {output_miles} Miles")


def miles_to_km(input_miles):
    output_km = round(input_miles/0.62137,2)
    print(f"Your Journey in KiloMeter : {output_km} KM ")

def celsius_to_fahrenheit(input_celsius):
    output_fahrenheit = round(((input_celsius*1.8)+32),2)
    print(f" Temperature is  : {output_fahrenheit: .2f}\u00b0F  ")

def fahrenheit_to_celsius(input_fahrenheit):
    output_celsius = round(((input_fahrenheit-32)/1.8),2)
    print(f" Temperature is  : {output_celsius: .2f}\u00b0C")
     
     

def reject_or_not(input_action ):
    if(input_action.upper() == 'N'):
         return False
    else:
         return True
      



while(flag_input):
    try:
        user_input = int(input("Provide the Input which you want : "))
    except ValueError:
        print("Please Select Numerical values ")
        continue


    if(user_input==1 or user_input == 2 or user_input == 3 or user_input == 4):
        if user_input == 1:
            print("You select KM -> Miles")
            # take user input for KM 
            input_km = float(input("Provide your KM journey : "))
            km_to_miles(input_km=input_km)
            # Asking User To perform more actions 

            print("Do you want to perform more actions : [Y/N]")
            
            more_action_input = str(input("Provide your input :--> "))

            flag_input  = reject_or_not(input_action = more_action_input)

        elif user_input == 2:
                print("You select Miles -> KM")
                # take user input for KM 
                input_miles = float(input("Provide your miles journey : "))
                miles_to_km(input_miles = input_miles)
                

            # Asking User To perform more actions 
    
                print("Do you want to perform more actions : [Y/N]")
                
                more_action_input = str(input("Provide your input :--> "))

                flag_input  = reject_or_not(input_action = more_action_input)
            

        elif user_input == 3:
                print("You select Celsius to Fahrenheit")
                # take user input for KM 
                input_celsius = float(input("Provide your celsius : "))
                celsius_to_fahrenheit(input_celsius)

                # Asking User To perform more actions 
    
                print("Do you want to perform more actions : [Y/N]")
                
                more_action_input = str(input("Provide your input :--> "))
                flag_input  = reject_or_not(input_action = more_action_input)

        elif user_input == 4:
                print("You select Fahrenheit to Celsius")
                # take user input for KM 
                input_fahrenheit = float(input("Provide your celsius : "))
                fahrenheit_to_celsius(input_fahrenheit)

                # Asking User To perform more actions 
        
                print("Do you want to perform more actions : [Y/N]")
                
                more_action_input = str(input("Provide your input :--> "))
                flag_input  = reject_or_not(input_action = more_action_input)
                
    else:
        print("Please Select Input Integer b/w 1 to 4 only as per dropdown")






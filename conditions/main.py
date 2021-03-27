# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather,time,needs_milking,location,season,tank_is_full,grass_is_long):
    action = ""
   
    if (time == "night" or weather == "rainy") and location == "pasture":
        action = "take cows to cowshed"        
    elif needs_milking:
        if location == "cowshed":
            action = "milk cows"
        elif location == "pasture":
            action = "take cows to cowshed\nmilk cows\ntake cows back to pasture"
        else: action = "wait"
    elif tank_is_full and  weather != "sunny" and weather != "windy":
        if location != "pasture":
            action += "fertilize pasture"
        else: action = "take cows to cowshed\nfertilize pasture\ntake cows back to pasture"
    elif grass_is_long and season == "spring" and weather == "sunny":
        if location != "pasture":
            action = "mow grass"
        else: action = "take cows to cowshed\nmow grass\ntake cows back to pasture"
    else: action = "wait"
    
    return action


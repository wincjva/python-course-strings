# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

gullit = "Ruud Gullit"
basten = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = gullit + " " + str(goal_0)+", "+basten + " " + str(goal_1)
report = f"""{gullit} scored in the {goal_0}nd minute
{basten} scored in the {goal_1}th minute"""

player = "Berry van Aerle" # PSV 
first_name = player[:player.find(" ")]
last_name_len = len(player)-player.find(" ")-1
last_name = player[-last_name_len:]
name_short = first_name[:1]+". "+last_name
chant = first_name+"!"+(" "+first_name+"!")*(len(first_name)-1) #lekker voor de sfeer
good_chant = chant[len(chant)-1] != " "
# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

spain_language = "Castilian Spanish"
switzerland_language = "German"
print(spain_language == switzerland_language) # Is the language spoken the most in Switzerland the same as in Spain?

spain_religion = "Roman Catholic"
switzerland_religion = "Roman Catholic"
print(spain_religion == switzerland_religion) # Is the most prevalent religion in Switzerland the same as in Spain?

spain_capital_name_length = len("Madrid")
switzerland_capital_name_length = len("Bern")
print(spain_capital_name_length != switzerland_capital_name_length) # Does the name length of Spain's capital not equal that of Switzerland?

spain_gdp = 1.778 #trillion USD
switzerland_gdp = 0.580 #trillion USD
print(switzerland_gdp > spain_gdp) # Is Switzerland's GDP greater than Spain's GDP?

spain_population_growth = 0.67 # percent
switzerland_population_growth = 0.66 # percent
print((spain_population_growth < 1) & (switzerland_population_growth < 1)) # Is the population growth less than 1% in Switzerland and Spain?

spain_population = 50.0 #million
switzerland_population = 8.4 #million
print((spain_population > 10) | (switzerland_population > 10)) # Does at least one of the two countries have a population count of over 10 million?
print((spain_population > 10) != (switzerland_population > 10)) # Does exactly one of the two countries have a population count of over 10 million?

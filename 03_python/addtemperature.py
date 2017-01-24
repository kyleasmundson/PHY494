# temperature difference in Fahrenheit

T = int(input("First Temperature (in Kelvin) --> "))
deltheta = int(input("Difference (in Fahrenheit) to the second temperature --> "))

T2F = (((T - 32) * (5/9) + 273.15) - deltheta)

T2K = ((T2F - 32) * (5/9) + 273.15)

SUM = (T + T2K)

print("The second temperature (in Kelvin) is  ", (T2K))

print("The sum of the two temperatures (in Kelvin) is ", (SUM))

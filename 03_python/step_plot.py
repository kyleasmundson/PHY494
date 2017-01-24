# Heaviside step function

numbers = [-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4]
   for x in numbers:
       def heaviside(x):
       """Heaviside step function"""

   	theta = None
       if x < 0:
          theta = 0.
       elif x == 0:
          theta = 0.5
       else:

       return theta

theta = heaviside(x)

print(theta)

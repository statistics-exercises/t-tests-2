import matplotlib.pyplot as plt
import numpy as np

def gen_t_variable( n ) : 
  # Your code to generate the random variable described in the text goes here
 
  
# This code generates a 100 random variables using your function above and 
# plots them on a graph
xvals, yvals = np.linspace(0,100,100), np.zeros(100)
for i in range(100) : yvals[i] = gen_t_variable(5)

plt.plot( xvals, yvals, 'ko')
plt.savefig("variables.png")

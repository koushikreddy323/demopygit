#TO KNOW THE SPEED OF THE CODE WE USE THESE MODULES

import timeit
statement='''
mod1(10)
'''
setup='''
def mod1(n):
  return(str(num) for num in range(n))
'''
print(timeit.timeit(statement,setup,number=10000))

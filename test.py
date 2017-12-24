"""
@author: MPatel

"""

import calculator as c

add_1 = c.calculator()
print ('Addition is:', add_1.addition(1,2,3))


nums = [10,20,30]
add_2 = c.calculator()
print ('Addition is:', add_2.addition(*nums))
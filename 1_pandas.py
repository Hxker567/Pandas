#Creating Series

import pandas as pd
L = [1,2,3,4,5]
S = pd.Series(L)
#print(S)

#Empty Series - (No Element)
#By defalt data type is floaT
L = ['H','E','L','L','O']
S = pd.Series(L)
#print(S)

#Scalar Value
import pandas as pd
S = pd.Series (98, index = (0,1,2,3))
#print(S)

#Dictionary
#Note - {Key:Value}
#       {index:Data}
import pandas as pd
S= pd.Series ({'INDIA' : 'DELHI', 'USA' : 'WASHINGTON', 'PAKISTAN' : 'ISLAMABAD'})
#print(S)

#Mathematical function
#like - +,-,*,/,                //                        ,                                       %    
#                        floor division                                                        modulus 
#                 (integer part of the quotient)                                             (remainder)
#For ex-   (2 is divided by 5 the quotient is 2.5 the integer part is 2)     (2 is divided by 5 the remainder of division is 'Modulus')

S = pd.Series (1 , index = (0,1,2,3))
#print(S)

#Numpy array
import pandas as pd
import numpy as np
A1 = np.array([50,60,70])
S = pd.Series(A1)
#print(S)

#NaN = Not a No.
L = ('Jatin','Neha','NaN')
S = pd.Series(L)
#print(S)


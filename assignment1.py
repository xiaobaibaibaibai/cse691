import numpy as np
import time

# - Fill in the code below the comment Python and NumPy same as in example.
# - Follow instructions in document.
###################################################################
# Example: Create a zeros vector of size 10 and store variable tmp.
# Python
pythonStartTime = time.time()
# tmp_1 = [0 for i in range(10)]


# NumPy
numPyStartTime = time.time()
# tmp_2 = np.zeros(10)


'''
z_1 = None
z_2 = None
################################################################
# 1. Create a zeros array of size (3,5) and store in variable z.
# Python
z_1 = [[0]*5]*3
# NumPy
z_2 = np.zeros((3, 5), dtype= np.int)

#################################################
# 2. Set all the elements in first row of z to 7.
# Python
z_1[0] = [7]*len(z_1[0])
# NumPy
z_2[:1,] = [7, 7, 7, 7, 7]

#####################################################
# 3. Set all the elements in second column of z to 9.
# Python
for i in range(len(z_1)):
    z_1[i][1] = 9
# NumPy
z_2[:,1:2] = 9

#############################################################
# 4. Set the element at (second row, third column) of z to 5.
# Python
z_1[1][2] = 5
# NumPy
z_2[1, 2] = 5

##############
print(z_1)
print(z_2)
##############


x_1 = None
x_2 = None
##########################################################################################
# 5. Create a vector of size 50 with values ranging from 50 to 99 and store in variable x.
# Python
x_1 = []
for i in range(50, 100):
    x_1.append(i);
# NumPy
x_2 = np.arange(50, 100)

##############
print(x_1)
print(x_2)
##############
'''

y_1 = None
y_2 = None
##################################################################################
# 6. Create a 4x4 matrix with values ranging from 0 to 15 and store in variable y.
# Python

# NumPy
y_2 = np.arange(16).reshape(4,4)

##############
print(y_1)
print(y_2)
pythonEndTime = time.time()
numPyEndTime = time.time()
print('Python time: {0} sec.'.format(pythonEndTime-pythonStartTime))
print('NumPy  time: {0} sec.'.format(numPyEndTime-numPyStartTime))
##############

'''
tmp_1 = None
tmp_2 = None
####################################################################################
# 7. Create a 5x5 array with 1 on the border and 0 inside amd store in variable tmp.
# Python

# NumPy


##############
print(tmp_1)
print(tmp_2)
##############


a_1 = None; a_2 = None
b_1 = None; b_2 = None
c_1 = None; c_2 = None
#############################################################################################
# 8. Generate a 50x100 array of integer between 0 and 5,000 and store in variable a.
# Python

# NumPy


###############################################################################################
# 9. Generate a 100x200 array of integer between 0 and 20,000 and store in variable b.
# Python

# NumPy


#####################################################################################
# 10. Multiply matrix a and b together (real matrix product) and store to variable c.
# Python

# NumPy


d_1 = None; d_2 = None
################################################################################
# 11. Normalize a 3x3 random matrix ((x-min)/(max-min)) and store to variable d.
# Python

# NumPy


##########
print(d_1)
print(d_2)
#########


################################################
# 12. Subtract the mean of each row of matrix a.
# Python

# NumPy


###################################################
# 13. Subtract the mean of each column of matrix b.
# Python

# NumPy


################
print(np.sum(a_1 == a_2))
print(np.sum(b_1 == b_2))
################

e_1 = None; e_2 = None
###################################################################################
# 14. Transpose matrix c, add 5 to all elements in matrix, and store to variable e.
# Python

# NumPy


##################
print (np.sum(e_1 == e_2))
##################


#####################################################################################
# 15. Reshape matrix e to 1d array, store to variable f, and print shape of f matrix.
# Python

# NumPy
'''
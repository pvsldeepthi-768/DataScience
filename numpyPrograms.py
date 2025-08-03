import numpy as np
#create an array with tuple or list
a= np.array([(1, 2, 3), (4, 5, 6)])
print("normal array :\n",a) 
#creating an array filled with zeroes
a= np.zeros((2, 3))
print("array filled with zeroes\n :",a)
#creating an array filled with ones
a= np.ones((2, 3))  
print("array filled with ones :\n",a)
#creating an array filled with a constant value
a= np.full((2, 3), 7)
print("array filled with constant value 7 :\n",a)
#creating an identity matrix
a=np.eye(3)
print("identity matrix :\n",a)
#creating an array of range of values
a=np.arange(0, 10, 2)
print("array of range of values from 0 to 10 with step 2 :",a)
#creating an array of evenly spaced values
a=np.linspace(0, 1, 5)      
print("array of evenly spaced values from 0 to 1 with 5 points :",a)
#random floats between 0 and 1
a=np.random.random((2, 3))
print("random floats between 0 and 1 :\n",a)
a= np.random.rand(2, 3)
print("random floats between 0 and 1 :\n",a)
#random floats from standard normal distribution
a=np.random.randn(2, 3)
print("random floats from standard normal distribution :\n",a)
#random integers within a specified range
a=np.random.randint(0, 10, (2, 3))
print("random integers between 0 and 10 :\n",a)
#create uninitialized array
b=np.empty((2, 3))      
print("uninitialized array :\n",b)
#copy an array
c=np.copy(a)
print("copy of the array a in c:\n",c)
#shape of an array 
print("shape of an array:",a.shape)
#ndimensions of an array 
print("number of dimensions of an array:",a.ndim)
#data type of an array
print("data type of an array:",a.dtype)
#Total no of elements in an array
print("no. of elements in an array:",a.size)
#Total no.of bytes consumed by an element of an array
print("itemsize of an array:",a.itemsize)
#Total no.of bytes consumed by the array
print("toatal bytes consumed by the array a:",a.nbytes)
#reshaping an array
b = a.reshape(3, 2)
print("reshaped array:\n", b)
#flattening an array
c = a.flatten()
print("flattened array:\n", c)
#review the flattened array
d=np.ravel(a)
print("review the flattened array:\n",d)
#transposing an array
print("transposed array:\n", a.T)
#print the array in transpose form
print("transposed array using transpose function:\n", np.transpose(a))
#expanding dimensions of an array
e = np.expand_dims(a, axis=1)
print("array after expanding dimensions:\n", e)
#reducing dimwnsions by 1d
b = np.squeeze()
print("Array after reducing dimensions:\n", b)
#swap axes of an array

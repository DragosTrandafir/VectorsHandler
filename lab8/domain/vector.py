import numpy as np
import math
class MyVector:

    colours=["r","g","b","y","m"]

    '''
    Descr: contains the initial, string representation, setters, getters
    and different functions and features for a vector
    '''

    def __init__(self, name_id="0", colour="r", type=1, values=[1,2]):
        '''
        Descr: initializes the attributes of a vector in the class
        Precondition: name_id,colour-strings, type-number, values-array of numbers
        Input: (self),name_id, colour, type, values
        '''
        if len(name_id)<1:
            raise ValueError("Input an available name_id!")
        else:
            self.__nameId=name_id
        if self.available_colour(colour):
            self.__colour=colour
        else:
            raise ValueError("The color is not available!")
        if type<1:
            raise ValueError("Not a possible value for type!")
        else:
            self.__type=type
        if len(values) < 2:
            raise ValueError("Add at least 2 values!")
        self.__values = values

    '''
    Descr: each getter function returns an attribute of a vector predefined in the class
    Input: the class itself
    Output: name_id, colour, type, values- accessed through the corresponding initial value defined in the class for each function
    '''
    def get_nameId(self):
        return self.__nameId
    def get_colour(self):
        return self.__colour
    def get_type(self):
        return self.__type
    def get_values(self):
        return self.__values

    '''
    Descr: each setter function changes a specific attribute of a vector, predefined variables in the class, with new 
    values
    Precondition: name_id,colour-strings, type-number, values-array of numbers
    Input: name_id,colour, type, values - the new values
    Output: name_id,colour, type, values - accessed through the corresponding initial value defined in the 
    class for each function and modified with the new value
    '''
    def set_nameId(self,name_id="0"):
        if len(name_id)<1:
            raise ValueError("Input an available name_id!")
        self.__nameId=name_id
    def set_colour(self,colour=""):
        if self.available_colour(colour):
            self.__colour=colour
        else:
            raise ValueError("Not an available colour!")
    def set_type(self,type):
        if type<1:
            raise ValueError("Not a possible value for type!")
        else:
            self.__type=type
    def set_values(self,values):
        if len(values)<2:
            raise ValueError("Add at least 2 values!")
        self.__values=values


    # checking if a colour is available
    def available_colour(self,colour):
        '''
        Descr: checks if the color of a vector is in our predefined list of available colors in the class
        Input: the class itself
        Output: True or False
        '''
        for elem in self.colours:
            if elem == colour:
                return True
        return False

    def read_vector_domain(self):
        '''
        Descr: reads values for the class attributes
        Precondition: name_id,colour-strings, type-number, values-array of numbers, n-positive integer
        Input: the class itself
        Output: the class attributes modified with the read values
        '''
        name_id=input("Name id: ")
        colour=input("Colour: ")
        type=int(input("Type: "))
        values=[]
        n=int(input("Values list length: "))
        for i in range (0,n):
            value=int(input("Value "+str(i+1)+" "))
            values.append(value)
        self.set_nameId(name_id)
        self.set_colour(colour)
        self.set_type(type)
        self.set_values(values)

    def __str__(self):
        '''
        Descr: string representation of a point
        Input: the class itself
        Output: the required string representation of a point in the lab assignment
        '''
        return "Vector with name_id=" + self.__nameId +", colour "+ self.__colour+", type "+str(self.__type)+", values "+str(self.__values)

    #length on a vector
    def length_vector(self):
        '''
        Descr: gets the length of the vector in the class
        Input: the class itself
        Output: the length
        '''
        length=0
        for elem in self.__values:
            length+=elem*elem
        return math.sqrt(length)

    #1. Scalar operations:
    #a. Add the scalar to each element in the values
    def add_scalar(self,j):
        '''
        Descr: adds a scalar to each value in the values attribute
        Input: the class itself, the scalar j
        Output: the vector modified with the new values list
        '''
        array_from_list=np.array(self.__values)
        array_from_list+=j
        self.set_values(array_from_list.tolist())

    #2. Vector operations
    #a. Add two vectors
    def __add__(self,other):
        '''
        Descr: adds two vectors
        Input: two classes of type MyVector
        Output: the values attribute addition corresponding to the classes
        '''
        if len(self.__values)!=len(other.__values):
            return "Not a possible operation"
        else:
            array_from_list1 = np.array(self.__values)
            array_from_list2 = np.array(other.__values)
            new_array=array_from_list1+array_from_list2
            return new_array.tolist()

    #b. Substraction of two vectors
    def __sub__(self,other):
        '''
        Descr: substracts two vectors
        Input: two classes of type MyVector
        Output: the values attribute substraction corresponding to the classes
        '''
        if len(self.__values)!=len(other.__values):
            return "Not a possible operation"
        else:
            array_from_list1 = np.array(self.__values)
            array_from_list2 = np.array(other.__values)
            new_array = array_from_list1 - array_from_list2
            return new_array.tolist()
    #c. Multiplication
    def __mul__(self,other):
        '''
        Descr: multiplies two vectors
        Input: two classes of type MyVector
        Output: the values attribute multiplication corresponding to the classes
        '''
        if len(self.__values)!=len(other.__values):
            return "Not a possible operation"
        else:
            array_from_list1 = np.array(self.__values)
            array_from_list2 = np.array(other.__values)
            new_array = array_from_list1 * array_from_list2
            sum=np.sum(new_array)
            return sum

    #3. Reduction operations
    #a. sum of all elements in a vector
    def sum_elements(self):
        '''
        Descr: sums the values in the values attribute of a vector
        Input: the class itself
        Output: sum
        '''
        array_from_list = np.array(self.__values)
        sum=np.sum(array_from_list)
        return sum

    #b. Product of elements in a vector
    def product_elements(self):
        '''
        Descr: gets the product of the values in the values attribute of a vector
        Input: the class itself
        Output: product
        '''
        array_from_list = np.array(self.__values)
        product = np.prod(array_from_list)
        return product

    #c. Average of elements in a vector
    def avg_elements(self):
        '''
        Descr: gets the average of the values in the values attribute of a vector
        Input: the class itself
        Output: avg
        '''
        array_from_list = np.array(self.__values)
        avg = np.mean(array_from_list)
        return avg

    #d. Minimum of a vector
    def min_elements(self):
        '''
        Descr: gets the minimum of the values in the values attribute of a vector
        Input: the class itself
        Output: minn
        '''
        array_from_list = np.array(self.__values)
        minn = np.min(array_from_list)
        return minn

    #e. Maximum of a vector
    def max_elements(self):
        '''
        Descr: gets the maximum of the values in the values attribute of a vector
        Input: the class itself
        Output: max
        '''
        array_from_list = np.array(self.__values)
        max = np.max(array_from_list)
        return max


'''
#10 examples 

s1=MyVector("Vector1","r",1,[3,4])
s2=MyVector("Vector2","g",2,[1,2,3])
s3=MyVector("Vector3","b",3,[3,4,88])
s4=MyVector("Vector4","y",4,[0])
s5=MyVector("Vector5","m",5,[2,4,5])
s6=MyVector("Vector6","nocolor",6,[11,222,333,1,2,4])
s7=MyVector("Vector7","r",2,[99,2,4,1,2])
s8=MyVector("Vector8","g",4,[9,3,2,5,66,77])
s9=MyVector("Vector9","b",1,[3])
s10=MyVector("Vector10","y",1,[29292,38392,2828])

print(str(s1))
print(str(s2))
print(str(s3))
print(str(s4))
print(str(s5))
#print(str(s6)) #we get an error, because the color is not available!
print(str(s7))
print(str(s8))
print(str(s9))
print(str(s10))
'''



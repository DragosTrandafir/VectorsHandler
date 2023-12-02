

class MyVector:

    colours=["r","g","b","y","m"]

    def __init__(self, name_id="0", colour="", type=1, values=[]):
        self.__nameId=name_id
        self.__colour=colour
        if type<1:
            raise ValueError("Not a possible value for type!")
        else:
            self.__type=type
        self.__values=values


    def get_nameId(self):
        return self.__nameId
    def get_colour(self):
        return self.__colour
    def get_type(self):
        return self.__type
    def get_values(self):
        return self.__values

    def set_nameId(self,name_id="0"):
        self.__nameId=name_id
    def set_colour(self,colour=""):
        self.__colour=colour
    def set_type(self,type):
        self.__type=type
    def set_values(self,values):
        self.__values=values

    # checking if a colour is available
    def available_colour(self):
        for elem in self.colours:
            if elem == self.__colour:
                return True
        return False

    def read_vector_domain(self):
        name_id=input("Name id: ")
        colour=input("Colour: ")
        type=int(input("Type: "))
        values=[]
        n=int(input("Values list length: "))
        for i in range (0,n):
            value=int(input("Value "+str(i+1)+" "))
            values.append(value)
        self.__nameId=name_id
        self.__colour=colour
        self.__type=type
        self.__values=values

    def __str__(self):
        if self.available_colour():
            return "Vector with id=" + self.__nameId +", colour "+ self.__colour+", type "+str(self.__type)+", values "+str(self.__values)
        else:
            raise ValueError("Not an available colour!")

    #1. Scalar operations:
    #a. Add the scalar to each element in the values
    def add_scalar(self,j):
        for elem in self.__values:
            elem+=j

    #2. Vector operations
    #a. Add two vectors
    def __add__(self,other):
        if len(self.__values)!=len(other.__values):
            return "Not a possible operation"
        else:
            new_vector = []
            for i in range(0, len(self.__values)):
                new_vector.append(self.__values[i] + other.__values[i])
            return new_vector
    #b. Substraction of two vectors
    def __sub__(self,other):
        if len(self.__values)!=len(other.__values):
            return "Not a possible operation"
        else:
            new_vector=[]
            for i in range(0,len(self.__values)):
                new_vector.append(self.__values[i]-other.__values[i])
            return new_vector
    #c. Multiplication
    def __mul__(self,other):
        if len(self.__values)!=len(other.__values):
            return "Not a possible operation"
        else:
            s=0
            for i in range(0,len(self.__values)):
                s+=self.__values[i]*other.__values[i]
            return s
    #3. Reduction operations
    #a. sum of all elements in a vector
    def sum_elements(self):
        s=0
        for elem in self.__values:
            s+=elem
        return s
    #b. Product of elements in a vector
    def product_elements(self):
        p=1
        for elem in self.__values:
            p*=elem
        return p
    #c. Average of elements in a vector
    def avg_elements(self):
        return self.sum_elements()//len(self.__values)
    #d. Minimum of a vector
    def min_elements(self):
        minn=self.__values[0]
        for i in range(1,len(self.__values)):
            if self.__values[i]<minn:
                minn=self.__values[i]
        return minn
    #e. Maximum of a vector
    def max_elements(self):
        maxx=self.__values[0]
        for i in range(1,len(self.__values)):
            if self.__values[i]>maxx:
                maxx=self.__values[i]
        return maxx

'''
s=MyVector("Vector1","r",1,[1,2,3])
print(str(s))
print(s.sum_elements())
print(s.product_elements())
print(s.avg_elements())
print(s.min_elements())
print(s.max_elements())

s2=MyVector("Vector1","b",1,[33,2,3])
s3=s+s2
print(str(s3))
s4=s-s2
print(str(s4))
s5=s*s2
print(str(s5))
s=MyVector("Vector1","b",1,[1,2,3])
print(str(s))
assert s.add_scalar(2)==print([3, 4, 5]))

print(s.sum_elements())
print(str(s)+'\n')
'''



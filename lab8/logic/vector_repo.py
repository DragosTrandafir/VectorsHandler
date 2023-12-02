import sys
sys.path.append(r"D:\lab8")
from domain.vector import MyVector
import matplotlib.pyplot as plt



class VectorRepository:
    # Descr: contains the container with all the vectors
    #GENERAL REMARK: all the vectors in the repository must have a unique id_name!

    def __init__(self):
        # Descr: initializes the container in the class with an empty array
        self.__vl = []

    '''
    Descr: the getter function and setter function return, respectively change the repository container at 
    a specific moment
    Input: the class itself
    Output: the container itself(in getter), respectively the container changed(in setter)
    '''
    def getList(self):
        return self.__vl
    def setList(self,vl):
        self.__vl=vl


    # 2. Get all vectors
    def __str__(self):
        # the string representation of the container
        s = ""
        for i in range(0, len(self.__vl)):
            s += str(self.__vl[i]) + "\n"
        return s

    def readVectorRepo(self):
        '''
        Descr: imports the read_vector_domain() function, so as to maintain a layered arhitecture
        Input: the class itself
        Output: the vector read in the class MyVector
        '''
        vector = MyVector()
        vector.read_vector_domain()
        return vector

    #1. Add a vector to the repository
    def add_vector(self,vector):
        '''
        Descr: adds a vector to the repository (if the conditions similar to the ones in the constructor
        of MyVector class are fulfilled)
        Precondition: vector is of type MyVector
        Input: (self),vector of type MyVector
        Output: our self.__vl(modified)
        '''
        if (vector.available_colour(vector.get_colour()) and len(vector.get_values())>1
                and vector.get_type()>=1 and len(vector.get_nameId())>=1):
            self.__vl.append(vector)
        else:
            raise ValueError("Not an available vector!")


    #3. Get a vector at a given index
    def vector_at_index(self,index):
        '''
        Descr: gets the string repr of the vector at a certain index in the repository
        Precondition: index-number
        Input: (self),index
        Output: the requested vector
        '''
        if index<0 or index>len(self.__vl):
            return "Choose an available index!"
        return str(self.__vl[index])

    #4. Update a vector at a given index
    def update_vector_at_index(self,index,vector):
        '''
        Descr: updates a vector at given index
        Precondition: index-number, vector - of type MyVector
        Input: (self),index, vector
        Output: our self.__vl(modified)
        '''
        if index<0 or index>len(self.__vl):
            return "Choose an available index!"
        self.__vl[index]=vector

    #(auxiliary function) Get index of a vector by name_id
    def get_index_by_name_id(self,name_id):
            '''
            Descr: gets the corresponding index of a name_id
            Precondition: name_id - string
            Input: (self),name_id
            Output: index or -1, if there is no such name_id
            '''
            for i in range(0,len(self.__vl)):
                if self.__vl[i].get_nameId()==name_id:
                    return i
            return -1

    # 5. Update a vector by name_id
    def update_vector_at_name_id(self, name_id, colour, type, values):
        '''
        Descr: updates a vector at given name_id
        Precondition: name_id,colour-strings, type-number, values-array of numbers
        Input: (self),name_id, colour, type, values
        Output: our self.__vl(modified)
        '''
        index=self.get_index_by_name_id(name_id)
        if index==-1:
            raise ValueError("No such name_id in the repository!")
        self.__vl[index].set_colour(colour)
        self.__vl[index].set_type(type)
        self.__vl[index].set_values(values)

    #6. Delete a vector by index
    def delete_vector_at_index(self, index):
        '''
        Descr: deletes a vector at given index
        Precondition: index-number
        Input: (self),index
        Output: our self.__vl(modified)
        '''
        if index<0 or index>len(self.__vl):
            raise ValueError("Choose an available index!")
        del self.__vl[index]

    #7. Delete a vector by name_id
    def delete_vector_at_name_id(self, name_id):
        '''
        Descr: deletes a vector at given name_id
        Precondition: name_id-string
        Input: (self),name_id
        Output: our self.__vl(modified)
        '''
        index=self.get_index_by_name_id(name_id)
        if index==-1:
            raise ValueError("No such name_id in the repository!")
        self.delete_vector_at_index(index)


    #8. Plot all vectors in a chart
    def plot_vectors(self):
        '''
        Descr: plots all vectors in a chart, based on their type and colour
        Input: class itself
        Output: the chart
        '''
        fig, ax = plt.subplots()
        for vector in self.__vl:
            values=vector.get_values()
            x,y=values[:2]
            vector_type = vector.get_type()
            color= vector.get_colour()
            if vector_type == 1:
                marker = 'o'  # Circle
            elif vector_type == 2:
                marker = 's'  # Square
            elif vector_type == 3:
                marker = '^'  # Triangle
            else:
                marker = 'D'  # Diamond

            ax.scatter(x, y, marker=marker, color=color, s=50)  # s is the marker size

        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Vector Plot')
        plt.show()

    # 9.Get the min of all vectors
    def smallest_vector(self):
        '''
        Descr: gets the smallest vector in the repository
        Precondition: the repository should be non-empty
        Input: class itself
        Output: our self.__vl(modified)
        '''
        # it will get the first if 2 are equal
        minlength=self.__vl[0].length_vector()
        vector=self.__vl[0]
        for i in range(1,len(self.__vl)):
            if self.__vl[i].length_vector()<minlength:
                minlength = self.__vl[i].length_vector()
                vector = self.__vl[i]
        return vector

    # 10. Delete all vectors between 2 given indexes
    def del_between_indexes(self,index1,index2):
        '''
        Descr: deletes the vectors between 2 vectors (the vectors at indexes are included)
        Precondition: the repository should be non-empty, index1, index2 - numbers
        Input: class itself, index1, index2
        Output: our self.__vl(modified)
        '''
        if index1<0 or index1>len(self.__vl) or index2<0 or index2>len(self.__vl) or index1>index2:
            raise ValueError("Choose available indexes!")
        del self.__vl[index1:index2+1]

    # 11. Add a scalar to each element
    def add_scalar_repo(self,scalar):
        '''
        Descr: adds a scalar to all the numbers in the values attribute of each vector
        Precondition: scalar - number
        Input: class itself, scalar
        Output: our self.__vl(modified)
        '''
        for elem in self.__vl:
            elem.add_scalar(scalar)



s1=MyVector("Vector1","r",1,[3,4])
s2=MyVector("Vector2","g",2,[1,2,3])
s3=MyVector("Vector3","b",3,[3,4,88])
s4=MyVector("Vector4","y",4,[0,21])
s5=MyVector("Vector5","m",5,[2,4,5])
#s6=MyVector("Vector6","nocolor",6,[11,222,333,1,2,4])
s7=MyVector("Vector7","r",2,[99,2,4,1,2])
s8=MyVector("Vector8","g",4,[9,3,2,5,66,77])
s9=MyVector("Vector9","b",1,[3,33])
s10=MyVector("Vector10","y",1,[292,382,28])



#example 1
vectorRepoInitial=VectorRepository()
vectorRepoInitial.add_vector(s1)
vectorRepoInitial.add_vector(s2)
vectorRepoInitial.add_vector(s3)
vectorRepoInitial.add_vector(s4)
vectorRepoInitial.add_vector(s5)
#vectorRepoInitial.add_vector(s6) #the color is not available, so we get an error
vectorRepoInitial.add_vector(s7)
vectorRepoInitial.add_vector(s8)
vectorRepoInitial.add_vector(s9)
vectorRepoInitial.add_vector(s10)

'''
#example 2
vectorRepoInitial=VectorRepository()
vectorRepoInitial.add_vector(s1)
vectorRepoInitial.add_vector(s2)

#example 3
vectorRepoInitial=VectorRepository()
vectorRepoInitial.add_vector(s1)
vectorRepoInitial.add_vector(s9)
vectorRepoInitial.add_vector(s10)

#example 4
vectorRepoInitial=VectorRepository()
vectorRepoInitial.add_vector(s2)
vectorRepoInitial.add_vector(s9)
vectorRepoInitial.add_vector(s10)

#example 5
vectorRepoInitial=VectorRepository()
vectorRepoInitial.add_vector(s3)
vectorRepoInitial.add_vector(s7)
vectorRepoInitial.add_vector(s10)

#example 6
vectorRepoInitial=VectorRepository()
vectorRepoInitial.add_vector(s2)
vectorRepoInitial.add_vector(s3)
vectorRepoInitial.add_vector(s4)

#example 7
vectorRepoInitial=VectorRepository()
vectorRepoInitial.add_vector(s7)
vectorRepoInitial.add_vector(s2)
vectorRepoInitial.add_vector(s3)
vectorRepoInitial.add_vector(s8)
vectorRepoInitial.add_vector(s5)

#example 8
vectorRepoInitial=VectorRepository()
vectorRepoInitial.add_vector(s8)
vectorRepoInitial.add_vector(s2)
vectorRepoInitial.add_vector(s9)
vectorRepoInitial.add_vector(s4)
vectorRepoInitial.add_vector(s10)

#example 9
vectorRepoInitial=VectorRepository()
vectorRepoInitial.add_vector(s5)
vectorRepoInitial.add_vector(s2)
vectorRepoInitial.add_vector(s9)
vectorRepoInitial.add_vector(s4)
vectorRepoInitial.add_vector(s10)

#example 10
vectorRepoInitial=VectorRepository()
vectorRepoInitial.add_vector(s1)
vectorRepoInitial.add_vector(s2)
vectorRepoInitial.add_vector(s4)
vectorRepoInitial.add_vector(s5)
#vectorRepoInitial.add_vector(s6) #the color is not available, so we get an error
vectorRepoInitial.add_vector(s7)
vectorRepoInitial.add_vector(s10)
'''


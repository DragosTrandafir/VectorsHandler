import sys
sys.path.append(r"D:\lab8")
from logic.vector_repo import VectorRepository


class VectorUI:
    # Descr: contains all the reading and displaying functions
    def __init__(self,vCtrl):
        self.__vCtrl=vCtrl

    def printMenu(self):
        s="\n\n\nMenu:\n\t1. Add a vector to the repository\n\t2. Get all vectors\n\t3. Get a vector at a given index\n"+ "\t4. Update a vector at a given index\n"+ "\t5. Update a vector by name_id\n"+ "\t6. Delete a vector at index\n"+ "\t7. Delete a vector by name_id\n" + "\t8. Plot all vectors in a chart based on type and colour of each vector(using library matplotlib) (1=circle, 2=square, 3=triangle, diamond-rest)\n" + "\t9.Get the min of all vectors\n"+"\t10.Delete all the vectors between 2 given indexes\n"+"\t11.Add a scalar to each element\n"+"\t0. STOP"
        return s

    def readOption(self):
        option= int(input("Read an option: "))
        return option
    def readIndex(self):
        index= int(input("Read an index: "))
        return index

    def readName_id(self):
        name_id=input("Read a name_id: ")
        return name_id

    def readColour(self):
        colour=input("Read a colour: ")
        return colour

    def readType(self):
        type=int(input("Read a type: "))
        return type

    def readValues(self):
        values=[]
        n=int(input("Values list length: "))
        for i in range (0,n):
            value=int(input("Value "+str(i+1)+" "))
            values.append(value)
        return values
    def readScalar(self):
        scalar= int(input("Read an scalar: "))
        return scalar
    def readVectorConsole(self):
        vector=self.__vCtrl.readVectorRepo()
        return vector



    def start(self):
        start=False
        while start==False:
            print(self.printMenu())
            option=self.readOption()
            if option==1:
                vector=self.readVectorConsole()
                self.__vCtrl.add_vector(vector)
                print(str(self.__vCtrl))
            elif option==2:
                print(str(self.__vCtrl))
            elif option==3:
                index=self.readIndex()
                print(self.__vCtrl.vector_at_index(index))
            elif option==4:
                index=self.readIndex()
                vector = self.readVectorConsole()
                self.__vCtrl.update_vector_at_index(index, vector)
                print(str(self.__vCtrl))
            elif option==5:
                name_id = self.readName_id()
                print("This will be the new vector: "+"\n")
                colour=self.readColour()
                type = self.readType()
                values = self.readValues()
                self.__vCtrl.update_vector_at_name_id(name_id, colour, type, values)
                print(str(self.__vCtrl))
            elif option==6:
                index = self.readIndex()
                self.__vCtrl.delete_vector_at_index(index)
                print(str(self.__vCtrl))
            elif option==7:
                name_id = self.readName_id()
                self.__vCtrl.delete_vector_at_name_id(name_id)
                print(str(self.__vCtrl))
            elif option==8:
                self.__vCtrl.plot_vectors()
            elif option==9:
                vector=self.__vCtrl.smallest_vector()
                print(str(vector))
            elif option==10:
                index1 = self.readIndex()
                index2 = self.readIndex()
                self.__vCtrl.del_between_indexes(index1, index2)
                print(str(self.__vCtrl))
            elif option==11:
                scalar = self.readScalar()
                self.__vCtrl.add_scalar_repo(scalar)
                print(str(self.__vCtrl))
            elif option==0:
                start=True
            else:
                print("The option is not available!")



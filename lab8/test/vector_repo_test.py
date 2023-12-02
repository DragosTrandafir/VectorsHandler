import unittest
from logic.vector_repo import VectorRepository
from domain.vector import MyVector


class VectorRepositoryTest(unittest.TestCase):
    def test_functions(self):

        #1+2 (the function which gets all vectors is tested in the string representation of the vector repository)
        s1 = MyVector("Vector1", "r", 1, [3, 4])
        s2 = MyVector("Vector2", "g", 2, [1, 2, 3])
        vectorRepoInitial = VectorRepository()

        vectorRepoInitial.add_vector(s1)
        self.assertEqual(str(vectorRepoInitial), "Vector with name_id=Vector1, colour r, type 1, values [3, 4]\n")

        vectorRepoInitial.add_vector(s2)
        self.assertEqual(str(vectorRepoInitial), "Vector with name_id=Vector1, colour r, type 1, values [3, 4]\n"
                         + "Vector with name_id=Vector2, colour g, type 2, values [1, 2, 3]\n")

        vector = MyVector("Vector10", "y", 1, [292, 382, 28])
        vectorRepoInitial.add_vector(vector)
        self.assertEqual(str(vectorRepoInitial),"Vector with name_id=Vector1, colour r, type 1, values [3, 4]\n"
                         + "Vector with name_id=Vector2, colour g, type 2, values [1, 2, 3]\n"
                         + "Vector with name_id=Vector10, colour y, type 1, values [292, 382, 28]\n")

        #3
        self.assertEqual(vectorRepoInitial.vector_at_index(0),
                         "Vector with name_id=Vector1, colour r, type 1, values [3, 4]")
        self.assertEqual(vectorRepoInitial.vector_at_index(1),
                         "Vector with name_id=Vector2, colour g, type 2, values [1, 2, 3]")
        self.assertEqual(vectorRepoInitial.vector_at_index(9),
                         "Choose an available index!")

        #4
        vector = MyVector("Vector12", "y", 1, [292, 382, 28])
        vectorRepoInitial.update_vector_at_index(0, vector)
        self.assertEqual(vectorRepoInitial.vector_at_index(0),
                         "Vector with name_id=Vector12, colour y, type 1, values [292, 382, 28]")

        vector = MyVector("Vector13", "y", 1, [292, 382, 28])
        vectorRepoInitial.update_vector_at_index(1, vector)
        self.assertEqual(vectorRepoInitial.vector_at_index(1),
                         "Vector with name_id=Vector13, colour y, type 1, values [292, 382, 28]")

        vector = MyVector("Vector14", "y", 1, [292, 382, 28])
        vectorRepoInitial.update_vector_at_index(-1, vector)
        self.assertEqual(vectorRepoInitial.vector_at_index(-1),
                         "Choose an available index!")

        #5
        vectorRepoInitial.update_vector_at_name_id("Vector13", "m", 3, [2, 22, 222])
        self.assertEqual(vectorRepoInitial.vector_at_index(1),
                         "Vector with name_id=Vector13, colour m, type 3, values [2, 22, 222]")

        vectorRepoInitial.update_vector_at_name_id("Vector10", "m", 3, [2, 22, 222])
        self.assertEqual(vectorRepoInitial.vector_at_index(2),
                         "Vector with name_id=Vector10, colour m, type 3, values [2, 22, 222]")

        try:
            vectorRepoInitial.update_vector_at_name_id("Vector15", "m", 3, [2, 22, 222])
            self.assertTrue(False)
        except:
            self.assertTrue(True)

        #6
        '''#I put this in a comment in order to keep the repository with some elements for the other tests
        vectorRepoInitial.delete_vector_at_index(0)
        self.assertEqual(str(vectorRepoInitial),"Vector with name_id=Vector13, colour m, type 3, values [2, 22, 222]\n"
                         + "Vector with name_id=Vector10, colour m, type 3, values [2, 22, 222]\n")
        vectorRepoInitial.delete_vector_at_index(1)
        self.assertEqual(str(vectorRepoInitial), "Vector with name_id=Vector13, colour m, type 3, values [2, 22, 222]\n")
        
        try:
            vectorRepoInitial.delete_vector_at_index(6)
            self.assertTrue(False)
        except:
            self.assertTrue(True)
        '''
        #7
        '''#I put this in a comment in order to keep the repository with some elements for the other tests
        vectorRepoInitial.delete_vector_at_name_id("Vector12")
        self.assertEqual(str(vectorRepoInitial), "Vector with name_id=Vector13, colour m, type 3, values [2, 22, 222]\n"
                         + "Vector with name_id=Vector10, colour m, type 3, values [2, 22, 222]\n")

        vectorRepoInitial.delete_vector_at_name_id("Vector10")
        self.assertEqual(str(vectorRepoInitial),
                         "Vector with name_id=Vector13, colour m, type 3, values [2, 22, 222]\n")

        try:
            vectorRepoInitial.delete_vector_at_name_id("NoAvailableId")
            self.assertTrue(False)
        except:
            self.assertTrue(True)
        
        '''

        #9
        self.assertEqual(str(vectorRepoInitial.smallest_vector()),"Vector with name_id=Vector13, colour m, type 3, values [2, 22, 222]")

        vector = MyVector("Vector22", "y", 1, [0,1,2])
        vectorRepoInitial.add_vector(vector)
        self.assertEqual(str(vectorRepoInitial.smallest_vector()),
                         "Vector with name_id=Vector22, colour y, type 1, values [0, 1, 2]")

        vector = MyVector("Vector23", "y", 1, [0, 1, 0])
        vectorRepoInitial.add_vector(vector)
        self.assertEqual(str(vectorRepoInitial.smallest_vector()),
                         "Vector with name_id=Vector23, colour y, type 1, values [0, 1, 0]")


        # 10
        vectorRepoInitial.del_between_indexes(0,1)
        self.assertEqual(str(vectorRepoInitial),
                         "Vector with name_id=Vector10, colour m, type 3, values [2, 22, 222]\n"
                         + "Vector with name_id=Vector22, colour y, type 1, values [0, 1, 2]\n"
                         + "Vector with name_id=Vector23, colour y, type 1, values [0, 1, 0]\n")

        try:
            vectorRepoInitial.del_between_indexes(22,33)
            self.assertTrue(False)
        except:
            self.assertTrue(True)

        try:
            vectorRepoInitial.del_between_indexes(2,1)
            self.assertTrue(False)
        except:
            self.assertTrue(True)


        # 11
        vectorRepoInitial.add_scalar_repo(0)
        self.assertEqual(str(vectorRepoInitial),
                         "Vector with name_id=Vector10, colour m, type 3, values [2, 22, 222]\n"
                         + "Vector with name_id=Vector22, colour y, type 1, values [0, 1, 2]\n"
                         + "Vector with name_id=Vector23, colour y, type 1, values [0, 1, 0]\n")

        vectorRepoInitial.add_scalar_repo(2)
        self.assertEqual(str(vectorRepoInitial),
                         "Vector with name_id=Vector10, colour m, type 3, values [4, 24, 224]\n"
                         + "Vector with name_id=Vector22, colour y, type 1, values [2, 3, 4]\n"
                         + "Vector with name_id=Vector23, colour y, type 1, values [2, 3, 2]\n")

        vectorRepoInitial.add_scalar_repo(-1)
        self.assertEqual(str(vectorRepoInitial),
                         "Vector with name_id=Vector10, colour m, type 3, values [3, 23, 223]\n"
                         + "Vector with name_id=Vector22, colour y, type 1, values [1, 2, 3]\n"
                         + "Vector with name_id=Vector23, colour y, type 1, values [1, 2, 1]\n")





if __name__ == '__main__':
    unittest.main()


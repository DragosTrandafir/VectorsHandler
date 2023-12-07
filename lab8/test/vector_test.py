import unittest
from domain.vector import MyVector


class MyVectorTest(unittest.TestCase):
    def test_create(self):
        s3 = MyVector("Vector3", "b", 3, [3, 4, 88])
        self.assertEqual(s3.get_nameId(), "Vector3")
        self.assertEqual(s3.get_colour(),"b")
        self.assertEqual(s3.get_type(), 3)
        self.assertEqual(s3.get_values(), [3, 4, 88])
        s3.set_nameId("vectornew")
        s3.set_colour("m")
        s3.set_type(1)
        s3.set_values([0,1])
        self.assertEqual(s3.get_nameId(), "vectornew")
        self.assertEqual(s3.get_colour(),"m")
        self.assertEqual(s3.get_type(), 1)
        self.assertEqual(s3.get_values(), [0,1])




        s6 = MyVector("Vector6", "r", 6, [11, 222, 333, 1, 2, 4])
        self.assertEqual(s6.get_nameId(), "Vector6")
        self.assertEqual(s6.get_colour(),"r")
        self.assertEqual(s6.get_type(), 6)
        self.assertEqual(s6.get_values(), [11, 222, 333, 1, 2, 4])

        s6.set_nameId("y")
        s6.set_colour("m")
        s6.set_type(1)
        s6.set_values([0,1])

        self.assertEqual(s6.get_colour(),"m")
        self.assertEqual(s6.get_type(), 1)
        self.assertEqual(s6.get_values(), [0,1])
        self.assertEqual(s6.get_nameId(),"y")

        '''
        s3 = MyVector("Vector5", "y", 0, [3, 4, 88])
        self.assertEqual(s3.get_nameId(), "Vector5")
        self.assertEqual(s3.get_colour(),"y")
        self.assertEqual(s3.get_type(), 0) #we get an error, type integer >=1
        self.assertEqual(s3.get_values(), [3, 4, 88])
        '''

        s3 = MyVector("Vector5", "y", 1, [3, 4, 88])
        self.assertEqual(s3.get_nameId(), "Vector5")
        self.assertEqual(s3.get_colour(),"y")
        self.assertEqual(s3.get_type(), 1)
        self.assertEqual(s3.get_values(), [3, 4, 88])
        s3.set_nameId("vectornew")
        s3.set_colour("m")
        s3.set_type(1)
        s3.set_values([1,2])
        s3.set_values([1,0,82])
        self.assertEqual(s3.get_nameId(), "vectornew")
        self.assertEqual(s3.get_colour(),"m")
        self.assertEqual(s3.get_type(), 1)
        self.assertEqual(s3.get_values(), [1,0,82])

        self.assertEqual(str(MyVector("Vector3", "b", 1, [3, 4, 88])),"Vector with name_id=Vector3, colour b, type 1, values [3, 4, 88]")


        self.assertEqual(str(MyVector("", "r", 1, [3, 4, 88])),"Vector with name_id=, colour r, type 1, values [3, 4, 88]")

        self.assertEqual(str(MyVector("Vector3", "r", 1, [])),"Vector with name_id=Vector3, colour r, type 1, values [1]")

    def test_features(self):
        #1. Scalar operations
        s3 = MyVector("Vector3", "b", 3, [3, 4, 0])
        s3.add_scalar(34)
        self.assertEqual(str(s3),str(MyVector("Vector3", "b", 3, [37, 38, 34])))

        s3 = MyVector("Vector3", "b", 3, [3, 44, 55])
        s3.add_scalar(0)
        self.assertEqual(str(s3),str(MyVector("Vector3", "b", 3, [3,44,55])))

        s3 = MyVector("Vector3", "b", 3, [3, 4, 0])
        s3.add_scalar(-1)
        self.assertEqual(str(s3),str(MyVector("Vector3", "b", 3, [2, 3, -1])))

        #2. Vector operations
        s3 = MyVector("Vector3", "b", 3, [3, 4, 0])
        s4 = MyVector("Vector3", "b", 3, [3, 4, 0])
        self.assertEqual(s3+s4,[6,8,0])

        s3 = MyVector("Vector3", "b", 3, [3, 4, 0])
        s4 = MyVector("Vector3", "b", 3, [3, 4])
        self.assertEqual(s3 + s4, 'Not a possible operation')

        s3 = MyVector("Vector3", "b", 3, [22,33])
        s4 = MyVector("Vector3", "b", 3, [101,45])
        self.assertEqual(s3+s4,[123, 78])


        s3 = MyVector("Vector3", "b", 3, [3, 4, 0])
        s4 = MyVector("Vector3", "b", 3, [3, 4, 0])
        self.assertEqual(s3-s4,[0,0,0])

        s3 = MyVector("Vector3", "b", 3, [3, 4, 0])
        s4 = MyVector("Vector3", "b", 3, [3, 4])
        self.assertEqual(s3 - s4, 'Not a possible operation')

        s3 = MyVector("Vector3", "b", 3, [22,33])
        s4 = MyVector("Vector3", "b", 3, [101,45])
        self.assertEqual(s3-s4,[-79, -12])


        s3 = MyVector("Vector3", "b", 3, [3, 4, 0])
        s4 = MyVector("Vector3", "b", 3, [3, 4, 0])
        self.assertEqual(s3*s4,25)

        s3 = MyVector("Vector3", "b", 3, [3, 4, 0])
        s4 = MyVector("Vector3", "b", 3, [3, 4])
        self.assertEqual(s3 * s4, 'Not a possible operation')

        s3 = MyVector("Vector3", "b", 3, [22,33])
        s4 = MyVector("Vector3", "b", 3, [101,45])
        self.assertEqual(s3*s4,3707)

        #3. Reduction operations
        s3 = MyVector("Vector3", "b", 3, [3, 4, 20])
        self.assertEqual(s3.sum_elements(),27)
        self.assertEqual(s3.product_elements(), 240)
        self.assertEqual(s3.avg_elements(), 9)
        self.assertEqual(s3.min_elements(), 3)
        self.assertEqual(s3.max_elements(), 20)

        s3 = MyVector("Vector3", "b", 3, [0,1])
        self.assertEqual(s3.sum_elements(),1)
        self.assertEqual(s3.product_elements(), 0)
        self.assertEqual(s3.avg_elements(), 0.5)
        self.assertEqual(s3.min_elements(), 0)
        self.assertEqual(s3.max_elements(), 1)

        s3 = MyVector("Vector3", "b", 3, [22,33,44])
        self.assertEqual(s3.sum_elements(),99)
        self.assertEqual(s3.product_elements(), 31944)
        self.assertEqual(s3.avg_elements(), 33)
        self.assertEqual(s3.min_elements(), 22)
        self.assertEqual(s3.max_elements(), 44)


if __name__ == '__main__':
    unittest.main()

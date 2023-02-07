

""" Self Driving Car Class """

class selfDrivingCar(object):

    def __init__(self):
        self.speed = 0
        self.destination = None

    def _accelerate(self):
        self.speed +=1

    def _deaccelerate(self):
        if self.speed >0:
            self.speed -=1

    def _calculate_distance_to_object_infront(self):
        pass

    def stop(self):
        self.speed = 0

    def _get_speed_limit(self):
        pass

    def _has_arrived(self):
        pass

    def _advance_to_destination(self):
        distance = self._calculate_distance_to_object_infront()
        if distance <10 :
            self.stop()
        elif distance < self.speed/2 :
            self._deaccelerate()
        elif self.speed < self._get_speed_limit() :
            self._accelerate()

    def drive(self , destination):
        self.destination = destination

        while not self._has_arrived:
            self._advance_to_destination()

        self.stop()



""" Self Driving Car Test"""

import unittest

class selfDrivingCarTest(unittest.TestCase):

    def setUp(self):
        self.car = selfDrivingCar()

    def test_stop(self):
        self.car.speed = 5
        self.car.stop()

        #Verify If car speed is 0 after stop
        self.assertEqual( 0 , self.car.speed )

        #Verify is it OK to stop again if car speed is 0 .
        self.car.stop()
        self.assertEqual(0 , self.car.speed )


    # def test_accelerate(self):
    #     self.car.speed = 0
    #     self.car.accelerate()

    #     #Verify if car speed increased after it accelerate .
    #     self.assertTrue(self._accelerate)

if __name__ == '__main__' :
    unittest.main()






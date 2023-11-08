import unittest
from robot import RobotVacuum


class TestRobotVacuum(unittest.TestCase):
    def setUp(self):
        self.robot = RobotVacuum(id=1, model='xyz123')

    def test_start_cleaning(self):
        result = self.robot.start_cleaning()
        self.assertEqual(result, "Robot 1 is now cleaning.")

    def test_stop_cleaning(self):
        result = self.robot.stop_cleaning()
        self.assertEqual(result, "Robot 1 has stopped cleaning.")


if __name__ == '__main__':
    unittest.main()

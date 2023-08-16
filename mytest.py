import unittest
from spacecraft import Spacecraft

class TestSpacecraftCommands(unittest.TestCase):
    def test_move_forward(self):
        spacecraft = Spacecraft(0, 0, 0, "N")
        spacecraft.move_forward()
        self.assertEqual(spacecraft.position, [0, 1, 0])

    def test_move_backward(self):
        spacecraft = Spacecraft(0, 0, 0, "N")
        spacecraft.move_backward()
        self.assertEqual(spacecraft.position, [0, -1, 0])

    # Similarly, write test cases for other methods

if _name_ == "_main_":
    unittest.main()
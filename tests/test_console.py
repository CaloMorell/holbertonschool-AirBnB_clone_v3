import unittest
import sys  
from io import StringIO
from console import HBNBCommand
from models.state import State
from models.place import Place

class TestHBNBCommandCreateWithParams(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_create_state_with_params(self):
        # Redirect stdout to capture console output
        sys.stdin = StringIO("create State name=\"California\"\nall State\n")
        self.console.cmdloop()
        output = sys.stdout.getvalue()
        self.assertIn("California", output)

    def test_create_place_with_params(self):
        # Redirect stdout to capture console output
        sys.stdin = StringIO("create Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297\nall Place\n")
        self.console.cmdloop()
        output = sys.stdout.getvalue()
        self.assertIn("My little house", output)

if __name__ == '__main__':
    unittest.main()


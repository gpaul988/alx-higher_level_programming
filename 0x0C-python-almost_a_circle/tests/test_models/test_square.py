#!/usr/bin/python3
# Graham S. Paul (test_square.py)
"""
Factor Assessment for Square Class
"""


import unittest
import pep8
from io import StringIO
from contextlib import redirect_stdout
from models import square
Square = square.Square


class TestPep8(unittest.TestCase):
    """Pep8 models/square.py & tests/test_models/test_square.py"""
    def test_pep8(self):
        """Pep8"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/square.py", "tests/test_models/test_square.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')


class TestBase(unittest.TestCase):
    """Assessment for models/square.py"""

    """Test attributes"""
    def test_all_attr_given(self):
        """Inspect all features to  match what's given"""
        s1 = Square(9, 99, 999, 1000)
        self.assertTrue(s1.width == 9)
        self.assertTrue(s1.height == 9)
        self.assertTrue(s1.size == 9)
        self.assertTrue(s1.x == 99)
        self.assertTrue(s1.y == 999)
        self.assertTrue(s1.id == 1000)

    def test_default_attr(self):
        """Assessment original features are set when not given"""
        s2 = Square(88)
        self.assertTrue(s2.width == 88)
        self.assertTrue(s2.height == 88)
        self.assertTrue(s2.size == 88)
        self.assertTrue(s2.x == 0)
        self.assertTrue(s2.y == 0)
        self.assertTrue(s2.id is not None)

    def test_attr_validated(self):
        """Assessment features are validated before set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")
            Square([10, 3])
            Square({20, })
            Square({"d": 20})
            Square(None)
            Square((30, 20), 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
            Square(9).size(-9)

    """Assessment args given"""
    def test_invalid_args(self):
        """Assessment too many args given throws error"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7)
        """Assessment too samll args given throws error"""
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    """Assessment class"""
    def test_class(self):
        """Assessment  class generated is indeed Rectangle"""
        s = Square(10)
        self.assertEqual(type(s), Square)

    """Assessment Procedures"""
    def test_area(self):
        """Assessment procedure: area"""
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(4, 0, 0).area(), 16)

    def test_display(self):
        """Assessment procedure: display"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Square(4).display()
            b = bufr.getvalue()
        self.assertEqual(b, '####\n####\n####\n####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Square(3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n ###\n ###\n ###\n')

    def test_print(self):
        """Assessment procedure: __str__"""
        s = Square(1, 2, 3, 44)
        s.size = 500
        self.assertEqual(str(s), '[Square] (44) 2/3 - 500')

    def test_update(self):
        """Assessment procedure: update(*args)"""
        s = Square(1, 2, 3, 4)
        s.update(10, 10, 10, 10)
        self.assertEqual(str(s), '[Square] (10) 10/10 - 10')
        s.update()
        self.assertEqual(str(s), '[Square] (10) 10/10 - 10')
        s.update(99)
        self.assertEqual(str(s), '[Square] (99) 10/10 - 10')
        s.update(99, 5)
        self.assertEqual(str(s), '[Square] (99) 10/10 - 5')
        s.update(44, 55, 1, 2)
        self.assertEqual(str(s), '[Square] (44) 1/2 - 55')
        """Assessment procedure: update(*kwargs)"""
        s.update(id=88, size=77, nokey=99)
        self.assertEqual(str(s), '[Square] (88) 1/2 - 77')

    def test_to_dictionary(self):
        """Assessment procedure: to_dictionary"""
        sdic = Square(1, 2, 3, 4).to_dictionary()
        self.assertEqual(type(sdic), dict)
        s2 = Square(10, 10)
        s2.update(**sdic)
        self.assertEqual(str(s2), '[Square] (4) 2/3 - 1')

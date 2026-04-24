import unittest
from unittest.mock import patch
import io
import hello

class TestHello(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main(self, mock_stdout):
        hello.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, world!")

if __name__ == '__main__':
    unittest.main()

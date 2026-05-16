import unittest
from unittest.mock import patch
import io
import subprocess
import sys
import hello

class TestHello(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main(self, mock_stdout):
        hello.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, world!")

    def test_cli(self):
        """Test the __main__ block by running it as a subprocess."""
        result = subprocess.run(
            [sys.executable, 'hello.py'],
            capture_output=True,
            text=True,
            check=True
        )
        self.assertEqual(result.stdout.strip(), "Hello, world!")

if __name__ == '__main__':
    unittest.main()

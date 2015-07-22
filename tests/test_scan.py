from unittest import TestCase

from wifi.scan import Cell
from wifi import subprocess_compat as subprocess
from wifi.subprocess_compat import check_output
from mock import Mock, MagicMock
from dummydata import ScanTesting as scan

class ScanTest(TestCase):
    def test_all_calls_check_output_with_good_args(self):
        #args should contain 'sudo' with Yohan's patch
            subprocess.check_output = MagicMock(return_value=scan.output)
            Cell.all('interface', True)
            subprocess.check_output.assert_called_with(scan.args_ws, **scan.kwargs)
            Cell.all('interface')
            subprocess.check_output.assert_called_with(scan.args_ls, **scan.kwargs)


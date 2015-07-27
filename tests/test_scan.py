from unittest import TestCase

from wifi.scan import Cell
from wifi import subprocess_compat as subprocess
from mock import MagicMock
from test_parsing import output

class ScanTest(TestCase):
    def test_all_calls_check_output_with_good_args(self):
        args = ['sudo', '/sbin/iwlist', 'interface', 'scan']
        kwargs = {'stderr':subprocess.STDOUT}
        subprocess.check_output = MagicMock(return_value=output)
        Cell.all('interface', True)
        subprocess.check_output.assert_called_once_with(args, **kwargs)
        args = ['/sbin/iwlist', 'interface', 'scan']
        subprocess.check_output = MagicMock(return_value=output)
        Cell.all('interface')
        subprocess.check_output.assert_called_once_with(args, **kwargs)


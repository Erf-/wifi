from unittest import TestCase
import tempfile
import os

from wifi.exceptions import ConnectionError
from dummydata import SchemeTesting as sch
from wifi.scheme import Scheme
from wifi import subprocess_compat as subprocess
from wifi.subprocess_compat import check_output
from mock import Mock, MagicMock


class TestSchemes(TestCase):
    def setUp(self):
        self.tempfile, interfaces = tempfile.mkstemp()
        with open(interfaces, 'w') as f:
            f.write(sch.NETWORK_INTERFACES_FILE)
        self.Scheme = Scheme.for_file(interfaces)

    def tearDown(self):
        os.remove(self.Scheme.interfaces)

    def test_scheme_extraction(self):
        assert sch.work.name == 'work'
        assert sch.work.options['wpa-ssid'] == 'workwifi'
        assert sch.coffee.name == 'coffee'
        assert sch.coffee.options['wireless-essid'] == 'Coffee WiFi'

    def test_str(self):
        assert str(sch.scheme) == 'iface wlan0-test inet dhcp\n'

        sch.scheme = self.Scheme('wlan0', 'test', {
            'wpa-ssid': 'workwifi',
        })

        self.assertEqual(str(sch.scheme), 
        'iface wlan0-test inet dhcp\n    wpa-ssid workwifi\n')

    def test_find(self):
        work = self.Scheme.find('wlan0', 'work')
        assert work.options['wpa-ssid'] == 'workwifi'

    def test_delete(self):
        work = self.Scheme.find('wlan0', 'work')
        work.delete()
        self.assertIsNone(self.Scheme.find('wlan0', work))
        assert self.Scheme.find('wlan0', 'coffee')

    def test_save(self):
        sch.scheme = self.Scheme('wlan0', 'test')
        sch.scheme.save()
        assert self.Scheme.find('wlan0', 'test')


class TestActivation(TestCase):
    def test_successful_connection(self):
        connection = sch.scheme.parse_ifup_output(sch.SUCCESSFUL_IFUP_OUTPUT)
        self.assertEqual(connection.scheme, sch.scheme)
        self.assertEqual(connection.ip_address, '192.168.1.113')

    def test_failed_connection(self):
        self.assertRaises(ConnectionError, sch.scheme.parse_ifup_output,
        sch.FAILED_IFUP_OUTPUT)

    def test_activate_is_called_with_good_args(self):
        subprocess.check_output = MagicMock(return_value=sch.SUCCESSFUL_IFUP_OUTPUT)
        sch.scheme.activate(True)
        subprocess.check_output.assert_called_with(sch.args_ws,
        **sch.kwargs)
        sch.scheme.activate()
        subprocess.check_output.assert_called_with(sch.args_ls,
        **sch.kwargs)


class TestForCell(TestCase):
    def test_unencrypted(self):
        sch.cell.ssid = 'SSID'
        sch.cell.encrypted = False

        sch.scheme = Scheme.for_cell('wlan0', 'test', sch.cell)

        self.assertEqual(sch.scheme.options, {
            'wireless-essid': 'SSID',
            'wireless-channel': 'auto',
        })

    def test_wep_hex(self):
        sch.cell.ssid = 'SSID'
        sch.cell.encrypted = True
        sch.cell.encryption_type = 'wep'

        # hex key lengths: 10, 26, 32, 58
        hex_keys = ("01234567ab", "0123456789abc" * 2,
        "0123456789abcdef" * 2,
        "0123456789abc" * 2 + "0123456789abcdef" * 2)
        for key in hex_keys:
            sch.scheme = Scheme.for_cell('wlan0', 'test', sch.cell, key)

            self.assertEqual(sch.scheme.options, {
                'wireless-essid': 'SSID',
                'wireless-key': key
            })

    def test_wep_ascii(self):
        sch.cell.ssid = 'SSID'
        sch.cell.encrypted = True
        sch.cell.encryption_type = 'wep'

        # ascii key lengths: 5, 13, 16, 29
        ascii_keys = ('a' * 5, 'a' * 13, 'a' * 16, 'a' * 29)
        for key in ascii_keys:
            sch.scheme = Scheme.for_cell('wlan0', 'test', sch.cell, key)

            self.assertEqual(sch.scheme.options, {
                'wireless-essid': 'SSID',
                'wireless-key': 's:' + key
            })

    def test_wpa2(self):
        sch.cell.ssid = 'SSID'
        sch.cell.encrypted = True
        sch.cell.encryption_type = 'wpa2'

        sch.scheme = Scheme.for_cell('wlan0', 'test', sch.cell, b'passkey')

        self.assertEqual(sch.scheme.options, {
            'wpa-ssid': 'SSID',
            'wpa-psk': 'ea1548d4e8850c8d94c5ef9ed6fe483981b64c1436952cb1bf80c08a68cdc763',
            'wireless-channel': 'auto',
        })

    def test_wpa(self):
        sch.cell.ssid = 'SSID'
        sch.cell.encrypted = True
        sch.cell.encryption_type = 'wpa'

        sch.scheme = Scheme.for_cell('wlan0', 'test', sch.cell, 'passkey')

        self.assertEqual(sch.scheme.options, {
            'wpa-ssid': 'SSID',
            'wpa-psk': 'ea1548d4e8850c8d94c5ef9ed6fe483981b64c1436952cb1bf80c08a68cdc763',
            'wireless-channel': 'auto',
        })


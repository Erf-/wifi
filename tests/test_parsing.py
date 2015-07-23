from unittest import TestCase

from wifi.scan import Cell
from wifi.exceptions import InterfaceError
from dummydata import ScanTesting as scan


class IWListParserTest(TestCase):
    def test_no_encryption(self):
        cell = Cell.from_string(scan.IWLIST_SCAN_NO_ENCRYPTION)
        self.assertFalse(cell.encrypted)
        self.assertEqual(cell.ssid, 'My Wireless Network')
        self.assertEqual(cell.signal, -51)
        self.assertEqual(cell.quality, '59/70')
        self.assertEqual(cell.frequency, '2.437 GHz')
        self.assertEqual(cell.mode, 'Master')
        self.assertEqual(cell.channel, 6)

    def test_wep(self):
        cell = Cell.from_string(scan.IWLIST_SCAN_WEP)
        self.assertTrue(cell.encrypted)
        self.assertEqual(cell.encryption_type, 'wep')

    def test_wpa2(self):
        cell = Cell.from_string(scan.IWLIST_SCAN_WPA2)
        self.assertTrue(cell.encrypted)
        self.assertEqual(cell.encryption_type, 'wpa2')

    def test_wpa1(self):
        cell = Cell.from_string(scan.IWLIST_SCAN_WPA1)
        self.assertTrue(cell.encrypted)
        self.assertEqual(cell.encryption_type, 'wpa')

    def test_alternative_iwlist_output(self):
        # https://github.com/rockymeza/wifi/issues/12
        cell = Cell.from_string(scan.ALTERNATIVE_OUTPUT)
        self.assertEqual(cell.quality, '78/100')
        self.assertEqual(cell.signal, -92)

    def test_signal_level_out_of_sixty(self):
        cell = Cell.from_string(scan.ALTERNATIVE_OUTPUT2)
        self.assertEqual(cell.signal, -71)

    def test_noname_cell(self):
        cell = Cell.from_string(scan.NONAME_WIRELESS_NETWORK)
        self.assertEqual(cell.ssid, '')

    def test_no_channel_output(self):
        # https://github.com/rockymeza/wifi/issues/24
        cell = Cell.from_string(scan.NO_CHANNEL_OUTPUT)
        self.assertEqual(cell.channel, 11)

    def test_list_index_error(self):
        # https://github.com/rockymeza/wifi/issues/42
        cell = Cell.from_string(scan.LIST_INDEX_ERROR)

    def test_frequency_no_channel_output(self):
        # https://github.com/rockymeza/wifi/issues/39
        cell = Cell.from_string(scan.FREQUENCY_NO_CHANNEL_OUTPUT)
        self.assertEqual(cell.channel, 149)

    def test_absolute_quality(self):
        # https://github.com/rockymeza/wifi/pull/45
        cell = Cell.from_string(scan.ABSOLUTE_QUALITY)
        self.assertEqual(cell.quality, '38/100')
        self.assertEqual(cell.signal, -92)


class ScanningTest(TestCase):
    def test_scanning(self):
        self.assertRaises(InterfaceError, Cell.all, 'fake-interface')


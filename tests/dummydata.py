#code implementing the tests variables of each class

from wifi import subprocess_compat as subprocess
from wifi.scheme import extract_schemes, Scheme
from wifi.scan import Cell

class ScanTesting(object):
    args_ws = ['sudo', '/sbin/iwlist', 'interface', 'scan']
    args_ls = ['/sbin/iwlist', 'interface', 'scan']
    #args_ls : args_less_sudo
    #args_ws : args_with_sudo
    kwargs = {'stderr':subprocess.STDOUT}
    output = """Scan completed :
          Cell 01 - Address: C4:04:15:8D:E2:26
                    Channel:6
                    Frequency:2.437 GHz (Channel 6)
                    Quality=50/70  Signal level=-60 dBm  
                    Encryption key:on
                    ESSID:"BSF"
                    Bit Rates:1 Mb/s; 2 Mb/s; 5.5 Mb/s; 11 Mb/s; 6 Mb/s
                              9 Mb/s; 12 Mb/s; 18 Mb/s
                    Bit Rates:24 Mb/s; 36 Mb/s; 48 Mb/s; 54 Mb/s
                    Mode:Master
                    Extra:tsf=000001081347641d
                    Extra: Last beacon: 296ms ago
                    IE: Unknown: 0003425346
                    IE: Unknown: 010882848B960C121824
                    IE: Unknown: 030106
                    IE: Unknown: 2A0100
                    IE: Unknown: 32043048606C
                    IE: Unknown: 2D1AAD0103FFFF0000000000000000000000000000000406E6E70D00
                    IE: Unknown: 3D1606001700000000000000000000000000000000000000
                    IE: Unknown: 4A0E14000A002C01C800140005001900
                    IE: Unknown: 7F0101
                    IE: Unknown: DD180050F2020101820003A4000027A4000042435E0062322F00
                    IE: Unknown: DD1E00904C33AD0103FFFF0000000000000000000000000000000406E6E70D00
                    IE: Unknown: DD1A00904C3406001700000000000000000000000000000000000000
                    IE: Unknown: DD0900037F01010000FF7F
                    IE: IEEE 802.11i/WPA2 Version 1
                        Group Cipher : CCMP
                        Pairwise Ciphers (1) : CCMP
                        Authentication Suites (1) : PSK
                    IE: Unknown: DD900050F204104A0001101044000102103B00010310470010427974EECF6C52788C94000000000000102100046E6F6E65102300046E6F6E65102400046E6F6E651042001253657269616C204E756D62657220486572651054000800060050F204000110110016574E5232303030763428576972656C65737320415029100800022008103C0001011049000600372A000120
          Cell 02 - Address: 00:0F:60:01:6D:02
                    Channel:1
                    Frequency:2.412 GHz (Channel 1)
                    Quality=62/70  Signal level=-48 dBm  
                    Encryption key:off
                    ESSID:"koombook"
                    Bit Rates:1 Mb/s; 2 Mb/s; 5.5 Mb/s; 11 Mb/s; 6 Mb/s
                              9 Mb/s; 12 Mb/s; 18 Mb/s
                    Bit Rates:24 Mb/s; 36 Mb/s; 48 Mb/s; 54 Mb/s
                    Mode:Master
                    Extra:tsf=00000000493574f5
                    Extra: Last beacon: 560ms ago
                    IE: Unknown: 00086B6F6F6D626F6F6B
                    IE: Unknown: 010882848B960C121824
                    IE: Unknown: 030101
                    IE: Unknown: 2A0104
                    IE: Unknown: 32043048606C
          Cell 03 - Address: 88:25:2C:70:45:A1
                    Channel:11
                    Frequency:2.462 GHz (Channel 11)
                    Quality=42/70  Signal level=-68 dBm  
                    Encryption key:on
                    ESSID:"OPTIPRO_WPA_2E4C"
                    Bit Rates:1 Mb/s; 2 Mb/s; 5.5 Mb/s; 6 Mb/s; 9 Mb/s
                              11 Mb/s; 12 Mb/s; 18 Mb/s
                    Bit Rates:24 Mb/s; 36 Mb/s; 48 Mb/s; 54 Mb/s
                    Mode:Master
                    Extra:tsf=00000003e56cce14
                    Extra: Last beacon: 32ms ago
                    IE: Unknown: 00104F50544950524F5F5750415F32453443
                    IE: Unknown: 010882848B0C12961824
                    IE: Unknown: 03010B
                    IE: IEEE 802.11i/WPA2 Version 1
                        Group Cipher : TKIP
                        Pairwise Ciphers (2) : CCMP TKIP
                        Authentication Suites (1) : PSK
                    IE: WPA Version 1
                        Group Cipher : TKIP
                        Pairwise Ciphers (2) : CCMP TKIP
                        Authentication Suites (1) : PSK
                    IE: Unknown: 2A0100
                    IE: Unknown: 32043048606C
                    IE: Unknown: DD180050F2020101850003A4000027A4000042435E0062322F00
                    IE: Unknown: DD0900037F01010000FF7F
                    IE: Unknown: DD0A00037F04010000000000
                    IE: Unknown: 0706465220010D14
                    IE: Unknown: DDA20050F204104A000110104400010210570001001041000100103B00010310470010411CF0BED37149EA932E4AB40CA6460410210005426577616E102300194152563435314150572D412D4C462D4C33205061726974656C1024000A307830304135304132331042000F3938303030303037353438343932371054000800060050F20400011011000F496E66696E656F6E2044616E756265100800020080103C000101
          Cell 04 - Address: B0:38:29:17:E3:C6
                    Channel:11
                    Frequency:2.462 GHz (Channel 11)
                    Quality=38/70  Signal level=-72 dBm  
                    Encryption key:off
                    ESSID:"Adapt_Setup_3C6"
                    Bit Rates:1 Mb/s; 2 Mb/s; 5.5 Mb/s; 11 Mb/s; 18 Mb/s
                              24 Mb/s; 36 Mb/s; 54 Mb/s
                    Bit Rates:6 Mb/s; 9 Mb/s; 12 Mb/s; 48 Mb/s
                    Mode:Master
                    Extra:tsf=000003286b693d83
                    Extra: Last beacon: 40ms ago
                    IE: Unknown: 000F41646170745F53657475705F334336
                    IE: Unknown: 010882848B962430486C
                    IE: Unknown: 03010B
                    IE: Unknown: 2A0100
                    IE: Unknown: 2F0100
                    IE: Unknown: 32040C121860
                    IE: Unknown: 2D1A0C1119FF00000000000000000000000000000000000000000000
                    IE: Unknown: 3D160B081100000000000000000000000000000000000000
                    IE: Unknown: DD09001018020000040000
                    IE: Unknown: DD180050F2020101800003A4000027A4000042435E0062322F00
          Cell 05 - Address: 96:FE:F4:9C:88:84
                    Channel:2
                    Frequency:2.417 GHz (Channel 2)
                    Quality=46/70  Signal level=-64 dBm  
                    Encryption key:on
                    ESSID:"Bbox-9C8884"
                    Bit Rates:1 Mb/s; 2 Mb/s; 5.5 Mb/s; 11 Mb/s; 9 Mb/s
                              18 Mb/s; 36 Mb/s; 54 Mb/s
                    Bit Rates:6 Mb/s; 12 Mb/s; 24 Mb/s; 48 Mb/s
                    Mode:Master
                    Extra:tsf=000000f65ac17e37
                    Extra: Last beacon: 644ms ago
                    IE: Unknown: 000B42626F782D394338383834
                    IE: Unknown: 010882848B961224486C
                    IE: Unknown: 030102
                    IE: Unknown: 2A0106
                    IE: Unknown: 32040C183060
                    IE: Unknown: 2D1A6C0017FFFF000000000000000000000000000000000000000000
                    IE: Unknown: 3D1602000000000000000000000000000000000000000000
                    IE: Unknown: 3E0100
                    IE: WPA Version 1
                        Group Cipher : CCMP
                        Pairwise Ciphers (1) : CCMP
                        Authentication Suites (1) : PSK
                    IE: IEEE 802.11i/WPA2 Version 1
                        Group Cipher : CCMP
                        Pairwise Ciphers (1) : CCMP
                        Authentication Suites (1) : PSK
                    IE: Unknown: DD180050F2020101800003A4000027A4000042435E0062322F00
                    IE: Unknown: 0B0500001E127A
                    IE: Unknown: DD07000C4300000000
                    IE: Unknown: 0706465220010D10
          Cell 06 - Address: 00:78:9E:79:14:A0
                    Channel:1
                    Frequency:2.412 GHz (Channel 1)
                    Quality=44/70  Signal level=-66 dBm  
                    Encryption key:on
                    ESSID:"Bbox-7563A466"
                    Bit Rates:1 Mb/s; 2 Mb/s; 5.5 Mb/s; 11 Mb/s; 9 Mb/s
                              18 Mb/s; 36 Mb/s; 54 Mb/s
                    Bit Rates:6 Mb/s; 12 Mb/s; 24 Mb/s; 48 Mb/s
                    Mode:Master
                    Extra:tsf=000000e41e34a153
                    Extra: Last beacon: 3352ms ago
                    IE: Unknown: 000D42626F782D3735363341343636
                    IE: Unknown: 010882848B961224486C
                    IE: Unknown: 030101
                    IE: Unknown: 32040C183060
                    IE: Unknown: 0706465220010B14
                    IE: Unknown: 33082001020304050607
                    IE: Unknown: 33082105060708090A0B
                    IE: Unknown: 050400010008
                    IE: Unknown: DD310050F204104A000110104400010210470010A804735689AB4ECA855E544E7B338DE2103C0001011049000600372A000120
                    IE: Unknown: 2A0104
                    IE: Unknown: 2D1AEC0103FFFFFF00000000000000000000000000000C1846471100
                    IE: Unknown: 3D1601000700000000000000000000000000000000000000
                    IE: Unknown: 7F0101
                    IE: WPA Version 1
                        Group Cipher : CCMP
                        Pairwise Ciphers (1) : CCMP
                        Authentication Suites (1) : PSK
                    IE: IEEE 802.11i/WPA2 Version 1
                        Group Cipher : CCMP
                        Pairwise Ciphers (1) : CCMP
                        Authentication Suites (1) : PSK
                    IE: Unknown: DD180050F2020101800003A4000027A4000042435E0062322F00
                    IE: Unknown: 0B05030025127A
                    IE: Unknown: DD07000C4307000000
          Cell 07 - Address: CE:2B:EB:BC:A4:18
                    Channel:8
                    Frequency:2.447 GHz (Channel 8)
                    Quality=42/70  Signal level=-68 dBm  
                    Encryption key:off
                    ESSID:"EpsonB40"
                    Bit Rates:1 Mb/s; 2 Mb/s; 5.5 Mb/s; 11 Mb/s
                    Bit Rates:6 Mb/s; 9 Mb/s; 12 Mb/s; 18 Mb/s; 24 Mb/s
                              36 Mb/s; 48 Mb/s; 54 Mb/s
                    Mode:Ad-Hoc
                    Extra:tsf=0000050c44d24343
                    Extra: Last beacon: 224ms ago
                    IE: Unknown: 00084570736F6E423430
                    IE: Unknown: 010482848B96
                    IE: Unknown: 030108
                    IE: Unknown: 06020000
                    IE: Unknown: 2A0100
                    IE: Unknown: 2F0100
                    IE: Unknown: 32080C1218243048606C
                    IE: Unknown: DD09001018020010000000"""

class SchemeTesting(object):
    args_ws = ['sudo', '/sbin/ifdown', 'wlan0', 'wlan0=wlan0-test']
    args_ls = ['/sbin/ifdown', 'wlan0', 'wlan0=wlan0-test']
    kwargs = {'stderr':subprocess.STDOUT}
    cell = Cell()
    scheme = Scheme('wlan0', 'test')
    NETWORK_INTERFACES_FILE = """
 This file describes the network interfaces available on your system
 and how to activate them. For more information, see interfaces(5).

 The loopback network interface
auto lo
iface lo inet loopback

 The primary network interface
allow-hotplug eth0
iface eth0 inet dhcp

iface wlan0-work inet dhcp
    wpa-ssid workwifi
    wireless-channel auto
    wpa-psk 1111111111111111111111111111111111111111111111111111111111111111

iface wlan0-coffee inet dhcp
    wireless-essid Coffee WiFi
    wireless-channel auto

iface wlan0-home inet dhcp
    wpa-ssid homewifi
    wpa-psk  2222222222222222222222222222222222222222222222222222222222222222
    wireless-channel auto

iface wlan0-coffee2 inet dhcp
    wireless-essid Coffee 2
    wireless-channel auto
"""
    work, coffee, home, coffee2 = extract_schemes(NETWORK_INTERFACES_FILE)
    SUCCESSFUL_IFDOWN_OUTPUT = """Internet Systems Consortium DHCP Client 4.2.4
Copyright 2004-2012 Internet Systems Consortium.
All rights reserved.
For info, please visit https://www.isc.org/software/dhcp/

Listening on LPF/wlan0/9c:4e:36:5d:2c:64
Sending on   LPF/wlan0/9c:4e:36:5d:2c:64
Sending on   Socket/fallback
DHCPRELEASE on wlan0 to 192.168.1.1 port 67
"""

    SUCCESSFUL_IFUP_OUTPUT = """Internet Systems Consortium DHCP Client 4.2.4
Copyright 2004-2012 Internet Systems Consortium.
All rights reserved.
For info, please visit https://www.isc.org/software/dhcp/

Listening on LPF/wlan0/9c:4e:36:5d:2c:64
Sending on   LPF/wlan0/9c:4e:36:5d:2c:64
Sending on   Socket/fallback
DHCPDISCOVER on wlan0 to 255.255.255.255 port 67 interval 4
DHCPDISCOVER on wlan0 to 255.255.255.255 port 67 interval 8
DHCPREQUEST on wlan0 to 255.255.255.255 port 67
DHCPOFFER from 192.168.1.1
DHCPACK from 192.168.1.1
bound to 192.168.1.113 -- renewal in 2776 seconds.
"""

    FAILED_IFUP_OUTPUT = """Internet Systems Consortium DHCP Client 4.2.4
Copyright 2004-2012 Internet Systems Consortium.
All rights reserved.
For info, please visit https://www.isc.org/software/dhcp/

Listening on LPF/wlan0/9c:4e:36:5d:2c:64
Sending on   LPF/wlan0/9c:4e:36:5d:2c:64
Sending on   Socket/fallback
DHCPDISCOVER on wlan0 to 255.255.255.255 port 67 interval 5
DHCPDISCOVER on wlan0 to 255.255.255.255 port 67 interval 8
DHCPDISCOVER on wlan0 to 255.255.255.255 port 67 interval 18
DHCPDISCOVER on wlan0 to 255.255.255.255 port 67 interval 18
DHCPDISCOVER on wlan0 to 255.255.255.255 port 67 interval 12
No DHCPOFFERS received.
No working leases in persistent database - sleeping.
"""


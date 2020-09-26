import unittest
import  ICMP
from collections import namedtuple

class Tests(unittest.TestCase):
    def test_cheksum(self):
        pack = b'\x08\x00\x00\x00\x00\x01\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self.assertEqual(ICMP.get_checksum(pack), 60670)

    def test_bPac(self):
        pack = b'\x08\x00\xf5\xfe\x00\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self.assertEqual(ICMP.build_packet(2), pack)

    def test_parce_header(self):
        pack = b'E\x00\x00\\\x00\x00\x00\x00g\x01\xaeR@\xe9\xa2\x8b\xc0\xa8\x012\x00\x00\xe4\xfe\x00\x01\x1b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        typ = namedtuple('Header', ['request_type', 'code', 'checksum', 'packet_id', 'sequence'])
        self.assertEqual(ICMP.parse_header(pack), typ(0, 0, 65252, 256, 27))

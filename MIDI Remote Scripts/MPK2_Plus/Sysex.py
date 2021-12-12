#
#   Sysex.py
#   Defines hardcoded sysex message stuff
#

from __future__ import absolute_import, print_function, unicode_literals

SYX_START = 0xF0
SYX_END = 0xF7
SYX_AKAI_ID = (0x47, 0x00)
SYX_DEVICE_ID_MPK225 = 0x23
SYX_DEVICE_ID_MPK249 = 0x24
SYX_DEVICE_ID_MPK261 = 0x25
SYX_FUNC_SET_PAD_COLOR = (0x31, 0x00, 0x04, 0x01, 0x05)
SYX_FUNC_SET_PAD_COLOR_ALL = (0x31, 0x00, 0x43, 0x40, 0x05)
SYX_FUNC_GET_PAD_BANK = (0x31, 0x00, 0x01, 0x00, 0x00, 0x18)
SYX_PAD_ON_BASE = 0xBC
SYX_PAD_OFF_BASE = 0x7C
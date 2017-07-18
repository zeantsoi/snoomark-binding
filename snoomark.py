import simplejson as json
from ctypes import *


pulldown = cdll.LoadLibrary('pulldown-cmark/target/release/libpulldown_cmark.dylib')
pulldown.html.restype = c_char_p

crak = cdll.LoadLibrary('comrak/target/release/libcomrak.dylib')
crak.html.restype = c_char_p


class pulldown_cmark:

    @staticmethod
    def to_html(cmark):
        pntr = pulldown.html(cmark.encode('utf-8'))
        return cast(pntr, c_char_p).value


class comrak:

    @staticmethod
    def to_html(cmark):
        pntr = crak.html(cmark.encode('utf-8'))
        return cast(pntr, c_char_p).value

import simplejson as json
from ctypes import *
pulldown = cdll.LoadLibrary('pulldown-cmark/target/debug/libpulldown_cmark.dylib')
pulldown.html.restype = c_char_p

def to_html(md):
    pntr = pulldown.html(md.encode('utf-8'))
    return cast(pntr, c_char_p).value

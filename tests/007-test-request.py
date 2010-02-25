# -*- coding: utf-8 -
#
# This file is part of restkit released under the MIT license. 
# See the NOTICE for more information.

import t
from restkit import request

from _server_test import HOST, PORT

LONG_BODY_PART = """This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client...
This is a relatively long body, that we send to the client..."""

def test_001():
    u = "http://%s:%s" % (HOST, PORT)
    r = request(u)
    t.eq(r.status_int, 200)
    t.eq(r.body, "welcome")
    
def test_002():
    u = "http://%s:%s" % (HOST, PORT)
    r = request(u, 'POST', body=LONG_BODY_PART)
    t.eq(r.status_int, 200)
    t.eq(int(r['content-length']), len(LONG_BODY_PART))
    t.eq(r.body, LONG_BODY_PART)
    
def test_003():
     u = "http://test:test@%s:%s/auth" % (HOST, PORT)
     r = request(u)
     t.eq(r.status_int, 200)
     u = "http://test:test2@%s:%s/auth" % (HOST, PORT)
     r = request(u)
     t.eq(r.status_int, 403)
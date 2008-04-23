#!/usr/bin/python

import sys
import rsa

pub = {'e': 248780186015280096941266517855109524861L, 'n': 289829846799217715870297548823528254304373554012264300246542488949110436220426067982155063515456468780177806574004719751854439098845391023946149242816599L}

print "Running rsa.verify(verslag, pub)..."

verslag = """
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
"""

verslag = rsa.verify(verslag, pub)

print "Decryption done, press enter to read"
sys.stdin.readline()
print verslag

print "Generating public & private keypair for demonstrational purposes..."
(pub, priv) = rsa.gen_pubpriv_keys(256)

print
print "Public:"
print "\te: %d" % pub['e']
print "\tn: %d" % pub['n']
print

print "Private:"
print "\td: %d" % priv['d']
print "\tp: %d" % priv['p']
print "\tq: %d" % priv['q']


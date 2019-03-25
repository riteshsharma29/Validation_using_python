#!/usr/bin/python

import sys
from pcodelib import ukpclib

#Testing UK Postcodes using ukpclib library

ukpclib.test_pccode("EC1A1BB", join=False)
ukpclib.test_pccode("W1A 0AX", join=False)
ukpclib.test_pccode("DN551PT", join=False)
ukpclib.test_pccode("AB1 1AA", join=False)
ukpclib.test_pccode("M1 1AE", join=False)
ukpclib.test_pccode("CR2 6XH", join=False)

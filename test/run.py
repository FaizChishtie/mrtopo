"""
    Run all mrtopo core tests
"""

from unittest import defaultTestLoader, TextTestRunner
import os
import sys

def runTests(testDir, verbosity=1):
    "discover and run all tests in testDir"
    # discover all tests in testDir
    testSuite = defaultTestLoader.discover( testDir )
    # run tests
    success = (TextTestRunner( verbosity=verbosity )
                .run( testSuite ).wasSuccessful())
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    # get the directory containing example tests
    dir = os.path.dirname(os.path.realpath(__file__ ))
    vlevel = 2 if '-v' in sys.argv else 1
    runTests(testDir=dir, verbosity=vlevel)
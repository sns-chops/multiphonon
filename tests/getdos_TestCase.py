#!/usr/bin/env python
#

import pytest
pytestmark = pytest.mark.skipif(True, reason="only run mannually")

interactive = False

import os
datadir = os.path.join(os.path.dirname(__file__), "data")

import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        "multiphonon.getdos"
        from multiphonon.getdos import getDOS
        getDOS(os.path.join(datadir, "ARCS_V_annulus.nxs"))
        return
        
    def test2(self):
        "multiphonon.getdos"
        from multiphonon.getdos import getDOS
        getDOS(
            os.path.join(datadir, "ARCS_V_annulus.nxs"),
            mt_nxs = os.path.join(datadir, "ARCS_V_annulus.nxs"),
            mt_fraction = 0.01,
        )
        return
        
    pass  # end of TestCase


if __name__ == "__main__":
    interactive = True
    unittest.main()
    
# End of file 

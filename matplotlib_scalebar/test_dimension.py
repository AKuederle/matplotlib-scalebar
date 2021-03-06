#!/usr/bin/env python
""" """

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.
from matplotlib_scalebar.dimension import \
    (SILengthDimension, SILengthReciprocalDimension, ImperialLengthDimension)

# Globals and constants variables.

class TestSILengthDimension(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.dim = SILengthDimension()

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testcalculate_preferred_km(self):
        value, units = self.dim.calculate_preferred(2000, 'm')
        self.assertAlmostEqual(2.0, value, 2)
        self.assertEqual('km', units)

    def testcalculate_preferred_m(self):
        value, units = self.dim.calculate_preferred(200, 'm')
        self.assertAlmostEqual(200.0, value, 2)
        self.assertEqual('m', units)

    def testcalculate_preferred_cm(self):
        value, units = self.dim.calculate_preferred(0.02, 'm')
        self.assertAlmostEqual(2.0, value, 2)
        self.assertEqual('cm', units)

    def testcalculate_preferred_cm2(self):
        value, units = self.dim.calculate_preferred(0.01, 'm')
        self.assertAlmostEqual(1.0, value, 2)
        self.assertEqual('cm', units)

    def testcalculate_preferred_mm1(self):
        value, units = self.dim.calculate_preferred(0.002, 'm')
        self.assertAlmostEqual(2.0, value, 2)
        self.assertEqual('mm', units)

    def testcalculate_preferred_mm2(self):
        value, units = self.dim.calculate_preferred(0.001, 'm')
        self.assertAlmostEqual(1.0, value, 2)
        self.assertEqual('mm', units)

    def testcalculate_preferred_mm3(self):
        value, units = self.dim.calculate_preferred(0.009, 'm')
        self.assertAlmostEqual(9.0, value, 2)
        self.assertEqual('mm', units)

    def testcalculate_preferred_nm(self):
        value, units = self.dim.calculate_preferred(2e-7, 'm')
        self.assertAlmostEqual(200.0, value, 2)
        self.assertEqual('nm', units)

    def testto_latex_cm(self):
        self.assertEqual('cm', self.dim.to_latex('cm'))

    def testto_latex_um(self):
        self.assertEqual('$\\mu$m', self.dim.to_latex(u'\u00b5m'))

class TestImperialLengthDimension(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.dim = ImperialLengthDimension()

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testcalculate_preferred_ft(self):
        value, units = self.dim.calculate_preferred(18, 'in')
        self.assertAlmostEqual(1.5, value, 2)
        self.assertEqual('ft', units)

    def testcalculate_preferred_yd(self):
        value, units = self.dim.calculate_preferred(120, 'in')
        self.assertAlmostEqual(3.33, value, 2)
        self.assertEqual('yd', units)

    def testcalculate_preferred_mi(self):
        value, units = self.dim.calculate_preferred(10000, 'ft')
        self.assertAlmostEqual(1.8939, value, 2)
        self.assertEqual('mi', units)

class TestSILengthReciprocalDimension(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.dim = SILengthReciprocalDimension()

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testcalculate_preferred_cm(self):
        value, units = self.dim.calculate_preferred(0.02, '1/m')
        self.assertAlmostEqual(2.0, value, 2)
        self.assertEqual('1/cm', units)

    def testcalculate_preferred_mm1(self):
        value, units = self.dim.calculate_preferred(0.002, '1/m')
        self.assertAlmostEqual(2.0, value, 2)
        self.assertEqual('1/mm', units)

    def testto_latex_cm(self):
        self.assertEqual('cm$^{-1}$', self.dim.to_latex('1/cm'))

    def testto_latex_um(self):
        self.assertEqual('$\mu$m$^{-1}$', self.dim.to_latex(u'1/\u00b5m'))

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()

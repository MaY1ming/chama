import unittest
from nose.tools import *
import os
from os.path import abspath, dirname, join, isfile
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import chama
        
testdir = dirname(abspath(__file__))
datadir = join(testdir, 'data')

class TestGraphics(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        x_grid = np.linspace(-100, 100, 21)
        y_grid = np.linspace(-100, 100, 21)
        z_grid = np.linspace(0, 40, 21)
        self.grid = chama.transport.Grid(x_grid, y_grid, z_grid)

        self.source = chama.transport.Source(-20, 20, 1, 1.5)

        self.atm = pd.DataFrame({'Wind Direction': [45,120,200], 
            'Wind Speed': [1.2,1,1.8], 'Stability Class': ['A','B','C']}, 
            index=[0,10,20])
    
        gauss_plume = chama.transport.GaussianPlume(self.grid, self.source, 
                                                    self.atm)
        self.signal = gauss_plume.conc
        
    @classmethod
    def tearDownClass(self):
        pass

    def test_signal_convexhull(self):
        filename = abspath(join(testdir, 'plot_signal_convexhull1.png'))
        if isfile(filename):
            os.remove(filename)
        
        plt.figure()
        chama.graphics.signal_convexhull(self.signal, ['S'], 0.001)
        plt.savefig(filename, format='png')
        plt.close()
        
        assert_true(isfile(filename))
    
    def test_signal_xsection(self):
        filename = abspath(join(testdir, 'plot_signal_xsection1.png'))
        if isfile(filename):
            os.remove(filename)
        
        plt.figure()
        chama.graphics.signal_xsection(self.signal, 'S')
        plt.savefig(filename, format='png')
        plt.close()
        
        assert_true(isfile(filename))

    def test_signal_animate(self):
        pass
        
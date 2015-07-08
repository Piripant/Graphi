from distutils.core import setup
import py2exe

setup(	name='Graphi',
		console=['StringManager.py'],
		options={"py2exe":{"includes":["sip"]}},
		version='1.0',
		py_modules=['DrawToFile', 'Equator', 'StringEquator'])
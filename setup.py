from setuptools import setup
import io

with io.open('README.rst', encoding = 'utf-8') as f:
	long_description = f.read()
	
setup(name = 'ulula',
	version = '0.2.2',
	description = 'A lightweight 2D hydro solver',
	long_description = long_description,
	url = 'https://bitbucket.org/bdiemer/ulula',
	author = 'Benedikt Diemer',
	author_email = 'diemer@umd.edu',
	license = 'MIT',
	requires = ['numpy', 'scipy', 'six', 'h5py'],
	packages = ['ulula', 'ulula.setups', 'ulula.examples'],
	classifiers = [
				'Environment :: Console',
				'Intended Audience :: Developers',
				'Intended Audience :: Education',
				'Intended Audience :: Science/Research',
				'License :: OSI Approved :: MIT License',
				'Operating System :: OS Independent',
				'Programming Language :: Python :: 2',
				'Programming Language :: Python :: 2.7',
				'Programming Language :: Python :: 3',
				'Programming Language :: Python :: 3.3',
				'Programming Language :: Python :: 3.4',
				'Programming Language :: Python :: 3.5',
				'Programming Language :: Python :: 3.6',
				'Programming Language :: Python :: 3.7',
				'Programming Language :: Python :: 3.8',
				'Topic :: Scientific/Engineering :: Astronomy',
				'Topic :: Scientific/Engineering :: Physics'
				],
	zip_safe = False)

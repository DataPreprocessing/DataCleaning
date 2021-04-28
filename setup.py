import setuptools
import os
import sys
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "README.md"), "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='data-cleaning',
     version='1.0',
     author="Murali krishna mopi devi, Induraj P.Ramamurthy",
     author_email="mopidevi@gmail.com, induraj.gandhian@yahoo.com",
     description="An utility to clean the data and return you the cleaned data",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/DataPreprocessing/DataCleaning",
     packages=setuptools.find_packages(),
     classifiers=[
         'Development Status :: 3 - Alpha',
         'Intended Audience :: Science/Research',
         'License :: OSI Approved :: MIT License',
         'Natural Language :: English',
         'Operating System :: OS Independent',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7',
         'Programming Language :: Python :: 3.8',
         'Topic :: Software Development :: Libraries :: Python Modules',
         'Topic :: Scientific/Engineering :: Artificial Intelligence',
     ],
    python_requires=">=3.6"
 )
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='dataprep',
     version='1.0',
     scripts=['dataprep'] ,
     author="Murali krishna mopi devi, Induraj P.Ramamurthy",
     author_email="mopidevi@gmail.com, induraj.gandhian@yahoo.com",
     description="An utility to clean the data and return you the cleaned data",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/DataPreprocessing/DataPrep",               ##########
     packages=setuptools.find_packages(),
     classifiers=[
         "Development Status :: 1- Alpha",
         "Intended Audience :: Science/Research/Python Developers", ## check this
         "Natural Language :: English",
         "Programming Language :: Python :: 3.7",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         "Topic :: Software Development :: Libraries :: Python Modules",
         "Topic :: Scientific/Engineering :: Artificial Intelligence",
     ],
 )
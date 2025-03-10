from setuptools import setup

setup(
    name="demuxalot",
    version='0.4.0',
    description="Scalable and reliable demultiplexing for single-cell RNA sequencing that refines genotypes",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Alex Rogozhnikov',
    packages=['demuxalot'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 ',
    ],
    keywords='genotype learning, single cell RNA sequencing, demultiplexing, bayesian modelling',
    install_requires=[
        'pysam',  # reads BAM files (alignment)
        'scipy',
        'numpy',
        'joblib',  # multiprocessing in separate processes
        'pandas',
        'pyarrow',  # required to read and write parquet files
    ],
)
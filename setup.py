from setuptools import setup, find_packages

setup(
    name='robofin',
    version='0.0.1',
    description='A collection of robotics tools tailored to machine learning',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'pybullet',
        'numpy',
        'pyquaternion',
        'geometrout',
        'torch>=1.10.0',
        'ikfast-pybind',
        'trimesh',
        'urchin'
    ]
)

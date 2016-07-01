from setuptools import setup, Extension
import platform

version = '2.7.0'

setup(name='dronekit',
      zip_safe=True,
      version=version,
      description='Developer Tools for Drones.',
      long_description='Python API for communication and control of drones over MAVLink.',
      url='https://github.com/dronekit/dronekit-python',
      author='3D Robotics',
      install_requires=[
          'pymavlink>=1.1.62',
          'monotonic<1.0'
      ],
      author_email='tim@3drobotics.com, kevinh@geeksville.com',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering',
      ],
      license='apache',
      packages=[
          'dronekit', 'dronekit.cloud', 'dronekit.test'
      ],
      ext_modules=[])

from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'counter_project'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'srv'), glob('srv/*.srv')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@xxx.com',
    description='ROS2 Counter Project',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'counter_node = counter_project.counter_node:main',
            'square_node = counter_project.square_node:main',
            'logger_node = counter_project.logger_node:main',
            'reset_service = counter_project.reset_service:main',
            'status_publisher = counter_project.status_publisher:main',
        ],
    },
)

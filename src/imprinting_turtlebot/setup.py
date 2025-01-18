from setuptools import setup

package_name = 'imprinting_turtlebot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/test.launch.py']),
        ('share/' + package_name, ['world/world.model']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuzu',
    maintainer_email='yuzu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'imprinting_turtlebot_node = imprinting_turtlebot.imprinting_turtlebot_node:main'
        ],
    },
)

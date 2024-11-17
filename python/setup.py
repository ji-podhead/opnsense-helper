from setuptools import setup
from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent.parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='opnsense_helper',
    version='0.1.26',    
    description='backend api for opnsense. assign lan interfaces, create vlans, vlan-interfaces and setup dhcp in a single script.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://ji-podhead.github.io/opnsense-helper/.docs/_build/html/index.html',
    author='ji-podhdead',
    author_email='ji.podhdead@proton.me',
    license='BSD 2-clause',
    packages=['opnsense_helper', "opnsense_helper.utils", "opnsense_helper.scripts", "opnsense_helper.commands", "opnsense_helper.config_manager"],
   # package_dir={'': 'python'},
    install_requires=['paramiko',                     
                      ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

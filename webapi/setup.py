from os.path import realpath, dirname, join
from setuptools import setup

if __name__ == '__main__':
    _reqs = []
    abspath = realpath(dirname(__file__))

    with open(join(abspath, 'requirements.txt')) as reqfile:
        _reqs = reqfile.readlines()

    setup(
        name='traefik-alb-demo',
        version='0.0.1a1',
        description='Traefik load balacing demo application',
        author='haliphax',
        packages=['demo'],
        install_requires=_reqs,
    )

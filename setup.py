from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)

setup(
    name="staccato",
    version="0.1.3",
    packages=find_packages(),
    install_requires = ['requests', 'requests_oauthlib'],
    author = "minamorl",
    description = "Twitter API wrapper for python 3",
    tests_require=['tox'],
    cmdclass={'test': Tox},
)

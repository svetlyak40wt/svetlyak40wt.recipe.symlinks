import os
from setuptools import setup, find_packages

def read(filename):
    return open(os.path.join(
        os.path.dirname(__file__), filename)).read()

entry_points = """
[zc.buildout]
    default = svetlyak40wt.recipe.symlinks:Symlinks

[zc.buildout.uninstall]
    default = svetlyak40wt.recipe.symlinks:uninstall_symlinks
"""

setup(
    version = '0.1.4',
    name = 'svetlyak40wt.recipe.symlinks',
    description = 'Simple recipe to collect symbolic links in one directory.',
    long_description = read('README.md'),
    classifiers = [
        'License :: OSI Approved :: BSD License',
        'Framework :: Buildout',
        'Programming Language :: Python',
    ],
    keywords = 'buildout recipe',
    author = 'Alexander Artemenko',
    author_email = 'svetlyak.40wt@gmail.com',
    url = 'http://githib.com/svetlyak40wt/svetlyak40wt.recipe.symlinks',
    license = 'New BSD License',
    packages = find_packages(),
    namespace_packages = ['svetlyak40wt', 'svetlyak40wt.recipe'],
    include_package_data = True,
    install_requires = [
        'zc.buildout',
        'zc.recipe.egg',
        'setuptools',
    ],
    zip_safe = False,
    entry_points = entry_points,
)

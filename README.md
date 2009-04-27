svetlyak40wt.recipe.symlinks
============================

Usage
-----

This is a simple buildout recipe to collect symbolic links.

For example, you have isolated buildout environment, but want
pull some files from a standart debian's distribution os pyexiv2.

In that case, you can collect all neccessary links in one directory
and add it as 'extra-path'. Here is a minimal buildout.cfg:

   [buildout]
   parts = pyexiv2 python

   [pyexiv2]
   recipe = svetlyak40wt.recipe.symlinks
   path = parts/pyexiv2
   files =
       /usr/share/pyshared/pyexiv2.py
       /usr/lib/python2.5/site-packages/libpyexiv2.so

   [python]
   recipe = zc.recipe.egg
   interpreter = python
   eggs = ipython
   extra-paths = ${pyexiv2:path}

Author
------

Alexander Artemenko <svetlyak.40wt@gmail.com>

Source
------

http://github.com/svetlyak40wt/svetlyak40wt.recipe.symlinks/

Feel free to comment, clone and send patches.


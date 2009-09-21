svetlyak40wt.recipe.symlinks
============================

Usage
-----

This is a simple buildout recipe to collect symbolic links.

For example, you have isolated buildout environment, but want
pull some files from a standart debian's distribution os pyexiv2.

In that case, you can collect all neccessary links in one directory
and add it as `extra-path`. Or use it to make symlink to django admin's
media directory.

Here is a minimal buildout.cfg:

    [buildout]
    parts = pyexiv2 python django-media

    [pyexiv2]
    recipe = svetlyak40wt.recipe.symlinks
    path = parts/pyexiv2
    files =
       /usr/share/pyshared/pyexiv2.py
       /usr/lib/python2.5/site-packages/libpyexiv2.so

    [django-media]
    recipe = svetlyak40wt.recipe.symlinks
    path = media
    files =
        ${buildout:parts-directory}/django/django/contrib/admin/media admin

    [python]
    recipe = zc.recipe.egg
    interpreter = python
    eggs = ipython
    extra-paths = ${pyexiv2:path}


ChangeLog
---------

### 0.1.2

Added ability to supply custom link name. So, if you specify files=`/blah/minor foo`
and `path=media`, then file `/blah/minor` will be linked as `media/foo`.

### 0.1.1

Fixed bug when first directories of the `path` don't exist.

### 0.1.0

Initial release. Seems that all work as supposed.


Author
------

Alexander Artemenko svetlyak.40wt at gmail.com


Source
------

<http://github.com/svetlyak40wt/svetlyak40wt.recipe.symlinks/>

Feel free to comment, clone and send patches.


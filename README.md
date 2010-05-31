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
       /tmp my-temp

    [django-media]
    recipe = svetlyak40wt.recipe.symlinks
    path = media
    files =
        ${buildout:parts-directory}/django/django/contrib/admin/media admin

    [django-egg-media]
    # Another way to link into the egg
    recipe = svetlyak40wt.recipe.symlinks
    path = media
    files =
        Django://django/contrib/admin/media admin

    [django-cms-egg-media]
    # An egg where the egg name differs from the first path segment
    recipe = svetlyak40wt.recipe.symlinks
    path = media
    files =
        django-cms://cms/media/cms

    [python]
    recipe = zc.recipe.egg
    interpreter = python
    eggs = ipython
    extra-paths = ${pyexiv2:path}


ChangeLog
---------

### 0.2.0

#### Backward incompatibilities:

Changed the way how paths into eggs are computed. Removed package.key from beeing
the first path segment. For example, if you used:

    Django://contrib/admin/media admin

It should be replaced with

    Django://django/contrib/admin/media admin

This allows to refer resources with diffrerent initial segments.

### 0.1.4

Added ability to link resources inside egg, using following syntax: package://relative-path
Now recipe removes old link when target changes.

### 0.1.3

Prevent zc.buildout from removing all directory content on uninstall. Now script removes
just those symlinks which was created during the previous call. Thanks to Shaun Sephton
for the patch.

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

Credits
-------

* Shaun Sephton: patch to remove symlinks only.
* Johannes Bornhold: patch to refer different resources within the package.


Source
------

<http://github.com/svetlyak40wt/svetlyak40wt.recipe.symlinks/>

Feel free to comment, clone and send patches.


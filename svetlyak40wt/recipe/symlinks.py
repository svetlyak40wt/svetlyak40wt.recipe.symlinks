import logging
import os
import zc.buildout
import pkg_resources
from zc.recipe.egg import Egg



class Symlinks(Egg):
    """Put symlinks to different files, into one directory.
       For example, such section can be defined to bring pyexiv2,
       from standart debian package to isolated buildout:

           [buildout]
           parts = pyexiv2 etree python

           [pyexiv2]
           recipe = svetlyak40wt.recipe.symlinks
           path = parts/pyexiv2
           files =
               /usr/share/pyshared/pyexiv2.py
               /usr/lib/python2.5/site-packages/libpyexiv2.so

           [etree]
           # This syntax uses pkg_resources to locate right path
           # to the module resource.
           path = parts/etree
           files =
               xml://xml/etree ElementTree

           [python]
           recipe = zc.recipe.egg
           interpreter = python
           eggs = ipython
           extra-paths =
               ${pyexiv2:path}
               ${etree:path}
    """
    def __init__(self, buildout, name, options):
        super(Symlinks, self).__init__(buildout, name, options)
        self.name, self.options = name, options
        options['path'] = os.path.join(
                              buildout['buildout']['directory'],
                              options['path'],
                              )


    def install(self):
        path = self.options['path']
        logger = logging.getLogger(self.name)
        logger.info(
            'Creating directory %s' % os.path.basename(path))
        if not os.path.exists(path):
            os.makedirs(path)

        files = (file for file in self.options['files'].split('\n') if file)
        for file in files:
            file = file.split(None, 1)
            if len(file) == 2:
                file, as_ = file
            else:
                file = file[0]
                as_ = os.path.basename(file)

            if '://' in file:
                file = self._get_resource_filename(file)

            to = os.path.join(path, as_)
            if os.path.islink(to) and os.readlink(to) != file:
                logger.info('Removing symlink from "%s" to "%s"' % (os.readlink(to), to))
                os.remove(to)

            if not os.path.exists(to):
                logger.info('Making symlink from "%s" to "%s"' % (file, to))
                os.symlink(file, to)
        
        # Since other processes may create resources in path it 
        # should be excluded during uninstall, so return empty list.
        # We can't return list of created symlinks as buildout does not
        # currently support symlink removal, see uninstall_symlinks below.
        return []


    def update(self):
        pass


    def _get_resource_filename(self, uri):
        logger = logging.getLogger(self.name)
        logger.info('getting resource filename for uri "%s"' % uri)

        package, path = uri.split('://', 1)

        self.options['eggs'] = package
        ws = self.working_set()[1]
        distributions = ws.require(package)

        if not distributions:
            raise RuntimeError('Can\'t find package "%"' % package)

        package = distributions[0]

        result = os.path.join(package.location, path)
        logger.info('resource filename for uri "%s" is "%s"' % (uri, result))
        return result



def uninstall_symlinks(name, options):
    """
    Buildout does not currently support symlink removal.
    This uninstall method removes created symlinks.

    Inspired by https://bugs.launchpad.net/zc.buildout/+bug/144228
    """
    path = options['path']
    files = (file for file in options['files'].split('\n') if file)
    for file in files:
        file = file.split(None, 1)
        if len(file) == 2:
            file, as_ = file
        else:
            file = file[0]
            as_ = os.path.basename(file)

        to = os.path.join(path, as_)
        if os.path.isfile(to) or os.path.islink(to):
            os.remove(to)


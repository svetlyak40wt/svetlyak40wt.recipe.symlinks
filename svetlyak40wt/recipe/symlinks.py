import logging, os, zc.buildout

class Symlinks:
    """Put symlinks to different files, into one directory.
       For example, such section can be defined to bring pyexiv2,
       from standart debian package to isolated buildout:

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
    """
    def __init__(self, buildout, name, options):
        self.name, self.options = name, options
        options['path'] = os.path.join(
                              buildout['buildout']['directory'],
                              options['path'],
                              )


    def install(self):
        path = self.options['path']
        logger = logging.getLogger(self.name)
        logger.info(
            'Creating directory %s', os.path.basename(path))
        if not os.path.exists(path):
            os.makedirs(path)

        files = (file for file in self.options['files'].split('\n') if file)
        for file in files:
            to = os.path.join(path, os.path.basename(file))
            if not os.path.exists(to):
                logger.info('Making symlink from "%s" to "%s"' % (file, to))
                os.symlink(file, to)
        return path

    def update(self):
        pass


class StringMixin(object):
    def __repr__(self):
        classname  = self.__class__.__name__
        attributes = ', '.join('%s: %s' % item for item in sorted(vars(self).items()))
        return '%s { %s }' % (classname, attributes)
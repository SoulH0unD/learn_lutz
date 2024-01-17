class ListInherited:
    """
    Применяет dir() для сбора атрибутов экземпляра и имен, унаследованных
    из его классов;
    в Python З.Х отображается больше имен, чем в Python 2.Х из-за наличия
    подразумеваемого суперкласса object в модели классов нового стиля;
    getattr() извлекает унаследованные имена не в self.__ diet__ ;
    используйте __ str__ , а не __ герг__ , иначе произойдет зацикливание при
    вызове связанных методов!
    """
      
    def __attrnames(self):
        result = ''
        for attr in dir(self):                                      # instance dir
            if attr[:2] == '__' and attr[-2:] == '__':              # skip internals
                result += '\t%s\n' % attr
            else:
                result += '\t%s=%s\n' % (attr, getattr(self,attr))
        return result

    def __str__(self):
        return 'Instance of %s, address %s\n%s' % (
            self.__class__.__name__,                                # class name
            id(self),                                               # address
            self.__attrnames()                                      # name = value list
        )


if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)
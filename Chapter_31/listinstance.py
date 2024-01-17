class ListInstance:
    """
    Подмешивает класс, который представляет форматированную функцию
    print() или str() для экземпляров через наследование реализованного
    в нем метода __str__; отображает только атрибут экземпляра; self
    является экземпляром самого нижнего класа;
    имена __X предотвращают конфликты с атрибутами клиента
    """

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result
    
    def __str__(self):
        return '<Instance of %s, address %s:\n%s' % (
                        self.__class__.__name__,
                        id(self),
                        self.__attrnames())
    
if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInstance)

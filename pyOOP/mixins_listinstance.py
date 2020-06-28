#!/usr/bin/env python
# listinstance.py defines a mix-in class -- ListInstance -- that overloads the
# __str__ method for all classes that include it in their header lines.


class ListInstance:
    """Mix-in class that provides a formatted print() or str() of instances via
    inheritance of __str__ coded here; displays instance attrs only; self is
    instance of lowest class; __X names avoid clashing with client's attrs
    """
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += f"\t{attr}={self.__dict__[attr]}\n"
        return result

    def __str__(self):
        return "<Instance of {}, address {}:\n{}>".format(
            self.__class__.__name__,  # fetches name of instance's class
            id(self),
            self.__attrnames())


if __name__ == "__main__":
    import testmixin
    testmixin.tester(ListInstance)

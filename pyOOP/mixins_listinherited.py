#!/usr/bin/env python
# use dir() instead of loop though __dict__, the latter holds instance
# attributes only, but the former also collects all inherited attributes.


class ListInherited:
    """Use dir() to collect both instance attrs and names inherited from its
    classes; Python3.X shows more names than 2.X because of the implied object
    superclass in the new-style class model; getattr() fetches inherited names
    not in self.__dict__; use __str__, not __repr__, or else this loops when
    printing bound methods!
    """
    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += f"\t{attr}\n"
            else:
                result += f"\t{attr}={getattr(self, attr)}\n"
        return result

    def __attrnames2(self, indent=' '*4):
        others = ''
        unders = []
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                unders.append(attr)
            else:
                display = str(getattr(self, attr))[:82-(len(indent)+len(attr))]
                others += f"{indent}{attr}={display}\n"
        return f"Unders{'-'*77}\n{indent}{', '.join(unders)}\nOthers{'-'*77}\n{others}"

    def __str__(self):
        return "<Instance of {}, address {}:\n{}>".format(
            self.__class__.__name__,  # fetches name of instance's class
            id(self),
            self.__attrnames2())


if __name__ == "__main__":
    import testmixin
    testmixin.tester(ListInherited)

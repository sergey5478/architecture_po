# import zope.interface
from abc import ABC, ABCMeta, abstractmethod, abstractproperty


# # "интерфейс"
# class Test1(zope.interface.Interface):
#     def test(self):
#         pass
#
#
# # "интерфейс"
# class Test2(zope.interface.Interface):
#     def test(self):
#         pass
#
#
# class A(object):
#     zope.interface.implements(Test1)


class ATest(ABC):
    @abstractmethod
    def test_a(self):
        pass


class BTest(ABC):
    @abstractmethod
    def test_b(self):
        pass


class CTest(ATest, BTest):
    def test_a(self):
        print('a')

    def test_b(self):
        print('b')


if __name__ == '__main__':
    c = CTest()
    c.test_a()
    c.test_b()

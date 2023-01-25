"""
type(object_or_name, bases, dict)
type(object) -> the object's type
type(name, bases, dict) -> a new type
"""


def mro(self, *args, **kwargs):  # real signature unknown
    """ Return a type's method resolution order. """
    pass


def __call__(self, *args, **kwargs):  # real signature unknown
    """ Call self as a function. """
    pass


def __delattr__(self, *args, **kwargs):  # real signature unknown
    """ Implement delattr(self, name). """
    pass


def __dir__(self, *args, **kwargs):  # real signature unknown
    """ Specialized __dir__ implementation for types. """
    pass


def __getattribute__(self, *args, **kwargs):  # real signature unknown
    """ Return getattr(self, name). """
    pass


def __init__(cls, what, bases=None, dict=None):  # known special case of type.__init__
    """
    type(object_or_name, bases, dict)
    type(object) -> the object's type
    type(name, bases, dict) -> a new type
    # (copied from class doc)
    """
    pass


def __instancecheck__(self, *args, **kwargs):  # real signature unknown
    """ Check if an object is an instance. """
    pass


@staticmethod  # known case of __new__
def __new__(*args, **kwargs):  # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass


def __or__(self, *args, **kwargs):  # real signature unknown
    """ Return self|value. """
    pass


def __prepare__(self):  # real signature unknown; restored from __doc__
    """
    __prepare__() -> dict
    used to create the namespace for the class statement
    """
    return {}


def __repr__(self, *args, **kwargs):  # real signature unknown
    """ Return repr(self). """
    pass


def __ror__(self, *args, **kwargs):  # real signature unknown
    """ Return value|self. """
    pass


def __setattr__(self, *args, **kwargs):  # real signature unknown
    """ Implement setattr(self, name, value). """
    pass


def __sizeof__(self, *args, **kwargs):  # real signature unknown
    """ Return memory consumption of the type object. """
    pass


def __subclasscheck__(self, *args, **kwargs):  # real signature unknown
    """ Check if a class is a subclass. """
    pass


def __subclasses__(self, *args, **kwargs):  # real signature unknown
    """ Return a list of immediate subclasses. """
    pass


__abstractmethods__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

__annotations__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

__bases__ = (
    object,
)
__base__ = object
__basicsize__ = 888
__dictoffset__ = 264
__dict__ = None  # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x00007FFAD538A920>, '__repr__': <slot wrapper '__repr__' of 'type' objects>, '__call__': <slot wrapper '__call__' of 'type' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'type' objects>, '__setattr__': <slot wrapper '__setattr__' of 'type' objects>, '__delattr__': <slot wrapper '__delattr__' of 'type' objects>, '__init__': <slot wrapper '__init__' of 'type' objects>, '__or__': <slot wrapper '__or__' of 'type' objects>, '__ror__': <slot wrapper '__ror__' of 'type' objects>, 'mro': <method 'mro' of 'type' objects>, '__subclasses__': <method '__subclasses__' of 'type' objects>, '__prepare__': <method '__prepare__' of 'type' objects>, '__instancecheck__': <method '__instancecheck__' of 'type' objects>, '__subclasscheck__': <method '__subclasscheck__' of 'type' objects>, '__dir__': <method '__dir__' of 'type' objects>, '__sizeof__': <method '__sizeof__' of 'type' objects>, '__basicsize__': <member '__basicsize__' of 'type' objects>, '__itemsize__': <member '__itemsize__' of 'type' objects>, '__flags__': <member '__flags__' of 'type' objects>, '__weakrefoffset__': <member '__weakrefoffset__' of 'type' objects>, '__base__': <member '__base__' of 'type' objects>, '__dictoffset__': <member '__dictoffset__' of 'type' objects>, '__mro__': <member '__mro__' of 'type' objects>, '__name__': <attribute '__name__' of 'type' objects>, '__qualname__': <attribute '__qualname__' of 'type' objects>, '__bases__': <attribute '__bases__' of 'type' objects>, '__module__': <attribute '__module__' of 'type' objects>, '__abstractmethods__': <attribute '__abstractmethods__' of 'type' objects>, '__dict__': <attribute '__dict__' of 'type' objects>, '__doc__': <attribute '__doc__' of 'type' objects>, '__text_signature__': <attribute '__text_signature__' of 'type' objects>, '__annotations__': <attribute '__annotations__' of 'type' objects>})"
__flags__ = 2148031744
__itemsize__ = 40
__mro__ = (
    None,  # (!) forward: type, real value is "<class 'type'>"
    object,
)
__name__ = 'type'
__qualname__ = 'type'
__text_signature__ = None
__weakrefoffset__ = 368

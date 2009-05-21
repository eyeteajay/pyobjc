# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _blend_equation_separate

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


__version__ = _blend_equation_separate.__version__
__date__ = _blend_equation_separate.__date__
__api_version__ = _blend_equation_separate.__api_version__
__author__ = _blend_equation_separate.__author__
__doc__ = _blend_equation_separate.__doc__

glBlendEquationSeparateEXT = _blend_equation_separate.glBlendEquationSeparateEXT
GL_BLEND_EQUATION_ALPHA_EXT = _blend_equation_separate.GL_BLEND_EQUATION_ALPHA_EXT

glInitBlendEquationSeparateEXT = _blend_equation_separate.glInitBlendEquationSeparateEXT

__info = _blend_equation_separate.__info

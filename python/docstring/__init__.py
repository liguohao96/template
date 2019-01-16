"""
Python Template for docstring
=============================

python.docstring is a package cotaining TEMPLATE for docstring in python. 
usage:
    >>> from python import docstring
    >>> help(docstring)
    >>> print(docstring.module_.__doc__)
    >>> print(docstring.class_.__doc__)
    >>> print(docstring.method_.__doc__)
"""

import importlib
import os

from . import module as module_ 
from .method import template_method as method_
spec = importlib.util.spec_from_file_location('class', os.path.join(os.path.dirname(__file__), 'class.py'))
class_ = importlib.util.module_from_spec(spec)
spec.loader.exec_module(class_)
class_ = class_.TemplateClass
TemplateClass = class_  # TODO: change type(TemplateClass()) to '<class python.docstring.TemplateClass>'

del spec, os, importlib
"""
Python Template for docstring
-----------------------------

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

spec = importlib.util.spec_from_file_location(
    '.'.join([__name__, 'module']), os.path.join(os.path.dirname(__file__), 'module.py'))
module_ = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module_)

spec = importlib.util.spec_from_file_location(
    'method', os.path.join(os.path.dirname(__file__), 'method.py'))
method_ = importlib.util.module_from_spec(spec)
spec.loader.exec_module(method_)
method_ = method_.template_method
method_.__module__ = __name__

spec = importlib.util.spec_from_file_location(
    'class', os.path.join(os.path.dirname(__file__), 'class.py'))
class_ = importlib.util.module_from_spec(spec)
spec.loader.exec_module(class_)
class_ = class_.TemplateClass
class_.__module__ = __name__

del spec, os, importlib

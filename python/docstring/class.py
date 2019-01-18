"""
class docstring template
------------------------
"""


class TemplateClass(object):
    """TemplateClass(position_arg1, position_arg2, 
            keyword_arg1=None, keyword_arg2=1)

    Description of this class should be put here.

    Parameters
    ---
    position_arg1 : int
        description for position_arg1
    position_arg2 : str or int
        description for position_arg2
    keyword_arg1 : int, optional
        description for keyword_arg1, by default 'None'
    keyword_arg2 : int, str or None, optional
        description for keyword_arg2, by default 'None'

    Attributes
    ---
    attr1 : int
        RO description for attr1
    attr2 : str
        RW description for attr2

    Examples
    ---
    Example1:
        >>> template_class = TemplateClass(0,0,0,0)

    Notes:
    ---
    supplyment for description, describe black magic used in this class.
    """

    def __init__(self):
        """
        """
        super().__init__()
        pass

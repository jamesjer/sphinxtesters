""" Sphinxtesters package
"""

from .sphinxutils import (Converter, UnicodeOutput, SourcesBuilder,
                          ModifiedPageBuilder)

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

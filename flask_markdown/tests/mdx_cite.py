"""
Taken from Cite Extension for Python-Markdown.

Used here only as a markdown extension test.

For documentation and more information about Cite plugin
see: https://github.com/aleray/mdx_cite
"""
import markdown
from markdown.inlinepatterns import SimpleTagPattern

CITE_RE = r'(\|{3})(.+?)\2'


class CiteExtension(markdown.extensions.Extension):
    """Adds cite extension to Markdown class."""

    def extendMarkdown(self, md, md_globals):
        """Modify inline patterns."""
        md.inlinePatterns.add(
            'cite',
            SimpleTagPattern(
                CITE_RE,
                'cite'
            ),
            '<not_strong'
        )


def makeExtension(configs={}):
    """Make the Cite Extension."""
    return CiteExtension(configs=dict(configs))

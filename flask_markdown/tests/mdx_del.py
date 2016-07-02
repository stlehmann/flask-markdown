"""
Example of a Del extension.

Used here only as a markdown extension test.

"""
import markdown
from markdown.inlinepatterns import SimpleTagPattern

DEL_RE = r'(~~)(.*?)~~'


class DelExtension(markdown.extensions.Extension):
    """Adds cite extension to Markdown class."""

    def extendMarkdown(self, md, md_globals):
        """Modify inline patterns."""
        md.inlinePatterns.add(
            'del',
            SimpleTagPattern(
                r'(\~{2})(.+?)\2',
                'del'
            ),
            '<not_strong'
        )


def mdx_del(configs={}):
    """Make the Cite Extension."""
    return DelExtension(configs=dict(configs))

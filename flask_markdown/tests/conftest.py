"""Initialize flask app for pytest."""

import pytest
from flask import Flask, render_template_string
from flask_markdown import Markdown
from .mdx_cite import makeExtension
from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagPattern


@pytest.fixture
def app():
    """Create testing application."""
    app = Flask(__name__)
    md = Markdown(app, auto_escape=True, auto_reset=True)

    @app.route('/test_filter_inline')
    def render_filter_inline():
        mystr = 'This is *markdown*'
        return render_template_string('{{mystr|markdown}}', mystr=mystr)

    @app.route('/test_filter_block_string')
    def filter_block_string():
        mystr = 'This is a *markdown* block'
        template = """{% filter markdown %}{{mystr}}{% endfilter %}"""
        return render_template_string(template, mystr=mystr)

    @app.route('/test_filter_block')
    def filter_block():
        tmp = '{% filter markdown %}This is a *markdown* block{% endfilter %}'
        return render_template_string(tmp)

    @app.route('/test_filter_autoescape_off')
    def filter_autoescape_off():
        mystr = 'This is a <b>markdown</b> block'
        result = render_template_string(
            ('{% autoescape false %}'
             '{{mystr|markdown}}'
             '{% endautoescape %}'), mystr=mystr)
        return result

    @app.route('/test_filter_autoescape_on')
    def filter_autoescape_on():
        mystr = 'This is a <b>markdown</b> block'
        result = render_template_string(
            ('{% autoescape true %}'
             '{{mystr|markdown}}'
             '{% endautoescape %}'), mystr=mystr)
        return result

    @app.route('/test_extension')
    def test_extension():
        md.register_extension(makeExtension)
        mystr = '|||I am a cite tag|||'
        return render_template_string('{{mystr|markdown}}', mystr=mystr)

    @app.route('/test_decorator')
    def test_decorator():
        @md.extend()
        class deleteExtension(Extension):
            def extendMarkdown(self, md, md_globals):
                # Create the del pattern
                del_tag = SimpleTagPattern(r'(--)(.*?)--', 'del')
                # Insert del pattern into markdown parser
                md.inlinePatterns.add('del', del_tag, '>not_strong')
                md.registerExtension(self)
        mystr = '--Some Deleted Test--'
        return render_template_string('{{mystr|markdown}}', mystr=mystr)
    return app

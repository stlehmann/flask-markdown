"""
# Tests: for Flask_Markdown.

A series of tests of the Markdown functionality.

## TODO:

1. Test extentions (use common built in)
"""

from flask import url_for


def test_filter_inline(client):
    """
    Test: Render markdown inline.

    {{ 'This is *markdown*' |markdown}}

    which should become:

    <p>This is <em>markdown</em></p>
    """
    response = client.get(url_for('render_filter_inline'))
    assert (
        response.data.decode("utf-8") ==
        '<p>This is <em>markdown</em></p>'
    )


def test_filter_block_string(client):
    """
    Test: Filter Block w/ String Variable.

    mystr = 'This is a *markdown* block'
    {% filter markdown %}{{mystr}}{% endfilter %}

    which should become:

    <p>This is <em>markdown</em> block</p>
    """
    response = client.get(url_for('filter_block_string'))
    assert (
        response.data.decode("utf-8") ==
        '<p>This is a <em>markdown</em> block</p>'
    )


def test_filter_block(client):
    """
    Test: Filter Block w/ String Variable.

    {% filter markdown %}This is a *markdown* block{% endfilter %}

    which should become:

    <p>This is <em>markdown</em> block</p>
    """
    response = client.get(url_for('filter_block'))
    assert (
        response.data.decode("utf-8") ==
        '<p>This is a <em>markdown</em> block</p>'
    )


def test_filter_autoescape_off(client):
    """
    Test: Filter w/ auto_escape=False.

    {% autoescape false %}
    {{'This is a <b>markdown</b> block'|markdown}}
    {% endautoescape %}

    which should become:

    <p>This is <b>markdown</b> block</p>
    """
    response = client.get(url_for('filter_autoescape_off'))
    assert (
        response.data.decode("utf-8") ==
        '<p>This is a <b>markdown</b> block</p>'
    )


def test_filter_autoescape_on(client):
    """
    Test: Filter w/ auto_escape=True.

    {% autoescape true %}
    {{'This is a <b>markdown</b> block'|markdown}}
    {% endautoescape %}

    which should become:

    <p>This is a &lt;b&gt;markdown&lt;/b&gt; block</p>
    """
    response = client.get(url_for('filter_autoescape_on'))
    assert (
        response.data.decode("utf-8") ==
        '<p>This is a &lt;b&gt;markdown&lt;/b&gt; block</p>'
    )


def test_register_extension(client):
    """
    Test: Register Extension.

    |||I am a cite tag|||

    which should become:

    <p><cite>I am a cite tag</cite></p>
    """
    response = client.get(url_for('test_extension'))
    assert (
        response.data.decode("utf-8") ==
        '<p><cite>I am a cite tag</cite></p>'
    )


def test_register_decorator(client):
    """
    Test: Register Decorator.

    |||I am a cite tag|||

    which should become:

    <p><cite>I am a cite tag</cite></p>
    """
    response = client.get(url_for('test_decorator'))
    assert (
        response.data.decode("utf-8") ==
        '<p><del>Some Deleted Test</del></p>'
    )

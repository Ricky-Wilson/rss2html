#!/usr/bin/env python

""" Simple rss to html converter """

__version__ = "0.0.2"
__author__ = "Ricky L Wilson"
__email__ = "echoquote@gmail.com"

from feedparser import parse as parsefeed
import StringIO

def entry2html(**kwargs):
    """
    Transform the entries in a feedparser object into into html.
    """
    # returns a utf-8 encoded unicode string.
    # convert_feed will write this to a StringIO.StringIO file like object
    return u"""
    <span class='entry-title'>{title}</span>
    <a class='entry-link' href='{link}'>{title}</a>
    <span class='entry-description'>{description}</span>
    """.format(**kwargs).encode('utf-8')


def meta2html(**kwargs):
    """
    Transform the meta information of a feedparser object into
    into html.
    """
    # returns a utf-8 encoded unicode string.
    # convert_feed will write this to a StringIO.StringIO file like object
    return u"""
    <span class='feed-title'>{title}</span>
    <span class='feed-date'>{date}</span>
    <span class='feed-description'>{description}</span>
    """.format(**kwargs).encode('utf-8')


def convert_feed(**kwargs):
    """
    convert_feed(url='http://stackoverflow.com/feeds')
    """
    out = StringIO.StringIO("")
    url = kwargs['url']
    tmp = parsefeed(url)
    feed = tmp.feed
    entries = tmp.entries
    print >>out, meta2html(title=feed.title,
                        description=feed.description,
                        date=feed.date)

    for entry in entries:
        print >>out, entry2html(title=entry.title,
                                link=entry.link,
                                description=entry.description)
    return out.getvalue()


if __name__ == '__main__':
    print convert_feed(url='http://stackoverflow.com/feeds')


#!/usr/bin/env python

""" Simple rss to html converter """

__version__ = "0.0.2"
__author__ = "Ricky L Wilson"
__email__ = "echoquote@gmail.com"

from feedparser import parse as parsefeed
import StringIO

def entry2html(**kwargs):
    """ Base template for formating rss entries """
    template = u"""
    <span class='entry-title'>{title}</span>
    <a class='entry-link' href='{link}'>{title}</a>
    <span class='entry-description'>{description}</span>
    """
    return template.format(**kwargs).encode('utf-8')


def feedinfo(**kwargs):
    """ Format feed meta data """
    return u"""
    <span class='feed-title'>{title}</span>
    <span class='feed-date'>{date}</span>
    <span class='feed-description'>{description}</span>
    """.format(**kwargs).encode('utf-8')


def convert_feed(**kwargs):
    """ Convert a single rss feed to html """
    out = StringIO.StringIO("")
    url = kwargs['url']
    tmp = parsefeed(url)
    feed = tmp.feed
    entries = tmp.entries
    print >>out, feedinfo(title=feed.title,
                        description=feed.description,
                        date=feed.date)

    for entry in entries:
        print >>out, entry2html(title=entry.title,
                                link=entry.link,
                                description=entry.description)
    return out.getvalue()


def convert_feeds(**kwargs):
    """ Convert multiple rss feeds to html """
    for url in kwargs['urls']:
        print convert_feed(url=url)


if __name__ == '__main__':
    convert_feeds(urls=['http://stackoverflow.com/feeds'])


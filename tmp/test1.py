
from feedparser import parse as parsefeed

def entry2html(**kwargs):
    """ Format feedparser entry """
    template = u"""
    <h2 class='title'>{title}</h2>
    <a class='link' href='{link}'>{title}</a>
    <span class='description'>{description}</span>
    """
    return template.format(**kwargs)

def convert_feed(**kwargs):
    """ Main loop """
    out = u'\n'.join(entry2html(**entry) 
                    for entry in parsefeed(kwargs['url']).entries)
    return out.encode('utf-8')




print convert_feed(url='http://stackoverflow.com/feeds')

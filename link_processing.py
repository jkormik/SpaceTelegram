import os
from urllib.parse import urlparse, unquote


def get_file_format_from_link(link):
    unquoted = unquote(link)
    parsed = urlparse(unquoted)
    splited_parsed_path = os.path.splitext(parsed.path)
    return splited_parsed_path[-1]

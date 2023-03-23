import re

def url_to_name(repo):
    if re.match(r"https?://github.com/(.*)/(.*)", repo): # if a URL was passed
        repo_name = re.match(r"https?://github.com/(.*)/(.*)", repo).group(1) + "/" + re.match(r"https?://github.com/(.*)/(.*)", repo).group(2)
    else:
        repo_name = repo
    return repo_name
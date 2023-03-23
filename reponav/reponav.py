from github import Github
from .utils import url_to_name

def get_struct(repo):
    repo = url_to_name(repo) # convert urls
    g = Github()
    repo = g.get_repo(repo)
    print(f"Repository: {repo.full_name}\n")
    contents = repo.get_contents("")
    print_contents(contents)

def print_contents(contents, indent_level=0):
    from __init__ import repo # import inside the function to avoid circular import
    for content in contents:
        if content.type == "dir":
            print("  " * indent_level + f"📁 {content.name}")
            print_contents(repo.get_contents(content.path), indent_level + 1)
        else:
            print("  " * indent_level + f"📄 {content.name}")

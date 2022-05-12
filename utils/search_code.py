import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
EXAMPLE_APPS_DIR = os.path.join(ROOT_DIR, "pages", "examples")

"""
Note:  The file names of the example apps must be unique, even if they are in subdirectories.  This will make it 
       possible to match the example app file name with the correct page in the dash.page_registry, even if the 
       file structure for two are different.
"""


def code_files():
    code = {}
    for filename in os.listdir(EXAMPLE_APPS_DIR):
        if not filename.startswith("_") and filename.endswith(".py"):
            with open(os.path.join(EXAMPLE_APPS_DIR, filename), encoding="utf-8") as f:
                content = f.read()
            filename = filename.replace(".py", "")
            if filename in code:
                raise Exception(
                    f"filenames must be unique.  `{filename}.py` already exists"
                )
            code[filename] = content
    return code


sourcecode = code_files()


def search_code_files(searchterms, case_sensitive):
    """
    returns a list of filenames of the example apps that contain the search terms
    todo: search for exact string, and/or
    """
    filtered = []
    for filename, code in sourcecode.items():
        if not case_sensitive:
            code = code.lower()
            searchterms = searchterms.lower()

        if searchterms in code:
            filtered.append(filename)
    return filtered
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append(1, '/child-project/child_project_module')
from flask import Request
import print_child
from root_project_module import print_parent


def process_request(request: Request) -> str:
    """HTTP Cloud Function entry point."""

    print_parent()
    print_child()

    return "Done"

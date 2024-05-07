import os

if bool(int(os.environ.get("DEBUG", 1))):
    from .dev import *
else:
    from .prod import *

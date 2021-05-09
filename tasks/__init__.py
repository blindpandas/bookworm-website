# -*- coding: utf-8 -*-

import os
from pathlib import Path
os.chdir(str(Path(__file__).parent.parent))


from invoke import task, Collection
from . import pelican
from . import images

# Task collections    
ns = Collection()
ns.add_collection(pelican)
ns.add_collection(images)


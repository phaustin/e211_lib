from setuptools_scm import get_version
from pathlib import Path
this_dir = Path().resolve()
print(this_dir)
root_dir = this_dir.parents[1].resolve()
print(str(root_dir))
version = get_version(root=str(root_dir))
print(version)

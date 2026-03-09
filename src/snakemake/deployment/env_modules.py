__author__ = "Johannes Köster"
__copyright__ = "Copyright 2022, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"


import hashlib


class EnvModules:
    def __init__(self, module_names=None, precommand=None):
        self.names = module_names if module_names is not None else []
        self.precommand = precommand

    def shellcmd(self, cmd):
        """Return shell command with given modules loaded."""
        precommand_str = ''
        if self.precommand is not None:
            precommand_str = f"{self.precommand} && "
        to_load = " ".join(self.names)
        return f"{precommand_str}module purge && module load {to_load}; {cmd}"

    def __str__(self):
        return ", ".join(self.names)

    @property
    def hash(self) -> str:
        md5hash = hashlib.md5(usedforsecurity=False)
        for name in self.names:
            md5hash.update(name.encode())
        return md5hash.hexdigest()

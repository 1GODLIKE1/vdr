from pathlib import Path

class Tree:
    def __init__(self, RELEASE_PATH, VERSION):
        self.DIR = fr"{RELEASE_PATH}/{VERSION}/"

    def tree(self):
        path = Path(self.DIR)
        files = [str(f.absolute()) for f in path.glob("**/*") if f.is_file()]
        return files
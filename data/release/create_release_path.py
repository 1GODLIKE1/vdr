class ReleasePath:
    def __init__(self, JSON_FULL):
        self.JSON_FULL = JSON_FULL


    def release_path(self):
        pass

    def info(self, *args):
        for arr in args[0]:
            if str(arr).endswith(args[1]):
                return True
        return False
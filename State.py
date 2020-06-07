class State:

    def __init__(self, nm, isF, isT):
        self.name = nm
        self.isFinal = isF
        self.isTrap = isT

    def __str__(self):
        return self.name + " | isFinal:" + str(self.isFinal) + ", isTrap" + str(self.isTrap)


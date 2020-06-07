class Transition:

    def __init__(self, start, target, lbls):
        self.startS = start
        self.targetS = target
        self.labels = lbls

    def __str__(self):
        lbls = ','.join(self.labels)
        return self.startS.name + " --" + lbls + "--> " + self.targetS.name

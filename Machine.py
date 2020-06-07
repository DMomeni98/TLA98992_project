class Machine:
    def __init__(self, ab, sts, trans, t):
        self.alphabet = ab
        self.states = sts
        self.transactions = trans
        self.type = t

    def __str__(self):
        ab = ', '.join(self.alphabet)
        sts = ',\n'.join([str(i) for i in self.states])
        trans = ',\n'.join([str(i) for i in self.transactions])
        return "machine type: " + self.type + "\nalphabet: " + ab + "\nstates:\n" + sts + "\ntransitions:\n" + trans

    def check_string(self, string):
        success = False
        trans = []
        string_index = 0
        pointer = self.get_start_state()
        while string_index < len(string) and not success:
            if string[string_index] not in self.alphabet:
                print("invalid alphabet")
                break
            self.find_transition(pointer,string[string_index])

        if success:
            print("accepted")
        else:
            print("failed")
            trans.clear()
        return trans

    def find_transition(self, pointer, char):
        print("finding")

    def get_start_state(self):
        for item in self.states:
            if item.name == '0':
                return item
        raise ValueError("invalid state input")
        return None

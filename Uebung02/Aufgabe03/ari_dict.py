

class AriDict(dict):

    def __init__(self, seq=None):
        dict.__init__(self, seq)

    def __str__(self):
        return dict.__str__(self)

    def __repr__(self):
        return dict.__repr__(self)

    def __add__(self, other):
        this = AriDict(self)
        for k, v in other.items():
            if k in this:
                if _is_addable(this[k]) and _is_addable(v):
                    this[k] = v + this[k]
            else:
                this[k] = v
        return this

    def __radd__(self, other):
        return AriDict(other).__add__(self)

    def __len__(self):
        return dict.__len__(self)



def _is_addable(val):
    return type(val) is float or type(val) is int

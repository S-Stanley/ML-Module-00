class Matrix:
    def __init__(self, default_shape):
        self.data = []
        self.shape = ()
        i = 0
        while i < default_shape[0]:
            x = 0
            lst = []
            while x < default_shape[1]:
                x += 1
                lst.append(0)
            self.data.append(lst)
            i += 1

    def __str__(self):
        return self.data

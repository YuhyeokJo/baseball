class Game:
    def guess(self, guess_name):
        if guess_name is None:
            raise TypeError()

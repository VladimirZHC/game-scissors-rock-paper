from variants import Variants

class Player:
    def __init__(self, choices=Variants.Rock, name='Bot'):
        self.choices = choices
        self.name = name
    
    def whoWins(self, first_p, sec_p):
        outcome = 'Победил игрок с именем: '
        if first_p.choices == Variants.Paper and sec_p.choices == Variants.Rock:
            return outcome + first_p.name
        elif first_p.choices == Variants.Paper and sec_p.choices == Variants.Scissors:
            return outcome + sec_p.name 
        elif first_p.choices == Variants.Rock and sec_p.choices == Variants.Paper:
            return outcome + sec_p.name
        elif first_p.choices == Variants.Rock and sec_p.choices == Variants.Scissors:
            return outcome + first_p.name
        elif first_p.choices == Variants.Scissors and sec_p.choices == Variants.Rock:
            return outcome + sec_p.name
        elif first_p.choices == Variants.Scissors and sec_p.choices == Variants.Paper:
            return outcome + sec_p.name
        
        return 'Ничья'
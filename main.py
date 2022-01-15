
from variants import Variants
from player import Player


bot = Player()


alex = Player(Variants.Rock, "Alex")


print(bot.whoWins(bot, alex))


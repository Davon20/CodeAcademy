class Casino:
    def __init__(self, balance, location):
      self.balance = 10000
      self.location = "First Casino"
      def __repr__(self):
        return "{location} requies {balance}in order to play".format(location = self.location, balance = self.balance)
      def __begin_balance__(self):
          return "This stores the starting account balance."
      def __deposit__(self):
          return "This stores the initial deposit amount."
      def __withdraw__(self):
          return "This stores how much is withdrawn."

class Dealer:
  def __init__(self, game, risk):
    self.game = "Poker"
    self.risk = 0.02
    def __repr__(self):
      print("The {game} has a minimum risk requirement of {risk}".format(game = self.game, risk = self.risk))
    def __deals__():
      return "This begins whatever game."
    def __bets__():
      return "This stores the current bet."
    def __gain__():
      return "This stores how much was gained."
    def __loss__():
      return "This stores how much was lost."
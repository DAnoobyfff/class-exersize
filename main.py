class Thing:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def printinfo(self):
    print ("my name is {} - I am a {} ".format(self.name, self.breed))

thin = Thing("rat", "ratsssssssss")
thin.printinfo()
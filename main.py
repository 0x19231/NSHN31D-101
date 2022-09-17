class dogger:
    def __init__(self, name, age,whatdoesdogsay,wheredoglive):
        self.name = name
        self.whatdoesdogsay = whatdoesdogsay
        self.wheredoglive = wheredoglive
        self.age = age


dog = dogger("Barsik","idk isnt my dog","Bark","idk not my dog")
print("Name: {}\n"
      "Age: {}\n"
      "What does doggo say: {}\n"
      "Where does doggo live: {}".format(dog.name,dog.age,dog.whatdoesdogsay,dog.wheredoglive))



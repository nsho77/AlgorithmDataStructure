class HashTable:
    def __init__(self) -> None:
        self.capacity = 10;
        self.basket = [""] * self.capacity
    
    def Add(self, alpha : str) -> None:
        self.basket[ord(alpha) % self.capacity] = alpha

    def Find(self, alpha : str) -> str:
        return self.basket[ord(alpha) % self.capacity]

    def PrintTable(self) -> None:
        print(self.basket)

hash = HashTable()
hash.Add("A")
hash.Add("B")
print("Find A : {0}".format(hash.Find("A")))
hash.PrintTable()
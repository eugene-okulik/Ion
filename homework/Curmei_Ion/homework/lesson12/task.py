class Flower:
    def __init__(self, name, color, stem_lenght, freshness, price, lifespan):
        self.name = name
        self.color = color
        self.stem_lenght = stem_lenght
        self.freshness = freshness
        self.price = price
        self.lifespan = lifespan

    def __repr__(self):
        return f"{self.name} ({self.color} {self.stem_lenght}, {self.freshness}, {self.price},{self.lifespan})"


class Rose(Flower):
    def __init__(self, color, stem_lenght, freshness, price):
        super().__init__("Rose", color, stem_lenght, freshness, price, lifespan=9)


class Tulip(Flower):
    def __init__(self, color, stem_lenght, freshness, price):
        super().__init__("Tuplit", color, stem_lenght, freshness, price, lifespan=11)


class Lily(Flower):
    def __init__(self, color, stem_lenght, freshness, price):
        super().__init__("Lily", color, stem_lenght, freshness, price, lifespan=5)


class Bouqet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_by(self, atrribute):
        self.flowers.sort(key=lambda flower: getattr(flower, atrribute))

    def find_flowers(self, min_lifespan):
        return [flower for flower in self.flowers if flower.lifespan >= min_lifespan]

    def __repr__(self):
        return f"Bouqet({self.flowers})"


rose1 = Rose("Red", 40, 90, 10)
rose2 = Rose("Pink", 45, 80, 12)
tulip1 = Tulip("Yellow", 30, 70, 5)
lily1 = Lily("Red Pink", 60, 95, 15)

bouqet = Bouqet()
bouqet.add_flower(rose1)
bouqet.add_flower(rose2)
bouqet.add_flower(lily1)
bouqet.add_flower(tulip1)

print("Bouqet:", bouqet)
print("Total price of buqet :", bouqet.total_price(), "$$")
print("Average life of bouqet:", bouqet.average_lifespan(), "days")

bouqet.sort_by("freshness")
print("Bouqet after sort by freshness:", bouqet)

print("Flower for life cicle more than 6 days:", bouqet.find_flowers(6))

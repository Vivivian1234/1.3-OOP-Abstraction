
list = []

class Weapon:
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage

    def get_stats(self):
        print(f"Name: {self.name}\nCategory: {self.category}\nDamage: {self.damage}")

    def set_name(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

    def set_damage(self, damage):
        self.damage = damage


class Sword(Weapon):
    def __init__(self, name, category, damage, melee_type):
        super().__init__(name, category, damage)
        self.melee_type = melee_type

    def get_stats(self):
        print(f"Name: {self.name}\nCategory: {self.category}\nDamage: {self.damage}\n Melee Type: {self.melee_type}\nCrit Damage: {self.damage * 3}")
        list.append("Name: {self.name}\nCategory: {self.category}\nDamage: {self.damage}\n Melee Type: {self.melee_type}\nCrit Damage: {self.damage * 3}")

    def set_melee_type(self, melee_type):
        self.melee_type = melee_type


class Bow(Weapon):
    def __init__(self, name, category, damage, range_type):
        super().__init__(name, category, damage)
        self.range_type = range_type

    def get_stats(self):
        print(f"Name: {self.name}\nCategory: {self.category}\nDamage: {self.damage}\n Range Type: {self.range_type}\nCrit Damage: {self.damage * 2}")

    def set_range_type(self, range_type):
        self.range_type = range_type

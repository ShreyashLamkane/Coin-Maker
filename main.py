import random


class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25

        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.original_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.original_color

    def flip(self):
        option_list = [True, False]
        coin_side = random.choice(option_list)
        self.heads = coin_side

    def __del__(self):
        print("coin spent!")

    def __str__(self):
        if self.original_value>=1:
            return "{} Pound Coin ".format(int(self.original_value))
        else:
            return "{}p Coin ".format(int(self.original_value*100))


class One_pence(Coin):
    def __init__(self, rare=False, clean=True):
        self.rare = rare
        self.clean = clean
        data = {
            "original_value": 0.01,
            "original_color": "bronze",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56

        }
        super().__init__(self.rare, self.clean, **data)

class Two_pence(Coin):
    def __init__(self, rare=False, clean=True):
        self.rare = rare
        self.clean = clean
        data = {
            "original_value": 0.02,
            "original_color": "bronze",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12

        }
        super().__init__(self.rare, self.clean, **data)

class Five_pence(Coin):
    def __init__(self, rare=False, clean=True):
        self.rare = rare
        self.clean = clean
        data = {
            "original_value": 0.05,
            "original_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.55

        }
        super().__init__(self.rare, self.clean, **data)

    def rust(self):
        self.color=self.original_color

class Ten_pence(Coin):
    def __init__(self, rare=False, clean=True):
        self.rare = rare
        self.clean = clean
        data = {
            "original_value": 0.10,
            "original_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 1.85,
            "mass": 6.50

        }
        super().__init__(self.rare, self.clean, **data)

    def rust(self):
        self.color=self.original_color

class Twenty_pence(Coin):
    def __init__(self, rare=False, clean=True):
        self.rare = rare
        self.clean = clean
        data = {
            "original_value": 0.20,
            "original_color": "silver",
            "rusty_color": None,
            "num_edges": 7,
            "diameter": 21.4,
            "thickness": 1.7,
            "mass": 5.00

        }
        super().__init__(self.rare, self.clean, **data)

    def rust(self):
        self.color=self.original_color



class Fifty_pence(Coin):
    def __init__(self, rare=False, clean=True):
        self.rare = rare
        self.clean = clean
        data = {
            "original_value": 0.50,
            "original_color": "silver",
            "rusty_color": None,
            "num_edges": 7,
            "diameter": 27.3,
            "thickness": 1.78,
            "mass": 8.00

        }
        super().__init__(self.rare, self.clean, **data)

    def rust(self):
        self.color=self.original_color


class Two_pound(Coin):
    def __init__(self, rare=False, clean=True):
        self.rare = rare
        self.clean = clean
        data = {
            "original_value": 2.00,
            "original_color": "gold & silver",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 28.4,
            "thickness": 2.50,
            "mass": 12.00

        }
        super().__init__(self.rare, self.clean, **data)


class Pound(Coin):
    def __init__(self, rare=False, clean=True):
        self.rare = rare
        self.clean = clean
        data = {
            "original_value": 1.00,
            "original_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5

        }
        super().__init__(self.rare, self.clean, **data)



coins=[One_pence(), Two_pence(), Five_pence(), Ten_pence(), Twenty_pence(), Fifty_pence(), Pound(), Two_pound()]
for coin in coins:
    arguments=[coin,  coin.value,coin.color, coin.diameter, coin.thickness, coin.mass, coin.num_edges]

    string="{}- Color:{}, value:{}, diameter(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)
    print(string)


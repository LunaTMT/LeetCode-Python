def __init__(self, w: List[int]):
    if not w:
        self.numbers = []
        self.weights = []
    else:
        self.numbers = list(range(len(w)))
        self.weights = [weight / sum(w) for weight in w]

def pickIndex(self) -> int:
    return random.choices(self.numbers, self.weights)[0]
def fizzBuzz(self, n: int) -> List[str]:

    def get_value(n):
        if n % 3 == 0 and n % 5 == 0: 
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 ==0:
            return "Buzz"
        return str(n)

    return [get_value(i) for i in range(1, n+1)]
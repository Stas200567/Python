class FibonacciContainer:
    def __init__(self, n):
        self.fib_numbers = self._generate_fibonacci(n)
    
    def _generate_fibonacci(self, n):
        fib = [0, 1]
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[:n]
    
    def __len__(self):
        return len(self.fib_numbers)
    
    def __getitem__(self, index):
        return self.fib_numbers[index]

if __name__ == "__main__":
    n = int(input("Введіть кількість чисел Фібоначчі: "))
    fib_container = FibonacciContainer(n)
    print("Довжина контейнера:", len(fib_container))
    print("Перші 5 чисел Фібоначчі:", fib_container[:5])

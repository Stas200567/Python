class Order:
    def __init__(self):
        self.__items = []  # Список товарів (інкапсуляція)
    
    def add_item(self, name, price, quantity):
        self.__items.append({"name": name, "price": price, "quantity": quantity})
    
    def get_items(self):
        return self.__items
    
    def calculate_total(self):
        return sum(item["price"] * item["quantity"] for item in self.__items)

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []  # Список замовлень
    
    def place_order(self):
        order = Order()
        while True:
            name = input("Введіть назву товару (або 'exit' для завершення): ")
            if name.lower() == "exit":
                break
            price = float(input("Введіть ціну товару: "))
            quantity = int(input("Введіть кількість товару: "))
            order.add_item(name, price, quantity)
        
        if order.get_items():
            self.orders.append(order)
            return order
        else:
            print("Замовлення не містить товарів!")
            return None

class OrderProcessor:
   
    @staticmethod
    def process_order(order):
        
        if not order:
            print("Немає замовлення для обробки.")
            return
        
        print("\nЗамовлення підтверджено! Ось список товарів:")
        for item in order.get_items():
            print(f"- {item['name']}: {item['quantity']} шт. x {item['price']} грн")
        
        total = order.calculate_total()
        print(f"Загальна сума: {total:.2f} грн")
        print("Дякуємо за покупку!")

if __name__ == "__main__":
    customer_name = input("Введіть ваше ім'я: ")
    customer = Customer(customer_name)

    print("\nРозміщення нового замовлення...")
    order = customer.place_order()

    if order:
        OrderProcessor.process_order(order)

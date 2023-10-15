from abc import ABC, abstractmethod


class AbstractInterface(ABC):
    @abstractmethod
    def use_tool(self, tool_name):
        pass

    @abstractmethod
    def save(self, product):
        pass

    @abstractmethod
    def load(self, name):
        pass


class Product:
    def __init__(self, name):
        self.name = name
        self.data = None

    def set_data(self, data):
        self.data = data


class Database:
    def __init__(self):
        self.products = {}

    def save(self, product):
        self.products[product.name] = product.data

    def load(self, name):
        if name in self.products:
            product = Product(name)
            product.set_data(self.products[name])
            return product
        else:
            return None


class ProductRepo:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None


class Interface3D(AbstractInterface):
    def __init__(self, product_repo, database):
        self.product_repo = product_repo
        self.database = database

    def use_tool(self, tool_name):
        print(f"Using tool: {tool_name}")

    def save(self, product):
        self.database.save(product)

    def load(self, name):
        return self.database.load(name)


if __name__ == "__main__":
    database = Database()
    product_repo = ProductRepo()

    product1 = Product("Product1")
    product1.set_data("Data for Product 1")
    product_repo.add_product(product1)
    product2 = Product("Product2")
    product2.set_data("Data for Product 2")
    product_repo.add_product(product2)

    interface = Interface3D(product_repo, database)
    interface.use_tool("Some Tool")
    interface.save(product1)

    loaded_product = interface.load("Product1")
    if loaded_product:
        print(f"Loaded product {loaded_product.name}: {loaded_product.data}")
    else:
        print("Product not found")
    interface.use_tool("Another Tool")

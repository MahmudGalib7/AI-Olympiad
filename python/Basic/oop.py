import abc
from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional, Any, Tuple


class ProductCategory(Enum):
    """Enumeration for product categories"""
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    FOOD = "food"
    BOOKS = "books"
    OTHER = "other"


class Discountable(abc.ABC):
    """Abstract interface for items that can be discounted"""
    
    @abc.abstractmethod
    def apply_discount(self, percent: float) -> float:
        """Apply discount to the item and return the discounted price"""
        pass


class Taxable(abc.ABC):
    """Abstract interface for items that can be taxed"""
    
    @abc.abstractmethod
    def calculate_tax(self, tax_rate: float) -> float:
        """Calculate tax on the item and return the tax amount"""
        pass


class Logger:
    """Mixin class for logging functionality"""
    
    @staticmethod
    def log(message: str) -> None:
        """Log a message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")


class Product(Discountable, Taxable, Logger):
    """Class representing a product in the inventory system"""
    
    # Class attribute
    total_products = 0
    
    def __init__(self, name: str, price: float, category: ProductCategory = ProductCategory.OTHER, 
                 stock: int = 0) -> None:
        """Initialize a new product.
        
        Args:
            name: Product name
            price: Product price
            category: Product category (default: OTHER)
            stock: Initial stock quantity (default: 0)
        """
        self.__name = name
        self.__price = price
        self.__category = category
        self.__stock = stock
        self.__id = Product.generate_id()
        
        # Update total products count
        Product.total_products += 1
        self.log(f"Product created: {name} (ID: {self.__id})")
    
    @property
    def name(self) -> str:
        """Get product name"""
        return self.__name
    
    @property
    def price(self) -> float:
        """Get product price"""
        return self.__price
    
    @price.setter
    def price(self, value: float) -> None:
        """Set product price with validation"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
        self.log(f"Price updated for {self.__name}: ${value:.2f}")
    
    @property
    def category(self) -> ProductCategory:
        """Get product category"""
        return self.__category
    
    @property
    def stock(self) -> int:
        """Get current stock"""
        return self.__stock
    
    @property
    def id(self) -> str:
        """Get product ID"""
        return self.__id
    
    def add_stock(self, quantity: int) -> None:
        """Add stock to the product"""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.__stock += quantity
        self.log(f"Added {quantity} units to {self.__name}. New stock: {self.__stock}")
    
    def remove_stock(self, quantity: int) -> None:
        """Remove stock from the product"""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self.__stock:
            raise ValueError("Not enough stock available")
        self.__stock -= quantity
        self.log(f"Removed {quantity} units from {self.__name}. New stock: {self.__stock}")
    
    def apply_discount(self, percent: float) -> float:
        """Apply discount to the product price
        
        Args:
            percent: Discount percentage (0-100)
            
        Returns:
            Discounted price
        """
        if not 0 <= percent <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        
        discount_amount = self.__price * (percent / 100)
        discounted_price = self.__price - discount_amount
        self.log(f"Applied {percent}% discount to {self.__name}. New price: ${discounted_price:.2f}")
        return discounted_price
    
    def calculate_tax(self, tax_rate: float) -> float:
        """Calculate tax on the product
        
        Args:
            tax_rate: Tax rate percentage (0-100)
            
        Returns:
            Tax amount
        """
        if not 0 <= tax_rate <= 100:
            raise ValueError("Tax rate must be between 0 and 100")
        
        tax_amount = self.__price * (tax_rate / 100)
        self.log(f"Calculated tax for {self.__name}: ${tax_amount:.2f}")
        return tax_amount
    
    def __str__(self) -> str:
        """String representation of the product"""
        return f"{self.__name} (${self.__price:.2f}) - {self.__category.value.title()}"
    
    def __repr__(self) -> str:
        """Official string representation of the product"""
        return f"Product(name='{self.__name}', price={self.__price}, " \
               f"category={self.__category}, stock={self.__stock})"
    
    @classmethod
    def generate_id(cls) -> str:
        """Generate a unique product ID based on current count"""
        return f"P{cls.total_products + 1:04d}"
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Product':
        """Create a product from a dictionary
        
        Args:
            data: Dictionary with product data
            
        Returns:
            New Product instance
        """
        # Handle category conversion from string to enum
        category_str = data.get('category', 'other')
        category = None
        for cat in ProductCategory:
            if cat.value == category_str:
                category = cat
                break
        
        if not category:
            category = ProductCategory.OTHER
        
        # Create and return product
        return cls(
            name=data['name'],
            price=data['price'],
            category=category,
            stock=data.get('stock', 0)
        )


class ElectronicsProduct(Product):
    """Specialized product class for electronics"""
    
    def __init__(self, name: str, price: float, warranty_months: int = 12, 
                 stock: int = 0) -> None:
        """Initialize a new electronics product
        
        Args:
            name: Product name
            price: Product price
            warranty_months: Warranty period in months
            stock: Initial stock quantity
        """
        super().__init__(name, price, ProductCategory.ELECTRONICS, stock)
        self.warranty_months = warranty_months
    
    def extend_warranty(self, additional_months: int) -> None:
        """Extend the warranty period
        
        Args:
            additional_months: Number of months to add
        """
        if additional_months <= 0:
            raise ValueError("Additional months must be positive")
        
        self.warranty_months += additional_months
        self.log(f"Extended warranty for {self.name} by {additional_months} months. "
                 f"Total warranty: {self.warranty_months} months")
    
    def calculate_tax(self, tax_rate: float) -> float:
        """Calculate tax for electronics (overridden with special rules)
        
        Args:
            tax_rate: Base tax rate
            
        Returns:
            Tax amount
        """
        # Electronics have a 2% additional tax
        effective_rate = tax_rate + 2
        self.log(f"Using electronics tax rate: {effective_rate}%")
        return super().calculate_tax(effective_rate)
    
    def __str__(self) -> str:
        """String representation of the electronics product"""
        return f"{super().__str__()} - {self.warranty_months} months warranty"


class Inventory:
    """Class to manage a collection of products"""
    
    def __init__(self) -> None:
        """Initialize an empty inventory"""
        self.__products: Dict[str, Product] = {}
        self.log_enabled = True
    
    def add_product(self, product: Product) -> None:
        """Add a product to the inventory
        
        Args:
            product: Product to add
        """
        self.__products[product.id] = product
        if self.log_enabled:
            Logger.log(f"Added product to inventory: {product.name}")
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Get a product by ID
        
        Args:
            product_id: Product ID to look up
            
        Returns:
            Product if found, None otherwise
        """
        return self.__products.get(product_id)
    
    def remove_product(self, product_id: str) -> bool:
        """Remove a product from the inventory
        
        Args:
            product_id: Product ID to remove
            
        Returns:
            True if removed, False if not found
        """
        if product_id in self.__products:
            product = self.__products.pop(product_id)
            if self.log_enabled:
                Logger.log(f"Removed product from inventory: {product.name}")
            return True
        return False
    
    def list_products(self, category: Optional[ProductCategory] = None) -> List[Product]:
        """List products, optionally filtered by category
        
        Args:
            category: Category to filter by (optional)
            
        Returns:
            List of products
        """
        if category:
            return [p for p in self.__products.values() if p.category == category]
        return list(self.__products.values())
    
    def get_total_value(self) -> float:
        """Calculate total value of inventory
        
        Returns:
            Total value
        """
        return sum(p.price * p.stock for p in self.__products.values())
    
    def search_products(self, keyword: str) -> List[Product]:
        """Search for products by name
        
        Args:
            keyword: Search keyword
            
        Returns:
            List of matching products
        """
        keyword = keyword.lower()
        return [p for p in self.__products.values() if keyword in p.name.lower()]
    
    def apply_bulk_discount(self, category: ProductCategory, discount_percent: float) -> None:
        """Apply discount to all products in a category
        
        Args:
            category: Category to apply discount to
            discount_percent: Discount percentage
        """
        products = self.list_products(category)
        for product in products:
            product.apply_discount(discount_percent)


# Demonstration of usage
if __name__ == "__main__":
    # Create an inventory
    store = Inventory()
    
    # Create some products
    laptop = ElectronicsProduct("Lenovo ThinkPad", 999.99, 24, 10)
    phone = ElectronicsProduct("iPhone 13", 799.99, 12, 15)
    book = Product("Python Programming", 49.99, ProductCategory.BOOKS, 50)
    
    # Products from dictionary data (e.g., from JSON)
    shirt_data = {
        "name": "Cotton T-Shirt",
        "price": 19.99,
        "category": "clothing",
        "stock": 100
    }
    shirt = Product.from_dict(shirt_data)
    
    # Add products to inventory
    store.add_product(laptop)
    store.add_product(phone)
    store.add_product(book)
    store.add_product(shirt)
    
    # Print all products
    print("\nAll Products:")
    for product in store.list_products():
        print(f"  - {product}")
    
    # Filter by category
    print("\nElectronics:")
    for product in store.list_products(ProductCategory.ELECTRONICS):
        print(f"  - {product}")
    
    # Search products
    print("\nSearch Results for 'th':")
    for product in store.search_products("th"):
        print(f"  - {product}")
    
    # Apply discounts and calculate taxes
    print("\nApplying discounts and calculating taxes:")
    laptop_discounted = laptop.apply_discount(10)
    laptop_tax = laptop.calculate_tax(8.5)
    print(f"  Laptop original price: ${laptop.price:.2f}")
    print(f"  Laptop discounted price: ${laptop_discounted:.2f}")
    print(f"  Laptop tax amount: ${laptop_tax:.2f}")
    
    # Apply bulk discount
    store.apply_bulk_discount(ProductCategory.ELECTRONICS, 15)
    
    # Get total inventory value
    total_value = store.get_total_value()
    print(f"\nTotal inventory value: ${total_value:.2f}")
    
    # Manage stock
    print("\nManaging stock:")
    try:
        book.remove_stock(5)
        print(f"  New book stock: {book.stock}")
        
        # This will raise an error
        book.remove_stock(100)
    except ValueError as e:
        print(f"  Error: {e}")
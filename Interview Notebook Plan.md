# ============================================
# EXERCISE 1 SOLUTION: List Manipulation
# ============================================

# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ============================================
# 1. FIND THE SUM OF ALL NUMBERS
# ============================================

# sum() is a built-in function that adds all numbers in a list
total = sum(numbers)  # 1+2+3+4+5+6+7+8+9+10 = 55
print(f"Sum: {total}")  # Output: Sum: 55

# ============================================
# 2. FIND THE MAXIMUM VALUE
# ============================================

# max() is a built-in function that finds the largest number in a list
maximum = max(numbers)  # The largest number is 10
print(f"Maximum: {maximum}")  # Output: Maximum: 10

# ============================================
# 3. CREATE A NEW LIST WITH ONLY EVEN NUMBERS
# ============================================

# This uses a "list comprehension" - a compact way to create lists
# Syntax: [expression for item in list if condition]
# 
# Breaking it down:
# - n for n in numbers: Loop through each number 'n' in the list
# - if n % 2 == 0: Only include numbers where remainder when divided by 2 is 0 (even numbers)
# - n % 2 means "remainder of n divided by 2" (modulo operator)
# - If remainder is 0, the number is even
evens = [n for n in numbers if n % 2 == 0]  # Creates [2, 4, 6, 8, 10]
print(f"Even numbers: {evens}")  # Output: Even numbers: [2, 4, 6, 8, 10]


# ============================================
# ANSWER KEY: Question 1
# ============================================

scores = [85, 92, 78, 96, 88, 73, 91, 67]

# List comprehension: Filter scores >= 80 and convert to letter grades
# [expression for item in iterable if condition]
# Expression: "A" if score >= 90 else "B" (ternary operator)
# Condition: score >= 80 (filters out scores below 80)
grades = ["A" if score >= 90 else "B" for score in scores if score >= 80]
print(f"Letter grades (scores >= 80): {grades}")  # Output: ['B', 'A', 'B', 'A', 'B', 'A']

# Lambda function: Returns True if number is divisible by 3
# lambda x: x % 3 == 0 checks if remainder when divided by 3 is 0
divisible_by_3 = lambda x: x % 3 == 0

# Use filter() with lambda to get scores divisible by 3
# filter(function, iterable) keeps only items where function returns True
filtered_scores = list(filter(divisible_by_3, scores))
print(f"Scores divisible by 3: {filtered_scores}")  # Output: [78, 96] (only 78 and 96 are divisible by 3)


# ============================================
# ANSWER KEY: Question 3
# ============================================

class ShoppingCart:
    """
    A shopping cart that stores items and calculates totals.
    
    Demonstrates:
    - *args for variable positional arguments
    - **kwargs for variable keyword arguments
    - Class methods and attributes
    - __str__ for string representation
    - Error handling
    """
    
    def __init__(self, *args):
        """
        Initialize shopping cart with items.
        
        *args collects any number of tuples: (item_name, price)
        Each tuple represents one item in the cart.
        """
        # Store items as a list of tuples
        # *args is a tuple of all arguments passed
        # We convert it to a list so we can modify it later
        self.items = list(args)
    
    def add_item(self, **kwargs):
        """
        Add an item to the cart using keyword arguments.
        
        **kwargs collects keyword arguments into a dictionary
        Expected keys: 'name' and 'price'
        """
        # Extract name and price from kwargs dictionary
        # .get() returns None if key doesn't exist (safer than direct access)
        name = kwargs.get('name')
        price = kwargs.get('price')
        
        # Error handling: Ensure both name and price are provided
        if name is None or price is None:
            raise ValueError("Both 'name' and 'price' must be provided")
        
        # Bonus: Error handling for positive prices
        if price <= 0:
            raise ValueError(f"Price must be positive, got {price}")
        
        # Add item as tuple (name, price) to items list
        self.items.append((name, price))
    
    def total(self):
        """
        Calculate and return the total price of all items.
        
        Returns:
            Sum of all item prices
        """
        # Sum all prices (second element of each tuple)
        # [item[1] for item in self.items] extracts prices
        # sum() adds them all together
        return sum(item[1] for item in self.items)
    
    def __str__(self):
        """
        Return formatted string representation of the cart.
        
        Called automatically when you use print(cart) or str(cart)
        """
        # Build string with cart contents
        lines = ["Shopping Cart:"]
        
        # Loop through items and format each one
        # item[0] is name, item[1] is price
        for name, price in self.items:
            # Format: "  name: $price" with 2 decimal places
            lines.append(f"  {name}: ${price:.2f}")
        
        # Add total at the end
        lines.append(f"Total: ${self.total():.2f}")
        
        # Join all lines with newline character
        return "\n".join(lines)

# ============================================
# TEST THE SHOPPING CART
# ============================================

# Create cart with initial items using *args
# Each tuple (name, price) is one argument
cart = ShoppingCart(("apple", 1.50), ("banana", 0.75), ("orange", 2.00))

# Add item using **kwargs (keyword arguments)
cart.add_item(name="bread", price=3.50)

# Print cart (calls __str__ automatically)
print(cart)

# Test error handling: Try to add item with negative price
try:
    cart.add_item(name="milk", price=-1.00)
except ValueError as e:
    print(f"\nError caught: {e}")  # Output: Error caught: Price must be positive, got -1.0

# ============================================
# IMPORTING LIBRARIES: Multiple Classifiers
# ============================================

# Scikit-learn: Machine learning library
from sklearn.datasets import load_digits  # Handwritten digits dataset
from sklearn.linear_model import LogisticRegression  # Logistic regression classifier
from sklearn.svm import SVC  # Support Vector Machine classifier
from sklearn.neighbors import KNeighborsClassifier  # K-Nearest Neighbors classifier
from sklearn.tree import DecisionTreeClassifier  # Decision tree classifier
from sklearn.ensemble import RandomForestClassifier  # Random Forest (ensemble) classifier
from sklearn.naive_bayes import GaussianNB  # Naive Bayes classifier

# Our custom utility functions
from src.models.supervised import split_data, evaluate_classifier  # Supervised learning utilities
import pandas as pd  # Data manipulation

# ============================================
# LOADING THE DATASET: Handwritten Digits
# ============================================

# load_digits() loads the Handwritten Digits dataset from scikit-learn
# This is a multiclass classification problem: predict digit (0-9) from image pixels
# No download needed - it's built into scikit-learn
digits = load_digits()  # Returns a Bunch object with data, target, etc.

# X = Features (inputs): Image pixels (8×8 = 64 pixels per image)
# digits.data contains pixel values (1797 samples × 64 features)
# We convert to DataFrame for easier manipulation
X = pd.DataFrame(digits.data)  # Features: 64 pixel values per image

# y = Target (output): Digit class (what we want to predict)
# digits.target contains class labels (0, 1, 2, ..., 9 for each sample)
# We convert to Series for easier manipulation
y = pd.Series(digits.target)  # Target: digit class (0-9)

print(f"Digits Dataset: {X.shape[0]} samples, {X.shape[1]} features")  # 1797 images, 64 pixels
print(f"Classes: {len(digits.target_names)}")  # 10 classes (digits 0-9)

# ============================================
# TRAIN/TEST SPLIT: Separating Data
# ============================================

# Split data into training (80%) and test (20%) sets
X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2, random_state=42)

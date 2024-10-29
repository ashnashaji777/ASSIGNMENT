class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        # Yielding length and width as dictionaries in the required format
        yield {'length': self.length}
        yield {'width': self.width}

# Usage example
rect = Rectangle(15, 19)  # Initializes a Rectangle with length 5 and width 10
for dimension in rect:
    print(dimension)

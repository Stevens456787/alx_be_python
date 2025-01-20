class Book:
    def _init_(self, title, author, price):
        self.title = title
        self.author = author
        self.year = year
    
    def _del_(self):
        print(f"Book {self.title} has been deleted.")
        
    def _str_(self):
        return f"{self.title} by {self.author}", published in {self.year}
    
    def _repr_(self):
        return f"Book(title={self.title}, author={self.author}, year={self.year})"
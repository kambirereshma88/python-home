class library:
    def __init__(self,acc_number,publisher,title,author):
        self.acc_number=acc_number
        self.publisher=publisher
        self.title=title
        self.author=author

    def read(self):
        print(f"Acc number: {self.acc_number}")
        print(f"title :{self.title}")
        print(f"author: {self.author}")

    def compute(self,days_late):
        fine = days_late * 1.50
        print(f"fine for {days_late} days late : {fine:.2f}")

    def display(self):
        print(f"acc number:{self.acc_number}")
        print(f"publisher :{self.publisher}")
        print(f"title: {self.title}")
        print(f"author : {self.author}")

book= library(acc_number="25846",publisher= "Navneet Publish",title="The Rich Man",author="john Doe")

book.read()
book.compute(5)
book.display()


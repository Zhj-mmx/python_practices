import sys

class Book:
    """图书类"""
    def __init__(self, isbn, title, price):
        self.isbn = isbn
        self.title = title
        self.price = price

    def __str__(self):
            return f"{self.isbn} {self.title} {self.price:.2f}"    
    
class SeqList:
     """顺序表类"""
     def __init__(self):
          self.data = []

     def create_from_input(self):
          """1基于顺序存储结构的图书信息表的创建和输出"""
          self.data.clear()
          n = 0
          for line in sys.stdin:
               n += 1
               line = line.strip()
               if line == "0 0 0":
                    break
               parts = line.split()
               if len(parts) != 3:
                    continue
               isbn, title, price = parts
               book = Book(isbn, title, float(price))
               self.data.append(book)
               self.sum_num = n - 1
               
     def display(self):
          """2显示所有图书信息"""
          print(len(self.data))
          for book in self.data:
               print(book)

     def change_price_by_average(self):
          """3根据平均价格调整图书价格"""
          total_price = sum(book.price for book in self.data)
          average = total_price / len(self.data)
          print(f"{average:.2f}")
          for book in self.data:
               if book.price < average:
                    book.price *= 1.2
               elif book.price >= average:
                    book.price *= 1.1
               print(book)

     def reverse(self):
          """4反转列表"""
          self.data.reverse()
          for book in self.data:
               print(book)

     def find_most_expensive(self):
          """5查找最贵的书"""
          if not self.data:
               return None
          max_price = max(self.data, key=lambda book: book.price) 
          num = 0
          for book in self.data:
               if book.price == max_price:
                    num += 1
                    print(book)
          print(num)          

     def find_by_title(self, title):
          """6通过名字查找"""
          for book in self.data:
               if book.title == title:
                    print(book)
          return None                     

     def find_by_position(self, pos):
          """7查找最佳位置图书"""
          if 1 <= pos <= len(self.data):
               print(self.data[pos-1]) 
          else:
               print("抱歉，最佳位置上的图书不存在！")     

     def list_insert(self, book, pos):
          """8添加图书"""
          if 1 <= pos <= len(self.data) + 1:
               self.data.insert(pos-1, book)
               self.display()
          else:
               print("抱歉，入库位置非法！")   

     def deduplicate(self):
          """10去重"""
          seen = set()
          unique_books = []
          for book in self.data:
               if book.isbn not in seen:
                    unique_books.append(book)
                    seen.add(book.isbn)
          self.data = unique_books
          print(len(self.data))
          for book in self.data:
               print(book)


    
          
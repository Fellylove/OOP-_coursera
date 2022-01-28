class A:
  def hello(self):
    print("Hello from class A")

class B:
  def hello(self):
    print("Hello from class B")

# class C(A, B):
#   def bonjour(self):
#     print("Bonjour")
#
# obj= C()
# obj.bonjour()

# class C(A, B):
#   def goodbye(self):
#     print("Goodbye")
#
# obj= C()
# obj.goodbye()

class C(A, B):
  def hello(self):
    print("Hello from class C")
    super().hello()
    B.hello(self)

obj= C()
obj.hello()
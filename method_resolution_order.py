class A:
  def hello(self):
    print("Hello from class A")

class B:
  def hello(self):
    print("Hello from class B")

class C(A, B):
  def hello(self):
    super().hello()

# obj= C()
# obj.hello()

#method resolution order (MRO)
obj= C()
print(C.mro())
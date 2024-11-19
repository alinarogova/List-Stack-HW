
print("Task 1".center(60, "="))

class Node:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password
        self.prev = None
        self.next = None

class List_bidirectional(Node):
    def __init__(self):
        self.head = None
        self.tail = None

    def isuserinlist(self, name, login):
        if self.head.name == name or self.head.login == login:
            return True
        temp = self.head
        while temp.next:
            temp = temp.next
            if temp.name == name or temp.login == login:
                return True
        return False

    def append(self, name, login, password):
        new_node = Node(name, login, password)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        if self.isuserinlist(name, login):
            print(f"This name {name} or login {login} has already used. If it's your acc - authorize, please.")
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last
        self.tail = new_node

    def display_top(self):
        # print(self.head.data)
        current = self.head
        while current:
            print("* ", current.name, ":", current.login, current.password)
            current = current.next

    '''
    def display_tail(self):
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")
    '''
    def del_nodes(self, name, login):
        #searching value is in first node
        if self.head.name == name or self.head.login == login:
            tmp = self.head
            self.head = self.head.next
            self.head.prev = None
            del tmp
            return f"{name}, {login}"
        #search value
        current = self.head
        while current.next:
            if current.next.name == name or current.next.login == login:
                tmp = current.next
                current.next = current.next.next
                if tmp.next is None:
                    self.tail = self.tail.prev
                else:
                    tmp.next.prev = current
                del tmp
            current = current.next
        return f"{name}, {login}"

    def reverse(self, name, newlogin=None, newpassword=None):
        if self.head.name == name:
            if newlogin:
                self.head.login = newlogin
            if newpassword:
                self.head.password = newpassword
            return
        temp = self.head
        while temp.next:
            temp = temp.next
            if temp.next.name == name:
                if newlogin:
                    temp.next.login = newlogin
                if newpassword:
                    temp.next.password = newpassword
                return


dll=List_bidirectional()

while True:
    sw = int(input("1 - add, 2 - del, 3 - display, 4 - search, 5 - reverse login, 6 - reverse password, 0 - exit: "))
    if sw == 1:
        name = input("Enter the name for adding: ")
        login = input("Enter the login for adding: ")
        password = input("Enter the password for adding: ")
        dll.append(name, login, password)
    elif sw == 2:
        name = input("Enter the name for deleting: ")
        login = input("Enter the login for deleting: ")
        dll.del_nodes(name, login)
    elif sw == 3:
        dll.display_top()
    elif sw == 4:
        name = input("Enter the name for finding: ")
        login = input("Enter the login for finding: ")
        if dll.isuserinlist(name, None):
            print(f"'{name}' is in List.")
        elif dll.isuserinlist(None, login):
            print(f"'{login}' is in List.")
        else:
            print(f"name='{name}' and login={login} aren't in List.")
    elif sw == 5:
        name = input("Enter the name for reversing: ")
        newlogin = input("Enter the new login: ")
        dll.reverse(name, newlogin=newlogin, newpassword=None)
    elif sw == 6:
        name = input("Enter the name for reversing: ")
        newpassword = input("Enter the new password: ")
        dll.reverse(name, newlogin=None, newpassword=newpassword)
    elif sw == 0:
        break

print("Task 2".center(40, '='))
class Stack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def size(self):
        return len(self.items)

    def is_full(self):
        return self.max_size <= len(self.items)
    def push(self, value):
        if self.is_full():
            raise IndexError("Push in full stack.")
        self.items.append(value)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack.")
        val = self.items[-1]
        del self.items[-1]
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack.")
        return self.items[-1]

    def clear(self):
        del self.items
        self.items = []


stack = Stack(5)
"""
Реалізуйте клас стека для роботи з рядками (стек
рядків).
Стек повинен мати фіксований розмір.
Реалізуйте набір операцій для роботи зі стеком:
■ поміщення рядка в стек;
■ виштовхування рядка зі стека;
■ підрахунок кількості рядків у стеку;
■ перевірку чи порожній стек;
■ перевірку чи повний стек;
■ очищення стека;
■ отримання значення без виштовхування верхнього рядка
"""
while True:
    sw = input("1 - add, 2 - take last value, 3 - size, 4 - is empty, 5 - is full, 6 - del all values from stack,"
               "7 - peek, 0 - exit: ")
    if sw=="1":
        stack.push(input("Enter str for add: "))
    elif sw=='2':
        print(stack.pop())
    elif sw=='3':
        print(stack.size())
    elif sw=="4":
        print(stack.is_empty())
    elif sw=='5':
        print(stack.is_full())
    elif sw=='6':
        print(stack.clear())
    elif sw=="7":
        print(stack.peek())
    elif sw == "0":
        break


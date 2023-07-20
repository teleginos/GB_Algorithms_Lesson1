# Определение класса узла двусвязного списка
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Определение класса двусвязного списка
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Метод разворота двусвязного списка
    def reverse(self):
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    # Метод добавления элемента в начало списка
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Метод сортировки пузырьком
    def bubble_sort(self):
        if not self.head:
            return
        end = None
        while end != self.head:
            swapped = False
            current = self.head
            while current.next != end:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next
            end = current
            if not swapped:
                break

    # Метод вывода элементов списка
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Пример использования
dllist = DoublyLinkedList()
dllist.prepend(4)
dllist.prepend(2)
dllist.prepend(1)
dllist.prepend(3)

print("Исходный список:")
dllist.display()

print("Разворот списка:")
dllist.reverse()
dllist.display()

print("Сортировка пузырьком:")
dllist.bubble_sort()
dllist.display()

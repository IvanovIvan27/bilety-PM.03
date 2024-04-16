class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def first(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def swap_first_and_last(self):
        if not self.is_empty():
            first_item = self.dequeue()
            last_item = self.items[-1]
            self.items[0] = last_item
            self.items[-1] = first_item
            self.enqueue(first_item)
        else:
            raise IndexError("Queue is empty")


# Пример использования
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print("Исходная очередь:", queue.items)

queue.swap_first_and_last()

print("Очередь после перестановки первого и последнего элементов:", queue.items)

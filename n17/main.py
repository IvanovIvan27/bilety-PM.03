class Vector:
    def __init__(self, values):
        self.values = values

    def merge(self, other):
        result = []
        i, j = 0, 0

        while i < len(self.values) and j < len(other.values):
            if self.values[i] < other.values[j]:
                result.append(self.values[i])
                i += 1
            else:
                result.append(other.values[j])
                j += 1

        result.extend(self.values[i:])
        result.extend(other.values[j:])
        return result

    def __str__(self):
        return str(self.values)


vector1 = Vector([1, 3, 5, 7])
vector2 = Vector([2, 4, 6, 8])

merged_vector = vector1.merge(vector2)
print(merged_vector)

class Text(str):
    def duplicate(self):
        return self + self

    def reverse(self):
        return self[::-1]

    def is_palendrome(self):
        return self.lower() == self.reverse().lower()


text = Text("Racecar")

print(text.duplicate())

print(text.reverse())

print(text.is_palendrome())

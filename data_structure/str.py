string_variable = 'hello'
print(string_variable)

multiline_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multiline_string)

print(string_variable[1])

for character in "banana":
    print(character)

print(len(string_variable))

txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")

print("expensive" not in txt)

if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

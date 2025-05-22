marks = {
    "Ayush": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Ayush"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99, "Renuka": 100})
# print(marks)

print(marks.get("Ayush2")) # Prints None
print(marks["Ayush2"]) # Returns an error
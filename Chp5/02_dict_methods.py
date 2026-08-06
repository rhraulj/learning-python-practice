marks = {
    "Rituraj": 100,
    "Isha": 56,
    "Dhruvi": 55,
    0: "Raj"
}

#print(marks.items())
#print(marks.keys())
#print(marks.values())
#marks.update({"Rituraj": 99, "Renuka": 100})
#print(marks)

print(marks.get("Dhruvi2")) # Prints none
print(marks["Dhruvi2"]) # Returns an error
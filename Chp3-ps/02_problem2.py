# Write a program to fill in a letter template given below with name and date

letter = '''Dear <|NAME|>,
            You are selected!
            <|DATE|>'''
print(letter.replace("<|NAME|>", "Raj")
      .replace("<|DATE|>", "2026-10-10"))
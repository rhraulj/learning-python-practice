# Given seconds as input, convert it into hours, minutes, and seconds (e.g., 3665 → 1h 1m 5s).

seconds_input = int(input("Enter seconds: "))
hours = seconds_input // 3600
minutes = (seconds_input % 3600) // 60
seconds = seconds_input % 60
print(f"{hours}h {minutes}m {seconds}s")
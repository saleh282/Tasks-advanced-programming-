# ============================== 1 ===============================
products = ["  LAPTOP ", "phone  ", "  Tablet", "CAMERA  "]

cleaned = list(map(lambda p: p.strip().title(), products))
print(cleaned)


# ============================== 2 ===============================

celsius = [0, 10, 20, 30, 40] 
Fahrenheit= list(map( lambda c: (9/5)*c + 32, celsius))
print(Fahrenheit)

# ============================== 3 ===============================

nums = [1, 2, 3, 4, 5] 
result= list( map(lambda x: x**2 +10,nums))
print(result)

# ============================== 4 ===============================
words = ["python", "lambda", "programming", "map", "function"] 
result= list( map(lambda w: (w[0], w[-1]) ,words))
print(result) 

# ============================== 5 ===============================

marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]]
result= list(map(lambda row: list(map(lambda x: round(x * 1.05), row)), marks))
print(result)

# ============================== 6 ===============================

numbers = [5, 10, 15, 20, 25]

min_val = min(numbers)
max_val = max(numbers)

normalized = list(
    map(lambda x: (x - min_val) / (max_val - min_val), numbers)
)

print(normalized)
# ============================== 7 ===============================


names = [  "saleh mohamed", "ali kareem", "mohamed ahmed"]

lengths = list( map( lambda names: list( map(lambda word: len(word), names.split())    ),  names))

print(lengths)


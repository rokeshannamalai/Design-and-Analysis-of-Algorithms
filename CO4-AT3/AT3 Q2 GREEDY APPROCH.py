packages = [
    ("P1", 10, 60),
    ("P2", 20, 100),
    ("P3", 30, 120),
    ("P4", 25, 110)
]

capacity = 50

# Calculate profit/weight ratio
packages.sort(key=lambda x: x[2] / x[1], reverse=True)

selected = []
total_weight = 0
total_profit = 0

for name, weight, profit in packages:
    if total_weight + weight <= capacity:
        selected.append(name)
        total_weight += weight
        total_profit += profit

print("Selected Packages:", selected)
print("Total Weight:", total_weight)
print("Total Profit:", total_profit)

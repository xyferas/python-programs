temperature =  [72, 75, 78, 82, 91, 95, 88]
threshold = 90
index = 0

while index < len(temperature):
    if temperature[index] > threshold:
        print("Danger!")
        print(f"Temperature: {temperature[index]} Index: {index}")
        break
    index+=1
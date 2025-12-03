# مهم: input همیشه متن میده، نه عدد
age = input("چند سالته؟ ")
print(type(age))  # <class 'str'>

# باید تبدیل کنی
age = int(input("چند سالته؟ "))
print(type(age))  # <class 'int'>
print(f"سال دیگه میشی {age + 1} سالت")
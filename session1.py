"""""print ("hello world") # string datatype,enclosed in quotations

student_name = "John" 

age = 25  #integer

marks = 90

datatype_bool = True #boolean

print(marks)

no_1 = 10

no_2 = 25

no_3 = 40.5         # float

no_4 = 44.2

print(no_1+no_3) # addition

print(no_2-no_4) # subtraction

print(no_2*no_3) # multiplication

print(no_4/no_2) # division

print(no_4//no_2) # eliminates the float(decimal)

print(no_2%no_3)  # gives the remainder

print(type(student_name)) # gives the datatype

print(type(datatype_bool))

print(100**1/2) # exponential"""
"""""
# 2.1 VARIABLES

#2.2 DATATYPES

# 2.3 OPERATORS
<<<<<<< HEAD

print(100>50) #greater than
print(100<50)
print(100>=50)
print(100<=50)
print(100!=50)
=======
#LISTS
#Track land parcels IDs
parcels = ["P001" , "P002" , "P003"]
>>>>>>> 5e76307a561f5735400114cba3fca9ceeebcba3f

parcels.append("P001") #ADD

parcels.insert(1, "P001B") #INSERT

parcels.remove("P002") # DELETE


#TUPLES
Capital_cities =("Nairobi","Dodoma","Kampala","washinngton")

print(Capital_cities[0])

#sets
survey_A = {"Nairobi", "Mombasa" ,...}
survey_B = {"Kisumu", "Nakuru", ...}

# Union- all covered counties
print(survey_A | survey_B)

# intersection - in both surveys
print(survey_A & survey_B)

<<<<<<< HEAD
#dictionary is just like sets but separated using a colon 
student={
    "reg:FGS35474,"
    "AGE:25,"
    "JOIN:2024"
}
"""
# Control flows
#if else statements - making decisions
temperature =32

if temperature > 30:

 print ("it is hot outside")

elif temperature > 20:

 print("Nice weather")
# memebersgip test with in
east_african_capitals = [
    "Nairobi",
    "Kampala",
    "Kigali",
    "Dodoma"
]

city = "Nairobi"

if city in east_african_capitals:
    print(f"{city} is an East African capital")

    # for loops - iterating over collections
    #1 zip(iterate coordinates)

coordinates = [
    (-1.28, 36.82),
    (0.52, 35.227),
    (-4.05, 39.67)
]

labels = [
    "Nairobi",
    "Eldoret",
    "Mombasa"
]

for name, (lat, lon) in zip(labels, coordinates):
    print(f"{name}: lat={lat}, lon={lon}")
=======
# DIFFERENCE- ONLY IN SURVEY A
print(survey_A - survey_B)

survey_A.add("Nairobi")

print(survey_A)

#DICTIONARIES\
student = {
    "name" : "Meshack" , 
    "age" :  21 ,
    "nationality" : "Kenyan"
 }

print(student)
print(student["name"])

#inputs
student_2 = {}
name_2 = input("Enter your name")
student_2["name"  ]= name_2

print(student_2)

print(student.keys())

print(student.values())

#indexing and slicing
fruits=['apple', 'banana', 'mango', 'pineapple']

print(fruits[0])

print(fruits[0:2])

print(fruits[:3])

print(fruits[-1]) # starts from the last one

print(fruits[1:3]) # starting from the middle

print(fruits[::2])

print(fruits[-1:])
>>>>>>> 5e76307a561f5735400114cba3fca9ceeebcba3f

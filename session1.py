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

# 2.1 VARIABLES

#2.2 DATATYPES

# 2.3 OPERATORS
#LISTS
#Track land parcels IDs
parcels = ["P001" , "P002" , "P003"]

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
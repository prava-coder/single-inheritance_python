#In this program to exceute how inheritance works
#this is the program for single level inheritace

class School:
    def school_name(self):
        print("Montessori Public School")

#Address class inherites the properties of school class

class Address(School):
    def student_name(self):
        print("Ongole")

#creating an object "adr"

adr=Address()
adr.student_name()
adr.school_name()

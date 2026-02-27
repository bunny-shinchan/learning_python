#Property
# We use @property decorator on any method in the class
# as a property

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

st1 = Student(98, 89,88)
print(st1.percentage) #91.66666666666667%

# Now lets considere if the teacher wants to change the marks
# of any subject, then they can change the marks but the percentage will remain same as it is being saved already.

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    @property
    def calcPercentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 89,88)
print(stu1.percentage)

stu1.phy = 86
print(stu1.calcPercentage) #87.66666666666667% Now the percentage has been dropped when the makrs of phy were updated.


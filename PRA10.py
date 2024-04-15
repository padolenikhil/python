#Student class
class Student():

#Details method to get the student marks and name
 def details(self,mark1,mark2,mark3,name):
  self.m1=mark1
  self.m2=mark2
  self.m3=mark3
  self.n=name

#printing the marks and name
 def _Print(self):
   print("Enter the mark1:",self.m1)
   print("Enter the mark2:",self.m2)
   print("Enter the mark3:",self.m3)
   print("Enter the name:",self.n)

#loop method to check whether student is pass or fail
 def loop(self,passmark=40):
   self.pm=passmark
   if(self.m1>=self.pm):
     print( "Pass")
   else:
     print( "Fail")

   if(self.m2>=self.pm):
     print( "Pass")
   else:
     print( "Fail")

   if(self.m3>=self.pm):
     print( "Pass")
   else:
     print( "Fail")

#Object creation
s=Student()

#passing arguments
s.details(24,60,35,'harshal.')

#method calling
s._Print()
s.loop()
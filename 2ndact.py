# ==========================================================
# Experiment No. 2
# Dynamic Report Generator using Decorators, Class Methods,
# Static Methods and Magic Methods
# ==========================================================

#Decorator Function
def report_decorate(func):
    def wrapper(*args,**kwargs):
        print("="*60)
        print("DYNAMIC REPORT GENERATOR".center(60))
        print("="*60)

        func(*args,**kwargs)

        print("="*60)
        print("END OF REPORT".center(60))
        print("="*60)

    return wrapper

#Report Class
class report:

    #Class Variable
    company_name="ARYA technologies pvt.ltd."

    #constructor
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.contents=[]

    #Instance Method
    def add_content(self,text):
        self.contents.append(text)

    #class method
    @classmethod
    def change_company(cls,new_company):
        cls.company_name=new_company

    #static method
    @staticmethod
    def line():
        print("-"*60)

    #magic method
    def __str__(self):
        return f"Report Title: {self.title}\nAuthor : {self.author}"

    #magic method
    def __len__(self):
        return len(self.contents)

    #decorated method
    @report_decorate
    def display_report(self):

        print("Company:",report.company_name)
        print(self)
        report.line()

        print("Report Contents:")

        for i, item in enumerate(self.contents, start=1):
            print(f"{i}. {item}")

        report.line()

        print("Total Sections :", len(self))

# ===========================
# Report 1
# ===========================

r1 = report("Advanced Python Practical Report", "Arya Jaiswal")

r1.add_content("Completed Experiment No. 2 successfully.")
r1.add_content("Implemented Decorators, Class Methods, Static Methods and Magic Methods.")
r1.add_content("Learned Object-Oriented Programming concepts.")
r1.add_content("Report prepared by Arya Jaiswal.")

r1.display_report()

# Change Company Name
print("\nChanging Company Name...\n")
report.change_company("MIT ADT University")


# ===========================
# Report 2
# ===========================

r2 = report("Employee Performance Report", "Arya Jaiswal")

r2.add_content("Employee Name : Rohan Sharma")
r2.add_content("Attendance : 98%")
r2.add_content("Projects Completed : 8")
r2.add_content("Rating : Excellent")
r2.add_content("Department : Computer Engineering")
r2.add_content("Recommendation : Promotion Approved")

r2.display_report()


# ===========================
# Report 3
# ===========================

r3 = report("Student Result Report", "Arya Jaiswal")

r3.add_content("Student Name : Priya Singh")
r3.add_content("Roll No : 101")
r3.add_content("CGPA : 9.25")
r3.add_content("Result : Pass with Distinction")

r3.display_report()

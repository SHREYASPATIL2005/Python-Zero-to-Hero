class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Shrey", 100000, 1234)
print(p.name, p.salary, p.pin, p.company)

r = programmer("Rohan", 90000, 4321)
print(r.name, r.salary, r.pin, r.company)
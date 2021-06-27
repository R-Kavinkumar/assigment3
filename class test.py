class A:  # Base Class
    name = ‘ ‘
    age = 0


class B(A):  # Derived Class inheriting Base Class A
    height = ‘ ‘

    class C(B):  # Derived Class inheriting his Base Class B
        weight = ‘ ‘

        def Read(self):
            print(‘Please
            Enter
            the
            Following
            Values’)
            self.name = input(‘Enter
            Name:’)
            self.age = (int(input(‘Enter Age:’)))
            self.height = (input(‘Enter Height:’))
            self.weight = (int(input(‘Enter Weight:’)))

            def Display(self):
                print(‘EnteredValues are as follows’)
                print(‘ Name = ‘, self.name)
                print(‘ Age = ‘, self.age)
                print(‘ Height = ‘, self.height)
                print(‘ Weight = ‘, self.weight)
B1 = C()  # Instance of Class C
B1.Read()  # Invoke Method Read
B1.Display()  # Invoke Method Display
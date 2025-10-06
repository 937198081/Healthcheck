class HealthCheck:
   
    def init(self):
        self.accounts = {} 

    def greet_user(self):
        print("Welcome to the Health Check!")
        print("This program provides personalized health suggestions based on your data.")

    def get_user_name(self):
        name = input("Please enter your name: ")
        print(f"Hello {name}, we will get started!")
        return name

    def have_account(self):
        answer = input("Do you have an existing account? (yes/no): ").lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
            
    def create_account(self):
        print("Create a new account")
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        self.accounts[username] = password
        print("Account created successfully.\n")
        return username

    def login(self):
        print("Login")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if self.accounts.get(username) == password:
            print("Login successful!")
            return username
        else:
            print("Login failed. Username or password may be incorrect.")
            return self.login()

    def start(self):
        self.greet_user()
        self.get_user_name()
        if self.have_account():
            username = self.login()
        else:
            username = self.create_account()
        print(f"Welcome, {username}! You're now ready to use the health check program.")
        self.calculate_bmi()

    def calculate_bmi(self):
        print("BMI Calculator")
        print("This tool helps you understand if your weight is healthy based on your height.")
        print("Please provide the following details:")

        while True:
            try:
                height = float(input("1. Enter your height in meters (like: 1.70): "))
                weight = float(input("2. Enter your weight in kilograms (like: 65): "))

                if height <= 0 or weight <= 0:
                    print("Height and weight must be positive numbers. Please try again.")
                    continue

                bmi = weight / (height ** 2)
                print(f"\nCalculation complete! Your Body Mass Index (BMI) is: {bmi:.2f}\n")

                print("BMI Classification:")
                if bmi < 18.5:
                    print(" • You are underweight. It's recommended to consult a healthcare provider.")
                elif bmi < 24.9:
                    print(" • You are in the normal weight range. Keep up the good lifestyle!")
                elif bmi < 29.9:
                    print(" • You are overweight. Consider regular exercise and a balanced diet.")
                else:
                    print(" • You are in the obese range. Medical advice is strongly recommended.")
                break

            except ValueError:
                print("Invalid input. Please enter numbers only (e.g. 1.75 or 70).")
    

app = HealthCheck()
app.start()

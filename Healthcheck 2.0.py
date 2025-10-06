class HealthCheck:
    def __init__(self):
        self.accounts = {}

    def greet_user(self):
        print("Welcome to the Health Check!")
        print("This program provides personalized health suggestions based on your data.")

    def get_user_name(self):
        name = input("Please enter your name: ")
        print(f"Hello {name}, we will get started!\n")
        return name

    def have_account(self):
        answer = input("Do you have an existing account? (yes/no): ").strip().lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
            return self.have_account()

    def create_account(self):
        print("Create a new account")
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        self.accounts[username] = password
        print("Account created successfully.")
        return username

    def login(self):
        print("Login")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if self.accounts.get(username) == password:
            print("Login successful!\n")
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
        self.calorie_advice() 
    
    def calculate_bmi(self):
        print(" BMI Calculator ")
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
                print(f"Calculation complete! Your Body Mass Index (BMI) is: {bmi:.2f}")

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
                print("Invalid input. Please enter numbers only (like: 75 or 70).")
    
    def calorie_advice(self):
        print("Daily Calorie Advice")
        print("Next, based on your basal metabolism, activity level and food portions, we will provide suggestions for maintaining/losing fat or building muscle")

        while True:
            try:
                age = int(input("Age (years): ").strip())
                sex = input("Gender (M/F): ").strip().lower()
                height_m = float(input("Height (meters, like: 1.70):").strip())
                weight = float(input("Weight (kg,like: 65): ").strip())
                if age <= 0 or height_m <= 0 or weight <= 0 or sex not in ("m", "f"):
                   print("Invalid input. Please enter correct positive values")
                   continue
                break
            except ValueError:
                print("Invalid format. Please enter numbers only (like: 1.75 or 70)")
        
        height_cm = height_m * 100
        if sex == "m":
            bmr = 10 * weight + 6.25 * height_cm - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height_cm - 5 * age - 161
        
        print("Select your AVERAGE DAILY exercise duration range (A-E):")
        print("A = 0-30 minutes - Activity factor 1.2")
        print("B = 30-60 minutes - Activity factor 1.375")
        print("C = 60-90 minutes - Activity factor 1.55")
        print("D = 90-120 minutes - Activity factor 1.725")
        print("E = 120+ minutes - Activity factor 1.9")
        level_map = {"a": 1.2,"b": 1.375,"c": 1.55,"d": 1.725,"e": 1.9}
        
        while True:
            act = input("Your choice (A/B/C/D/E): ").strip().lower()
            if act in level_map:
                activity_factor = level_map[act]
                break
            print("Please choose one from A/B/C/D/E.")
        
        tdee = bmr * activity_factor
        print("Estimate your total servings consumed today (enter integers, 0 if none):")
        print(" A: Main carbs (rice/noodles 100g or bread 2 slices) = 260 kcal")
        print(" B: Meat/Eggs (chicken breast 150g / beef 100g / 2 eggs) = 270 kcal")
        print(" C: Vegetables (200g cooked / 100g raw salad) = 40 kcal")
        print(" D: Fruits (1 medium or 200g slices) = 80 kcal") 
        print(" E: Dairy (milk 250ml / yogurt 200g) = 130 kcal")
        print(" F: Sweet drinks/desserts (milk tea, cake, cookies) = 200 kcal")
        print(" G: Fried snacks (fries, fried chicken, chips) = 240 kcal")

        kcal_map = {"a": 260, "b": 270, "c": 40, "d": 80, "e": 130, "f": 200, "g": 240}
        def ask_servings(letter):
            while True:
                try:
                    n = int(input(f"{letter.upper()} servings: ").strip())
                    if n < 0:
                        print("Servings cannot be negative.")
                        continue
                    return n
                except ValueError:
                    print("Please enter an integer (e.g., 0, 1, 2, 3).")
        
        a = ask_servings("a"); b = ask_servings("b"); c = ask_servings("c"); d = ask_servings("d"); e = ask_servings("e"); f = ask_servings("f"); g = ask_servings("g")

        intake = (a * kcal_map["a"] + b * kcal_map["b"] + c * kcal_map["c"] + d * kcal_map["d"] + e * kcal_map["e"] + f * kcal_map["f"] + g * kcal_map["g"])
        print(" Here is the result ")
        print(f"BMR (Basal Metabolic Rate) = {bmr:.0f} kcal/day")
        print(f"TDEE (Total Daily Energy Expenditure) = {tdee:.0f} kcal/day")
        print(f"Estimated intake today = {intake:.0f} kcal")

        diff = intake - tdee
        status = "lower than" if diff < -200 else ("higher than" if diff > 200 else "close to")
        print(f"Calorie intake compared to maintenance: {status} (difference {diff:+.0f} kcal)")
        
        maintain_low, maintain_high = tdee - 200, tdee + 200
        cut_low, cut_high = tdee - 500, tdee - 300
        bulk_low, bulk_high = tdee + 250, tdee + 500

        print("Here are some suggestions")
        print(f"Maintain weight: {maintain_low:.0f} - {maintain_high:.0f} kcal/day")
        print(f"Fat loss: {cut_low:.0f} - {cut_high:.0f} kcal/day (combine strength + cardio)")
        print(f"Muscle gain: {bulk_low:.0f} - {bulk_high:.0f} kcal/day (protein 1.6-2.2g/kg)")
        
        if diff < -200:
            print("Tip: Likely in a calorie deficit today. Avoid excessive hunger, ensure protein/veggies intake.")
        elif diff > 200:
            print("Tip: Likely in a calorie surplus today. Reduce high-sugar/high-fat snacks.")
        else:
            print("Tip: Intake is close to maintenance today. Keep up good habits and regular exercise.")                                                                      

app = HealthCheck()
app.start()


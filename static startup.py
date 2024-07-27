
# Made by Static Startup 2.0 on 27th of July 2024 for GIIS Hackathon X

# Importing libaries for GUI and random operation
import sys
import tkinter as tk
from tkinter import messagebox
import random

#Main Screen GUI and Input
def get_user_input():
    root = tk.Tk()
    root.title("Human Health Risk Assessor")
    

    age_label = tk.Label(root, text="Enter your age")
    age_label.pack()
    age_entry = tk.Entry(root)
    age_entry.pack()

    weight_label = tk.Label(root, text="Enter your weight in Kg")
    weight_label.pack()
    weight_entry = tk.Entry(root)
    weight_entry.pack()

    height_label = tk.Label(root, text="Enter your height in cm")
    height_label.pack()
    height_entry = tk.Entry(root)
    height_entry.pack()

    exercise_label = tk.Label(root, text="Enter daily exercise time in minutes")
    exercise_label.pack()
    exercise_entry = tk.Entry(root)
    exercise_entry.pack()

    water_label = tk.Label(root, text="Enter daily water intake in liters")
    water_label.pack()
    water_entry = tk.Entry(root)
    water_entry.pack()

    sleep_label = tk.Label(root, text="Enter hours of sleep per night")
    sleep_label.pack()
    sleep_entry = tk.Entry(root)
    sleep_entry.pack()

    smoking_label = tk.Label(root, text='Type "Yes" if you smoke and "No" if you do not')
    smoking_label.pack()
    smoking_entry = tk.Entry(root)
    smoking_entry.pack()

    alcohol_label = tk.Label(root, text="Enter the amount of absolute alcohol consumption in mL per day")
    alcohol_label.pack()
    alcohol_entry = tk.Entry(root)
    alcohol_entry.pack()
    
    #Main Script
    def calculate_health_score():
        try:
            #Defines the values based on user input
            age = int(age_entry.get())
            weight = float(weight_entry.get())
            height = float(height_entry.get())
            exercise = int(exercise_entry.get())
            water_intake = float(water_entry.get())
            sleep = float(sleep_entry.get())
            smoking = str(smoking_entry.get())
            alcohol = float(alcohol_entry.get())
            
            #The default medical score
            score = 0

            #Zero Error function to terminate the program if needed
            def zeroerror():
                a = 1/0
            
            # Age scoring
            if 18 <= age <= 30:
                score += 20
            elif 31 <= age <= 50:
                score += 15
            elif age <= 0:
                zeroerror()
            else:
                score += 10

            # Weight factor (based on BMI, simplified)
            if height > 300:
                score = 0

            #BMI Calculation
            bmi = weight / (height/100)**2
            if bmi < 18.5:
                score -= 5
            elif bmi < 25:
                score += 10
            elif bmi < 30:
                score += 5
            else:
                score -= 5

            # Exercise scoring
            if exercise >= 30:
                score += 30
            elif exercise >= 15:
                score += 20
            else:
                score += 10

            # Water intake scoring
            if water_intake >= 2:
                score += 20
            elif water_intake >= 1:
                score += 10
            elif water_intake >= 10:
                zeroerror()
            else:
                score += 5

            # Sleep scoring
            if 7 <= sleep <= 9:
                score += 30
            elif 5 <= sleep < 7:
                score += 20
            elif sleep > 24:
                zeroerror()
            else:
                score += 10
            
                
            # Smoking Scoring
            if smoking == "Yes" or "yes" or "YES":
                score -= 10

            # Alcohol consumption
            if alcohol > 30:
                score -= 5
            elif alcohol > 10:
                score -= 2
            else:
                score += 2

            
            #Threshold for being healthy
            healthy_threshold = 60

            #Generic advice
            Healthy = ["Base your meals on higher fibre starchy carbohydrates.", "⁠Eat lots of fruit and veg", "⁠Cut down on saturated fat and sugar", "⁠Get enough good sleep", "Maintain a healthy weight and body shape", "Avoid processed foods", "⁠Limit you sugar intake"]
            Unhealthy = ["Drink water and stay hydrated, and limit the amount of sugared beverages", "Get enough sleep in order to feel refreshed and be healthy. Lack of sleep can Lead to many chronic health problems such as heart disease, stroke, obesity etc.", "Try to implement more healthy foods such as fruits and vegetables into your diet and limit junk foods such as burgers, pizza and French fries etc.", "Reduce sitting and screen time instead try to exercise every single day to improve your muscle strength and boost endurance.", "Limit the intake of alcohol to 2 drinks or less"]

            # Conditional to check healthy or not healthy
            if score >= healthy_threshold:
                
                result = "You are healthy!"
                recommendations = Healthy[random.randint(0,6)]
                
            else:
                
                result = "You need to improve your health."
                recommendations = Unhealthy[random.randint(0,4)]
            
            
            
            #Output window code    
            output = tk.Tk()
            output.title("Assesment")
            
            #Healthy is Green Background
            #Unhealthy is Red Background
            if score >= healthy_threshold:
                output.configure( bg = "#00FF00" )
            else:
                output.configure( bg = "#FF0000" )

            #Data on the output window
            title_label_o = tk.Label(output, text = "Assessment Report")
            title_label_o.pack()
            
            result_label = tk.Label(output, text =result)
            result_label.pack()

            score_label = tk.Label(output, text ="Your Health Score Result is:")
            score_label.pack()

            score_num = tk.Label(output, text = score)
            score_num.pack()

            recommendation_label = tk.Label(output, text ="Health Recommendations:-")
            recommendation_label.pack()

            recommendation_text = tk.Label(output, text =recommendations)
            recommendation_text.pack()

            #Function to close output window
            def close_win():
                root.grab_set()
                root.focus()
                output.destroy()

            #Close output window button
            close_button = tk.Button(output, text = "Return Back to Main Window", command=close_win)
            close_button.pack()

            output.mainloop()


            
        # Errors for invalid numerical values entered
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Invalid Value Entered")
            
       
     
        

     # Function for quitting application               
    def quit():
        sys.exit()            

    calculate_button = tk.Button(root, text = "Calculate Health Score", command=calculate_health_score) 
    calculate_button.pack()
    quit_button = tk.Button(root, text = "Quit Application", command =quit)
    quit_button.pack()
   
    
    #loops the code
    root.mainloop()

    #Conditional to check whether the window is active and user intends to execute the script
if __name__ == "__main__":
    get_user_input()
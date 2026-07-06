import tkinter as tk
from tkinter import messagebox


print("Initializing Window, Please Wait...")
print("Window Loaded!")


def calculate_trip(distance, current_balance, transport_type):
    if transport_type == "Student Bus/MRT":
        rate_per_km = 0.05  
        base_fare = 0.45    
    else:  
        rate_per_km = 0.10  
        base_fare = 0.95    


    total_cost = base_fare + (distance * rate_per_km)
    total_cost = round(total_cost, 2) 


    if current_balance >= total_cost:
        remaining_balance = round(current_balance - total_cost, 2)
        status = "APPROVED"
        color = "#2ecc71" 
        message = f"""Trip Approved!\nFare Deducted: ${total_cost:.2f}\nNew Balance: ${remaining_balance:.2f}"""
    else:
        status = "DENIED"
        color = "#e74c3c" 
        message = f"Insufficient Funds!\nTrip Cost: ${total_cost:.2f}\nYou need ${round(total_cost - current_balance, 2):.2f} more."


    return status, color, message


class SimpleFareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SJI Transit Analytics Node")
        self.root.geometry("400x450")
        self.root.configure(bg="#2c3e50") 


        title = tk.Label(root, text="SJI SMART TRANSIT CALCULATOR", font=("Arial", 12, "bold"), fg="white", bg="#2c3e50", pady=10)
        title.pack()


        tk.Label(root, text="Enter Distance of travel (in km):", fg="white", bg="#2c3e50").pack(pady=5)
        self.distance_entry = tk.Entry(root, font=("Arial", 12), justify="center")
        self.distance_entry.pack()


        tk.Label(root, text="Enter Current EZ-Link Balance ($):", fg="white", bg="#2c3e50").pack(pady=5)
        self.balance_entry = tk.Entry(root, font=("Arial", 12), justify="center")
        self.balance_entry.pack()


        tk.Label(root, text="Select Fare Type:", fg="white", bg="#2c3e50").pack(pady=5)
        self.fare_type = tk.StringVar(root)
        self.fare_type.set("Student Bus/MRT") 
        dropdown = tk.OptionMenu(root, self.fare_type, "Student Bus/MRT", "Adult Fare")
        dropdown.config(font=("Arial", 10), width=18)
        dropdown.pack(pady=5)


        calc_btn = tk.Button(root, text="TAP CARD / CALCULATE", command=self.process_payment, bg="#3498db", fg="white", font=("Arial", 11, "bold"), height=2, width=22) 
        calc_btn.pack(pady=20)


        self.output_label = tk.Label(root, text="Awaiting Card Tap...", font=("Arial", 11, "bold"), bg="#34495e", fg="white", width=35, height=5, relief=tk.SUNKEN)
        self.output_label.pack(pady=10)


    def process_payment(self):
        try:
            dist = float(self.distance_entry.get())
            bal = float(self.balance_entry.get())
            transport = self.fare_type.get()


            status, bg_color, result_text = calculate_trip(dist, bal, transport)


            self.output_label.config(text=f"[{status}]\n{result_text}", bg=bg_color)
            
        except ValueError:
            messagebox.showerror("Input Error", """Please enter valid numbers for distance and balance.""")


if __name__ == "__main__":
    window = tk.Tk()
    app = SimpleFareApp(window)
    window.mainloop()

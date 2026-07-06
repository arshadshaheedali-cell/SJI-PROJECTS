import tkinter as tk
from tkinter import messagebox


class SimplePOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Retail POS System")
        self.root.geometry("800x500")
        self.root.configure(bg="#f4f4f4")


        self.menu_items = {
            "Burger": 5.99,
            "Fries": 2.49,
            "Soda": 1.50,
            "Pizza Slice": 3.99,
            "Ice Cream": 2.99,
            "Coffee": 2.00
        }


        self.order = {}
        self.setup_ui()


    def setup_ui(self):
        title = tk.Label(self.root, text="FAST FOOD POS", font=("Arial", 20, "bold"), bg="#333333", fg="white", pady=10)
        title.pack(fill=tk.X)


        main_frame = tk.Frame(self.root, bg="#f4f4f4")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


        menu_frame = tk.LabelFrame(main_frame, text=" Menu Items ", font=("Arial", 12, "bold"), bg="#f4f4f4")
        menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))


        row, col = 0, 0
        for item, price in self.menu_items.items():
            btn_text = f"{item}\n${price:.2f}"
            btn = tk.Button(
                menu_frame, 
                text=btn_text, 
                font=("Arial", 11, "bold"), 
                width=12, 
                height=3,
                command=lambda i=item, p=price: self.add_to_order(i, p)
            )
            btn.grid(row=row, column=col, padx=10, pady=10)
            
            col += 1
            if col > 2:
                col = 0
                row += 1


        receipt_frame = tk.LabelFrame(main_frame, text=" Current Order ", font=("Arial", 12, "bold"), bg="#f4f4f4")
        receipt_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)


        self.receipt_text = tk.Text(receipt_frame, font=("Courier", 10), width=35, height=15, state=tk.DISABLED)
        self.receipt_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)


        self.totals_label = tk.Label(receipt_frame, text="", font=("Courier", 10, "bold"), justify=tk.LEFT, bg="#f4f4f4")
        self.totals_label.pack(anchor="w", padx=10, pady=5)
        
        self.update_receipt_display()


        btn_container = tk.Frame(receipt_frame, bg="#f4f4f4")
        btn_container.pack(fill=tk.X, padx=5, pady=5)


        clear_btn = tk.Button(btn_container, text="Clear", bg="#e74c3c", fg="black", font=("Arial", 10, "bold"), command=self.clear_order, width=12)
        clear_btn.pack(side=tk.LEFT, padx=5)


        pay_btn = tk.Button(btn_container, text="Checkout", bg="#2ecc71", fg="black", font=("Arial", 10, "bold"), command=self.checkout, width=12)
        pay_btn.pack(side=tk.RIGHT, padx=5)


    def add_to_order(self, item, price):
        if item in self.order:
            self.order[item]['qty'] += 1
        else:
            self.order[item] = {'price': price, 'qty': 1}
        self.update_receipt_display()


    def update_receipt_display(self):
        self.receipt_text.config(state=tk.NORMAL)
        self.receipt_text.delete("1.0", tk.END)


        self.receipt_text.insert(tk.END, f"{'Item':<15}{'Qty':<5}{'Total':<10}\n")
        self.receipt_text.insert(tk.END, "-" * 30 + "\n")


        subtotal = 0.0


        for item, details in self.order.items():
            item_total = details['price'] * details['qty']
            subtotal += item_total
            self.receipt_text.insert(tk.END, f"{item:<15}{details['qty']:<5}${item_total:.2f}\n")


        self.receipt_text.config(state=tk.DISABLED)


        tax = subtotal * 0.10
        total = subtotal + tax


        totals_string = (
            f"Subtotal:  ${subtotal:.2f}\n"
            f"Tax (10%): ${tax:.2f}\n"
            f"Total:     ${total:.2f}"
        )
        self.totals_label.config(text=totals_string)


    def clear_order(self):
        self.order.clear()
        self.update_receipt_display()


    def checkout(self):
        if not self.order:
            messagebox.showwarning("Empty Order", "Please add items to the order first!")
            return
        
        messagebox.showinfo("Success", "Payment Processed Successfully!")
        self.clear_order()


if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePOS(root)
    root.mainloop()



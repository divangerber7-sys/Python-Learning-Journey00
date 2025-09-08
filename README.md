👋 Hi, I’m Divan Gerber  

🎯 **Career Goal**: Aspiring Cybersecurity Engineer with a focus on **Python scripting & automation for security**.  
💻 Currently building hands-on projects while completing **Python for Cybersecurity** courses & tutorials.  

---

## 🛠️ Tech Stack (in progress)  
- **Programming**: Python (beginner–intermediate, applied to cybersecurity automation)  
- **Cybersecurity Tools**: Wireshark, Nmap, Vanta (automation & compliance)  
- **Operating Systems**: Linux (basic administration, shell scripting), Windows  
- **Version Control**: Git, GitHub  

---

## 🚀 Projects  

### ☕ Coffee Shop Ordering System  
*A beginner Python project simulating a point-of-sale system.*  
- Features conditional logic, input handling, price calculation, and quantity multiplication.  
- Demonstrates Python fundamentals (variables, if/else, string formatting).  

**Code Example:**  
```python
menu = ["Black Coffee", "Espresso", "Latte", "Cappucino", "Frappucino"]

print("Hello, welcome to the Coffee Emporium!!!")

name = input("What is your name?\n")

if name == "Divan":
    evil_status = input("Are you evil?\n").strip().lower()
    if evil_status == "yes":
        print("I am sorry but you are not welcome here")
        exit()
    else:
        print("Oh, so you are one of those good Divans. Welcome!!!")
else:
    print(f"Hello {name}. Thank you for coming in today.\n")

print(f"What would you like today? On our menu we have: {', '.join(menu)}")

order = input().title().strip()
quantity = int(input("How many would you like?\n"))

prices = {
    "Frappucino": 13,
    "Black Coffee": 3,
    "Espresso": 5,
    "Cappucino": 10,
    "Latte": 9
}

if order in prices:
    price = prices[order]
    if order == "Latte":
        latte_order = input("Do you want extra whipped cream? \n").strip().lower()
        if latte_order == "yes":
            price = 13
else:
    print("I am sorry, we don't have that here today")
    exit()

total = price * quantity
print(f"That is great. Your price is: ${total}")
print(f"We will have your {quantity} cups of {order} ready shortly. Have a great day!")
________________________________________
🔍 Simple Port Scanner (coming soon)
•	Python script to scan open ports on a target system.
•	Educational use for understanding networking + Python socket library.
________________________________________
📊 Log Parser (planned)
•	Python tool to extract failed login attempts from system logs.
•	Helps automate basic incident detection.
________________________________________
📈 Learning Roadmap
•	Python fundamentals (input, variables, conditionals)
•	First project: Coffee Shop Ordering System
•	Networking basics in Python (sockets, port scanner)
•	Log analysis and parsing with Python
•	Automation scripts for common security tasks
________________________________________
🌍 Connect with Me
•	LinkedIn - https://www.linkedin.com/in/divan-gerber-9a6922356/
•	📧 divangerber7@gmail.com

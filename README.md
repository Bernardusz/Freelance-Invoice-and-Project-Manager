# 💼 Freelance Project & Invoice Manager (Python CLI App)

A command-line application to manage freelance clients, projects, and invoices. Built fully with Python and OOP principles. Designed to streamline your freelance workflow: track clients, log completed work, mark projects done, and auto-generate invoices!

---

## 🔧 Features

- ✅ Add clients and projects
- ✅ Log work (with hours, description, and date)
- ✅ View project summaries per client
- ✅ Mark projects as completed
- ✅ Auto-generate invoices (rate × hours)
- ✅ Save and load data from JSON
- ✅ Modular OOP design

---

## 📁 Project Structure

```bash
.
├── allfunctions.py   # All class definitions and logic
├── script.py         # Main CLI interface
├── welcome.txt       # Welcome message
└── file.json         # Saved project and worklog data
```

---

## 🚀 How to Run
```bash
git clone https://github.com/Bernardusz/Freelance-Invoice-and-Project-Manager.git
cd Freelance-Invoice-and-Project-Manager
python script.py
```

---

## 📌 Sample Commands
Add Client

Add Project to Client

Log Work

View Project

Mark Project as Completed

Generate Invoice

Save to JSON

Load from JSON

Exit

---

## 💾 JSON Format
```
{
  "client": {
    "Anastasia": {
      "Design Website": {
        "title": "Design Website",
        "rate": 30000,
        "hour": 10,
        "status": "Done"
      }
    }
  },
  "worklog": {
    "Anastasia": {
      "Title": "Design Website",
      "Description": "Created homepage",
      "Rate per hour": 30000,
      "Total hours": 10,
      "Date finished": "2025-04-19"
    }
  }
}
```

---

## 🧠 Concepts Used
Python OOP: Classes, inheritance, polymorphism

Encapsulation

JSON I/O

CLI Interface

Class composition and delegation

---

✨ Credit
Created with love and 4+ hours of sweat by **Bernardus** ❤️

"More work = Brighter future 💼"

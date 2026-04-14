# Coffee Machine Simulator (OOP Version) ☕

This project is an Object-Oriented Programming implementation of a terminal-based coffee machine simulator built in Python.

Unlike the procedural version, this implementation focuses on coordinating multiple classes to simulate how real-world systems collaborate through structured responsibilities.

---

## Project Objective

The goal of this project was to practice:

- Working with prebuilt classes
- Understanding object interaction
- Passing objects between modules
- Managing program flow using class methods
- Simulating a real-world machine workflow using OOP structure

Instead of writing the internal logic of the machine manually, the task was to integrate and control existing components correctly.

---

## Classes Used

This project uses three provided classes:

### Menu

Responsible for:

- Storing available drinks
- Returning drink options
- Returning drink objects

---

### CoffeeMaker

Responsible for:

- Tracking available resources
- Checking ingredient availability
- Preparing drinks
- Printing machine resource reports

---

### MoneyMachine

Responsible for:

- Handling coin input
- Processing payments
- Validating transactions
- Tracking profit
- Printing money reports

---

## Application Workflow

The program follows this object interaction pipeline:

User selects drink
↓
Menu returns drink object
↓
CoffeeMaker checks resources
↓
MoneyMachine processes payment
↓
CoffeeMaker prepares drink


Each component performs only its assigned responsibility, demonstrating proper separation of concerns.

---

## Features

- Interactive terminal interface
- Resource availability checking
- Payment processing system
- Profit tracking
- Machine status reporting
- Clean modular workflow using OOP structure

---


## Concepts Practiced

This project demonstrates practical usage of:

- Object instantiation
- Method invocation
- Class responsibility separation
- External module interaction
- Program control loops
- Real-world system simulation using OOP

---

## Tech Stack

Python (Intermediate Level)

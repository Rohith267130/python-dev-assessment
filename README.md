# Python Developer Assessment
This repository is for my developer assessment tasks.


## Project Overview

This repository contains my work for the **Python Developer Assessment Program**. The purpose of this project was to practice and demonstrate some core Python development skills. These include setting up a Python environment, using Git and GitHub for version control, maintaining good code style with formatting and linting tools, working with basic data structures and algorithms, applying object-oriented programming concepts, handling errors properly, and interacting with a simple REST API.

Each task in the assessment focuses on a specific topic and was developed on its own branch to follow a typical Git workflow.

---

# Completed Tasks

## Phase 1 – Setup & Foundational Review

### Task 1.1 – Hello World

To begin, I created a simple Python script to confirm that the development environment was correctly installed and working.

**File**

* `hello.py`

**What it does**

* Prints a short message to the console to verify that Python runs successfully.

---

### Task 1.2 – Git & GitHub Basics

In this step, I set up version control for the project and connected the local repository to GitHub.

**Actions completed**

* Created a GitHub repository
* Initialized a Git repository locally
* Added a README file
* Made the initial commit
* Created and pushed a feature branch

**Files**

* `README.md`
* `hello.py`

**Branch**

* `task-1.2-git-basics`

---

### Task 1.3 – Code Style & Linting

For this task, I explored tools that help maintain consistent and clean Python code.

**Tools used**

* **Black** – automatically formats Python code
* **Flake8** – checks the code for style issues based on the PEP 8 guidelines

**File**

* `bad_style.py`

This file initially contained poorly formatted code which I then corrected using the formatter and linter.

**Branch**

* `task-1.3-code-style`

---

# Phase 2 – Core Programming Concepts

### Task 2.1 – Data Structures & Algorithms

In this task, I implemented a couple of functions that work with lists, dictionaries, and string data.

**Functions implemented**

* `filter_and_sort_evens(numbers)` – filters even numbers from a list and returns them sorted
* `count_character_frequency(text)` – counts how often each character appears in a string

**File**

* `dsa_challenges.py`

**Branch**

* `task-2.1-dsa`

---

### Task 2.2 – Object-Oriented Programming

Here I created a simple `Book` class to demonstrate basic object-oriented programming concepts.

**Features of the class**

* An `__init__` method to initialize book attributes
* A method to calculate how old the book is
* A method that returns a summary of the book’s details

**File**

* `book_store.py`

**Branch**

* `task-2.2-oop`

---

### Task 2.3 – Error Handling & Debugging

This task focused on writing more reliable code by handling potential runtime errors.

**Functions implemented**

* `calculate_average(numbers)` – calculates the average of a list and safely handles empty lists
* `get_list_element(my_list, index)` – safely retrieves an element while handling invalid indexes or incorrect input types

**File**

* `debug_errors.py`

**Branch**

* `task-2.3-error-debug`

---

# Phase 3 – Integration

### Task 3.1 – API Interaction

In the final task, I worked with a public API and used Python’s `requests` library to retrieve and display user data.

**API used**

https://jsonplaceholder.typicode.com/users

**Function implemented**

* `fetch_and_display_users(num_users)` – fetches user information from the API and prints selected details such as name, email, and city.

**File**

* `api_client.py`

**Branch**

* `task-3.1-api-interaction`

---

# How to Run the Code

### 1. Clone the repository

```
git clone https://github.com/your-username/python-dev-assessment.git
```

### 2. Navigate to the project folder

```
cd python-dev-assessment
```

### 3. Install required dependencies

```
pip install requests black flake8
```

### 4. Run any of the Python files

Examples:

```
python hello.py
python dsa_challenges.py
python book_store.py
python debug_errors.py
python api_client.py
```

---

# Reflections

### Most Challenging

The most challenging part for me was implementing proper error handling. I needed to think about different edge cases, such as empty lists or invalid inputs, and make sure the program could handle them without crashing.

---

### Most Interesting

The API interaction task was the most interesting. It was helpful to see how Python can communicate with external services and work with JSON data returned from an API.

---

### What I Learned

During this assessment, I strengthened my understanding of several important development practices, including:

* Using Git branches to organize work
* Writing cleaner and more consistent Python code using **Black** and **Flake8**
* Handling exceptions to make programs more reliable
* Applying basic **object-oriented programming concepts**
* Fetching and processing data from a REST API

Overall, this project helped reinforce my foundational Python skills and gave me more confidence working with common development tools.

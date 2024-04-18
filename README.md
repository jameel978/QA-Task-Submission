<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/8759/8759133.png" width="400" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">QA TASK SUBMISSION</h1>
</p>
<p align="center">
    <em>This repository presents a solution to a QA task, comprising two parts. The first part analyzes a suggested loan offer generation process, detailing the application workflow, models, decision criteria, and evaluation of response outputs. The second part involves Python programming tasks focusing on string manipulation and palindrome detection.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/jameel978/QA-Task-Submission?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/jameel978/QA-Task-Submission?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/jameel978/QA-Task-Submission?style=default&color=0080ff" alt="repo-top-language">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#overview)
- [ Repository Structure](#repository-structure)
- [ Modules](#modules)
- [ Getting Started](#getting-started)
  - [ Installation](#installation)
  - [ Test Functions Example](#Test-Functions-Example)
  - [ Import Functions Example](#Import-Functions-Example)
- [ Contributing](#contributing)
- [ License](#license)
</details>
<hr>

##  Overview

This repository contains a comprehensive solution to a Production QA exam, divided into two parts. The exam involves a detailed analysis of a loan offer generation process and implementation of Python programs to perform specific tasks.

### Part 1: Loan Offer Generation Process

- This section presents a thorough examination of the loan offer generation process. It includes:
  - Overview of the application and offer generation process.
  - Explanation of models, converters, alignment components, and loan restrictions involved in the process.
  - Discussion on the final decision-making criteria for approving or declining loan offers.
  - Evaluation of response outputs for various applications to ensure adherence to the defined criteria.
  - Bonus question analyzing the behavior of the system with different threshold values.

### Part 2: Python Programming

- The second part of the exam involves solving programming tasks using Python. It includes:
  - Implementation of a Python program to find words longer than a specified length in a given string.
  - Development of a Python function to determine if a string is a palindrome or not, applied to a list of words.

---


##  Repository Structure

```sh
└── QA-Task-Submission/
    ├── LICENSE
    ├── QA_exam_answers.pdf
    ├── README.md
    └── word_operations.py
```

---

##  Modules



| File                                                                                                   | Summary                                                                                                                                                                                                                                                                                                |
| ---                                                                                                    | ---                                                                                                                                                                                                                                                                                                    |
| [word_operations.py](https://github.com/jameel978/QA-Task-Submission/blob/master/word_operations.py) | 1. Words_longer_than_n: `Filters and returns a list of words longer than a specified length from an input string` (2 versions available, with and without using built-in Python functions).   <br />2. is_palindrome: `Checks if a given word is identical to its reverse order, becoming a palindrome`  (2 versions available, with and without using built-in Python functions).|



---

##  Getting Started

**System Requirements:**

* **Python**: `version 3.12`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the QA-Task-Submission repository:
>
> ```console
> git clone https://github.com/jameel978/QA-Task-Submission
> ```
>
> 2. Change to the project directory:
> ```console
> cd QA-Task-Submission
> ```
>


###  Test Functions Example

<h4>From <code>source</code></h4>

> Run QA-Task-Submission using the command below:
> ```console
> python word_operations.py
> ```

###  Import Functions Example

<h4>From <code>source</code></h4>

> Run QA-Task-Submission using the command below:
> ```python
>    from word_operations import words_longer_than_n, words_longer_than_n_no_builtin, is_palindrome,is_palindrome_no_builtin
>
>    # Example usage of words_longer_than_n function
>    string = 'The quick brown fox jumps over the lazy dog'
>    n = 4
>    longer_words = words_longer_than_n(string, n)
>    print(f"Words longer than {n} characters: {longer_words}")
>
>    # Example usage of words_longer_than_n_no_builtin function
>    string = 'The quick brown fox jumps over the lazy dog'
>    n = 4
>    longer_words_no_builtin = words_longer_than_n_no_builtin(string, n)
>    print(f"Words longer than {n} characters without using built-in functions: {longer_words_no_builtin}")
>    
>    # Example usage of is_palindrome function
>    words_list = ['sheep', 'xenex', 'cow', 'radar', 'level']
>    for word in words_list:
>        print(f"{word} is a palindrome: {is_palindrome(word)}")
>
>    # Example usage of is_palindrome_no_builtin function
>    words_list = ['sheep', 'xenex', 'cow', 'radar', 'level']
>    for word in words_list:
>        print(f"{word} is a palindrome without using built-in functions: {is_palindrome_no_builtin(word)}")
> ```

---



##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/jameel978/QA-Task-Submission/issues)**: Submit bugs found or log feature requests.
- **[Submit Pull Requests](https://github.com/jameel978/QA-Task-Submission/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/jameel978/QA-Task-Submission/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/jameel978/QA-Task-Submission
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updat
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>


---

##  License

This project is protected under the [MIT License](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/mit) file.

---

[**Return**](#-overview)

---

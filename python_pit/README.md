
# Python Pit 8-Week Program

## Overview

Welcome to the **Python Pit** 8-week coding program! This program is designed to progressively teach Python programming concepts through hands-on activities and challenges. Each week focuses on specific topics, helping learners build their Python skills with practical examples, challenges, and pseudocode exercises.

The program is structured to cover key Python concepts from basic syntax to advanced problem-solving techniques. By the end of the 8 weeks, participants will have a strong understanding of Python programming and be able to apply it to various projects.

---

## Folder Structure

The repository is organized into weekly folders (`wk01`, `wk02`, ..., `wk08`), each representing one week of the program. Inside each folder, you'll find the following content:

```
.
├── readme_files                 # Contains README templates for each week
├── wk01 - wk08                  # Folders for each week of the program
│   ├── python_scripts           # Contains Python scripts and challenges for each week
│   │   ├── activity.py          # Main activity for the week
│   │   ├── advanced_challenge.py# Advanced challenge for those who want to go further
│   │   ├── challenge.py         # Additional challenge for skill enhancement
│   └── README.md                # Overview of the week's objectives and content
```

---

## Instructions for Students

### 1. Fork the Repository

To get started with the program, you need to fork this repository to your own GitHub account.

1. Go to the main page of the repository: [python_pit](https://github.com/yourusername/python_pit).
2. In the top-right corner of the page, click **Fork**.
3. GitHub will create a copy of the repository under your own account. You now have your own version of the repository, and you can make changes to it independently.

### 2. Clone Your Forked Repository

After forking the repository, clone it to your local machine so that you can start working on the assignments.

1. Copy the URL of your forked repository (you can find it by clicking the green **Code** button on your repository page).
2. Open your terminal and run the following command, replacing `yourusername` with your GitHub username:
   ```bash
   git clone https://github.com/yourusername/python_pit.git
   ```
3. Navigate to the cloned repository:
   ```bash
   cd python_pit
   ```

### 3. Work on the Assignments

1. Each week, go to the corresponding folder (e.g., `wk01`, `wk02`) and open the `README.md` file for instructions on the activities and challenges.
2. Make changes to the Python scripts as required by the assignments.

### 4. Commit Your Changes

After working on an assignment, you need to commit your changes to your local repository:

1. Stage the changes you want to commit:
   ```bash
   git add .
   ```

2. Commit the changes with a descriptive message:
   ```bash
   git commit -m "Completed Week 1 Assignment"
   ```

### 5. Push Your Changes to Your Fork

After committing your changes, push them to your forked repository on GitHub:

```bash
git push origin master
```

### 6. Submit a Pull Request (For Feedback Only)

Once you have completed an assignment and pushed your changes to your forked repository, you need to submit a pull request to the original repository so that your work can be reviewed.

1. Go to your forked repository on GitHub.
2. Click on the **Pull Requests** tab.
3. Click on the **New Pull Request** button.
4. Select the branch you want to merge from (typically `master` in your fork) and the branch you want to merge into (`master` in the original repository).
5. Add a meaningful title and description for your pull request, explaining the changes you made.
6. Submit the pull request.

**Important**: The pull request will not affect the main repository code. It is solely for feedback and review. The teacher will review your code and provide feedback through the pull request.

### 7. Wait for Feedback

Once your pull request is submitted, the repository owner (your teacher) will review your code and provide feedback. If changes are requested, you can make the necessary updates to your fork and the pull request will automatically update.

---

## How to Use This Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python_pit.git
   ```

2. Navigate to the week you are working on:
   ```bash
   cd python_pit/wk01  # For Week 1
   ```

3. Open the `python_scripts` folder for each week and follow the instructions in the `README.md` files.

4. Work through the activities and challenges, starting from basic concepts in Week 1 and progressing to advanced topics in Week 8.

---

## Contributing

If you would like to contribute to this program, feel free to fork the repository, make your changes, and submit a pull request. Suggestions for new activities, challenges, or improvements are always welcome!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

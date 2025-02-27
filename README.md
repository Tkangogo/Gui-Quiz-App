# GUI Quiz App
## How It Works

1. The app **fetches 10 True/False questions** from the Open Trivia Database API.
2. Each question is displayed in the **Tkinter window** one at a time.
3. The user answers by clicking either the **True ✅ or False ❌ button**.
4. The app **checks the answer** and updates the score if correct.
5. It provides visual feedback:
   - ✅ **Green background** → Correct answer
   - ❌ **Red background** → Incorrect answer
6. The quiz continues until all questions are answered.
7. At the end, it displays **"You have reached the end of the quiz."**, and the buttons are disabled.

---

## Files Breakdown

- `question_class.py` → Defines a **Question class** to store the question and correct answer.
- `data.py` → Fetches quiz questions from an **API** and formats them for use.
- `quiz_brain_class.py` → Handles **quiz logic**, including keeping track of the current question, checking answers, and updating the score.
- `ui_class.py` → Creates the **Graphical User Interface (GUI)** using Tkinter. It:
  - Displays the questions  
  - Updates the score  
  - Handles button clicks  
- `false.png` & `true.png` → Images used for True/False buttons.

---

## How to Run the App

1. **Install Python (if not already installed)**  
2. **Install dependencies:**  
   ```sh
   pip install requests
   ```
3. **Run the app:**  
   ```sh
   python main.py
   ```

---

## Future Improvements

- Add more question types (multiple choice).  
- Allow users to select difficulty levels.  
- Save scores for user progress tracking.  

---


# Step 1: Sabse pehle hum questions aur unke options ki ek list bana rahe hain.
# Har question ke andar uska question text, 4 options aur correct answer ka option key hai.
questions = [
    {
        "question": "1. Python kya hai?",
        "options": ["A) Ek Snake", "B) Programming Language", "C) Ek Car", "D) Ek Game"],
        "answer": "B"
    },
    {
        "question": "2. Python me message print karne ke liye konsa function use karte hain?",
        "options": ["A) print()", "B) write()", "C) speak()", "D) show()"],
        "answer": "A"
    },
    {
        "question": "3. Computer ka brain kise kaha jata hai?",
        "options": ["A) RAM", "B) Mouse", "C) CPU", "D) Keyboard"],
        "answer": "C"
    }
]

# Step 2: User ka score count karne ke liye variable initialize kar rahe hain
score = 0

# Step 3: Game start hone par welcome message display kar rahe hain
print("--- Welcome to Python Quiz Game ---")
print()

# Step 4: Har question ko ek ek karke display karne ke liye loop chala rahe hain
for q in questions:
    # Question text print kar rahe hain
    print(q["question"])
    
    # Options print karne ke liye inner loop ka use kar rahe hain
    for option in q["options"]:
        print(option)
    
    # User se input le rahe hain aur upper() function se lowercase ko uppercase me convert kar rahe hain
    user_answer = input("\nApna option chune (A, B, C, D): ").upper()
    
    # Check kar rahe hain ki user ka answer correct answer se match hota hai ya nahi
    if user_answer == q["answer"]:
        print("Sahi jawab!\n")
        score = score + 1
    else:
        print(f"Galat jawab. Sahi answer tha: {q['answer']}\n")

# Step 5: Final score display kar rahe hain
print("-----------------------------------")
print(f"Quiz Finished! Aapka Total Score hai: {score}/{len(questions)}")
print("-----------------------------------")
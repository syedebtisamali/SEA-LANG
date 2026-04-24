# SEA Lang: The Ultimate Family Language 🌊

**SEA Lang** is a "Family Language" designed to make the power of Python accessible to everyone. It provides the easiest possible roadmap for beginners, children, and professionals who are not familiar with mathematics or complex computer science terms. By stripping away the "fear factor" of coding, SEA Lang allows anyone to utilize the maximum abilities of Python through a warm, readable, and flexible interface.

## 🌟 The True Face of SEA

SEA is more than a language; it is a more efficient and user-friendly way to interact with Python. 

* **Human-Centric Design:** Perfect for those who find symbols, byte-width operations, and rigid syntax intimidating. It speaks your language.
* **The Python Powerhouse:** It doesn't just "mimic" Python; it utilizes Python's maximum capabilities. If Python can do it, SEA can do it—but easier.
* **A Gentle Roadmap:** It serves as a bridge for beginners, moving them from natural language into logical thinking without the "wall" of complex mathematics.

---

## ✅ Advantages vs. ❌ Disadvantages

### Advantages
* **Dual-Mode Syntax:** SEA is flexible. Use natural language phrases (like `is equal to`) when you want readability, or switch to standard symbols (`=`, `+`, `**`) if you are a fast typer or feel "bored" with words.
* **No Math Required:** Complex arithmetic and bitwise operations are mapped to plain English, removing the barrier for non-mathematicians.
* **Onion Parsing:** Sophisticated recursive logic handles nested function calls automatically, so you never have to count closing parentheses again.
* **Indentation Control:** Combines the visual discipline of C with the clean look of Python.

### Disadvantages
* **Performance Overhead:** There is a minor conversion delay when translating SEA to Python. However, because it supports direct symbol usage, this overhead is kept to a minimum.
* **Ambiguity Management:** While natural language can be broad, SEA provides C-style symbols as a fallback to ensure 100% precision when needed.
* **Debugging Layers:** Currently, errors are traced through the generated Python code. **Note:** We are actively developing an internal SEA-debugger to map errors directly back to your source lines (Coming soon, Insha Allah).

---

## 🛠 How SEA Works (The Pipeline)

1.  **Ingestion:** Accepts `.sea` files containing either words, symbols, or a mix of both.
2.  **Sanitization:** Cleans comments and empty lines while protecting your data.
3.  **Keyword & Symbol Mapping:** Converts phrases or C-style symbols into Python-compatible logic.
4.  **The "Onion" Parser:** Recursively wraps functions (like `write len list`) into valid executable code.
5.  **F-String Promotion:** Automatically detects variables in strings via `{}` and handles the formatting.
6.  **Direct Execution:** Runs the final optimized Python payload instantly.

---

## 💻 Example: Words or Symbols? You Choose.

### Natural Style
```text
n is equal to 7
n_sq = square n
print "The square is {n_sq}"
Symbol Style (C/Python Style)

Plaintext
n = 7
n_sq = square(n)
print("The square is {n_sq}")
Both styles work perfectly in SEA Lang!

🔧 Technical Challenges Solved
The Recursive "Onion" Fix

To handle layers like write len list, the engine "peels" the code, wrapping the innermost function first and moving outward until the statement is stable.

Assignment Protection

Using Negative Lookaheads, the engine is smart enough to know that list = [1,2,3] is a variable, while list my_data is a function call.

📂 Installation
Clone the repository:

Bash
git clone [https://github.com/yourusername/sea-lang.git](https://github.com/yourusername/sea-lang.git)
Run the interpreter:

Bash
python3 main.py
👤 Author

Syed Ebtisam Ali - Developer of SEA Lang
"Making technology speak the language of the family."

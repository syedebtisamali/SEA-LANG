# main.py

# MAIN FUNCTION: (Workflow of interpreter)
def main():
    debug = True
    # Step 1: Get SEA code (from file or input)
    sea_code = get_sea_code();
    if debug:
        print(f"\nSEA CODE:\n\n{sea_code}")
    # Step 2: Remove empty lines from SEA code
    code_without_empty_lines = remove_empty_lines(sea_code);
    if debug:
        print(f"\nCODE WITHOUT EMPTY LINES:\n\n{code_without_empty_lines}")
    # Step 3: Remove single-line comments from SEA code
    code_without_single_line_comments = remove_single_line_comments(code_without_empty_lines);
    if debug:
        print(f"\nCODE WITHOUT SINGLE-LINE COMMENTS:\n\n{code_without_single_line_comments}")
    # Step 4: Convert uppercase to lowercase
    code_without_uppercase = uppercase_to_lowercase(code_without_single_line_comments);
    if debug:
        print(f"\nCODE WITHOUT UPPERCASE:\n\n{code_without_uppercase}")
    # Step 5: Replace SEA KEYWORDS with Python SYMBOLS
    code = replace_keywords(code_without_uppercase);
    if debug:
        print(f"\nCODE AFTER KEYWORD REPLACEMENT:\n\n{code}")
    # Step 6: Add spaces around symbols
    code_with_spaces_around_symbols = add_spaces_before_and_after_symbols(code);
    if debug:
        print(f"\nCODE WITH SPACES AROUND SYMBOLS:\n\n{code_with_spaces_around_symbols}")
    # Step 7: Handle "approches" loops:
    python_code = approches_loop(code_with_spaces_around_symbols);
    if debug:
        print(f"\nPYTHON CODE WITH APPROCHES LOOPS:\n\n{python_code}")
    # Step 8: Convert SEA functions to Python functions
    code_with_python_functions = sea_func_to_python_func(python_code);
    if debug:
        print(f"\nCODE WITH PYTHON FUNCTIONS:\n\n{code_with_python_functions}")
    # Step 9: Translate SEA Syntax to Python Syntax:
    python_code = translate_sea_to_python(code_with_python_functions);
    if debug:
        print(f"\nPYTHON CODE:\n\n{python_code}")
    # Step 10: Add f before strings for f-string support
    python_code = add_f_to_strings(python_code);
    if debug:
        print(f"\nPYTHON CODE WITH F-STRINGS:\n\n{python_code}")
    # Step 11: Run the generated Python code
    run_python_code(python_code)

# HELPER FUNCTIONS:

import re

def get_sea_code():
    sea_code = input("Enter SEA code file location: ")
    with open(sea_code, 'r') as code:
        sea_code = code.read() # Read the contents of the SEA code file
        return sea_code # Return the SEA code as a string

def remove_empty_lines(code):
    lines = code.splitlines() # Split the code into lines
    non_empty_lines = [] # List to hold non-empty lines
    for line in lines:
        stripped_line = line.strip() # Remove leading and trailing whitespace from the line
        if len(stripped_line) > 0: 
            non_empty_lines.append(line) # Add the original line (with indentation) to the list of non-empty lines
    code_without_empty_lines = '\n'.join(non_empty_lines) # Join the non-empty lines back into a single string
    return code_without_empty_lines # Return the code without empty lines

def remove_single_line_comments(code):
    lines = code.splitlines()
    final_code = []

    for line in lines:
        new_line = []
        in_string = False
        quote_type = None
        escaped = False

        for char in line:
            # 1. Handle Escape Characters
            if char == "\\" and in_string and not escaped:
                escaped = True
                new_line.append(char)
                continue

            # 2. Handle Quote Toggling
            if (char == '"' or char == "'") and not escaped:
                if not in_string:
                    in_string = True
                    quote_type = char
                elif char == quote_type:
                    in_string = False
                    quote_type = None
            
            # 3. Handle the Comment Marker
            if char == "#" and not in_string:
                break
            
            new_line.append(char)
            escaped = False # Reset escape flag after any character

        # Reconstruct the line
        cleaned_line = "".join(new_line).rstrip()
        if cleaned_line:
            final_code.append(cleaned_line)

    return "\n".join(final_code)

def uppercase_to_lowercase(code):
    new_code = []
    in_string = False
    quote_type = None
    escaped = False

    for char in code:
        # 1. Handle Escape Characters (so \" doesn't end a string)
        if char == "\\" and in_string and not escaped:
            escaped = True
            new_code.append(char)
            continue

        # 2. Track String State
        if (char == '"' or char == "'") and not escaped:
            if not in_string:
                in_string = True
                quote_type = char
            elif char == quote_type:
                in_string = False
                quote_type = None
        
        # 3. Transform Logic: Lowercase ONLY if not in a string
        if not in_string:
            new_code.append(char.lower())
        else:
            new_code.append(char)
        
        escaped = False # Reset escape flag

    return "".join(new_code)

def replace_keywords(code):
    KEYWORDS = {
        # Assignment Operators:
        "is equal to": "=",
        # Compound Assignment Operators:
        "plus equal to": "+=",
        "minus equal to": "-=",
        "times equal to": "*=",
        "over equal to": "/=",
        "mod equal to": "%=",
        "to power of equal to": "**=",
        "bitwise and equal to": "&=",
        "bitwise or equal to": "|=",
        "bitwise xor equal to": "^=",
        "left shift equal to": "<<=",
        "right shift equal to": ">>=",
        # Arithmetic Operators:
        "plus": "+",
        "minus": "-",
        "times": "*",
        "over": "/",
        "mod": "%",
        "to power of": "**",
        # Comparison Operators:
        "equal to": "==",
        "not equal to": "!=",
        "greater than": ">",
        "less than": "<",
        "greater than or equal to": ">=",
        "less than or equal to": "<=",
        # Logical Operators:
        "and": "and",
        "or": "or",
        "not": "not",
        # Identity Operators:
        "is": "is",
        "is not": "is not",
        # Membership Operators:
        "in": "in",
        "not in": "not in",
        # Bitwise Operators:
        "bitwise and": "&",
        "bitwise or": "|",
        "bitwise xor": "^",
        "bitwise not": "~",
        "left shift": "<<",
        "right shift": ">>",
        # ".": "\n", # Its dine in the code with regex to avoid replacing periods in strings
        "...": "pass",
        "the": "",
        "is input": "= input",
        "Nothing": "None",
        "scan": "input",
        "get": "input",
        "read": "input",
        "write": "print",
        "display": "print",
        "output": "print",
        "if": "if", "else": "else", "else if": "elif",

    # Constants
    "true": "True", "false": "False", "none": "None", 
    "ellipsis": "Ellipsis", "notimplemented": "NotImplemented",

    # Base Classes
    "baseexception": "BaseException", "exception": "Exception", 
    "arithmeticerror": "ArithmeticError", "buffererror": "BufferError", 
    "lookuperror": "LookupError",

    # Concrete Exceptions (The Big List)
    "assertionerror": "AssertionError", "attributeerror": "AttributeError",
    "eoferror": "EOFError", "floatingpointerror": "FloatingPointError",
    "generatorexit": "GeneratorExit", "importerror": "ImportError",
    "indexerror": "IndexError", "keyerror": "KeyError",
    "keyboardinterrupt": "KeyboardInterrupt", "memoryerror": "MemoryError",
    "nameerror": "NameError", "notimplementederror": "NotImplementedError",
    "oserror": "OSError", "overflowerror": "OverflowError",
    "recursionerror": "RecursionError", "referenceerror": "ReferenceError",
    "runtimeerror": "RuntimeError", "stopiteration": "StopIteration",
    "stopasynciteration": "StopAsyncIteration", "syntaxerror": "SyntaxError",
    "indentationerror": "IndentationError", "taberror": "TabError",
    "systemerror": "SystemError", "systemexit": "SystemExit",
    "typeerror": "TypeError", "unboundlocalerror": "UnboundLocalError",
    "unicodeerror": "UnicodeError", "unicodeencodeerror": "UnicodeEncodeError",
    "unicodedecodeerror": "UnicodeDecodeError", "unicodetranslateerror": "UnicodeTranslateError",
    "valueerror": "ValueError", "zerodivisionerror": "ZeroDivisionError",

    # OS Error Subclasses (Very common in file handling)
    "blockingioerror": "BlockingIOError", "childprocesserror": "ChildProcessError",
    "connectionerror": "ConnectionError", "brokenpipeerror": "BrokenPipeError",
    "connectionabortederror": "ConnectionAbortedError", "connectionrefusederror": "ConnectionRefusedError",
    "connectionreseterror": "ConnectionResetError", "fileexistserror": "FileExistsError",
    "filenotfounderror": "FileNotFoundError", "interruptederror": "InterruptedError",
    "isadirectoryerror": "IsADirectoryError", "notadirectoryerror": "NotADirectoryError",
    "permissionerror": "PermissionError", "processlookuperror": "ProcessLookupError",
    "timeouterror": "TimeoutError",

    # Warnings (Rarely used in SEA, but good for completeness)
    "warning": "Warning", "userwarning": "UserWarning", "deprecationwarning": "DeprecationWarning",
    "syntaxwarning": "SyntaxWarning", "runtimewarning": "RuntimeWarning",
    "futurewarning": "FutureWarning", "importwarning": "ImportWarning",
    "unicodewarning": "UnicodeWarning", "byteswarning": "BytesWarning",
    "resourcewarning": "ResourceWarning"

    }
    # 1. PROTECT STRINGS
    strings = []
    def save_str(match):
        strings.append(match.group(0))
        return f"__STR_PLACEHOLDER_{len(strings)-1}__"
    
    # We start with protected_code
    protected_code = re.sub(r'(".*?"|\'.*?\')', save_str, code)

    # 2. REPLACE PERIODS (Corrected variable name)
    # Use protected_code here, NOT code
    protected_code = re.sub(r'\.(?=\s|$)', '\n', protected_code)

    # 3. REPLACE PHRASES
    sorted_keywords = sorted(KEYWORDS.keys(), key=len, reverse=True)
    for keyword in sorted_keywords:
        if keyword == "": continue 
        
        # --- ADD THIS SPECIAL CASE HERE ---
        if keyword == "the":
            # This matches "the" and all following spaces, then removes them
            pattern = r'\bthe\s+'
            protected_code = re.sub(pattern, "", protected_code, flags=re.IGNORECASE)
        else:
            # This is your existing logic for all other keywords
            pattern = r'\b' + re.escape(keyword) + r'\b'
            protected_code = re.sub(pattern, KEYWORDS[keyword], protected_code, flags=re.IGNORECASE)

    # 4. RESTORE STRINGS
    for i, original_str in enumerate(strings):
        protected_code = protected_code.replace(f"__STR_PLACEHOLDER_{i}__", original_str)

    return protected_code

def add_spaces_before_and_after_symbols(code):
    lines = code.splitlines()
    final_lines = []

    SYMBOLS = ['**=', '<<=', '>>=', '+=', '-=', '*=', '/=', '%=', '==', '!=', '>=', '<=', '**', '<<', '>>',
               '+', '-', '*', '/', '%', '=', '>', '<', '&', '|', '^']

    for line in lines:
        new_line_chars = []
        in_string = False
        quote_type = None
        i = 0
        
        while i < len(line):
            char = line[i]
            # 1. String Protection
            if char in ('"', "'") and (i == 0 or line[i-1] != "\\"):
                if not in_string:
                    in_string = True
                    quote_type = char
                elif char == quote_type:
                    in_string = False
                    quote_type = None
                new_line_chars.append(char)
                i += 1
                continue
            if in_string:
                new_line_chars.append(char)
                i += 1
                continue
            # 2. Scientific Notation
            if char in ('+', '-') and i > 0 and line[i-1].lower() == 'e' and line[i-2].isdigit():
                new_line_chars.append(char)
                i += 1
                continue
            # 3. Negative Numbers
            if char == '-' and i + 1 < len(line) and line[i+1].isdigit():
                prev_text = "".join(new_line_chars).strip()
                if not prev_text or prev_text[-1] in ('=', '(', '[', '+', '-', '*', '/'):
                    new_line_chars.append(char)
                    i += 1
                    continue
            # 4. Symbol Spacing
            found_symbol = False
            for sym in SYMBOLS:
                if line.startswith(sym, i):
                    new_line_chars.append(f" {sym} ")
                    i += len(sym)
                    found_symbol = True
                    break
            if not found_symbol:
                new_line_chars.append(char)
                i += 1

        # 5. RIGOROUS INDENTATION CLEANUP
        temp_line = "".join(new_line_chars)
        stripped = temp_line.lstrip()
        
        if not stripped:
            continue

        # Calculate leading whitespace
        indent_size = len(temp_line) - len(stripped)
        
        # If indentation is less than 4 spaces, it's likely a 'Step 5' residue.
        # Python standard indentation is 4 spaces. We strip anything less than that.
        if 0 < indent_size < 4:
            final_line = stripped
        else:
            # Preserve valid indentation (0, 4, 8, etc.)
            indentation = temp_line[:indent_size]
            final_line = indentation + " ".join(stripped.split())
            
        final_lines.append(final_line)

    return "\n".join(final_lines)

def sea_func_to_python_func(code):
    """
    Translates SEA function definitions and calls into valid Python syntax.
    Handles nested calls (e.g., 'write len list') and protects variable assignments.
    """
    # 1. Python keywords to ignore (don't wrap these)
    RESERVED_KEYWORDS = {
        "if", "else", "elif", "for", "while", "try", "except", "finally", 
        "with", "class", "def", "return", "yield", "break", "continue", "pass"
    }

    # 2. Python built-ins to recognize for auto-parentheses
    builtin_funcs = [
        "abs", "all", "any", "ascii", "bin", "bool", "breakpoint", "bytearray", "bytes", 
        "callable", "chr", "classmethod", "compile", "complex", "delattr", "dict", 
        "dir", "divmod", "enumerate", "eval", "exec", "filter", "float", "format", 
        "frozenset", "getattr", "globals", "hasattr", "hash", "help", "hex", "id", 
        "input", "int", "isinstance", "issubclass", "iter", "len", "list", "locals", 
        "map", "max", "memoryview", "min", "next", "object", "oct", "open", "ord", 
        "pow", "print", "property", "range", "repr", "reversed", "round", "set", 
        "setattr", "slice", "sorted", "staticmethod", "str", "sum", "super", 
        "tuple", "type", "vars", "zip"
    ]

    # Protect Strings
    strings = []
    def save_str(match):
        strings.append(match.group(0))
        return f"__STR_HOLDER_{len(strings)-1}__"
    
    processing_code = re.sub(r'(".*?"|\'.*?\')', save_str, code)
    lines = processing_code.splitlines()
    new_code = []
    custom_defined_funcs = []

    # STEP 1: IDENTIFY CUSTOM DEFINITIONS (Scan for "func_name arg1 arg2:")
    for line in lines:
        stripped = line.strip()
        if stripped.endswith(":"):
            parts = stripped[:-1].split()
            if parts and parts[0] not in RESERVED_KEYWORDS:
                custom_defined_funcs.append(parts[0])

    all_funcs = builtin_funcs + custom_defined_funcs

    # STEP 2: PROCESS EACH LINE
    for line in lines:
        stripped = line.strip()
        if not stripped:
            new_code.append(line)
            continue
            
        indent = line[:line.find(stripped)]

        # A. Transform Definitions: 'square x:' -> 'def square(x):'
        if stripped.endswith(":"):
            parts = stripped[:-1].split()
            if parts and parts[0] in custom_defined_funcs:
                name = parts[0]
                params = ", ".join(parts[1:])
                new_code.append(f"{indent}def {name}({params}):")
                continue
            else:
                new_code.append(line)
                continue

        # B. Transform Calls: 'write len list' -> 'print(len(list))'
        current_line = line
        changes_made = True
        
        # Recursive Loop: Keep wrapping until no more changes can be made
        while changes_made:
            previous_state = current_line
            for func in all_funcs:
                # regex:
                # \b({func}) -> matches the function name
                # (?!\s*=)   -> ensures it's NOT a variable assignment (like 'list =')
                # \s+        -> matches the space before arguments
                # ([^#\n]+)  -> matches the arguments (aggressive match)
                pattern = rf'\b({func})(?!\s*=)\s+([^#\n]+)(?=\s|$|#)'
                
                # Wrap it! We use .strip() to clean up trailing spaces in arguments
                current_line = re.sub(pattern, lambda m: f"{m.group(1)}({m.group(2).strip()})", current_line)
            
            # If the string didn't change, we've wrapped everything
            if previous_state == current_line:
                # Cleanup: remove accidental double-spaces inside nested parentheses
                current_line = current_line.replace("( (", "((").replace(") )", "))")
                changes_made = False
        
        new_code.append(current_line)

    final_code = "\n".join(new_code)

    # RESTORE STRINGS
    for i, original_str in enumerate(strings):
        final_code = final_code.replace(f"__STR_HOLDER_{i}__", original_str)

    return final_code
def approches_loop(code):
    loop_pattern = r'\b(\w+)\s+approches\s+to\s+([\d\w\s,.-]+):'
    
    def convert_loop(match):
        var = match.group(1)
        args = match.group(2).replace(" ", "") # Clean up spaces in 1, 15, 2
        return f"for {var} in range({args}):"

    return re.sub(loop_pattern, convert_loop, code, flags=re.IGNORECASE)

def translate_sea_to_python(code): #
    return code
def add_f_to_strings(code):
    """
    Identifies Python strings and prefixes them with 'f'.
    Safely ignores comments and existing f-strings.
    """
    final_lines = []
    
    for line in code.splitlines():
        # 1. Separate code from comment to protect apostrophes in comments
        if '#' in line:
            # If the whole line is a comment, keep it as is
            if line.strip().startswith('#'):
                final_lines.append(line)
                continue
            
            # Split once at the first #
            code_part, comment_part = line.split('#', 1)
            comment_part = '#' + comment_part
        else:
            code_part = line
            comment_part = ""

        # 2. Add 'f' to strings in the code part only
        # Pattern: (?<!f) ensures we don't match if an 'f' is already there
        # (["'].*?["']) matches any string inside single or double quotes
        string_pattern = r'(?<!f)(["\'].*?["\'])'
        
        # Add the f-prefix
        processed_code = re.sub(string_pattern, r'f\1', code_part)

        # 3. Rejoin the line
        final_lines.append(processed_code + comment_part)

    return "\n".join(final_lines)

def run_python_code(code):
    exec(code) # Execute the generated Python code

if __name__ == "__main__":
    main()
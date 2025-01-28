
# Caesar Cipher Workshop README

## **Overview**
In this workshop, you’ll create a Caesar Cipher program that can encode and decode messages. You’ll work through the problem using **computational thinking** and **step-by-step problem-solving**.

Instead of copying full sections of code, you’ll piece together smaller parts based on logic snippets and templates provided. This will help you better understand Python and how to solve problems programmatically.

---

## **Goals**
1. Learn how to manipulate strings and lists in Python.
2. Write a Caesar Cipher function that encodes and decodes messages.
3. Handle edge cases, such as wrapping letters around the alphabet.
4. Build a user-friendly program that runs continuously until the user decides to stop.

---

## **Step-by-Step Instructions**
There are two routes
- Easy here
- Hard here

### **1. Setup the Program**
#### **Task**
1. Import any modules if needed.
2. Create a list of the alphabet that the cipher will use.

**Setup code**:
```python
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    # Create an empty string to hold the final result.
    output_text = ""

    # If the user wants to decode, reverse the shift amount.
    if encode_or_decode == "decode":
        shift_amount = __________  # Reverse the shift using multiplication.

    # Loop through each letter in the original text.
    for __________ in __________:
        # Check if the letter is in the alphabet.
        if __________:
            # Find the letter’s position in the alphabet.
            current_position = alphabet.__________(__________)

            # Calculate the new position by adding the shift amount.
            new_position = (current_position + shift_amount) % __________

            # Add the letter at the new position to the result.
            output_text += alphabet[__________]
        else:
            # Add non-alphabet characters (like spaces) unchanged.
            output_text += __________

    # Print the result for the user.
    print(f"Here is the {encode_or_decode}d result: {__________}")


should_continue = true


#While loop


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #CAll the function caesar
    
    #Restart
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    # conditional to check restart yes/no
    
        should_continue = False
        print("Goodbye")



```

---

### **2. Create the Caesar Cipher Function**
#### **Task**
Write a function called `caesar()` that can handle both encoding and decoding. The function will:
1. Take three inputs: the original text, the shift amount, and whether to "encode" or "decode."
2. Loop through each letter in the text.
3. If the letter is in the alphabet:
   - Find its current position in the alphabet.
   - Shift the position forward or backward, depending on the task.
   - Wrap around the alphabet if needed.
4. Add the shifted letter to the result.
5. If the character is not in the alphabet (e.g., space or punctuation), add it unchanged to the result.

**Pseudocode**:
```plaintext
Define a function caesar():
1. Create an empty string to store the result.
2. If the task is "decode," reverse the shift amount by multiplying it by -1.
3. Loop through each character in the original text:
   - If the character is in the alphabet:
     1. Find its position in the alphabet.
     2. Add the shift amount to the position.
     3. Wrap the position using modulo (so it stays within the alphabet).
     4. Find the letter at the new position and add it to the result.
   - If the character is not in the alphabet:
     1. Add the character to the result unchanged.
4. Print the result.
```

#### **Template**
```python
def caesar(original_text, shift_amount, encode_or_decode):
    # Step 1: Create an empty string to store the result.

    # Step 2: Reverse the shift amount if the task is "decode."

    # Step 3: Loop through each character in the text.
        # If the character is in the alphabet:
            # Step 3.1: Find the current position.
            # Step 3.2: Add the shift amount.
            # Step 3.3: Wrap around using modulo.
            # Step 3.4: Add the shifted letter to the result.
        # Else, add the character unchanged.

    # Step 4: Print the result.
```

**Logic Snippet**:
- Find a letter’s position in the alphabet:
  ```python
  alphabet.index(letter)
  ```
- Wrap around the alphabet using modulo:
  ```python
  new_position = (current_position + shift_amount) % len(alphabet)
  ```

---

### **3. Add User Input**
#### **Task**
Prompt the user to:
1. Choose whether to "encode" or "decode."
2. Input the message they want to process.
3. Provide the shift amount.

**Pseudocode**:
```plaintext
1. Ask the user if they want to encode or decode.
2. Ask the user to input their message.
3. Ask the user for the shift amount.
```

**Logic Snippet**:
- Convert the user’s input to lowercase: `.lower()`.
- Ensure the shift amount is an integer: `int()`.

---

### **4. Call the Function**
#### **Task**
Pass the user inputs into the `caesar()` function to process the message.

**Pseudocode**:
```plaintext
1. Call the caesar() function.
2. Pass the user's message, shift amount, and task ("encode" or "decode") as arguments.
```

**Logic Snippet**:
```python
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
```

---

### **5. Make the Program Continuous**
#### **Task**
Wrap the program in a loop so it keeps running until the user decides to stop.

**Pseudocode**:
```plaintext
1. Create a variable to control the loop (e.g., `should_continue = True`).
2. While the loop is running:
   - Ask the user for inputs (direction, message, shift).
   - Call the caesar() function to process the message.
   - Ask if the user wants to go again.
   - If not, break the loop and print a goodbye message.
```

#### **Template**:
```python
should_continue = True

while should_continue:
    # Step 1: Get user inputs for direction, message, and shift amount.
    # Step 2: Call the caesar() function with these inputs.
    # Step 3: Ask if the user wants to restart.
    # Step 4: If the user says "no," exit the loop and print "Goodbye."
```

---

### **6. Test Edge Cases**
#### **Task**
Test your program with the following:
1. A basic message: Shift "hello" by 5.
2. A message with spaces and punctuation: Shift "hello, world!" by 3.
3. A large shift amount: Shift "abc" by 50.
4. Decoding: Decode a previously encoded message.

**Pseudocode for Wrapping Around**:
```plaintext
1. Find the current position of the letter.
2. Add the shift amount to the position.
3. Use modulo to ensure the position wraps around the alphabet.
4. Find the letter at the new position.
```

**Logic Snippet**:
```python
new_position = (current_position + shift_amount) % len(alphabet)
```

---

## **Final Steps**
By now, your program should:
1. Allow the user to encode or decode a message.
2. Handle non-alphabetic characters like spaces and punctuation.
3. Use modular arithmetic to wrap letters around the alphabet.
4. Run continuously until the user chooses to exit.

---

### **Extensions**
If you finish early, try these challenges:
1. **Custom Alphabet**: Add uppercase letters or special symbols to your alphabet.
2. **Large Shifts**: Allow users to input very large shift amounts and handle them efficiently.
3. **Cipher Cracking**: Write a function to guess the shift amount for an encoded message.

---

## **Conclusion**
In this workshop, you’ve:
- Learned how to manipulate strings and lists in Python.
- Written a function to encode and decode messages using a Caesar Cipher.
- Used computational thinking to break down and solve problems.
- Built a program that is interactive and user-friendly.

Great work! 🎉 Keep experimenting and building on this program to improve your skills.

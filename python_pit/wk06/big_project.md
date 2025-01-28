
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
- [Easy](#easy) here
- [Hard](#hard) here

## Easy
---

## **Step-by-Step Instructions**

### **1. Setup the Program**
#### **Task**
Start by setting up the basic program:
1. Create a list of all the lowercase letters in the alphabet.
2. Prompt the user to provide:
   - Whether they want to encode or decode a message.
   - The message they want to process.
   - The shift amount.

**Pseudocode**:
```plaintext
1. Create an alphabet list containing 'a' to 'z'.
2. Ask the user if they want to encode or decode.
3. Ask the user for their message.
4. Ask the user for the shift amount.
```

---

### **2. Create the `encrypt()` Function**
#### **TODO-1: Define the Function**
Write a function called `encrypt()` that takes two inputs:
1. `original_text`: The message to encode.
2. `shift_amount`: The number of positions to shift each letter.

**Pseudocode**:
```plaintext
Define a function encrypt(original_text, shift_amount):
1. Create an empty string to hold the encoded result.
2. Loop through each letter in the original_text:
   - If the letter is in the alphabet:
     1. Find its current position in the alphabet.
     2. Add the shift_amount to the position.
     3. Handle wrapping around the alphabet.
     4. Find the new letter and add it to the result.
   - If the character is not in the alphabet, add it unchanged to the result.
3. Print the final encoded result.
```

#### **Logic Snippet**
To find and shift a letter:
- Use the `.index()` method to get the position of a letter in the alphabet list:
  ```python
  position = alphabet.index(letter)
  ```
- Add the shift amount and wrap around using modulo:
  ```python
  new_position = (position + shift_amount) % len(alphabet)
  ```

---

### **3. Test the `encrypt()` Function**
#### **TODO-2: Shift Letters**
1. Loop through each letter in the user’s message.
2. Use the logic snippets provided to:
   - Find the position of the letter in the alphabet.
   - Shift the letter by the user-provided shift amount.
   - Wrap around if necessary.
3. Build the encoded message letter by letter.
4. Print the final result.

**Example**:
Input:
```plaintext
plain_text = "hello"
shift_amount = 1
```
Output:
```plaintext
Here is the encoded result: ifmmp
```

---

### **4. Handle Edge Cases**
#### **TODO-3: Fix the Wrapping Around**
When shifting the letter 'z' by a positive shift amount, the position will go beyond the alphabet. To fix this:
1. Use modulo to ensure the position wraps around.
2. Test the program with larger shift amounts (e.g., shifting "z" by 9).

**Hint**: Modulo (`%`) helps keep numbers within a specific range.

**Pseudocode**:
```plaintext
1. Calculate the new position as (current_position + shift_amount) % len(alphabet).
2. Use the new position to find the correct letter.
```

---

### **5. Call the Function**
#### **TODO-4: Use User Inputs**
Once the `encrypt()` function is complete, call it using the inputs collected earlier:
1. Pass the user’s message and shift amount to the function.
2. Test the function with different inputs.

**Pseudocode**:
```plaintext
1. Get user inputs for direction, message, and shift.
2. Call encrypt() with the user inputs.
```

**Example Snippet**:
```python
encrypt(original_text=text, shift_amount=shift)
```

---

### **6. Test Your Program**
Test your program with different scenarios:
1. Basic encoding: Shift "hello" by 5.
2. Wrap-around case: Shift "zoo" by 3.
3. Special characters: Test with spaces and punctuation (e.g., "hello, world!").

---

## **Hints for Success**
1. **Break the Problem into Steps**:
   - Loop through the message.
   - Find each letter’s position.
   - Shift the position and wrap around if necessary.
2. **Handle Non-Alphabet Characters**:
   - Check if the character is in the alphabet before shifting.
3. **Test with Edge Cases**:
   - Large shifts (e.g., shift = 50).
   - Messages with special characters and spaces.

---

## **Extensions**
1. Add a `decrypt()` function to reverse the process.
2. Allow the program to handle uppercase letters.
3. Test with longer messages or custom alphabets.

---



## Hard
Copy the code templete then follow the steps described below. This is a hard challange. Take your time, break the problem down into manageable chuncks. Test code in a seperate file if that helps!!
GOODLUCK
### **1. Setup the Program**

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

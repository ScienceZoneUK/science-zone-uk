Getting started
---
There is lots of info online
[Click-Here](https://microbit.org/get-started/what-is-the-microbit/)

---

Open MU editor or download it [here](https://codewith.mu/)

![Mu](https://github.com/ScienceZoneUK/science-zone-uk/blob/main/Microbits/lv2/mu_editor.png)

## Microbit Documentation

vvv If you want to know how to use the microbit python library look here vvv

[Code Docs here](https://microbit-micropython.readthedocs.io/en/v2-docs/index.html)

---

### 🌟 1. Starter - Scroll a Message

This is your very first Micro\:bit program! You're using a built-in function called `display.scroll()` to scroll text across the LED screen. It's a great way to check if your Micro\:bit is working and to try your first bit of Python.     
**Pseudocode:**

```
Import the microbit tools
Scroll the message "Hello!" across the screen
```

Copy into the editor and flash your microbit.    

Troubleshooting if flash fails:       
- Close the repl to enable flash button
- If flash hangs up, disconnect/reconnect cable and flash again
- Press reset button on back of microbit resets the code

```python
from microbit import *

display.scroll("Hello!")
```

![Mu](https://github.com/ScienceZoneUK/science-zone-uk/blob/main/Microbits/lv2/mu_editor_flash.png)


---

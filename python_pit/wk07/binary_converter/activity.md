```blocks
let binary = ""
let decimal = 0
input.onButtonPressed(Button.A, () => {
    binary = binary + "1"
    basic.showString(binary)
    decimal = decimal * 2 + 1
})
input.onButtonPressed(Button.B, () => {
    binary = binary + "0"
    basic.showString(binary)
    decimal = decimal * 2
})
input.onButtonPressed(Button.AB, () => {
    basic.showNumber(decimal)
})
decimal = 0
binary = ""
```

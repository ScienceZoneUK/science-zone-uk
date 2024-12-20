# Making a 32x32 grid


### Step 1
Create your loop variables, we need to make a grid of boxes
```javascript
let row = 32
let col = 32
let box = 5
```

### Step 2
Now we need to make a loop to iterate through the grid
```javascript
  for(let i = 0; i < row; i ++){
    for(let j = 0; j < col; j ++) {
      
    }
  }
```
This is the standard loop for 2D

We now need to add a 2d primative, can you work out how to implement it using our variables?
```javascript
square(x,y,size)
```

```javascript
  for(let i = 0; i < row; i ++){
    for(let j = 0; j < col; j ++) {
      square(x,y,size)
    }
  }
```

### Step 3
Fixing the box size isnt the best idea, we want our grid to be scalebale dont we?!
In setup calculate the box size so the grid is dynamic. We can use the p5 built in functions to find out the canvas size ```width``` or ```height```

```javascript
  box = width/32
```

### Step 4
You should now see a grid of white





### Final code

```javascript
// https://coolors.co/54428e-0cce6b-1f2041-ff66d8-ed7d3a
// Generate ai colours

let row = 32;
let col = 32;
let box = 0;

function setup() {
  createCanvas(600, 600);
  background(220);
}

function draw() {
  grid32x32()
  
}



function grid32x32() {
  box = width / 32;

  let color1 = color(255, 102, 216);
  let color2 = color(237, 125, 58);
  let color3 = color(12, 206, 107);
  colorArr = [color1, color2, color3];

  
  if(frameCount % 10 == 0){
       for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      noStroke();
      fill(random(colorArr));
      square(i * box, j * box, box);
    }
  }
     }

}

```

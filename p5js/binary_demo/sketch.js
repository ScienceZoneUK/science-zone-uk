function setup() {
  createCanvas(400, 200);
  noLoop();
}

function draw() {
  background(255);

  // Binary color example (R: 202, G: 170, B: 240)
  let binaryColor = "11001010 10101010 11110000";
  let rgbFromBinary = binaryToRGB(binaryColor);
  
  // Hex color example (#CAAAF0)
  let hexColor = "#CAAAF0";
  let rgbFromHex = hexToRGB(hexColor);

  // Draw circles with the respective colors
  fill(rgbFromBinary.r, rgbFromBinary.g, rgbFromBinary.b);
  ellipse(width / 3, height / 2, 100);

  fill(rgbFromHex.r, rgbFromHex.g, rgbFromHex.b);
  ellipse(2 * width / 3, height / 2, 100);
  
  // Display text for reference
  fill(0);
  textAlign(CENTER, CENTER);
  text("Binary: " + binaryColor, width / 3, height - 20);
  text("Hex: " + hexColor, 2 * width / 3, height - 20);
}

// Convert binary color to RGB
function binaryToRGB(binaryStr) {
  let binaryValues = binaryStr.split(" ");
  return {
    r: parseInt(binaryValues[0], 2),
    g: parseInt(binaryValues[1], 2),
    b: parseInt(binaryValues[2], 2)
  };
}

// Convert hex color to RGB
function hexToRGB(hex) {
  return {
    r: parseInt(hex.substring(1, 3), 16),
    g: parseInt(hex.substring(3, 5), 16),
    b: parseInt(hex.substring(5, 7), 16)
  };
}

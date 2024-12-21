import processing.sound.*;

// Declare the microphone input and Waveform analyzer variables
AudioIn input;
Waveform waveform;
Amplitude amp;

// Define how many samples of the Waveform you want to be able to read at once
int samples = 100;

// Variables for tracking interesting frames
PImage savedFrame;
boolean displayInteresting = false;
int displayTimer = 0;
int displayDuration = 120;  // Duration to display the frame (2 seconds at 60 FPS)
float fadeAlpha = 255;      // Alpha for fade-out effect

// Thresholds and conditions for "interesting" frames
float amplitudeThreshold = 0.1;
float lastAmplitude = 0;

void setup() {
  size(800, 800);
  background(0);

  // Initialize the microphone input
  input = new AudioIn(this, 0); // '0' specifies the default input, usually the internal mic
  input.start();

  // Create an Input stream routed into the Amplitude analyzer
  amp = new Amplitude(this);
  amp.input(input);

  // Create the Waveform analyzer and connect it to the microphone input
  waveform = new Waveform(this, samples);
  waveform.input(input);
}

void draw() {
  noStroke();
  fill(0, 10); // Semi-transparent background for trailing effect
  rect(0, 0, width, height);
  stroke(255);
  strokeWeight(2);
  noFill();

  // Perform the analysis
  waveform.analyze();
  float currentAmplitude = amp.analyze();

  //if (isInterestingFrame(currentAmplitude)) {
  //  // Save the current frame and start the display timer
  //  savedFrame = get();
  //  displayInteresting = true;
  //  displayTimer = displayDuration;
  //  fadeAlpha = 255;  // Reset alpha to fully opaque
  //}

  // Draw circular waveform with curves
  if (frameCount % 2 == 0) {
    translate(random(width), random(height));  // Center the circular waveform
  } else {
    translate(width / 2, height / 2);  // Center the circular waveform
  }

 // translate(width / 2, height / 2);  // Center the circular waveform
  float radius = map(currentAmplitude, 0, 1, 0, 500);  // Radius of the circular waveform
  beginShape();
  for (int i = 0; i < samples; i++) {
    // Calculate the position of each sample point
    float angle = map(i, 0, samples, 0, TWO_PI);
    float nextAngle = map(i + 1, 0, samples, 0, TWO_PI);
    float x = cos(angle) * (radius + waveform.data[i] * 100);
    float y = sin(angle) * (radius + waveform.data[i] * 100);

    // Calculate control points for wavy curves
    float ctrlX1 = cos(angle + 0.05) * (radius + waveform.data[i] * 80);
    float ctrlY1 = sin(angle + 0.05) * (radius + waveform.data[i] * 80);
    float ctrlX2 = cos(nextAngle - 0.05) * (radius + waveform.data[(i + 1) % samples] * 80);
    float ctrlY2 = sin(nextAngle - 0.05) * (radius + waveform.data[(i + 1) % samples] * 80);

    // Draw curve to the next point with control points for smoothness
    if (i == 0) {
      vertex(x, y); // Start from the first point
    } else {
      bezierVertex(ctrlX1, ctrlY1, ctrlX2, ctrlY2, x, y);
    }
  }
  endShape(CLOSE);

  // Show saved frame if within the display time, applying fade-out
  if (displayInteresting) {
    tint(255, fadeAlpha);  // Set fade alpha
    image(savedFrame, -width / 2, -height / 2);  // Draw saved frame centered
    // Decrease timer and adjust fade
    displayTimer--;
    fadeAlpha -= 255.0 / displayDuration;  // Linear fade-out over display duration

    // Stop showing when timer reaches zero
    if (displayTimer <= 0) {
      displayInteresting = false;
    }
  }

  // Update last amplitude for comparison
  lastAmplitude = currentAmplitude;
}

boolean isInterestingFrame(float currentAmplitude) {
  // Check if the amplitude surpasses the threshold and has a significant difference from the last frame
  return currentAmplitude > amplitudeThreshold && abs(currentAmplitude - lastAmplitude) > 0.05;
}

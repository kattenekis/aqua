

// Include the Neopixel library
#include <Adafruit_NeoPixel.h>

// Declare and initialise global GPIO pin constant for Neopixel ring
const byte neoPin = 6;

// Declare and initialise global constant for number of pixels
const byte neoPixels = 8;

// Declare and initialise variable for Neopixel brightness
byte neoBright = 255;

// Create new Neopixel strip object
Adafruit_NeoPixel strip = Adafruit_NeoPixel(neoPixels, neoPin, NEO_GRB);

int cols[] = { 0, 25, 50, 100, 200, 100, 50, 25,0,0};
int i = 0;
int j =0;

void setup() {
  Serial.begin(9600);
  // Initialise the ring
  strip.begin();
  strip.setBrightness(neoBright);
  strip.show();

}

void loop() {
  // colorrun(); //for nice running demo-colours

  /*if (j > 6) {
    j = j + 1;
  }
  else
  {
    j = j+1;
  }*/

  j = j+1;
  if (j>10) {
    j = 0;
  }

  Serial.println(j);
  fixcol(cols[j]);
  delay(500);

}

void fixcol(int col) {
  for (int i = 0; i < neoPixels; i++) {
    strip.setPixelColor(i, strip.Color(0, 0, col));
    strip.show();
  }
}

void colorrun() {
  // Turn on pixels

  for (int i = 0; i < neoPixels; i++) {
    strip.setPixelColor(i, strip.Color(0, 0, 255));
    strip.show();
    delay(42);
  }
  // Turn off pixels

  for (int i = 0; i < neoPixels; i++) {
    strip.setPixelColor(i, strip.Color(0, 0, 0));
    strip.show();
    delay(42);
  }
}

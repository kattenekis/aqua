

// Include the Neopixel library
#include <Adafruit_NeoPixel.h>
#include <RtcDS3231.h>
#include "U8glib.h"
#include <Wire.h>


// create buttons
const int s1_pin = 2;     // the number of the pushbutton pin
const int s2_pin = 4;     // the number of the pushbutton pin

int s1_State = 0;   // holder of s1 button value
int s2_State = 0;   // holder of s1 button value
int fixLightState = 0; // HIGH to make the Neopixel be fixed value
float fixLightOnTime = 0;

// Create new SSD1306 I2C display with 128x64 resolution
U8GLIB_SSD1306_128X64 oled(U8G_I2C_OPT_NONE);  // I2C / TWI

// Create new RTC module
RtcDS3231<TwoWire> rtcModule(Wire);

// Create variables for time
byte hours;
byte minutes;
byte seconds;
float timeH = 0;

// Declare and initialise global GPIO pin constant for Neopixel stick
const byte neoPin = 6;

// Declare and initialise global constant for number of pixels
const byte neoPixels = 8;

// Declare and initialise variable for Neopixel brightness
byte neoBright = 255;

// Create new Neopixel strip object
Adafruit_NeoPixel strip = Adafruit_NeoPixel(neoPixels, neoPin, NEO_GRB);

// Neopixels have 0-255 resolution on value
int red[]   =       {0, 0,   2,  8,  8,  200,  200,   120   ,   40,   2,    1,   0,    0};
int green[] =       {0, 0,   0,  0,   0,   100,  100,    50,     0,     0,    0,   0,    0};
int blue[]  =       {0, 0,   5, 20,  30,  255,  255,   255,  100,  10,   2,  0,    0};

float col_time[]  = {0, 5.9, 6,  7.3, 9.0, 11,   13,     20,   20.8,  21.5, 22,  23.5, 24, 25}; // fake end time of the day to fit algorithm
int length_time_array = 13;

int i = 0;
float actualtime = 0.0; // j is aktually used as debug time...
float timestep = 0.1;  //timestep
int j = 2;

int r_now = 0;
int g_now = 0;
int b_now = 0;


int loopdelay = 20; // delay in the main loop, value in ms

void setup() {

  // initialize the pushbutton pin as an input:
  pinMode(s1_pin, INPUT);
  pinMode(s2_pin, INPUT);

  Serial.begin(115200);
  Serial.println("Program start");
  // Initialise the Neopixel
  strip.begin();
  strip.setBrightness(neoBright);
  strip.show();

}

void loop() {

  updateTime();

  // Read buttons
  s1_State = digitalRead(s1_pin);
  s2_State = digitalRead(s2_pin);

  // Button s1 pushed, accelerate the time!
  if (s1_State == HIGH) {
    // Serial.print("Normal time. ");
    timeH = (float)hours + (float)minutes / 60 + (float)seconds / 3600;
  } else {
    Serial.print("Hypertime! ");
    timeH = timeH + timestep;
    // replace time values to display accelerated time...
    hours = int(timeH);
    minutes = int((timeH - hours) * 60);
    seconds = 0;
  }

  // Button s2 pushed, set Pixels to fixed value
  // a certain time, i.e. white daylight
  if (s2_State == LOW) {
    Serial.print("Fixed lights. ");
    fixLightState = HIGH;
  }  else {
    fixLightState = LOW;
  }


  if (timeH >= 24.0) {
    timeH = 0.0;
  }

  actualtime = timeH;

  Serial.print("Current time, h: "); Serial.print(timeH);
  oled.firstPage();
  do {
    draw();
  } while (oled.nextPage());

  // Calculation of where in the array the colours can be found for the current time
  for (int t_index = 0; t_index < length_time_array; t_index++) {

    if (col_time[t_index] >= actualtime) {
      j = t_index - 1;
      break;
    }
  }


  // Set colours directly from the time
  /* No removed as linear approximation is used
    r_now = red[j];
    g_now = green[j];
    b_now = blue[j]; */

  // add linear approximation
  r_now = linapprox(actualtime, col_time[j], col_time[j + 1], red[j],   red[j + 1]) ;
  g_now = linapprox(actualtime, col_time[j], col_time[j + 1], green[j], green[j + 1]) ;
  b_now = linapprox(actualtime, col_time[j], col_time[j + 1], blue[j],  blue[j + 1]) ;

  Serial.print(" - RGB ");   Serial.print(r_now); Serial.print(":");   Serial.print(g_now); Serial.print(":");   Serial.println(b_now); // Serial.println("");

  if (fixLightState == HIGH) {
    r_now = 255;
    g_now = 130;
    b_now = 255;
  }

  showcolour(r_now, g_now, b_now);

  delay(loopdelay);
}


/* =================================
   Various functions declared below!
   =================================
*/


void updateTime() {
  RtcDateTime now = rtcModule.GetDateTime();
  hours = now.Hour();
  minutes = now.Minute();
  seconds = now.Second();
}

void draw(void) {
  // Set font to Helvetica size 24
  oled.setFont(u8g_font_helvB24);
  // Format and print time on display
  char timeString[10];
  sprintf(timeString, "%02u:%02u:%02u", hours, minutes, seconds);
  oled.setPrintPos(0, 45);
  oled.print(timeString);
}




int linapprox(float x, float x_start, float x_end, int y_start, int y_end) {
  /* Linear Approximantion from a look-up table:
      input are x, a floating value
                y, integer
      output is a trunkated integer.

  */

  float returnval = 0.0; // Defaults to Zero as output
  float k = 0.0;
  float m = 0.0;


  // solves the equation y = kx + m  and returns the actual value for x"""
  k = (float(y_end) - float(y_start)) / (x_end - x_start);
  m = (float(y_start)) - k * x_start;
  returnval = k * x + m;

  if (returnval < 0 ) {
    returnval = 0;
  }

  return returnval ;
}

void showcolour(int r_led, int g_led, int b_led ) {
  for (int i = 0; i < neoPixels; i++) {
    /*
      Serial.println("value to strip: ");
      Serial.print(r_led); Serial.print(":");
      Serial.print(g_led); Serial.print(":");
      Serial.println(b_led); Serial.println("========");
    */
    strip.setPixelColor(i, strip.Color(r_led, g_led, b_led));
    //strip.show();
  }
  strip.show();
}

#include <Arduino.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define LED_RED    18
#define LED_GREEN  19
#define Button_Pin 4
volatile bool btn_pressed = false;
void buttonTask(void *pvParameters)
{
    while (true)
    {
        btn_pressed = (digitalRead(Button_Pin) == LOW);

        vTaskDelay(pdMS_TO_TICKS(20));
    }
}
void redLedTask(void *pvParameters)
{
    while (true)
    {
        digitalWrite(LED_RED, HIGH);
        vTaskDelay(pdMS_TO_TICKS(500));

        digitalWrite(LED_RED, LOW);
        vTaskDelay(pdMS_TO_TICKS(500));
    }
}

void greenLedTask(void *pvParameters)
{
    while (true)
      {if(btn_pressed)
          {
            digitalWrite(LED_GREEN, HIGH);
            vTaskDelay(pdMS_TO_TICKS(200));
            digitalWrite(LED_GREEN, LOW);
            vTaskDelay(pdMS_TO_TICKS(500));
          }
        else
          {
            digitalWrite(LED_GREEN, HIGH);
            vTaskDelay(pdMS_TO_TICKS(1000));
            digitalWrite(LED_GREEN, LOW);
            vTaskDelay(pdMS_TO_TICKS(500));
          }
      
            
      }
}

void setup()
{
    pinMode(LED_RED, OUTPUT);
    pinMode(LED_GREEN, OUTPUT);
    pinMode(Button_Pin, INPUT_PULLUP);
    xTaskCreate( redLedTask, "Red Task", 1024,NULL,1,0);
    xTaskCreate(greenLedTask,"Green Task",1024,NULL,1,0);
    xTaskCreate(buttonTask, "Button Task", 1024, NULL, 1, NULL);
}

void loop()
{
}
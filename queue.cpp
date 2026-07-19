#include <Arduino.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/queue.h"

#define RED_LED     18
#define BUTTON_PIN  4

// Handle của Queue
QueueHandle_t buttonQueue;

//==================================================
// Button Task
//==================================================
void buttonTask(void *pvParameters)
{
    bool lastButtonState = HIGH;

    while (1)
    {
        bool currentButtonState = digitalRead(BUTTON_PIN);

        // Phát hiện cạnh nhấn
        if (lastButtonState == HIGH &&
            currentButtonState == LOW)
        {
            int message = 1;

            xQueueSend(
                buttonQueue,     // Queue cần gửi
                &message,        // Dữ liệu gửi
                portMAX_DELAY    // Chờ vô hạn nếu Queue đầy
            );
        }

        lastButtonState = currentButtonState;

        vTaskDelay(pdMS_TO_TICKS(20));
    }
}

//==================================================
// LED Task
//==================================================
void ledTask(void *pvParameters)
{
    int receivedData;

    while (1)
    {
        xQueueReceive(
            buttonQueue,      // Queue cần đọc
            &receivedData,    // Biến nhận dữ liệu
            portMAX_DELAY     // Chờ vô hạn nếu Queue rỗng
        );

        digitalWrite(
            RED_LED,
            !digitalRead(RED_LED)
        );
    }
}

//==================================================
// Setup
//==================================================
void setup()
{
    pinMode(RED_LED, OUTPUT);
    pinMode(BUTTON_PIN, INPUT_PULLUP);

    //------------------------------------------------
    // Tạo Queue
    //------------------------------------------------
    buttonQueue = xQueueCreate(
        5,              // Queue chứa tối đa 5 phần tử
        sizeof(int)     // Mỗi phần tử là int
    );

    //------------------------------------------------
    // Tạo Task
    //------------------------------------------------
    xTaskCreate(
        buttonTask,
        "Button Task",
        1024,
        NULL,
        1,
        NULL
    );

    xTaskCreate(
        ledTask,
        "LED Task",
        1024,
        NULL,
        1,
        NULL
    );
}

void loop()
{
}
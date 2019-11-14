#include "o3.h"
#include "gpio.h"
#include "systick.h"

#define STATE_SEC 0
#define STATE_MIN 1
#define STATE_HOUR 2
#define STATE_COUNT 3
#define STATE_ALARM 4

#define LED_PIN 2
#define LED_PORT GPIO_PORT_E
#define PB0_PIN 9
#define PB0_PORT GPIO_PORT_B
#define PB1_PIN 10
#define PB1_PORT GPIO_PORT_B

struct time_t {int h, m, s;};
int h, m, s;

struct gpio_port_t {
	word CTRL;
	word MODEL;
	word MODEH;
	word DOUT;
	word DOUTSET;
	word DOUTCLR;
	word DOUTTGL;
	word DOUTIN;
	word PINLOCKN;
};

volatile struct gpio_t {
	struct gpio_port_t port[6];
	word unused[10];
	word EXTIPSELL;
	word EXTIPSELH;
	word EXTIRISE;
	word EXTIFALL;
	word IEN;
	word IF;
	word IFS;
	word IFC;
	word ROUTE;
	word INSENSE;
	word LOCK;
	word CTRL;
	word CMD;
	word EM4WUEN;
	word EM4WUPOL;
	word EM4WUCAUSE;
} *GPIO = (struct gpio_t*) GPIO_BASE;

volatile struct systick_t {
	word CTRL;
	word LOAD;
	word VAL;
	word CALIB;
} *SYSTICK = (struct systick_t*) SYSTICK_BASE;

static int state = STATE_SEC;
static struct time_t time = {0};
static char str[8] = "0000000\0";

void int_to_string(char *timestamp, unsigned int offset, int i) {
    if (i > 99) {
			timestamp[offset]   = '9';
			timestamp[offset+1] = '9';
			return;
    }

    while (i > 0) {
	    if (i >= 10) {
		    i -= 10;
		    timestamp[offset]++;
	    } else {
		    timestamp[offset+1] = '0' + i;
		    i = 0;
	    }
    }
}

void time_to_string(char *timestamp, int h, int m, int s) {
	timestamp[0] = '0';
	timestamp[1] = '0';
	timestamp[2] = '0';
	timestamp[3] = '0';
	timestamp[4] = '0';
	timestamp[5] = '0';
	timestamp[6] = '\0';

	int_to_string(timestamp, 0, h);
	int_to_string(timestamp, 2, m);
	int_to_string(timestamp, 4, s);
}

void set_led(int on) {
    if(on == 1)
        GPIO->port[LED_PORT].DOUTSET = 0b0100;
    else
        GPIO->port[LED_PORT].DOUTCLR = 0b0100;
}

void set_4bit_flag(volatile word* w, int i, word flag) {
	*w &= ~(0b1111 << (i * 4));
	*w |= flag << (i*4);
}

void init_io() {
	set_4bit_flag(&GPIO->port[LED_PORT].MODEL, LED_PIN, GPIO_MODE_OUTPUT); // 
	set_4bit_flag(&GPIO->port[PB0_PORT].MODEH, PB0_PIN - 8, GPIO_MODE_INPUT);
	set_4bit_flag(&GPIO->port[PB1_PORT].MODEH, PB1_PIN - 8, GPIO_MODE_INPUT);
	set_4bit_flag(&GPIO->EXTIPSELH, PB0_PIN-8, 0b0001);
	set_4bit_flag(&GPIO->EXTIPSELH, PB1_PIN-8, 0b0001);

	GPIO->EXTIFALL |= 1 << PB0_PIN; // 
	GPIO->EXTIFALL |= 1 << PB1_PIN;
	GPIO->IEN |= 1 << PB0_PIN; // 
	GPIO->IEN |= 1 << PB1_PIN; // 
	SYSTICK->LOAD = FREQUENCY; // 
	SYSTICK->CTRL = SysTick_CTRL_CLKSOURCE_Msk | SysTick_CTRL_TICKINT_Msk;
}

void clock_start() {
	SYSTICK->VAL = SYSTICK->LOAD;
	SYSTICK->CTRL |= SysTick_CTRL_ENABLE_Msk;
}

void clock_stop() {
	SYSTICK->CTRL &= ~(SysTick_CTRL_ENABLE_Msk);
}

void increase_hour() {
	++h;
    ++time.h;
}

void increase_min() {
	++time.m;
    ++m;
	if (time.m >= 60) {
		time.m = 0;
        m = 0;
		increase_hour();
	}
}

void increase_sec() {
	++time.s;
    ++s;
	if (time.s >= 60) {
		time.s = 0;
        s = 0;
		increase_min();
	}
}

void update_display_time() {
	time_to_string(str, time.h, time.m, time.s);
	lcd_write(str);
}

// For putting button of PB0
void GPIO_ODD_IRQHandler() {
	switch (state) {
		case STATE_SEC: {
			increase_sec();
			update_display_time();
		} break;
		case STATE_MIN: {
			increase_min();
			update_display_time();
		} break;
		case STATE_HOUR: {
			increase_hour();
			update_display_time();
		} break;
		case STATE_COUNT: break;
		case STATE_ALARM: break;
			GPIO->port[LED_PORT].DOUTSET = 1 << LED_PIN;
	}
	GPIO->IFC = 1 << PB0_PIN;
}

// For putting putton on PB1
void GPIO_EVEN_IRQHandler() {
	switch (state) {
		case STATE_SEC: {
			state = STATE_MIN;
		} break;
		case STATE_MIN: {
			state = STATE_HOUR;
		} break;
		case STATE_HOUR: {
			state = STATE_COUNT;
			clock_start();
		} break;

		case STATE_COUNT: {
            break;
        }
		case STATE_ALARM: {
			state = STATE_SEC;
			GPIO->port[LED_PORT].DOUTCLR = 1 << LED_PIN;
		} break;
	}

	GPIO->IFC = 1 << PB1_PIN;
}

void SysTick_Handler() {
	if (state == STATE_COUNT) {
		if (time.s <= 0) {
			if (time.m <= 0) {
				if (time.h <= 0) {
					state = STATE_ALARM;
					clock_stop();
					GPIO->port[LED_PORT].DOUTSET = 1 << LED_PIN;
					update_display_time();
					return;
				}
				--time.h;
				time.m = 61;
			}
			--time.m;
			time.s = 61;
		}
		time.s--; // --time.s 와 time.s-- 는 뭐가 다른가?
		update_display_time();
	}
}

int main() {
	init();
	init_io();
	update_display_time();
	while (true);
	return 0;
}
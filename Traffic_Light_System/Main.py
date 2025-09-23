from machine import Pin
from time import sleep

class TrafficLightSystem:
    def __init__(self):
        """Initialize all components"""
        # Traffic Light LEDs
        self.red = Pin(0, Pin.OUT)
        self.yellow = Pin(1, Pin.OUT)
        self.green = Pin(2, Pin.OUT)
        
        # 7-Segment Display Pins
        self.segments = [
            Pin(3, Pin.OUT),  # Segment A
            Pin(4, Pin.OUT),  # Segment B
            Pin(5, Pin.OUT),  # Segment C
            Pin(6, Pin.OUT),  # Segment D
            Pin(7, Pin.OUT),  # Segment E
            Pin(8, Pin.OUT),  # Segment F
            Pin(9, Pin.OUT)   # Segment G
        ]
        
        # 7-Segment Display Patterns (Common Cathode)
        self.digits = {
            0: [1,1,1,1,1,1,0],  # ABCDEFG
            1: [0,1,1,0,0,0,0],
            2: [1,1,0,1,1,0,1],
            3: [1,1,1,1,0,0,1],
            4: [0,1,1,0,0,1,1],
            5: [1,0,1,1,0,1,1],
            6: [1,0,1,1,1,1,1],
            7: [1,1,1,0,0,0,0],
            8: [1,1,1,1,1,1,1],
            9: [1,1,1,1,0,1,1]
        }
        
        # Timing configuration (seconds)
        self.timing = {
            'red': 5,
            'green': 5,
            'yellow': 3
        }
    
    def display_number(self, number):
        """Display number on 7-segment display"""
        if 0 <= number <= 9:
            pattern = self.digits[number]
            for i in range(7):
                self.segments[i].value(pattern[i])
        else:
            # Turn off display for invalid numbers
            for segment in self.segments:
                segment.value(0)
    
    def set_lights(self, red_state, yellow_state, green_state):
        """Control traffic light states"""
        self.red.value(red_state)
        self.yellow.value(yellow_state)
        self.green.value(green_state)
    
    def countdown(self, seconds, phase_name):
        """Execute countdown for specified phase"""
        print(f"{phase_name} phase: {seconds} seconds")
        
        for sec in range(seconds, 0, -1):
            self.display_number(sec)
            sleep(1)
        
        self.display_number(0)  # Clear display
    
    def red_phase(self):
        """Red light phase"""
        self.set_lights(1, 0, 0)  # Red ON, others OFF
        self.countdown(self.timing['red'], "RED")
        self.set_lights(0, 0, 0)  # All OFF
    
    def green_phase(self):
        """Green light phase"""
        self.set_lights(0, 0, 1)  # Green ON, others OFF
        self.countdown(self.timing['green'], "GREEN")
        self.set_lights(0, 0, 0)  # All OFF
    
    def yellow_phase(self):
        """Yellow warning phase"""
        self.set_lights(0, 1, 0)  # Yellow ON, others OFF
        self.countdown(self.timing['yellow'], "YELLOW")
        self.set_lights(0, 0, 0)  # All OFF
    
    def run_cycle(self):
        """Execute complete traffic light cycle"""
        print("Starting traffic light cycle...")
        
        self.red_phase()
        self.green_phase()
        self.yellow_phase()
        
        print("Cycle completed!\n")

# Main execution
if __name__ == "__main__":
    traffic_system = TrafficLightSystem()
    
    print("Traffic Light System Started")
    print("=" * 30)
    
    try:
        while True:
            traffic_system.run_cycle()
    except KeyboardInterrupt:
        # Cleanup on exit
        traffic_system.set_lights(0, 0, 0)
        traffic_system.display_number(0)
        print("\nSystem stopped by user")
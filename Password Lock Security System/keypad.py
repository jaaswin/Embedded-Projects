import time

class Keypad:
    def __init__(self, row_pins, col_pins, keys):
        self.row_pins = row_pins
        self.col_pins = col_pins
        self.keys = keys

    def get_key(self):
        for r in range(4):
            self.row_pins[r].high()
            for c in range(4):
                if self.col_pins[c].value() == 1:
                    time.sleep(0.2)
                    self.row_pins[r].low()
                    return self.keys[r][c]
            self.row_pins[r].low()
        return None

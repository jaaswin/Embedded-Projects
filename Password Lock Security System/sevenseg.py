from machine import Pin
import time

class SevenSeg:
    # Patterns are 8 bits: a,b,c,d,e,f,g,dp  (1 = ON)
    PATTERNS = {
        '0': [1,1,1,1,1,1,0,0],
        '1': [0,1,1,0,0,0,0,0],
        '2': [1,1,0,1,1,0,1,0],
        '3': [1,1,1,1,0,0,1,0],
        '4': [0,1,1,0,0,1,1,0],
        '5': [1,0,1,1,0,1,1,0],
        '6': [1,0,1,1,1,1,1,0],
        '7': [1,1,1,0,0,0,0,0],
        '8': [1,1,1,1,1,1,1,0],
        '9': [1,1,1,1,0,1,1,0],
        '-': [0,0,0,0,0,0,1,0],
        ' ': [0,0,0,0,0,0,0,0],
        'O': [1,1,1,1,1,1,0,0],
        'P': [1,1,0,0,1,1,1,0],
        'E': [1,0,0,1,1,1,1,0],
        'N': [0,0,1,0,1,1,0,0]
    }

    def __init__(self, seg_pins, digit_pins):
        # seg_pins should be a list of 8 pins [a,b,c,d,e,f,g,dp]
        self.seg_pins = [Pin(p, Pin.OUT) for p in seg_pins]
        self.digit_pins = [Pin(p, Pin.OUT) for p in digit_pins]

        # default: disable all digits (set high, digits are active-low in this driver)
        for d in self.digit_pins:
            d.value(1)
        # turn all segments off
        for s in self.seg_pins:
            s.value(0)

    def _char_pattern(self, ch):
        return self.PATTERNS.get(str(ch).upper(), self.PATTERNS[' '])

    def display(self, text):
        """Multiplex 4 characters on the 4 digits. text -> string or iterable, up to 4 chars."""
        s = str(text).ljust(4)[:4]
        for i, ch in enumerate(s):
            pat = self._char_pattern(ch)
            # set segments according to pattern (zip handles if seg_pins shorter/longer)
            for pin, val in zip(self.seg_pins, pat):
                pin.value(1 if val else 0)
            # enable only this digit (active low)
            for d in self.digit_pins:
                d.value(1)
            try:
                self.digit_pins[i].value(0)
            except IndexError:
                # defensive: if digit pins shorter, skip
                pass
            time.sleep_ms(3)
            # disable digit
            try:
                self.digit_pins[i].value(1)
            except IndexError:
                pass

class Clock:
    def __init__(self, hr=0, min=0, sec=0):
        if 0 <= hr <= 23 and 0 <= min <= 59 and 0 <= sec <= 59:
            self._hr = hr  # HW
            self._min = min
            self._sec = sec
        else:
            raise ValueError("hour, minutes, or seconds out of range!")

    def __repr__(self):
        return f"{self._hr}:{self._min}:{self._sec}"  #HW

    def settime(self, hr, min=0, sec=0):
        self._hr = hr
        self._min = min
        self._sec = sec

    def tic(self):
        self._sec += 1
        if self._sec >= 60:
            self._sec = 0
            self._min += 1
            if self._min >= 60:
                self._min = 0
                self._hr += 1
                if self._hr >= 24:
                    self._hr = 0

    def __sub__(self, other):
        result = 0
        result += self._sec - other._sec
        result += (self._min - other._min) * 60
        result += (self._hr - other._hr) * 3600
        return abs(result)

    def __add__(self, other):
        pass


if __name__ == "__main__":
    my_clock = Clock(11, 30, 59)
    your_clock = Clock(10)
    your_clock.settime(11, 31, 00)
    my_clock.tic()
    your_clock.tic()
    my_clock.jjj = 6
    try:
        bad_clock = Clock(235, 568, 465)
    except ValueError:
        bad_clock = Clock(23, 56, 46)

    print(my_clock)
    print(your_clock)
    print(my_clock._hr)
    print(my_clock-your_clock)

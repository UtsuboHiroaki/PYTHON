
class DateError(ValueError):
    def __init__(self, message, dt):
        self.message = message
        self.dt = dt
        super().__init__(message)

    def __str__(self):
        return f'{self.message}:{self.dt.strftime("%Y/%m/%d")}'


class PastDateError(DateError):
    def __init__(self, dt):
        super().__init__('過去の日付は指定できません', dt)


class HolidayError(DateError):
    def __init__(self, dt):
        super().__init__('休日は指定できません', dt)

class FiveTenDayError(DateError):
    def __init__(self, dt):
        super().__init__('5,10日は指定できません', dt)











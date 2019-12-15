class Clock:
    ''' python program to calculate
    the angle between the min and
    hour hand of a time given by a user
    '''

    def __init__(self, time):
        self.time = time

    def work_angle(self):
        splitted_time = self.time.split(':')
        hour = int(splitted_time[0])
        minute = int(splitted_time[1])

        norm_hour_pos = hour % 12 * 5 # hour hand position from 12
        hour_rel_min = 5 * minute / 60 # hour position for every min hand's move

        # getting real hour position
        real_hour = norm_hour_pos + hour_rel_min

        hour_angle = 6 * real_hour
        min_angle = 6 * minute

        
        angle = int(abs(hour_angle - min_angle))
        if angle > 180:
            angle = 360 - angle
            print(f'The angle between the minute and the hour hand is: {angle}⁰')

        else:
            print(f'The angle between the minute and the hour hand is: {angle}⁰')

clock_angle = Clock('9:00')
if __name__ == "__main__":

    clock_angle.work_angle()
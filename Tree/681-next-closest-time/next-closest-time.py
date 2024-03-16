from datetime import datetime, timedelta
class Solution:
    def nextClosestTime(self, time: str) -> str:
        out = ''
        time_num = set(time.replace(':', ''))
        while True:
            # time = datetime.strptime(time, '%H:%M')
            new_time = datetime.strptime(time, '%H:%M') + timedelta(minutes=1)

            new_time_str = new_time.strftime('%H:%M')
            new_time_set = list(set(new_time_str.replace(':', '')))

            i = 0

            while i < len(new_time_set):
                if new_time_set[i] in time_num:
                    i+=1
                else:
                    break
            if i==len(new_time_set):
                return new_time_str
            time = new_time_str


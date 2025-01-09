from datetime import datetime

seconds = 2483228800
dt = datetime(2011, 11, 4)

# преобразовать секунды seconds (прошедшие от начала эпохи) в объект datetime
print(datetime.fromtimestamp(seconds))
# объект datetime в секунды (прошедшие от начала эпохи)
print(dt.timestamp())
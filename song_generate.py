# ...existing code...
from suno_api import Suno

# הכנס כאן את העוגיות שלך כפי שהעתקת מהדפדפן
cookies = {
    "_clck": "1qkbgqg%7C2%7Cfx9%7C0%7C2009",
    "_clsk": "1p2jr0t%7C1751419976778%7C4%7C1%7Cn.clarity.ms%2Fcollect",
    "_gcl_au": "1.1.692938906.1751419868.1348275018.1751419971.1751419976",
    "authorization": "b6ee24df-9f7e-4bbf-a4e8-3e40faf5faed",
    "g_state": '{"i_l":0}'
}

suno = Suno(cookies=cookies)

prompt = "כתוב שיר שמח בעברית על קיץ וחוף הים"

# יצירת השיר
result = suno.generate(prompt)

# הדפסת הלינק לקובץ האודיו (אם הצליח)
if result and "audio_url" in result:
    print("Audio URL:", result["audio_url"])
else:
    print("לא התקבל קישור לאודיו, התוצאה המלאה:")
    print(result)
# ...existing code...

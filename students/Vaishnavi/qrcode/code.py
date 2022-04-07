import qrcode

img=qrcode.make('www.youtube.com')
img.save('hello.png')
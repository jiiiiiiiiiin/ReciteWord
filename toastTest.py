import zroya
import time
zroya.init("Python", "a", "b", "c", "d")
# zroya is imported and initialized
template = zroya.Template(zroya.TemplateType.ImageAndText4)

template.setFirstLine("Hi, I am NotifyBot.")
template.setSecondLine("It is nice to meet you.")
template.setThirdLine("How are you?")

template.addAction("I'm OK, I guess")
template.addAction("Fine")

template.setImage("python.ico")

zroya.show(template)
while True:
    time.sleep(0.1)
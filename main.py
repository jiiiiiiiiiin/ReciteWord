from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
import zroya
import time

Base = declarative_base()
zroya.init("Recite Word", "a", "b", "c", "d")


class Words(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String(100))
    pos = Column(String(100))
    explain = Column(String(100))

    def __repr__(self):
        return "<Word(word='%s', pos='%s', explain='%s')>" % (self.word, self.pos, self.explain)


class ReciteWord:
    def __init__(self, db_name):
        engine = create_engine('sqlite:///{}'.format(db_name))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.template = zroya.Template(zroya.TemplateType.ImageAndText4)
        self.template.addAction("我记住了。")
        self.template.addAction("没记住。")
        self.template.setAudio(zroya.AudioMode.Silence)
        self.i = 0

    def get_one_word(self):
        print('start query')
        count = self.session.query(func.count(Words.id)).scalar()
        random_id = int(random.random() * count)
        random_word = self.session.query(Words).filter_by(id=random_id).all()[0]
        print(random_word)

        self.template.setImage("python.ico")
        self.template.setFirstLine("单词：{}".format(random_word.word))
        self.template.setSecondLine("词性：{}".format(random_word.pos))
        self.template.setThirdLine("解释：{}".format(random_word.explain))



if __name__ == '__main__':
    r = ReciteWord('word.db')
    r.get_one_word()
    is_click = False


    def action(nid, action_id):
        global is_click
        if action_id:
            print("没记住")
        else:
            print("记住")
        is_click = True


    zroya.show(r.template, on_action=action)

    while True:
        if is_click:
            r.get_one_word()
            is_click = False
            # time.sleep(0.1)
            zroya.show(r.template, on_action=action, on_click=action)


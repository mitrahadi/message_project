from sqlalchemy import Integer, String, Column, Boolean

from base import Base


class Lesson(Base):
    __tablename__ = 'lessons'
    _id = Column("id", Integer, primary_key=True)
    _title = Column("title", String(30))
    _teacher = Column("teacher", String(50))
    _class_no = Column("class_no", Integer)
    _duration = Column("duration", Integer)

    def __init__(self, id, title, teacher,class_no, duration):
        self.id = id
        self.title = title
        self.teacher = teacher
        self.class_no = class_no
        self.duration = duration

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        self._teacher = value

    @property
    def class_no(self):
        return self._class_no

    @class_no.setter
    def class_no(self, value):
        self._class_no = value


    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

from da.tools.database_manager import *
from model.lesson import Lesson

session = get_session()


def save(lesson):
    session.add(lesson)
    session.commit()


def edit(lesson):
    session.merge(lesson)
    session.commit()


def remove(lesson):
    session.delete(lesson)
    session.commit()


def find_all():
    return session.query(Lesson).all()


def find_by_id(lesson_id):
    return session.query(Lesson).get(lesson_id)



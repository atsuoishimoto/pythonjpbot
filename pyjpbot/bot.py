from . import session
from . models import *

from slackbot.bot import listen_to
import re

@listen_to('^(\+\+\+|\-\-\-)(\w+)$')
def add_plusminus(message, p, name):
    f = message._get_user_id()
    if p == '+++':
        n = 1
    else:
        n = -1

    p = PlusMinus(pointto=name, pointfrom=f, point=n)
    session.add(p)
    session.commit()

    message.send('%s: %s' % (name, get_plusminus(name)))

def get_plusminus(t):
    r = session.query(func.sum(PlusMinus.point)).filter(PlusMinus.pointto==t).all()
    return r[0][0] or 0


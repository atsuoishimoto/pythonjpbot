from . import session
from . models import *

from slackbot.bot import listen_to

@listen_to(r'(\w+)(\+{2,}|\-{2,})$')
def add_plusminus(message, name, p):
    f = message._get_user_id()
    if p[0] == '+':
        n = len(p)-1
    else:
        n = -1*(len(p)-1)

    p = PlusMinus(pointto=name, pointfrom=f, point=n)
    session.add(p)
    session.commit()

    message.send('%s: %s' % (name, get_plusminus(name)))

def get_plusminus(t):
    r = session.query(func.sum(PlusMinus.point)).filter(PlusMinus.pointto==t).all()
    return r[0][0] or 0


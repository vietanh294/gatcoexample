from gatco.response import json, text
from application.server import app
from application.database import db
from application.extensions import auth

# from gatco_restapi.helpers import to_dict

from application.models.model import User

@app.route("/test")
async def test(request):
    user = db.session.query(User).filter(User.id == 1).first()
    print(user)
    u = to_dict(user)
    print(u)
    
    return json(request['user_agent'].to_dict())
    #return json({ "hello": "world" })
    
@app.route("/checkpass")
async def checkpass(request):
    password = "123456"
    pass_hash = auth.encrypt_password(password)
    #pass_hash = "$6$rounds=656000$Nap.kHgpqAP5EXur$ZQpja3EUTx3nf4pZQY2XiAfEmiieDYDuuJ.0NcRN7odAEdVK.azltozKKYft3KYlzP7d.rUd7S/vmX/jHUXQ3/"
    is_pw = auth.verify_password(password, pass_hash)
    print(is_pw)
    return text(pass_hash)

@app.route("/test3")
def test3(request):
    return text("Hello")

@app.route('/login', methods=['GET', 'POST'])
async def login(request):
    user = db.session.query(User).filter(User.id == 1).first()
    auth.login_user(request, user)
    return text("OK")

@app.route('/profile', methods=['GET', 'POST'])
@auth.login_required
async def profile(request):
    uid = auth.current_user(request)
    if uid is not None:
        response = text("uid:" + str(uid))
    else:
        response = text("There's a cookie up in this response")
    #del response.cookies['_session']
    return response

@app.route('/logout', methods=['GET', 'POST'])
async def logout(request):
    auth.logout_user(request)
    return text("OK")

@app.route("/sess")
async def index(request):
    # interact with the session like a normal dict
    if not request['session'].get('foo'):
        request['session']['foo'] = 0

    request['session']['foo'] += 1

    return text(request['session']['foo'])
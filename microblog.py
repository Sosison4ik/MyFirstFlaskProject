from app import app
from app.models import User

u = User(username = 'Susan', email='susan@example.com')
print(u)
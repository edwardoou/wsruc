#from decouple import config
import datetime
#import jwt
#import pytz

class Security():
    #secret = config('JWT_KEY')
    #tz = pytz.timezone("America/Lima")

    """ @classmethod
    def generate_token(cls, authenticated_user):
        payload = {
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=10),
            'username': authenticated_user.username,
            'fullname': authenticated_user.fullname,
            'roles': ['Administrator', 'Editor']
        }
        return jwt.encode(payload, cls.secret, algorithm="HS256") """

    @classmethod
    def verify_token(cls, headers):
        if 'Authorization' in headers.keys():
            authorization = headers['Authorization']    
            
            if (authorization):
                try:
                    encoded_token = authorization.split(" ")[1]
                    #payload = jwt.decode(encoded_token, cls.secret, algorithms=["HS256"])
                    if encoded_token == 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.cThIIoDvwdueQB468K5xDc5633seEFoqwxjF_xSJyQQ':
                      return True
                    else:
                      return False
                #except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                except:
                    return False
        return False
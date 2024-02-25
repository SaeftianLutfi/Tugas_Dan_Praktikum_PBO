import bcrypt
from dbDosen import DBConnection as mydb


class users:
    def __init__(self):
        self.__id = None
        self.__nama = None
        self.__nidn = None
        self.__email = None
        self.__password = None
        self.__uservalid = None
        self.__passwordvalid = None
        self.__loginvalid = None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def id(self):
        return self.__id
    
    @property
    def nama(self):
        return self.__nama
    
    @nama.setter
    def nama(self, value):
        self.__nama = value
        
    @property
    def nidn(self):
        return self.__nidn
    
    @nidn.setter
    def nidn(self, value):
        self.__nidn = value
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        self.__password = value
        
    @property
    def loginvalid(self):
        return self.__loginvalid
    
    @loginvalid.setter
    def loginvalid(self, value):
        self.__loginvalid = value
        
    def cekUsername(self, email):
        self.conn = mydb()
        sql = "SELECT * FROM dosen WHERE Email='" + email + "'"
        self.result = self.conn.findOne(sql)
        if (self.result!=None):
            self.__nama = self.result[1]
            self.__nidn = self.result[2]
            self.__email = self.result[3]
            self.__password = self.result[4]
            self.affected = self.conn.cursor.rowcount
            self.__uservalid = True
        else:
            self.__nama = ''
            self.__nidn = ''
            self.__email = ''
            self.__password = ''
            self.affected = 0
            self.__uservalid = False
        return self.__uservalid
    
    def cekPassword(self, password):
        salt = bcrypt.gensalt(rounds = 12)
        hasheadpass = bcrypt.hashpw(self.__password.encode('utf-8'), salt)
        c = password.encode('utf-8')
        d = bcrypt.checkpw(c, hasheadpass)
        if (d):
            self.__passwordvalid = True
        else:
            self.__passwordvalid = False
        return self.__passwordvalid
    
    def Validasi(self, email, password):
        a = self.cekUsername(email)
        if (a==True):
            b = self.cekPassword(password)
            if(b==True):
                self.__loginvalid = True
            else:
                self.__loginvalid = False
        else:
            self.__loginvalid = False
            
        val = []
        val = [self.__email, self.__loginvalid]
        return val
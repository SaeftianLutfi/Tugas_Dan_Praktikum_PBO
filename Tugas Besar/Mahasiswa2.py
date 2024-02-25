from dbMahasiswa import DBConnection as mydb

class mahasiswa2:
    def __init__(self):
        self.__id = None
        self.__nama = None
        self.__nim = None
        self.__semester = None
        self.__ipsemester = None
        self.__sks = None
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
    def nim(self):
        return self.__nim
    
    @nim.setter
    def nim(self, value):
        self.__nim = value
        
    @property
    def semester(self):
        return self.__semester
    
    @semester.setter
    def semester(self, value):
        self.__semester = value
        
    @property
    def ipsemester(self):
        return self.__ipsemester
    
    @ipsemester.setter
    def ipsemester(self, value):
        self.__ipsemester = value
        
    @property
    def sks(self):
        return self.__sks
    
    @sks.setter
    def sks(self, value):
        self.__sks = value
        
    def cekIPSemester(self, ipsemester):
        self.conn = mydb()
        val = (self.__sks)
        sql = "SELECT * FROM mahasiswa2 WHERE IPSemester='" + ipsemester + "'"
        self.affected =self.conn.findOne(sql, val)
        self.conn.disconnect
        return self.affected
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM mahasiswa2"
        self.result = self.conn.findAll(sql)
        return self.result
    
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa2 WHERE ID='" + str(id) + "'"
        self.__id = self.result[0]
        self.__nama = self.result[1]
        self.__nim = self.result[2]
        self.__semester = self.result[3]
        self.__ipsemester = self.result[4]
        self.__sks = self.result[5]
        self.affected = self.conn.cursor.rowcount
        self.__datavalid = True

    def getByNIM(self, nim):
        a=str(nim)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa2 WHERE NIM='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[0]
            self.__nama = self.result[1]
            self.__nim = self.result[2]
            self.__semester = self.result[3]
            self.__ipsemester = self.result[4]
            self.__sks = self.result[5]
            self.affected = self.conn.cursor.rowcount
            self.__datavalid = True
        else:
            self.__id = ''
            self.__nama = ''
            self.__nim = ''
            self.__semester = ''
            self.__ipsemester = ''
            self.__sks = ''
            self.affected = 0
            self.__datavalid = False
        return self.result
    
# Tampilkan semua data
A = mahasiswa2()
B = A.getAllData()
print(B)
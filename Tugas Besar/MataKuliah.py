from dbKuliah import DBConnection as mydb

#kuliah1
class Kuliah1:
    def __init__(self):
        self.__id = None
        self.__Semester = None
        self.__MataKuliah = None
        self.__SKS = None
        self.__Kelas = None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, val):
        self.__id = val
    
    @property
    def semester(self):
        return self.__Semester
    
    @semester.setter
    def semester(self, val):
        self.__Semester = val
        
    @property
    def matakuliah(self):
        return self.__MataKuliah
    
    @matakuliah.setter
    def matakuliah(self, val):
        self.__MataKuliah = val
        
    @property
    def sks(self):
        return self.__SKS
    
    @sks.setter
    def sks(self,val):
        self.__SKS = val
        
    @property
    def kelas(self):
        return self.__Kelas
    
    @kelas.setter
    def kelas(self, val):
        self.__Kelas = val
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__id, self.__Semester, self.__MataKuliah, self.__SKS, self.__Kelas)
        sql = "INSERT INTO kuliah1 (ID, Semester, Mata_Kuliah, SKS, Kelas) VALUE " + str(val)
        self.affected =  self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    
    def update(self, id):
        self.conn = mydb()
        val = (self.__Semester, self.__MataKuliah, self.__SKS, self.__Kelas, id)
        sql = "UPDATE kuliah1 SET Semester = %s, Mata_Kuliah = %s, SKS = %s, Kelas = %s WHERE ID=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    
    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM kuliah1 WHERE ID='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    
    def getByID(self, id):
        a=str(id)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM kuliah1 WHERE ID='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[0]
            self.__Semester = self.result[1]
            self.__MataKuliah = self.result[2]
            self.__SKS = self.result[3]
            self.__Kelas = self.result[4]
            self.affected = self.conn.cursor.rowcount
            self.conn.disconnect
        else:
            self.__id = ''
            self.__Semester = ''
            self.__MataKuliah = ''
            self.__SKS = ''
            self.__Kelas = ''
            self.affected = 0
        self.conn.disconnect
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM kuliah1"
        self.result = self.conn.findAll(sql)
        return self.result
    
#kuliah2
class Kuliah2:
    def __init__(self):
        self.__id = None
        self.__Semester = None
        self.__MataKuliah = None
        self.__SKS = None
        self.__Kelas = None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, val):
        self.__id = val
    
    @property
    def semester(self):
        return self.__Semester
    
    @semester.setter
    def semester(self, val):
        self.__Semester = val
        
    @property
    def matakuliah(self):
        return self.__MataKuliah
    
    @matakuliah.setter
    def matakuliah(self, val):
        self.__MataKuliah = val
        
    @property
    def sks(self):
        return self.__SKS
    
    @sks.setter
    def sks(self,val):
        self.__SKS = val
        
    @property
    def kelas(self):
        return self.__Kelas
    
    @kelas.setter
    def kelas(self, val):
        self.__Kelas = val
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__id, self.__Semester, self.__MataKuliah, self.__SKS, self.__Kelas)
        sql = "INSERT INTO kuliah2 (ID, Semester, Mata_Kuliah, SKS, Kelas) VALUE " + str(val)
        self.affected =  self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    
    def update(self, id):
        self.conn = mydb()
        val = (self.__Semester, self.__MataKuliah, self.__SKS, self.__Kelas, id)
        sql = "UPDATE kuliah2 SET Semester = %s, Mata_Kuliah = %s, SKS = %s, Kelas = %s WHERE ID=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    
    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM kuliah2 WHERE ID='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    
    def getByID(self, id):
        a=str(id)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM kuliah1 WHERE ID='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[0]
            self.__Semester = self.result[1]
            self.__MataKuliah = self.result[2]
            self.__SKS = self.result[3]
            self.__Kelas = self.result[4]
            self.affected = self.conn.cursor.rowcount
            self.conn.disconnect
        else:
            self.__id = ''
            self.__Semester = ''
            self.__MataKuliah = ''
            self.__SKS = ''
            self.__Kelas = ''
            self.affected = 0
        self.conn.disconnect
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM kuliah2"
        self.result = self.conn.findAll(sql)
        return self.result
    
#kuliah3
class Kuliah3:
    def __init__(self):
        self.__id = None
        self.__Semester = None
        self.__MataKuliah = None
        self.__SKS = None
        self.__Kelas = None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, val):
        self.__id = val
    
    @property
    def semester(self):
        return self.__Semester
    
    @semester.setter
    def semester(self, val):
        self.__Semester = val
        
    @property
    def matakuliah(self):
        return self.__MataKuliah
    
    @matakuliah.setter
    def matakuliah(self, val):
        self.__MataKuliah = val
        
    @property
    def sks(self):
        return self.__SKS
    
    @sks.setter
    def sks(self,val):
        self.__SKS = val
        
    @property
    def kelas(self):
        return self.__Kelas
    
    @kelas.setter
    def kelas(self, val):
        self.__Kelas = val
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__id, self.__Semester, self.__MataKuliah, self.__SKS, self.__Kelas)
        sql = "INSERT INTO kuliah3 (ID, Semester, Mata_Kuliah, SKS, Kelas) VALUE " + str(val)
        self.affected =  self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    
    def update(self, id):
        self.conn = mydb()
        val = (self.__Semester, self.__MataKuliah, self.__SKS, self.__Kelas, id)
        sql = "UPDATE kuliah3 SET Semester = %s, Mata_Kuliah = %s, SKS = %s, Kelas = %s WHERE ID=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    
    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM kuliah3 WHERE ID='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    
    def getByID(self, id):
        a=str(id)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM kuliah1 WHERE ID='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[0]
            self.__Semester = self.result[1]
            self.__MataKuliah = self.result[2]
            self.__SKS = self.result[3]
            self.__Kelas = self.result[4]
            self.affected = self.conn.cursor.rowcount
            self.conn.disconnect
        else:
            self.__id = ''
            self.__Semester = ''
            self.__MataKuliah = ''
            self.__SKS = ''
            self.__Kelas = ''
            self.affected = 0
        self.conn.disconnect
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM kuliah3"
        self.result = self.conn.findAll(sql)
        return self.result
    
#kuliah4
class Kuliah4:
    def __init__(self):
        self.__id = None
        self.__Semester = None
        self.__MataKuliah = None
        self.__SKS = None
        self.__Kelas = None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, val):
        self.__id = val
    
    @property
    def semester(self):
        return self.__Semester
    
    @semester.setter
    def semester(self, val):
        self.__Semester = val
        
    @property
    def matakuliah(self):
        return self.__MataKuliah
    
    @matakuliah.setter
    def matakuliah(self, val):
        self.__MataKuliah = val
        
    @property
    def sks(self):
        return self.__SKS
    
    @sks.setter
    def sks(self,val):
        self.__SKS = val
        
    @property
    def kelas(self):
        return self.__Kelas
    
    @kelas.setter
    def kelas(self, val):
        self.__Kelas = val
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__id, self.__Semester, self.__MataKuliah, self.__SKS, self.__Kelas)
        sql = "INSERT INTO kuliah4 (ID, Semester, Mata_Kuliah, SKS, Kelas) VALUE " + str(val)
        self.affected =  self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    
    def update(self, id):
        self.conn = mydb()
        val = (self.__Semester, self.__MataKuliah, self.__SKS, self.__Kelas, id)
        sql = "UPDATE kuliah4 SET Semester = %s, Mata_Kuliah = %s, SKS = %s, Kelas = %s WHERE ID=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    
    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM kuliah4 WHERE ID='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    
    def getByID(self, id):
        a=str(id)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM kuliah1 WHERE ID='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[0]
            self.__Semester = self.result[1]
            self.__MataKuliah = self.result[2]
            self.__SKS = self.result[3]
            self.__Kelas = self.result[4]
            self.affected = self.conn.cursor.rowcount
            self.conn.disconnect
        else:
            self.__id = ''
            self.__Semester = ''
            self.__MataKuliah = ''
            self.__SKS = ''
            self.__Kelas = ''
            self.affected = 0
        self.conn.disconnect
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM kuliah4"
        self.result = self.conn.findAll(sql)
        return self.result
    
#kuliah5
class Kuliah5:
    def __init__(self):
        self.__id = None
        self.__Semester = None
        self.__MataKuliah = None
        self.__SKS = None
        self.__Kelas = None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, val):
        self.__id = val
    
    @property
    def semester(self):
        return self.__Semester
    
    @semester.setter
    def semester(self, val):
        self.__Semester = val
        
    @property
    def matakuliah(self):
        return self.__MataKuliah
    
    @matakuliah.setter
    def matakuliah(self, val):
        self.__MataKuliah = val
        
    @property
    def sks(self):
        return self.__SKS
    
    @sks.setter
    def sks(self,val):
        self.__SKS = val
        
    @property
    def kelas(self):
        return self.__Kelas
    
    @kelas.setter
    def kelas(self, val):
        self.__Kelas = val
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__id, self.__Semester, self.__MataKuliah, self.__SKS, self.__Kelas)
        sql = "INSERT INTO kuliah5 (ID, Semester, Mata_Kuliah, SKS, Kelas) VALUE " + str(val)
        self.affected =  self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    
    def update(self, id):
        self.conn = mydb()
        val = (self.__Semester, self.__MataKuliah, self.__SKS, self.__Kelas, id)
        sql = "UPDATE kuliah5 SET Semester = %s, Mata_Kuliah = %s, SKS = %s, Kelas = %s WHERE ID=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    
    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM kuliah5 WHERE ID='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    
    def getByID(self, id):
        a=str(id)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM kuliah1 WHERE ID='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[0]
            self.__Semester = self.result[1]
            self.__MataKuliah = self.result[2]
            self.__SKS = self.result[3]
            self.__Kelas = self.result[4]
            self.affected = self.conn.cursor.rowcount
            self.conn.disconnect
        else:
            self.__id = ''
            self.__Semester = ''
            self.__MataKuliah = ''
            self.__SKS = ''
            self.__Kelas = ''
            self.affected = 0
        self.conn.disconnect
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM kuliah5"
        self.result = self.conn.findAll(sql)
        return self.result
    
#kuliah6
class Kuliah6:
    def __init__(self):
        self.__id = None
        self.__Semester = None
        self.__MataKuliah = None
        self.__SKS = None
        self.__Kelas = None
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, val):
        self.__id = val
    
    @property
    def semester(self):
        return self.__Semester
    
    @semester.setter
    def semester(self, val):
        self.__Semester = val
        
    @property
    def matakuliah(self):
        return self.__MataKuliah
    
    @matakuliah.setter
    def matakuliah(self, val):
        self.__MataKuliah = val
        
    @property
    def sks(self):
        return self.__SKS
    
    @sks.setter
    def sks(self,val):
        self.__SKS = val
        
    @property
    def kelas(self):
        return self.__Kelas
    
    @kelas.setter
    def kelas(self, val):
        self.__Kelas = val
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__id, self.__Semester, self.__MataKuliah, self.__SKS, self.__Kelas)
        sql = "INSERT INTO kuliah6 (ID, Semester, Mata_Kuliah, SKS, Kelas) VALUE " + str(val)
        self.affected =  self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    
    def update(self, id):
        self.conn = mydb()
        val = (self.__Semester, self.__MataKuliah, self.__SKS, self.__Kelas, id)
        sql = "UPDATE kuliah6 SET Semester = %s, Mata_Kuliah = %s, SKS = %s, Kelas = %s WHERE ID=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    
    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM kuliah6 WHERE ID='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    
    def getByID(self, id):
        a=str(id)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM kuliah1 WHERE ID='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[0]
            self.__Semester = self.result[1]
            self.__MataKuliah = self.result[2]
            self.__SKS = self.result[3]
            self.__Kelas = self.result[4]
            self.affected = self.conn.cursor.rowcount
            self.conn.disconnect
        else:
            self.__id = ''
            self.__Semester = ''
            self.__MataKuliah = ''
            self.__SKS = ''
            self.__Kelas = ''
            self.affected = 0
        self.conn.disconnect
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM kuliah6"
        self.result = self.conn.findAll(sql)
        return self.result
    
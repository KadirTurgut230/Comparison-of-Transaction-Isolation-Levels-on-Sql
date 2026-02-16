import psycopg2
#from psycopg2 import OperationalError


def prepareDatabase(host, database, user, password, port,
                    filePath, dataSize):
    conn = psycopg2.connect(
       host = host,
       database= database,  # Veritabanı adı
       user= user,     # PostgreSQL kullanıcı adı
       password= password,# PostgreSQL şifre
       port = port
    )
    cursor = conn.cursor()
    conn.autocommit = True
       
    # SQL dosyasını oku ve çalıştır
    with open(filePath, 'r') as f:
        sql_commands = f.read()      
    # Tüm komutları tek seferde çalıştır
    cursor.execute(sql_commands)
    
    query = f"select insertWriteSkew({dataSize});"
    cursor.execute(query)
    
    query = "select resetValuesWriteSkew();"
    cursor.execute(query)
    
    cursor.close()
    conn.close()



def connectDatabase(host, database, user, password, port, dataSize):
    
     # Veritabanı bağlantısı (dosya yoksa oluşturur)
     conn = psycopg2.connect(
        host = host,
        database= database,  # Veritabanı adı
        user= user,     # PostgreSQL kullanıcı adı
        password= password,# PostgreSQL şifre
        port = port
    )
     cursor = conn.cursor()
     conn.autocommit = True
     
     query = 'select * from writeSkewTest ;'
     cursor.execute(query)
     testResult = int(cursor.fetchone()[0])

     query = 'select resetValuesWriteSkew();';
     cursor.execute(query)
     
     # Değişiklikleri kaydet ve bağlantıyı kapat
     cursor.close()
     conn.close()
        
     return testResult
        
        
        
    
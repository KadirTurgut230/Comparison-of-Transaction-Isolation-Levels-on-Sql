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
    
    query = f'select initialize_lost_Update({dataSize});';
    cursor.execute(query)
    
    cursor.close()
    conn.close()


def connectDatabase(host, database, user, password, port, dataSize):
    try:
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
        
        query = 'select sum(balance) from lost_update1;'
        cursor.execute(query)
        result1 = int(cursor.fetchone()[0])
         
        query = 'select * from lost_update_Test;'
        cursor.execute(query)
        result2 = int(cursor.fetchone()[0])
        
        testResult = abs(result1 - result2)
        
        query = f'select initialize_lost_Update({dataSize});';
        cursor.execute(query)
        
        # Değişiklikleri kaydet ve bağlantıyı kapat
        cursor.close()
        conn.close()
        
    except Exception as e:
        print("Hata oluştu:", e)
        
    return testResult     

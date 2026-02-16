import os
import subprocess
import numpy as np


def findFilePath(filename, search_path = 'C:\\'):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename), root
    return None, None


def findPatOfFileList(selection, pathFileOption):
    if pathFileOption == 1:
        if selection == 1:
            path_of_files = [r'C:\vtLab\lostUpdate1.sql', r'C:\vtLab\lostUpdate2.sql',
                           r'C:\vtLab\lostUpdate3.sql', r'C:\vtLab\lostUpdate4.sql',
                           r'C:\vtLab\lostUpdatePrep.sql']
        elif selection == 2:
            path_of_files = [r'C:\vtLab\writeSkew1.sql', r'C:\vtLab\writeSkew2.sql',
                           r'C:\vtLab\writeSkew3.sql', r'C:\vtLab\writeSkew4.sql',
                           r'C:\vtLab\writeSkewPrep.sql']
        elif selection == 3:
            path_of_files = [r'C:\vtLab\repRead1.sql', r'C:\vtLab\repRead2.sql',
                           r'C:\vtLab\repRead3.sql', r'C:\vtLab\repRead4.sql',
                           r'C:\vtLab\repReadPrep.sql']
        elif selection == 4:
            path_of_files = [r'C:\vtLab\phantom1.sql', r'C:\vtLab\phantom2.sql',
                           r'C:\vtLab\phantom3.sql', r'C:\vtLab\phantom4.sql',
                           r'C:\vtLab\phantomPrep.sql']   
    else:
        if selection == 1:
            files = ['lostUpdate1.sql','lostUpdate2.sql',
                     'lostUpdate3.sql', 'lostUpdate4.sql',
                    'lostUpdatePrep.sql']
         
        elif selection == 2:
            files = ['writeSkew1.sql','writeSkew2.sql',
                     'writeSkew3.sql','writeSkew4.sql',
                     'writeSkewPrep.sql']
        elif selection == 3:
            files = ['repRead1.sql', 'repRead2.sql', 
                     'repRead3.sql','repRead4.sql',  
                     'repReadPrep.sql'] 
        elif selection == 4:
            files = ['phantom1.sql', 'phantom2.sql', 
                     'phantom3.sql','phantom4.sql',  
                     'phantomPrep.sql'] 
        else:
            os.system("pause")
        
        path_of_files = 5*['']
        for i in range(5):
            if i == 0:
                path_of_files[i], old_path = findFilePath(files[i])
            else:
                path_of_files[i], old_path = findFilePath(files[i], old_path) 
                if old_path is None:
                        path_of_files[i], old_path = findFilePath(files[i])        
    
    return path_of_files

def executePgbench(host, db, user, password, port, 
                   filePath, connection, thread, txNumber):
    
    max_tries = '300'
    command = [
        'pgbench',
        '-h', host,        # Host
        '-p', port,             # Port
        '-U', user,         # Kullanıcı
        
        '--max-tries',max_tries,
        
        '-c', connection,        
        '-j', thread,             
        '-t', txNumber,
        '-f', filePath,
        db        # Database
    ]

    env = {
        'PGPASSWORD': password
    }

    # Komutu çalıştır
    result = subprocess.run(command, env={**env,
            **dict(**subprocess.os.environ)}, capture_output=True, text=True)

    arr = result.stdout
    print("Test tamamlandı.")
    
    return arr


def result2XandY(result, dataset, errorNumber):
    tokenizedResult = result.replace(': ', ' = ')
    tokenizedResult = tokenizedResult.replace('= ','=').split('\n')
    resultX = np.empty(13, dtype = 'U50')
    resultY = np.zeros(13, dtype = float)
    
    resultX[0] = "number of dataset"
    resultY[0] = dataset
    for i in range(4, 15):
        length = len(tokenizedResult[i])
        equalIndex = tokenizedResult[i].index('=')
        spaceIndex = tokenizedResult[i].find(' ', equalIndex)
        divIndex = tokenizedResult[i].find('/', equalIndex)
        
        if spaceIndex == -1 and divIndex == -1 :
            temp = tokenizedResult[i][equalIndex + 1 : length]
        elif spaceIndex != -1:
            temp = tokenizedResult[i][equalIndex + 1 : spaceIndex]
        else:
            temp = tokenizedResult[i][equalIndex + 1 : divIndex]

        tempX = tokenizedResult[i][0 : equalIndex]
        resultX[i - 3] = tempX
        if i == 12 or i == 13:
            resultX[i - 3] += '(ms)'
        
        temp = float(temp)
        resultY[i - 3] = temp
 
    resultX[12] = 'number of error'
    resultY[12] = errorNumber
 
    return resultX, resultY


import numpy as np
import matplotlib.pyplot as plt


def plotTable(x, y, suptitle, title, colLabels):
    #transpose almayı unutma np.transpose(dizi)
    # Örnek veriler
    y = np.transpose(y)
    # Şekil oluştur
    fig, ax = plt.subplots()
    
    # Tablo başlığı (sütun başlığı)
    column_labels = colLabels
    row_labels = x
    
    # Tabloyu oluştur
    ax.table(cellText=y.tolist(), 
                     colLabels=column_labels, 
                     rowLabels=row_labels,
                     loc='center')
    
    # Eksenleri kapat
    ax.axis('off')  
    # Başlık
    plt.suptitle(suptitle, x = 0.2, y = 0.85, ha = 'left',
                 color = 'red', fontsize = 15)
    plt.title(title, loc = 'right')
    # Göster
    plt.show()

def plotGraphic(x, y, suptitle, title, colLabels, indep_var):
    #transpose almayı unutma np.transpose(dizi)
    # Örnek veriler
    plt.suptitle(suptitle, x = 0.0, y = 0.95, ha = 'left',
                 color = 'red', fontsize = 13)
    plt.title(title, loc = 'right')
    if indep_var == 1:
        x_label = 'Number of Clients'
    elif indep_var == 2:
        x_label = 'Isolation Level'    
    elif indep_var == 3:
        x_label = 'Number of Transaction'
    elif indep_var == 4:
        x_label = 'Number of Dataset'
    plt.xlabel(x_label)
    
    graphic_y = y[ : ,11]
    plt.ylabel(x[11])
    
    plt.plot(colLabels, graphic_y)
    plt.show()
    
    
    plt.suptitle(suptitle, x = 0.0, y = 0.95, ha = 'left',
                 color = 'red', fontsize = 13)
    plt.title(title, loc = 'right')
    plt.xlabel(x_label)
    
    graphic_y = y[ : , 12]
    plt.ylabel(x[12])
    
    plt.plot(colLabels, graphic_y)
    plt.show()
    
    
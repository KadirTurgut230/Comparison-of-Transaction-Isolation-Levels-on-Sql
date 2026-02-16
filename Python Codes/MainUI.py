import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import PgbenchTester as tester
import PlottingTool as pt
import LostUpdate1
import WriteSkew1
import RepRead1
import Phantom1

class PostgreSQLAnomalyTester:
    def __init__(self, root):
        self.root = root
        self.root.title("PostgreSQL Anomaly Tester")
        self.root.geometry("1000x800")  
        
        
        self.large_font = ('Arial', 12)
        self.medium_font = ('Arial', 11)
        
        
        style = ttk.Style()
        style.configure('.', font=self.medium_font)
        style.configure('TLabel', font=self.medium_font)
        style.configure('TButton', font=self.medium_font)
        style.configure('TRadiobutton', font=self.medium_font)
        style.configure('TEntry', font=self.medium_font)
        style.configure('TLabelFrame', font=self.large_font)
        
        # Default values
        self.host = 'localhost'
        self.db = 'example2'
        self.user = 'postgres'
        self.password = '1234'
        self.port = '5432'
        self.selection = 1
        self.indep_var = 1
        self.connection = '10'
        self.isolation_level = 1
        self.tx_number = '10'
        self.data_size = '10'
        self.custom_values = ['10', '20', '40', '80']  # Default values
        self.file_path_option = 1  # 1: default, 2: find
        
        # Padding değerlerini artırdım
        self.padx = 15
        self.pady = 10
        
        # Create panels
        self.create_connection_panel()
        self.create_independent_var_panel()
        self.create_dependent_vars_panel()
        self.create_values_panel()
        
        # Initialize with default independent var selection
        self.update_dependent_vars_panel()
        self.update_values_panel_visibility()
    
    def create_connection_panel(self):
        panel1 = ttk.LabelFrame(self.root, text="Connection Settings", padding=(15, 15))
        panel1.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky="ew", columnspan=2)
        
        # Host
        ttk.Label(panel1, text="Host:").grid(row=0, column=0, sticky="w", pady=5)
        self.host_entry = ttk.Entry(panel1, width=25)
        self.host_entry.insert(0, self.host)
        self.host_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        # Database
        ttk.Label(panel1, text="Database:").grid(row=1, column=0, sticky="w", pady=5)
        self.db_entry = ttk.Entry(panel1, width=25)
        self.db_entry.insert(0, self.db)
        self.db_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        
        # User
        ttk.Label(panel1, text="User:").grid(row=2, column=0, sticky="w", pady=5)
        self.user_entry = ttk.Entry(panel1, width=25)
        self.user_entry.insert(0, self.user)
        self.user_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        
        # Password
        ttk.Label(panel1, text="Password:").grid(row=3, column=0, sticky="w", pady=5)
        self.password_entry = ttk.Entry(panel1, show="*", width=25)
        self.password_entry.insert(0, self.password)
        self.password_entry.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        
        # Port
        ttk.Label(panel1, text="Port:").grid(row=4, column=0, sticky="w", pady=5)
        self.port_entry = ttk.Entry(panel1, width=25)
        self.port_entry.insert(0, self.port)
        self.port_entry.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
        
        # Anomaly Selection
        ttk.Label(panel1, text="Anomaly Type:").grid(row=5, column=0, sticky="w", pady=5)
        self.anomaly_var = tk.IntVar(value=self.selection)
        anomalies = [
            ("1. Lost Update", 1),
            ("2. Write Skew", 2),
            ("3. Nonrepeatable Read", 3),
            ("4. Phantom Phenomenon", 4)
        ]
        for i, (text, val) in enumerate(anomalies):
            ttk.Radiobutton(panel1, text=text, variable=self.anomaly_var, value=val).grid(
                row=6+i//2, column=i%2, sticky="w", padx=5, pady=2)
        
        # File Path Options
        self.file_path_var = tk.IntVar(value=1)
        ttk.Radiobutton(panel1, text="Default File Path", variable=self.file_path_var, value=1).grid(
            row=10, column=0, sticky="w", padx=5, pady=5)
        ttk.Radiobutton(panel1, text="Find File Path", variable=self.file_path_var, value=2).grid(
            row=10, column=1, sticky="w", padx=5, pady=5)
    
    def create_independent_var_panel(self):
        panel2 = ttk.LabelFrame(self.root, text="Independent Variable", padding=(15, 15))
        panel2.grid(row=1, column=0, padx=self.padx, pady=self.pady, sticky="ew")
        
        self.indep_var_var = tk.IntVar(value=self.indep_var)
        options = [
            ("1. Connection Count", 1),
            ("2. Isolation Level", 2),
            ("3. Transaction Count", 3),
            ("4. Dataset Size", 4)
        ]
        for i, (text, val) in enumerate(options):
            ttk.Radiobutton(panel2, text=text, variable=self.indep_var_var, 
                          value=val, command=self.update_ui).grid(
                row=i//2, column=i%2, sticky="w", padx=5, pady=2)
    
    def create_dependent_vars_panel(self):
        self.panel3 = ttk.LabelFrame(self.root, text="Control Variables", padding=(15, 15))
        self.panel3.grid(row=2, column=0, padx=self.padx, pady=self.pady, sticky="ew")
        
        # Connection count (default shown)
        ttk.Label(self.panel3, text="Connection Count:").grid(row=0, column=0, sticky="w", pady=5)
        self.connection_entry = ttk.Entry(self.panel3, width=20)
        self.connection_entry.insert(0, self.connection)
        self.connection_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        # Isolation level
        ttk.Label(self.panel3, text="Isolation Level:").grid(row=1, column=0, sticky="w", pady=5)
        self.isolation_var = tk.IntVar(value=self.isolation_level)
        levels = [
            ("1. Read Committed", 1),
            ("2. Repeatable Read", 2),
            ("3. Serializable", 3)
        ]
        for i, (text, val) in enumerate(levels):
            ttk.Radiobutton(self.panel3, text=text, variable=self.isolation_var, value=val).grid(
                row=2+i, column=0, columnspan=2, sticky="w", padx=5, pady=2)
        
        # Transaction count
        ttk.Label(self.panel3, text="Transaction Count:").grid(row=5, column=0, sticky="w", pady=5)
        self.tx_entry = ttk.Entry(self.panel3, width=20)
        self.tx_entry.insert(0, self.tx_number)
        self.tx_entry.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
        
        # Dataset size
        ttk.Label(self.panel3, text="Dataset Size:").grid(row=6, column=0, sticky="w", pady=5)
        self.data_size_entry = ttk.Entry(self.panel3, width=20)
        self.data_size_entry.insert(0, self.data_size)
        self.data_size_entry.grid(row=6, column=1, sticky="ew", padx=5, pady=5)
        
        # Run button (daha büyük bir buton)
        ttk.Button(self.panel3, text="Run Test", command=self.run_test).grid(
            row=7, column=0, columnspan=2, pady=15, ipady=5)
    
    def create_values_panel(self):
        self.panel4 = ttk.LabelFrame(self.root, text="Test Values (for Independent Variable)", padding=(15, 15))
        self.panel4.grid(row=1, column=1, rowspan=2, padx=self.padx, pady=self.pady, sticky="nsew")
        
        # Create entry widgets for 4 values
        self.value_entries = []
        for i in range(4):
            ttk.Label(self.panel4, text=f"Value {i+1}:").grid(row=i, column=0, padx=10, pady=8, sticky="w")
            entry = ttk.Entry(self.panel4, width=15)
            entry.insert(0, self.custom_values[i])
            entry.grid(row=i, column=1, padx=10, pady=8, sticky="ew")
            self.value_entries.append(entry)
    
    def update_ui(self):
        self.update_dependent_vars_panel()
        self.update_values_panel_visibility()
    
    def update_values_panel_visibility(self):
        self.indep_var = self.indep_var_var.get()
        if self.indep_var == 2:  # Isolation Level
            self.panel4.grid_remove()
        else:
            self.panel4.grid()
    
    def update_dependent_vars_panel(self):
        # Hide all dependent variable widgets
        for widget in self.panel3.winfo_children():
            widget.grid_remove()
        
        # Get selected independent variable
        self.indep_var = self.indep_var_var.get()
        
        # Show only relevant dependent variables
        if self.indep_var != 1:  # If connection count is NOT the independent var
            ttk.Label(self.panel3, text="Connection Count:").grid(row=0, column=0, sticky="w", pady=5)
            self.connection_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        if self.indep_var != 2:  # If isolation level is NOT the independent var
            ttk.Label(self.panel3, text="Isolation Level:").grid(row=1, column=0, sticky="w", pady=5)
            levels = [
                ("1. Read Committed", 1),
                ("2. Repeatable Read", 2),
                ("3. Serializable", 3)
            ]
            for i, (text, val) in enumerate(levels):
                ttk.Radiobutton(self.panel3, text=text, variable=self.isolation_var, value=val).grid(
                    row=2+i, column=0, columnspan=2, sticky="w", padx=5, pady=2)
        
        if self.indep_var != 3:  # If transaction count is NOT the independent var
            ttk.Label(self.panel3, text="Transaction Count:").grid(row=5, column=0, sticky="w", pady=5)
            self.tx_entry.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
        
        if self.indep_var != 4:  # If dataset size is NOT the independent var
            ttk.Label(self.panel3, text="Dataset Size:").grid(row=6, column=0, sticky="w", pady=5)
            self.data_size_entry.grid(row=6, column=1, sticky="ew", padx=5, pady=5)
        
        # Always show run button (daha büyük)
        ttk.Button(self.panel3, text="Run Test", command=self.run_test).grid(
            row=7, column=0, columnspan=2, pady=15, ipady=5)
    
    def run_test(self):
        try:
            self.file_path_option = self.file_path_var.get()
            # Get all values from the UI
            self.host = self.host_entry.get() or 'localhost'
            self.db = self.db_entry.get() or 'example2'
            self.user = self.user_entry.get() or 'postgres'
            self.password = self.password_entry.get() or '1234'
            self.port = self.port_entry.get() or '5432'
            self.selection = self.anomaly_var.get()
            self.indep_var = self.indep_var_var.get()
            
            if self.indep_var != 1:
                self.connection = self.connection_entry.get()
            if self.indep_var != 2:   
                self.isolation_level = self.isolation_var.get()
            if self.indep_var != 3:
                self.tx_number = self.tx_entry.get()
            if self.indep_var != 4:
                self.data_size = self.data_size_entry.get()
                
            # Determine which module to use based on selection
            if self.selection == 1:
                module = LostUpdate1
                suptitle = 'Lost Update'
            elif self.selection == 2:
                module = WriteSkew1  
                suptitle = 'Write Skew'      
            elif self.selection == 3:
                module = RepRead1    
                suptitle = 'Nonrepeatable Read' 
            elif self.selection == 4:
                module = Phantom1
                suptitle = 'Phantom Phenomenon' 
            else:
                messagebox.showerror("Error", "Invalid anomaly selection")
                return
            
            path_of_fileList = tester.findPatOfFileList(self.selection, 
                                                        self.file_path_option)
            
            # Set up iterable and title based on independent variable
            if self.indep_var == 1:
                iterable = [entry.get() for entry in self.value_entries]
                title = 'Independent variable is number of connection'
            elif self.indep_var == 2:   
                iterable = path_of_fileList
                title = 'Independent variable is isolation level'
            elif self.indep_var == 3:
                iterable = [entry.get() for entry in self.value_entries]
                title = 'Independent variable is number of transaction'
            elif self.indep_var == 4:
                iterable = [int(entry.get()) for entry in self.value_entries]
                title = 'Independent variable is number of dataset'
                
            if self.indep_var != 2:
                if self.isolation_level == 1:
                    title += '\nIsolation Level is Read Committed'
                elif self.isolation_level == 2:
                    title += '\nIsolation Level is Repeatable Read'
                if self.isolation_level == 3:
                    title += '\nIsolation Level is Serializable'
            
            if self.indep_var != 2:
                colLabels = [entry.get() for entry in self.value_entries]
            else:
                colLabels = ['read committed', 'repeatable read', 'serializable', 'serial']
            
            resultY = np.zeros((4,13), dtype=float)
            
            module.prepareDatabase(self.host, self.db, self.user, self.password, self.port, 
                                 path_of_fileList[4], self.data_size)
            
            for i in range(4):
                if i == 3 and self.indep_var == 2:
                    connection = '1'
                    txNumber = '400'
                else:
                    connection = self.connection
                    txNumber = self.tx_number
                
                if self.indep_var == 1:
                    connection = iterable[i]
                elif self.indep_var == 3:
                    txNumber = iterable[i]
                
                if self.indep_var == 2:
                    filePath = iterable[i]
                else:
                    filePath = path_of_fileList[self.isolation_level - 1]
                
                if self.indep_var == 4:
                    dataSize = iterable[i]
                else:
                    dataSize = self.data_size
                
                result = tester.executePgbench(self.host, self.db, self.user, self.password, self.port,
                                             filePath, connection, connection, txNumber)
                errorNumber = module.connectDatabase(self.host, self.db, self.user, 
                                                 self.password, self.port, dataSize)
                resultX, resultY[i] = tester.result2XandY(result, dataSize, errorNumber)
            
            pt.plotTable(resultX, resultY, suptitle, title, colLabels)
            pt.plotGraphic(resultX, resultY, suptitle, title, colLabels, 
                         self.indep_var)
            
            print('Tablo oluşturuldu!')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")    
        
if __name__ == "__main__":
    root = tk.Tk()
    app = PostgreSQLAnomalyTester(root)
    root.mainloop()
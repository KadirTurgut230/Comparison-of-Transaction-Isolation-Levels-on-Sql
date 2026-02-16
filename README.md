# Comparison-of-Transaction-Isolation-Levels-on-Sql
This project is a comprehensive testing and analysis tool designed to evaluate the impact of transaction isolation levels and potential data anomalies in PostgreSQL database management systems. Built upon the pgbench utility, the system simulates critical scenarios—including Lost Update, Write Skew, Non-repeatable Read, and Phantom Read—to objectively report database behavior under various workloads and isolation configurations.

The architecture utilizes SQL scripts for database logic management, while Python modules automate the testing procedures and generate visual reports (tables and charts) via Matplotlib. Supporting both console and Tkinter-based graphical user interfaces, the system requires users to click the Find File Path button within the UI to define the necessary paths for the SQL scripts, ensuring that the files can be correctly located and the testing processes can be executed successfully.

Türkçe Açıklama:

Bu proje, PostgreSQL veritabanı yönetim sistemlerinde işlem (transaction) izolasyon seviyelerinin ve olası veri anomalilerinin etkilerini ölçmek için geliştirilmiş kapsamlı bir test ve analiz aracıdır. pgbench aracını temel alan sistem; Lost Update, Write Skew, Non-repeatable Read ve Phantom Read gibi kritik senaryoları simüle ederek, veritabanının farklı yük ve izolasyon ayarları altındaki davranışlarını objektif verilerle raporlar.

Sistem mimarisi, SQL betikleriyle veritabanı mantığını yönetirken, Python modülleriyle testlerin otomasyonunu ve sonuçların Matplotlib kullanılarak görselleştirilmesini sağlar. Hem konsol hem de Tkinter tabanlı grafiksel kullanıcı arayüzü desteği sunan bu platformda, test süreçlerinin hatasız yürütülebilmesi ve gerekli SQL dosyalarının sistem tarafından otomatik olarak bulunabilmesi için arayüzde yer alan Find File Path butonuna tıklanarak dosya yollarının tanımlanması gerekmektedir.

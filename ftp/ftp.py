from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print("Conexao com sucesso ",ftp.getwelcome())

ftp.quit()
def dados_usuario(**kwargs):
    for key, value in kwargs.items():
        print("%s  %s" %(key, value))
    

dados_usuario(Firstname= 'Yan',
              Lastname='Martins', 
              Email='yantmartins@nomail.com', 
              Country ='Wakanda', 
              Age='25', 
              Phone = '987654321')        





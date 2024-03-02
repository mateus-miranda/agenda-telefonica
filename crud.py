import psycopg2

class AppBD:
    def __init__(self):
        print('Metodo construtor')

    def abrirConexao(self):
        try:
            self.conn = psycopg2.connect(database = "agenda", user = "postgres", password = "#Mateus4151", host = "127.0.0.1", port = "5432")
            print('Banco de dados conectado com sucesso!')
        except (Exception, psycopg2.Error) as error:
            if (self.conn):
                print('Falha ao se conectar ao Banco de Dados', error)
    #---------------------------------------------------------------
    #Selecionar todos os dados da agenda
    #---------------------------------------------------------------                      
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.conn.cursor()

            print('Selecionando todos os numeros da agenda')
            select_query = '''select * from public. "agenda" '''
            
            cursor.execute(select_query)
            registro = cursor.fetchall()
            print(registro)

        except (Exception, psycopg2.Error) as error:
            print('Erro ao selecionar os dados', error)

        finally:
            if (self.conn):
                cursor.close()
                self.conn.close()
                print('A conexão com o banco de dados foi fechada')
            return registro 
    #---------------------------------------------------------------
    #Inserir dados na tabela
    #---------------------------------------------------------------  
    def inserirDados(self, id, nome, telefone):
        try:
            self.abrirConexao()
            cursor = self.conn.cursor()

            print('Inserindo dados na tabela')
            insert_query = '''INSERT INTO public. "agenda"("id", "nome", "telefone") VALUES (%s, %s, %s)'''
            record_to_insert = (id, nome, telefone)
            cursor.execute(insert_query, record_to_insert)
            self.conn.commit()
            count = cursor.rowcount
            print(count, "Registros inseridos com sucesso na tabela Agenda")
        except (Exception, psycopg2.Error) as error:
            if (self.conn):
                print('Error ao inserir dados na tabela', error)
        finally:
            if(self.conn):
                cursor.close()
                self.conn.close()
                print('A conexão com o banco de dados foi fechada')
    #---------------------------------------------------------------
    #Atualizar dados na tabela
    #---------------------------------------------------------------
    def atualizarDados(self, id, nome, telefone):
        try:
            self.abrirConexao()
            cursor = self.conn.cursor()
            
            #Consulta antes de atualizar os dados
            print("Registros antes da atualização")
            select_query = '''select * from public. "agenda" where "id" = %s '''
            cursor.execute(select_query, (id,))
            registro = cursor.fetchone()
            print(registro)

            #Atualizar registros
            print('Atualizando dados')
            update_query = '''Update public. "agenda" set "nome" = %s, "telefone" = %s where "id" = %s  '''
            record_to_update = (nome, telefone, id)
            cursor.execute(update_query, record_to_update)
            self.conn.commit()

            #Consulta após atualizar
            count = cursor.rowcount  
            print(count, 'Registros atualizados com sucesso')
            print('Registro depois da atualização')
            select_query = '''select * from public. "agenda" where "id" = %s '''
            cursor.execute(select_query, (id,))
            registro = cursor.fetchone()
            print(registro)
        except (Exception, psycopg2.Error) as error:
            print('Error na atualização de dados', error)
        finally:
            if(self.conn):
                cursor.close()
                self.conn.close()
                print('A conexão com o banco de dados foi fechada')
    #---------------------------------------------------------------
    #Deletar dados na tabela
    #---------------------------------------------------------------
    def excluirDados(self, id):
        try:
            self.abrirConexao()
            cursor = self.conn.cursor()

            #Excluir registros
            excluir_query = '''Delete from public. "agenda" where "id" = %s '''
            cursor.execute(excluir_query, (id,))
            self.conn.commit()
            count = cursor.rowcount
            print(count, "Registro excluido com sucesso!")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao excluir o registro na tabela", error)
        finally:
            if(self.conn):
                cursor.close()
                self.conn.close()
                print('A conexão com o banco de dados foi fechada')

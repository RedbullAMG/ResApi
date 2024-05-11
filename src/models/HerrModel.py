from database.db import get_connection
from .entities.Herr import Herr

from utils.ApiBanco import getSeries 

class HerrModel():
    
    @classmethod
    def get_herrms(self):
        try:
            connection=get_connection()
            herrms=[]
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, precio FROM herramientas ORDER BY nombre ASC")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    
                    herr=Herr(row[0],row[1],row[2],"{0:.2f}".format(getSeries(row[2])))
                    herrms.append(herr.to_JSON())
            connection.close()
            return herrms
                    
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def get_herr(self,id):
        try:
            connection=get_connection()
            
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, precio FROM herramientas WHERE id = %s",(id,))
                row=cursor.fetchone()
                
                herr=None
                if row != None:
                    herr=Herr(row[0],row[1],row[2],"{0:.2f}".format(getSeries(row[2])))
                    herr=herr.to_JSON()
                    
                    
            connection.close()
            return herr
                    
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def add_herr(self,herr):
        try:
            connection=get_connection()
            
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO herramientas (id, nombre, precio) VALUES (%s, %s, %s)", (herr.id,herr.nombre,herr.precio))
                affected_rows=cursor.rowcount
                connection.commit()
                
               
                    
                    
            connection.close()
            return affected_rows
                    
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def update_herr(self,herr):
        try:
            connection=get_connection()
            
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE herramientas SET nombre = %s, precio = %s WHERE id = %s", (herr.nombre,herr.precio, herr.id))
               
                affected_rows=cursor.rowcount
                connection.commit()
                    
            connection.close()
            return affected_rows
                    
        except Exception as ex:
            raise Exception(ex)
        
        
        
        
    @classmethod
    def delete_herr(self,herr):
        try:
            connection=get_connection()
            
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM herramientas WHERE id = %s", (herr.id,))
                affected_rows=cursor.rowcount
                connection.commit()
                
               
                    
                    
            connection.close()
            return affected_rows
                    
        except Exception as ex:
            raise Exception(ex)
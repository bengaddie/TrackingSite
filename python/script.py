import mysql.connector
from mysql.connector import errorcode

# Video Game Object 

class VideoGame():
    """ Video Game class stores videogames that are being tracked. """  
    Id = 0
    Name = ""

    def __init__(self, id, name):
          #super(VideoGame, self).__init__()
          self.Id = id
          self.Name = name         


def connectDB():
        try:
                cnx = mysql.connector.connect(user='bengaddi_admin', password='OG%XBmW#PT$5',
                              host='108.167.183.69',
                              database='bengaddi_tracker')
        except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                            print("Something is wrong with your user name or password")
                            print(err);
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)
        else:
                print("Connnection successful");
                cursor = cnx.cursor();
                query = ("SELECT ID, Name FROM vg");
                try:
                        cursor.execute(query);
                except Exception as e:
                        print("Error: " + e);
                else:
                    
                        for(ID, Name) in cursor:
                                print("ID: {}, Name: {}".format(ID, Name));
                                vgList = []
                                vgList.append(VideoGame(ID,Name))
                        g1 = vgList[0]
                        print(g1.Id)        

                # Close the cursor.              
                cursor.close()

        # Close the connection.
        cnx.close()     

connectDB()

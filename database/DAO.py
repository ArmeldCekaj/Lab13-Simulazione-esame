from database.DB_connect import DBConnect
from model.drivers import Drivers
from model.edges import Edges


class DAO():
    @staticmethod
    def getYear():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
                SELECT s.`year` as year
                FROM seasons s 
                order by s.`year` desc
                    """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row["year"])

        cursor.close()
        cnx.close()

        return result

    @staticmethod
    def get_nodes(idMap, year):
        cnx = DBConnect.get_connection()
        if cnx is None:
            raise RuntimeError("Connessione al DB fallita: controlla database/connector.cnf e import di GOsales.sql")
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT d.*
                    FROM drivers d, results r , races r2 
                    WHERE d.driverId = r.driverId 
                    AND r.raceId = r2.raceId 
                    AND r2.`year` = %s
                    AND r.`position` > 0 

                    """
        cursor.execute(query, (year,))
        for row in cursor:
            idMap[row["driverId"]] = Drivers(**row)
        cursor.close()
        cnx.close()
        return idMap

    @staticmethod
    def getAllEdges(idMap, year):
        cnx = DBConnect.get_connection()
        if cnx is None:
            raise RuntimeError("Connessione al DB fallita: controlla database/connector.cnf e import di GOsales.sql")
        cursor = cnx.cursor(dictionary=True)
        result = []
        query = """SELECT r.driverId as d1 ,r2.driverId as d2, COUNT(r.raceId) as n 
                    FROM results r ,results r2 , races rc
                    WHERE r2.raceId = rc.raceId 
                    AND r.raceId = rc.raceId 
                    AND rc.`year` = %s
                    AND r2.`position` > 0
                    AND r.`position` > 0
                    AND r.`position` > r2.`position` 
                    GROUP by r.driverId ,r2.driverId 
                    """

        cursor.execute(query, (year, ))

        for row in cursor:
            result.append(Edges(idMap[row['d1']],
                               idMap[row['d2']],
                               row['n']))

        cursor.close()
        cnx.close()
        return result

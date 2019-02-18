# queries to manage flights from DB
INSERT_FLIGHT_BY_NAME = """
            INSERT INTO flight () VALUES ();
            """

SELECT_FLIGHT_BY_NAME = """
            SELECT *
            FROM flight
            WHERE name LIKE '{flight_name}%';
            """

DELETE_FLIGHT_BY_NAME = """
            DELETE FROM flight
            WHERE name LIKE '{flight_name}%';
            """

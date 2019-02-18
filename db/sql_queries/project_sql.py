# queries to manage projects from DB
INSERT_PROJECT_BY_NAME = """
            INSERT INTO project () VALUES ();
            """

SELECT_PROJECT_BY_NAME = """
            SELECT *
            FROM project
            WHERE name LIKE '{project_name}%';
            """

DELETE_PROJECT_BY_NAME = """
            DELETE FROM project
            WHERE name LIKE '{project_name}%';
            """

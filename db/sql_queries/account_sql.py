# queries to manage accounts from DB
INSERT_ACCOUNT_BY_NAME = """
            INSERT INTO account () VALUES ();
            """

SELECT_ACCOUNT_BY_NAME = """
            SELECT *
            FROM account
            WHERE name LIKE '{account_name}%';
            """

DELETE_ACCOUNT_BY_NAME = """
            DELETE FROM account
            WHERE name LIKE '{account_name}%';
            """

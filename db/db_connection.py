import psycopg2

from db.statements import account_db_statement, project_db_statement, flight_db_statement


class DbConnection:

    def __init__(self, context):
        self.env = context.env
        self.conn = psycopg2.connect(host=self.env["db_host"],
                                     database=self.env["db_name"],
                                     port=self.env["db_port"],
                                     user=self.env["db_user"],
                                     password=self.env["db_pswd"])

    def close_conn(self):
        self.conn.close()

    # db cleanup before each test (deletion order is important, do not change without careful debugging)
    def cleanup_test_data_from_db(self):
        self.delete_all_flights_by_name_like("[AT] Flight")
        self.delete_all_projects_by_name_like("[AT] Project")
        self.delete_all_accounts_by_name_like("[AT] Account")

    # account table DB statements
    def insert_account(self, account_name):
        account_db_statement.insert_account(self.conn, account_name=account_name)

    def delete_all_accounts_by_name_like(self, account_name):
        account_db_statement.delete_all_accounts_by_name_like(self.conn,
                                                              account_name=account_name)

    def select_account_by_name(self, account_name):
        return account_db_statement.select_account_by_name(self.conn,
                                                           account_name=account_name)

    # project table DB statements
    def insert_project(self, project_name, account_name):
        project_db_statement.insert_project(self.conn,
                                            account_name=account_name,
                                            project_name=project_name)

    def delete_all_projects_by_name_like(self, project_name):
        project_db_statement.delete_all_projects_by_name_like(self.conn,
                                                              project_name=project_name)

    # flight table DB statements
    def insert_flight(self, flight_name, project_name):
        flight_db_statement.insert_flight(self.conn,
                                          flight_name=flight_name,
                                          project_name=project_name)

    def delete_all_flights_by_name_like(self, flight_name):
        flight_db_statement.delete_all_flights_by_name_like(self.conn,
                                                            flight_name=flight_name)

    def select_flight_by_name(self, flight_name):
        return flight_db_statement.select_flight_by_name(self.conn,
                                                         flight_name=flight_name)

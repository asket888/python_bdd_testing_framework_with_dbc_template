from hamcrest import assert_that, equal_to

from db.sql_queries import account_sql
from db.db_executor import execute_non_select_sql_query, execute_select_sql_query


# selects
def select_account_by_name(conn, account_name):
    return execute_select_sql_query(conn, account_sql.SELECT_ACCOUNT_BY_NAME
                                    .format(account_name=account_name))


# inserts
def insert_account(conn, account_name):
    delete_all_accounts_by_name_like(conn, account_name=account_name)
    execute_non_select_sql_query(conn, account_sql.INSERT_ACCOUNT_BY_NAME
                                 .format(account_name=account_name))
    assert_that(
        bool(select_account_by_name(conn, account_name=account_name)),
        equal_to(True),
        f"Account with '{account_name}' name wasn't created in DB"
    )


# deletes
def delete_all_accounts_by_name_like(conn, account_name):
    has_accounts = bool(select_account_by_name(conn, account_name=account_name))
    if has_accounts:
        execute_non_select_sql_query(conn, account_sql.DELETE_ACCOUNT_BY_NAME
                                     .format(account_name=account_name))
        assert_that(
            bool(select_account_by_name(conn, account_name=account_name)),
            equal_to(False),
            f"Account with '{account_name}' name wasn't deleted from DB"
        )

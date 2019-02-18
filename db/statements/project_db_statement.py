from hamcrest import assert_that, equal_to

from db.db_executor import execute_select_sql_query, execute_non_select_sql_query
from db.sql_queries import project_sql


# selects
def select_project_by_name(conn, project_name):
    return execute_select_sql_query(conn, project_sql.SELECT_PROJECT_BY_NAME
                                    .format(project_name=project_name))


# inserts
def insert_project(conn, account_name, project_name):
    delete_all_projects_by_name_like(conn, account_name)
    execute_non_select_sql_query(conn, project_sql.INSERT_PROJECT_BY_NAME
                                 .format(account_name=account_name,
                                         project_name=project_name))
    assert_that(
        bool(select_project_by_name(conn, project_name=project_name)),
        equal_to(True),
        f"Project with '{project_name}' name wasn't created in DB"
    )


# deletes
def delete_all_projects_by_name_like(conn, project_name):
    has_projects = bool(select_project_by_name(conn, project_name=project_name))
    if has_projects:
        execute_non_select_sql_query(conn, project_sql.DELETE_PROJECT_BY_NAME
                                     .format(project_name=project_name))
        assert_that(
            bool(select_project_by_name(conn, project_name=project_name)),
            equal_to(False),
            f"Project with '{project_name}' name wasn't deleted from DB"
        )

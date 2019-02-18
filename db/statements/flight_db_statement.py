from hamcrest import assert_that, equal_to

from db.db_executor import execute_select_sql_query, execute_non_select_sql_query
from db.sql_queries import flight_sql


# selects
def select_flight_by_name(conn, flight_name):
    return execute_select_sql_query(conn, flight_sql.SELECT_FLIGHT_BY_NAME
                                    .format(flight_name=flight_name))


# inserts
def insert_flight(conn, flight_name, project_name):
    delete_all_flights_by_name_like(conn, flight_name)
    execute_non_select_sql_query(conn, flight_sql.INSERT_FLIGHT_BY_NAME
                                 .format(flight_name=flight_name,
                                         project_name=project_name))
    assert_that(
        bool(select_flight_by_name(conn, flight_name=flight_name)),
        equal_to(True),
        f"Flight with '{flight_name}' name wasn't created in DB"
    )


# deletes
def delete_all_flights_by_name_like(conn, flight_name):
    has_flights = select_flight_by_name(conn, flight_name=flight_name)
    if has_flights:
        execute_non_select_sql_query(conn, flight_sql.DELETE_FLIGHT_BY_NAME
                                     .format(flight_name=flight_name))
        assert_that(
            bool(select_flight_by_name(conn, flight_name=flight_name)),
            equal_to(False),
            f"Flight with '{flight_name}' name wasn't deleted from DB"
        )

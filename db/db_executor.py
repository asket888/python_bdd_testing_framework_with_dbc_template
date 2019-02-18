import logging
import psycopg2

from psycopg2.extras import DictCursor

from utils.logging_util import LOGGER

LOGGER = logging.getLogger(__name__)


def execute_non_select_sql_query(conn, sql_query):
    try:
        with conn.cursor() as cur:
            cur.execute(sql_query)
            conn.commit()
            LOGGER.debug("Query to execute: " + str(cur.query.decode("utf-8")))
            LOGGER.debug("DB output: " + str(cur.statusmessage))
    except psycopg2.DatabaseError as error:
        LOGGER.error(error)


def execute_select_sql_query(conn, sql_query):
    try:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(sql_query)
            result = cur.fetchone()
            LOGGER.debug("Query to execute: " + str(cur.query.decode("utf-8")))
            LOGGER.debug("DB output: " + str(cur.statusmessage))
            LOGGER.debug("Query result set: " + str(result))
            return result
    except psycopg2.DatabaseError as error:
        LOGGER.error(error)

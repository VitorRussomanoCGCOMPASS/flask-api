""" Module containing all the SQL urls to further create engines """
import logging
from contextlib import contextmanager

import sqlalchemy
from sqlalchemy.engine import URL
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

CONNECTION_STRING = (
    "DRIVER={0};SERVER=" + "{1}" + ";DATABASE=" + "{2}"
)



urls = {

    "localdev": URL.create(
        "mssql+pyodbc",
        query={
            "odbc_connect": CONNECTION_STRING.format(
                "{SQL Server}", "DESKTOP-46RDGH3", "localdev"
            )
        },
    ),
    "testing": URL.create(
        "mssql+pyodbc",
        query={
            "odbc_connect": CONNECTION_STRING.format(
                "{SQL Server}", "DESKTOP-46RDGH3", "testing" 
            )
        },
    ),
}

class DatabaseNotRegistred(Exception):
    """
    This exception is raised when there is no database of that name
    registred

    Attributes
    --------
    message: str
        Explanation of the error
    """

    def __init__(self, message=None) -> None:
        if message is None:
            self.message = "There is not a database with that name registred."
            super().__init__(self.message)

    def __str__(self) -> str:
        return f"(Exception) {self.message}"


class Engine:
    """
    Methods
    ------
    create_engine: Creates an sqlalchelmy engine refering to the
    self.database
    """

    def __init__(self, database):
        self.database = database

    def create_engine(self):
        """
        Parameters
        ---------
        database: str
            Name of database

        Returns
        -------
        engine: sqlalchemy.engine
            If database is a valid database name, it returns the engine created

        DatabaseNotRegistred: Exception
            If database is not a valid database name, raises DatabaseNotRegistred instead
        """
        if self.database not in urls:
            raise DatabaseNotRegistred
        return sqlalchemy.create_engine(urls[self.database])


class EngineManager:
    """Manages all the Engines
    so that it allows for module level Engine usage
    that is way more efficient"""

    engines = {}

    @classmethod
    def get_engine(cls, database):
        """
        If there are no other engine
        refering to that database.
        Creates a new one refering to the database.

        Returns
        -------
        sqlalchemy.engine
        """
        if database not in cls.engines:
            cls.engines[database] = Engine(database).create_engine()
        return cls.engines[database]


@contextmanager
def session_manager(engine: Engine):
    """
    A context manager for sessions. Logs the errors as well.

    Parameters
    ----------
    engine : Engine
        sqlalchemy engine used to construct the session


    """
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    except SQLAlchemyError as exc:
        logging.error(exc.args)
        session.rollback()
        raise
    else:
        session.commit()
    finally:
        session.close()


# Sync

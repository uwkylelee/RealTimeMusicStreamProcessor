from typing import List, Dict, Type
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

from database_helper.models import Base

class PostgresDataManager:
    """
    A class for inserting and updating data in a PostgreSQL database using
    SQLAlchemy ORM.
    """

    def __init__(self, db_config: Dict[str, str]):
        """
        Initialize the database connection and session.

        :param db_config: A dictionary containing
        database connection parameters.
        """
        self.engine = create_engine(
            f"postgresql://"
            f"{db_config['user']}:"
            f"{db_config['password']}@"
            f"{db_config['host']}:"
            f"{db_config['port']}/"
            f"{db_config['database']}"
        )
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def close(self) -> None:
        """Close the session and connection."""
        self.session.close()
        self.engine.dispose()

    def get_new_session(self):
        return self.Session()

    def insert_record(self, model: Type[Base], record: Dict[str, any]) -> None:
        """
        Insert a single record into the specified table using the ORM model.

        :param model: The ORM model class corresponding to the table.
        :param record: A dictionary containing data for the single
        record to insert.
        """
        self.session = self.get_new_session()

        try:
            if 'created_timestamp' not in record:
                record['created_timestamp'] = datetime.utcnow()
            new_record = model(**record)
            self.session.add(new_record)
            self.session.commit()
            print(f"Successfully inserted a record into {model.__tablename__}.")
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error inserting record into {model.__tablename__}: {e}")
            raise
        finally:
            self.session.close()

    def insert(self, model: Type[Base], data: List[Dict[str, any]]) -> None:
        """
        Insert multiple records into the specified table using the ORM model.

        :param model: The ORM model class corresponding to the table.
        :param data: A list of dictionaries containing data for
        multiple records to insert.
        """
        self.session = self.get_new_session()

        try:
            for record in data:
                if 'created_timestamp' not in record:
                    record['created_timestamp'] = datetime.utcnow()
            self.session.bulk_insert_mappings(model, data)
            self.session.commit()
            print(
                f"Successfully inserted {len(data)} "
                f"records into {model.__tablename__}.")
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error inserting records into {model.__tablename__}: {e}")
            raise
        finally:
            self.session.close()

    def update(self, model: Type[Base], conflict_column: str,
               update_data: Dict[str, any]) -> None:
        """
        Update data in the specified table using the ORM model.

        :param model: The ORM model class corresponding to the table.
        :param conflict_column: The column to check for conflicts
        (usually the primary key).
        :param update_data: A dictionary containing the new data for the update.
        """
        self.session = self.get_new_session()

        try:
            record = self.session.query(model).filter(
                getattr(model, conflict_column) == update_data[
                    conflict_column]).one_or_none()
            if record:
                for key, value in update_data.items():
                    setattr(record, key, value)
                # Automatically update the modified_timestamp
                record.modified_timestamp = datetime.utcnow()
                print(
                    f"Updated record {conflict_column} ="
                    f" {update_data[conflict_column]}")
            else:
                print(
                    f"No record found with {conflict_column} ="
                    f" {update_data[conflict_column]}")
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error updating {model.__tablename__}: {e}")
            raise
        finally:
            self.session.close()

    def fetch_all(self, model: Type[Base]) -> List[Dict[str, any]]:
        """
        Fetch all records from the specified table using the ORM model.

        :param model: The ORM model class corresponding to the table.
        :return: A list of dictionaries representing all records in the table.
        """
        self.session = self.get_new_session()

        try:
            records = self.session.query(model).all()
            return [record.__dict__ for record in records if
                    "_sa_instance_state" in record.__dict__ and
                    record.__dict__.pop("_sa_instance_state")]
        except SQLAlchemyError as e:
            print(f"Error fetching records from {model.__tablename__}: {e}")
            raise
        finally:
            self.session.close()

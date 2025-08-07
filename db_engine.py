
import os
import sqlalchemy
import streamlit as st
import bcavault


def engine_oracle(db_user: str = "ciut") -> sqlalchemy.engine.base.Engine:
    """Baue eine Engine mittels SQLAlchemy für Oracle-Datenbanken.

    :param secret: Beinhaltet die secrets für die zu bauende Engine
    :returns: Eine SQLAlchemy-Engine
    """
    kv_engine = bcavault.KvSecretsEngine("analytics")
    secret = kv_engine.read(f"datse/vwh/{db_user}").to_dict()
    host = secret.get("host")
    port = secret.get("port")
    service = secret.get("service")
    user = secret.get("user")
    if db_user == "streamlit":
        password = os.getenv("ORACLE_STREAMLIT_PW")
    else:
        password = secret.get("password")

    connection_string = (
        f"oracle+oracledb://{user}:{password}@{host}:{port}/?service_name={service}"
    )
    engine = sqlalchemy.create_engine(connection_string)
    return engine

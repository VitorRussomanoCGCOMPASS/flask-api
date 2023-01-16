import json
from marshmallow import ValidationError
from api.schemas.indexes import IndexValuesSchema
from api.models.indexes import Indexes 

from api.config import Config
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

import http.client


def main():
    conn = http.client.HTTPSConnection("dashboard.jgp.com.br")

    payload = ""

    headers = {
        'Accept': "application/json, text/plain, */*",
        'Origin': "https://www.jgp.com.br",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
        }

    conn.request("GET", "/api/graphlist?l=pt&period=all-time", "payload", headers) # type: ignore
    res = conn.getresponse()
    data = res.read()

    graph_data = json.loads(data.decode('utf-8'))[0].get('data').get("graph")[0]

    if graph_data('name') == 'Rentabilidade acumulada':
        json_data  = json.loads(graph_data.get('json')).get("data")[1]
        if json_data.get("name") == "IDEX":
            x = json_data.get("x")
            y = json_data.get("y")
            return [x[-1], y[-1]]
        raise ValidationError(
                f"Jpg idex was expected. Received:{json_data.get('name')}"
            )
    raise ValidationError(
            f"Was expecting Rentabilidade acumulada. Received :{graph_data.get('name')}"
        )


if __name__ == "__main__":
    date, value = main()
    

    some_engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

    session_factory = sessionmaker(bind=some_engine)

    Session = scoped_session(session_factory)

    with Session() as session:
        jpg_idex = Indexes.query.filter_by(index='JPG Idex').one_or_none()
        
        data = {"value": value, "date": date, "index": jpg_idex} 

        jpg_idex =  IndexValuesSchema(session=session).load(data)
        session.add(jpg_idex)
        session.commit()

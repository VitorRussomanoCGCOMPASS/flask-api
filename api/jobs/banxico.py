
from api.jobs.getrequest import get_request
from api.schemas.currency import CurrencyValuesSchema
from dateparser import parse
from marshmallow import pre_load
from api.config import Config
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine


class BanxicoCurrencySchema(CurrencyValuesSchema):
    @pre_load
    def pre_loader(self, data, many, **kwargs):
        if "fechaEn" in data:
            date = parse(data["fechaEn"])
            if date is not None:
                value = float(data["valor"])
                return {
                    "date": str(date.date()),
                    "value": value,
                    "currency": {"id": 10, "currency": "MXNUSD"},
                }

# TODO :  DEAL WITH HOLIDAYS

def upload_banxico():
    
    some_engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

    session_factory = sessionmaker(bind=some_engine)

    Session = scoped_session(session_factory)

    response_banxico = get_request(
    host="www.banxico.org.mx",
    url="/canales/singleFix.json",
    headers={
        "cookie": "TS604574e3027=083fd6a492ab200039f8ed74dad9278f84898a6fe9d5ed66124e54de667d377eadcf02425c7ab03f081cbff094113000d7a4854dfd9d8b544088c674d82894c64ede3290cd655a9ca6c25c83debe20d5cb318b0fc6e16ee189c108166a165669; TS012f422b=01ab44a5a8accaecedd9fb0ad39686ec46b4d600b5e5fe33d2e63eb1e786dffb8d9a6af296eaee992ffcfa1f98210f1732a79bec44b0e16d6cdfa2dd4777018d9d71e287e06f8ba71977e3428e697851a42f777a89e49a4b4833b4532f315c3269725ec6d3",
        "Cookie": "Hex1580S1680=\u0021acl2tUbI4fj0uV/405nf5XFqnQVk9C1MUeQvh0PgwCDJ2B4UB8hlT47aImHjDvQ5MUxpTNmzSizOseg=; SRVCOOKIE=\u0021oNDaBJcs6TfCT7L405nf5XFqnQVk9O2+9+DZPxHSyQWBYWEqoouD8222uOR8acIAg8f0rn1Yh6KsUh0=; TS012f422b=01ab44a5a8329ced3dfc3185d064be0b73f093cf659e2e4e4ce17b3507291da73debcfd39b9da983c16ed8a07797a3e6c725d603266a6fc3c087d112be0f330b9bbec311ba7cbf091fee45af6f0aa5e2eaf3c950a2a1c5a7b8802c169e9de72b8a195542da; TS604574e3027=083fd6a492ab2000cb38b4d8e980ea2cae1e6a995b1b0c93d3e9ae2e4280a5a6aa2896a35d8d533608e76de9c01130001e83e9d1abe77da08a7d68c07541a747a2e105daf8aa58a34ed3e3151e09728ffef35505dd6f65b900bc9421a8dd0e80",
    },
    )

    exchange_fix = BanxicoCurrencySchema().loads(response_banxico) # type: ignore
    
    with Session() as session:
        session.add_all(exchange_fix)
        session.commit()


if __name__ == '__main__':
    upload_banxico()




from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from config import db, ma

class Quotes(db.Model):
    __tablename__ = 'quotes'
    id: Mapped[int] = mapped_column(primary_key=True)
    quote: Mapped[str]
    movie: Mapped[str] = mapped_column(String(50))
    keywords: Mapped[str]


class QuotesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quotes
        load_instance = True
        sqla_session = db.session

quote_schema = QuotesSchema()
quotes_schema = QuotesSchema(many=True)
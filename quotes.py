from flask import make_response, abort
from config import db
from models import Quotes, quotes_schema, quote_schema
from sqlalchemy import func
from flask import jsonify

def get_all_quotes():
    quotes = Quotes.query.all()
    serialized = quotes_schema.dump(quotes)
    return jsonify(serialized)
    

def get_random_quote(limit):
    quotes = Quotes.query.order_by(func.random()).limit(limit).all()
    if len(quotes) == 1:
        # return one quote
        
        return quote_schema.dump(quotes)
    
    #return a list of quotes
    return quotes_schema.dump(quotes)

def get_quote_by_movie(movie):
    quotes_by_movie = Quotes.query.filter(Quotes.movie.ilike(f"%{movie}%")).all()
    return quotes_schema.dump(quotes_by_movie)

def search_quote_by_keyword(keyword):
    quotes_by_keyword = Quotes.query.filter(Quotes.keywords.ilike(f"%{keyword}%")).all()
    if len(quotes_by_keyword) == 1:
        return quote_schema.dump(quotes_by_keyword[0])
    elif len(quotes_by_keyword) > 1:
        return quotes_schema.dump(quotes_by_keyword)
    else:
        abort(404, f"Quote with associated keyword {keyword} not found")
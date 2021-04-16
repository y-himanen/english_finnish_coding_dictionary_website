from app import db
from app.static.text.text import eng_dict, fin_dict


def get_entry(word, route):
    word = word.strip().lower()
    search = "%{}%".format(word)
    results = []
    lang_dict = check_route(route)
    try:
        query = db.session.query(Entry).filter(Entry.eng.ilike(search)).all()
        for row in query:
            fin = row.fin
            eng = row.eng
            results.append(eng + "  :  " + fin)
        if not query:
            query = db.session.query(Entry).filter(Entry.fin.ilike(search)).all()
            for row in query:
                eng = row.eng
                fin = row.fin
                results.append(fin + "  :  " + eng)
        if not results:
            results = lang_dict['no_entry']
    except Exception:
        results = lang_dict['tech_difficulties']
    finally:
        return results


def check_route(route):
    if route == 'fin':
        return fin_dict
    else:
        return eng_dict


class Entry(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    eng = db.Column(db.String(100))
    fin = db.Column(db.String(100))

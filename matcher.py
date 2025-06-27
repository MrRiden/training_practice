from tinydb import TinyDB
import os
from validators import detect_type

def match_template(query_fields):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "db.json")
    
    with open(db_path, "r", encoding="utf-8") as f:
        data = f.read()
        print("DEBUG: Содержимое db.json:")
        print(data)
    
    db = TinyDB(db_path)
    templates = db.all()
    print("DEBUG templates:", templates)

    query_types = {k: detect_type(v) for k, v in query_fields.items()}

    for template in templates:
        tpl_name = template["name"]
        required_fields = {k: v for k, v in template.items() if k != "name"}

        if all(
            field in query_types and query_types[field] == field_type
            for field, field_type in required_fields.items()
        ):
            return tpl_name

    return query_types

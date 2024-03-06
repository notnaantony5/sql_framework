import sqlite3


class BaseColumn:
    value: object


class Integer(BaseColumn):
    value: int


class String(BaseColumn):
    value: str

TYPES = {
    Integer: "INTEGER",
    String: "VARCHAR(50)"
}
class Model:
    db_name = "db.sqlite3"
    def __create_table(self):
        fields = []
        for name, _type in self.__annotations__.items():
            if issubclass(_type, BaseColumn):
                fields.append(f"{name.lower()} {TYPES[_type]}")
        tablename = self.__name__.lower()
        query = (f"CREATE TABLE IF NOT EXISTS "
                 f"{tablename} ( "
                 f"id INTEGER PRIMARY KEY AUTOINCREMENT,"
                 f"{', '.join(fields)}"
                 f" )")
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()


def run():
    for model in Model.__subclasses__():
        model._Model__create_table(model)

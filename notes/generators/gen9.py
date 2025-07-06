def ResultGenerator(cursor, batchsize=1000):
    while True:
        results = cursor.fetchmany(
            batchsize
        )  # buforowanie - połączenie do bazy raz na jakiś czas
        if not results:
            break
        for result in results:  # procesowanie
            yield result


db = MySQLdb.connect(host="localhost", user="root", passwd="Pasikonik666", db="domains")
cursor = db.cursor()

generator = ResultGenerator(cursor)

for record in generator:
    doSomethingWith(record)
db.close()

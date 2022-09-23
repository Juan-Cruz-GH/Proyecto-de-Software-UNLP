import psycopg2
import psycopg2.extras
class Issue:
    def getAll(self):
        conn = psycopg2.connect(
        host="localhost",
        database="Test",
        user="postgres",
        password="proyecto")
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute('select * from issues')
        issues = cur.fetchall()
        print(issues)
        cur.close()
        conn.close()
        return issues

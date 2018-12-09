'# Python --Version --> 3.6.2'
import psycopg2

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)
c = db.cursor()

print('')
print('1- What are the most popular three articles of all time?')
c.execute("select articles.title,\
           count(log.id) as Access_number \
           from articles left join log\
           on log.path like '%' || articles.slug\
           group by articles.title\
           order by Access_number desc\
           limit 3 ")

Articlas = c.fetchall()
for Artical in Articlas:
    print(Artical[0] + ' -- ' + str(Artical[1]) + ' views')
db.close()

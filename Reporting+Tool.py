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

print('')
print('2-  Who are the most popular article authors of all time?')
c.execute("select AA.name, Sum(ViewCount) as Page_views\
           from\
             (select authors.name,articles.slug\
              from authors, articles\
              where authors.id = articles.author)AA\
          left join \
             (select articles.slug, count(log.ip) as ViewCount\
              from articles, log\
              where log.path like '%' || articles.slug\
              group by articles.slug)AV\
          on AA.slug = AV.slug\
          group by AA.name\
          order by Page_views desc")

authors = c.fetchall()
for author in authors:
    print(author[0] + ' -- ' + str(author[1]) + ' views')
db.close()

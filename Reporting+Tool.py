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

print('')
print('3- On which days did more than 1% of requests lead to errors? ')
'#1 get Total number of all requests per day and save the result in view'
c.execute("create view AllRequests as\
           select date(time) as date, Count(Status) as requests\
           from log\
           group by date")

'#2 get the total number of Error Request per day and save the result in view'
c.execute("create view ErrorRequests as \
           select date(time) as date, count(status) as Error_requests\
           from log\
           where (status like '4%' or status like '5%')\
           group by date\
           order by date")

'#3 Join Both Views to Calculate the percentage of Error'
c.execute("select TO_CHAR(AllRequests.date,'Monthdd,yyyy') as RequestsDate,\
           AllRequests.Requests, ErrorRequests.Error_Requests , \
           round(((cast(ErrorRequests.Error_Requests as decimal)\
           /AllRequests.requests)*100),2)as Error_Percentage \
           from AllRequests, ErrorRequests\
           where  AllRequests.date =  ErrorRequests.date\
           and  (round(((cast(ErrorRequests.Error_Requests as decimal)\
           /AllRequests.requests)*100),2) > 1 )\
           order by ErrorRequests.Error_Requests desc")

Joined_Status = c.fetchall()
for JS in Joined_Status:
    print(str(JS[0]) + ' -- ' + str(JS[3]) + '% errors')
print('')

db.close()

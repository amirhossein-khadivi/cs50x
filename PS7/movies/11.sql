select title from movies
       join ratings on movies.id = ratings.movie_id
       where id in(select stars.movie_id from stars
                           where person_id in (select id from people where name like 'Chadwick Boseman'))
        order by rating desc limit 5;
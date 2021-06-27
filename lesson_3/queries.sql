select parent_id, sum(budget) from movies
where budget is not null and budget <> 0
group by parent_id
order by 2 desc;


select m.name, mc.country from movies m
left join movie_countries mc on m.id = mc.movie_id;


select mc.country, count(m.id) from movies m
left join movie_countries mc on m.id = mc.movie_id
group by mc.country;


select name, rank() over (order by cnt desc)
from
    (select p.name, count(p.name) as cnt
     from movies m
              join casts c on m.id = c.movie_id and c.job_id=15
              left join people p on c.person_id = p.id
     where m.date > now()
     group by p.name)t1;


SELECT 1
UNION
SELECT 2
UNION
SELECT 1;

SELECT 1
UNION ALL
SELECT 1;


select person_id, CASE WHEN job_id = 21 THEN 'Director' ELSE 'Actor' END as job_name, count(*) from casts
where job_id in (21, 15)
group by person_id, job_id
order by person_id;


select distinct m.id, count(*) from movies m
left join casts c on m.id = c.movie_id
group by m.id
order by 2 desc;


select distinct m.id, count(*) as cnt from movies m
left join casts c on m.id = c.movie_id
group by m.id
having count(*) > 100
order by 2 desc;
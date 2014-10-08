SELECT * FROM 
lab_data l
INNER JOIN pat_data p ON l.patient = p.patient
#INNER JOIN vis_data v ON l.patient = v.patient
;

create table lab_data2 like lab_data;
insert into lab_data2 
select * from lab_data order by patient limit 1000;
select * from lab_data2;

create table pat_data2 like pat_data;
insert into pat_data2
select * from pat_data order by patient limit 1000;
select * from pat_data2;

create table vis_data2 like vis_data;
insert into vis_data2
select * from vis_data order by patient limit 1000;
select * from vis_data2;


select * 
INTO OUTFILE '/tmp/tmp.csv'
  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
from lab_data2 l
INNER JOIN pat_data2 p on l.patient = p.patient
INNER JOIN
    (
        SELECT patient, MAX(weight) maxweight, MAX(height) maxheight
        FROM vis_data2
        GROUP BY patient
    ) v ON l.patient = v.patient
;

select * 
INTO OUTFILE '/tmp/tmp.csv'
  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
from lab_data l
INNER JOIN pat_data p on l.patient = p.patient
INNER JOIN
    (
        SELECT patient, MAX(weight) maxweight, MAX(height) maxheight
        FROM vis_data
        GROUP BY patient
    ) v ON l.patient = v.patient
;
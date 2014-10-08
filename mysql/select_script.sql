SELECT * FROM 
lab_data l
INNER JOIN pat_data p ON l.patient = p.patient
INNER JOIN vis_data v ON l.patient = v.patient
;
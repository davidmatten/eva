CREATE TABLE lab_data (
id INT NOT NULL AUTO_INCREMENT,
X INT NOT NULL,
merge_no INT NOT NULL,
cohort VARCHAR(255) NULL,
patient VARCHAR(255) NULL,
lab_dmy DATE NULL,
lab_id VARCHAR(255) NULL,
lab_v VARCHAR(255) NULL,
unit_txt VARCHAR(255) NULL,
lab_t VARCHAR(255) NULL,
rna_l VARCHAR(255) NULL,
tb_drug VARCHAR(255) NULL,
drug_res VARCHAR(255) NULL,
PRIMARY KEY (id)
);


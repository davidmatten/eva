ALTER TABLE `Eva`.`lab_data` 
ADD INDEX `secondary` (`patient` ASC) ;

ALTER TABLE `Eva`.`pat_data` 
ADD INDEX `secondary` (`patient` ASC) ;

ALTER TABLE `Eva`.`vis_data` 
ADD INDEX `secondary` (`patient` ASC) ;

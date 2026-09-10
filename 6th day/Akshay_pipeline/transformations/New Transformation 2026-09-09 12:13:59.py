
create streaming table dev.akshay_bronze.sales_pl as
select *,current_date() as current_date, _metadata.file_name  from stream read_files("/Volumes/dev/akshay/akshay_volume/months/months/");
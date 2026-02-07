create catalog iceberg with (
    'type' = 'iceberg',
    'catalog-type' = 'hadoop',
    'warehouse' = 's3a://data-bucket/warehouse'
);

create database if not exists iceberg.dl;

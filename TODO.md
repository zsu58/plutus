# TODOs

## Must
* Airflow
* Big data (parallel processing)
* Compaction
* Flink Resource Management/Configuration
* Test mini-batch processing for performance of UDFS
* K8S
* Catalog
* When to use specific-offset?
    * When the Flink State (Checkpoints/Savepoints) becomes corrupted or is accidentally deleted from your storage
    * Reprocessing the data due to logic change/bug
    * Initialization of the data is done using different framework(e.g. spark)

## Optional
* Paimon?
* Kafka (as buffer??)
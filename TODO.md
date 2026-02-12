* JAVA format
* Airflow
* k8s
* maven -> gradle
* Big data (parallel processing)
* when to use specific-offset?
    * when the Flink State (Checkpoints/Savepoints) becomes corrupted or is accidentally deleted from your storage
    * reprocessing the data due to logic change/bug
    * initialization of the data is done using different framework(e.g. spark)
* Compaction
* Paimon
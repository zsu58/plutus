import org.apache.flink.table.api.*;

public class MySQL2Iceberg {
    public static void main(String[] args) {
        // 1. Capture arguments
        // String targetRegion = args[0];
        // String startTime = args[1];

        // 2. Initialize the environment
        EnvironmentSettings settings = EnvironmentSettings.newInstance().inStreamingMode().build();
        TableEnvironment tEnv = (TableEnvironment.create(settings));

        // 3. Enable Checkpointing (Critical for Iceberg)
        tEnv.getConfig().getConfiguration().setString("execution.checkpointing.interval", "10s");

        // 4. Define MySQL CDC Source
        tEnv.executeSql("""
            create table messages (
                id int,
                chat_id int,
                chat_title string,
                sender_id string,
                sender_username string,
                text string,
                `timestamp` timestamp(0),
                primary key (id) not enforced
            ) with (
                'connector' = 'mysql-cdc',
                'hostname' = 'plutus_db',
                'port' = '3306',
                'username' = 'plutus',
                'password' = 'plutus',
                'database-name' = 'plutus',
                'table-name' = 'messages',
                'scan.startup.mode' = 'initial'
            )
        """);

        // 5. Create Iceberg Catalog
        tEnv.executeSql("""
            create catalog iceberg with (
                'type' = 'iceberg',
                'catalog-type' = 'hadoop',
                'warehouse' = 's3a://data-bucket/warehouse'
            )
        """);

        // 6. Create Database and Table in Iceberg (if not exists)
        tEnv.executeSql("create database if not exists iceberg.dl");
        tEnv.executeSql("""
            create table if not exists iceberg.dl.messages (
                id int,
                chat_id int,
                chat_title string,
                sender_id string,
                sender_username string,
                text string,
                `timestamp` timestamp(0),
                primary key (id) not enforced
            )
        """);

        // 7. Execute the Insert (Streaming Job)
        tEnv.executeSql("""
            insert into iceberg.dl.messages
            select * from messages
        """);


        // 8. Stop the job with savepoint (triggered outside of the job)
        // flink stop -p --savepointPath s3a://flink-bucket/savepoints/dl/messages {{ job_id }}

        /*

        // 1. Capture arguments from Airflow
        String targetRegion = args[0];
        String startTime = args[1];

        // 2. Initialize the environment
        EnvironmentSettings settings = EnvironmentSettings.newInstance().inStreamingMode().build();
        TableEnvironment tEnv = TableEnvironment.create(settings);

        // 3. Register Hive Catalog (for Hive UDFs and Dimension tables)
        tEnv.executeSql("CREATE CATALOG my_hive WITH ('type'='hive', 'hive-conf-dir'='/opt/flink/conf')");
        tEnv.useCatalog("my_hive");
        // 4. Define Source & Sink (same DDL syntax as SQL API)
        tEnv.executeSql("CREATE TABLE mysql_source (...) WITH ('connector'='mysql-cdc', ...)");
        tEnv.executeSql("CREATE TABLE iceberg_sink (...) WITH ('connector'='iceberg', ...)");

        /// 5. Build the transformation programmatically
        Table orders = tEnv.from("mysql_source");
        Table users = tEnv.from("hive_users");
        // Example of Performing Join and using Hive UDF
        Table result = orders
            .join(users).where($("customer_id").isEqual($("id")))
            .filter($("order_date").isGreaterOrEqual(startTime))
            .select(
                $("id"),
                call("my_hive_udf", $("price")).as("final_price"), // Hive UDF call
                $("region")
            )
            .filter($("region").isEqual(targetRegion)); // Dynamic Filter

        // 6. Execute the insert
        result.executeInsert("iceberg_sink");
    */
    }
}
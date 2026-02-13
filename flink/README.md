# Flink Job Development Guide

## 1. Prerequisites
- Java 17
- Maven 3.8+

## 2. Project Structure
```text
flink/
├── pom.xml                 # Maven configuration for Flink Job
├── src/
│   └── main/
│       └── java/
│           └── com/
│               └── dev/
│                   └── *.java  # Flink Job code
└── target/                   # Output JARs
```

## 3. Code Formatting (Spotless)
We use **Spotless** to enforce Google Java Style.

**Auto-fix formatting:**
```bash
mvn spotless:apply
```

**Check formatting:**
```bash
mvn spotless:check
```

> **Note:** Run `mvn spotless:apply` before pushing code to avoid CI failures.

## 4. Building the JAR
To compile your Java code and create a Flink Job JAR:

```bash
mvn clean package
```

**Output:**
The built JAR will be located at:
`target/flink-s3-iceberg-cdc-1.0.jar`

## 5. Running the Job
You can submit the JAR to your Flink cluster:

```bash
flink run -c MySQL2Iceberg target/flink-s3-iceberg-cdc-1.0.jar
```

## 6. Stoping and Restarting the Job (Savepoint)

```bash
# stop, TODO: need to add datetime
flink stop --type canonical --savepointPath s3a://flink-bucket/savepoints/dl/messages/ {job_id}

# restart, TODO: need to add datetime
flink run -s s3a://flink-bucket/savepoints/dl/messages/savepoint-{id} -c MySQL2Iceberg target/flink-s3-iceberg-cdc-1.0.jar
```

## 7. Restarting the Job (Checkpoint)
```bash
flink run -s s3a://flink-bucket/checkpoints/dl/messages/{job_id}/chk-{id} -c MySQL2Iceberg target/flink-s3-iceberg-cdc-1.0.jar
```
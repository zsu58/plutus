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
│           └── *.java  # Your Flink Job code
└── jobs/                   # (Optional) SQL scripts or output JARs
```

<!-- ## 3. Code Formatting (Spotless)
We use **Spotless** to enforce Google Java Style.

**Check formatting:**
```bash
mvn spotless:check
```

**Auto-fix formatting:**
```bash
mvn spotless:apply
```

> **Note:** Run `mvn spotless:apply` before pushing code to avoid CI failures. -->

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
flink run -c MySQL2IcebergInitTest target/flink-s3-iceberg-cdc-1.0.jar
```

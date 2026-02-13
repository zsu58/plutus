# 1. Use Maven instead of Gradle

Date: 2026-02-13

## Status
Accepted

## Context
We need to choose a build tool for our Flink jobs. The two main contenders are Maven and Gradle. While Gradle offers conciseness and speed, we need to consider the ecosystem support for Apache Flink.

## Decision
We will use **Maven**.

## Reasoning
1.  **Flink's Native Tool:** Apache Flink itself is built with Maven. The official documentation, examples, and Quickstart guides primarily support Maven.
2.  **Archetypes:** Flink provides official Maven Archetypes to generate correctly configured project skeletons.
3.  **Dependency Management:** Maven's `<scope>provided</scope>` mechanism aligns perfectly with Flink's requirement to exclude core libraries from the job JAR.
4.  **Shading Support:** The `maven-shade-plugin` is the standard way to build Flink "Fat JARs" and handles relocation (to avoid dependency conflicts) in a way that is well-documented for Flink.

## Consequences
- We will use `pom.xml` for build configuration.
- We will use the `maven-shade-plugin` for creating job JARs.
- We will follow Flink's standard project structure.

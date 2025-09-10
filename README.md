# 🛡️ AWS Cloud Cost Guardian

Automates the collection and ingestion of detailed AWS cost and usage data into New Relic, enabling enhanced cloud cost monitoring, real-time alerting, and powerful visualization.

## 📌 Overview

This project fetches daily unblended AWS cost data using the AWS Cost Explorer API, groups it by service and region, and sends the data as custom events to New Relic.

With this integration, you can:
- Monitor cloud spend in real-time.
- Set up alerts for unexpected spikes.
- Visualize costs by region/service.
- Optimize your AWS usage with data-driven insights.

## ✨ Features

- ✅ Automated daily cost retrieval for the past 365 days (configurable).
- ✅ Cost data grouped by AWS service and region.
- ✅ Output as newline-delimited JSON (NDJSON) for smooth Flex ingestion.
- ✅ Handles long date ranges with chunked queries.
- ✅ Includes New Relic Flex YAML config for scheduling ingestion.
- ✅ Easy-to-build New Relic dashboards using NRQL queries.

## 🏗️ Architecture

- +------------------------+
- | AWS Cost Explorer API |
- +----------+-------------+
-           |
-           v
- +---------------------------+
- | awscostfetcher.py (Python)|
- +---------------------------+
-           |
-           v
-  NDJSON events (daily cost)
-           |
-           v
- +---------------------------+
- | New Relic Flex Integration|
- +---------------------------+
-            |
-            v
- +---------------------------+
- |  New Relic Custom Events  |
- |      (eventType: CloudCost)|
- +---------------------------+
-            |
-            v
- +---------------------------+
- | New Relic Dashboards & Alerts |
- +---------------------------+

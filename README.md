# 🛡️ Cloud Cost Guardian

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

## 🔐 IAM Role Setup

The EC2 instance where Flex is running should have an IAM Role attached that allows it to query AWS APIs.
This IAM role should have permissions such as:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

## 🔧 Prerequisites

- EC2 instance with IAM role attached.
- Python3 installed with required libraries.
- New Relic account.

## 🛠️ Installation & Setup Instructions
- Install the New Relic Infrastructure Agent.
- Deploy Flex configuration.
  Files are placed at the following paths. 
```bash
 /etc/newrelic-infra/integrations.d/cloudcost.yml
```
- Python script is placed at the following which pulls the AWS cost fetcher.
```bash
/etc/newrelic-infra/integrations.d/cloudcost.yml
```
- Test script to validate the output.
```bash
python3 /opt/cloudcost/scripts/awscostfetcher.py
```

## 📈 Sample NRQL Queries

- please run the following NR Query to see if custom metric is ingested to New Relic.
```sql
SHOW eventTypes
```
- Basic NRQL Query to pull customized metrics
```sql
SELECT max(dailyCost) FROM CloudCost SINCE 1 day ago FACET service
```
```sql
SELECT max(dailyCost) FROM CloudCost SINCE 1 day ago FACET service
```


## 🚀 Scalability & Future Scope

This solution is designed to scale beyond just cost data ingestion. It can be extended to include detailed insights into all AWS services in your subscription, such as:
- Number of active EC2 instances and their statuses
- Cluster details for ECS, EKS, and other container services
- Usage metrics for services like RDS, Lambda, S3, and more
- By leveraging New Relic Flex’s custom integrations, this platform can evolve into a comprehensive cloud resource and cost monitoring system, providing holistic visibility and enabling more granular optimization across your entire AWS environment.

## 🗺️ Multi-Cloud Implementation

Yes! Cloud Cost Guardian can be extended to Azure, GCP, and IBM Cloud because:
- All major clouds provide cost and usage APIs (Azure Cost Management API, GCP Billing API, IBM Cloud Usage Reports).
- You can write similar ingestion scripts for those APIs.
- New Relic Flex supports custom integrations, so you can collect data from any cloud provider.
- This enables a multi-cloud cost monitoring solution.

## 🙏 Conclusion

Cloud Cost Guardian empowers teams to take control of their AWS cloud spending through automated cost and usage monitoring, real-time alerts, and insightful visualizations within New Relic. By extending this foundation, organizations can achieve comprehensive cost governance and operational visibility across their entire cloud environment.

Feel free to contribute, raise issues, or suggest enhancements to help evolve this project further.



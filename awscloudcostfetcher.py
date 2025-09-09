from datetime import datetime, timedelta
import boto3, json

def to_kebab_case(s):
    return s.lower().replace(" ", "-")

client = boto3.client("ce", region_name="us-east-1")
end = datetime.utcnow().date()
start = end - timedelta(days=365)  # last 365 days

resp = client.get_cost_and_usage(
    TimePeriod={"Start": start.isoformat(), "End": end.isoformat()},
    Granularity="DAILY",
    Metrics=["UnblendedCost"],
    GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"},
             {"Type": "DIMENSION", "Key": "REGION"}
    ]
)

cost_data = []
for result in resp["ResultsByTime"]:
    date = result["TimePeriod"]["Start"]
    for group in result["Groups"]:
        service = to_kebab_case(group["Keys"][0])
        region = group["Keys"][1]
        amount = float(group["Metrics"]["UnblendedCost"]["Amount"])
        cost_data.append({
            "event_type": "CloudCost",
            "provider": "AWS",
            "service": service,
            "region": region,
            "dailyCost": round(amount, 2),
            "timestamp": f"{date}T00:00:00Z"
            })

print(json.dumps(cost_data))

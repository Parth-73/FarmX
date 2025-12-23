📌 Purpose

Google Sheets is used in FarmX as a lightweight cloud database to log mission data, enabling:

Easy monitoring of drone operations

Transparent reporting for farmers and judges

Quick analytics without heavy backend setup

🧠 Why Google Sheets?

Simple, real-time data logging

Easy integration with Python

Cloud-hosted and shareable

Ideal for MVP and demos

🧪 Use Case in FarmX

Google Sheets stores:

Mission ID

Date & time

Field location

Area covered

Number of weeds detected

Number of spray actions

Herbicide usage estimate

Mission status

📂 Sheet Structure (Columns)
Column Name	Description
Mission_ID	Unique mission identifier
Timestamp	Date & time of mission
Field_Name	Farmer-defined field name
Latitude	Field center latitude
Longitude	Field center longitude
Weeds_Detected	Total weeds detected
Sprays_Executed	Total spray actions
Herbicide_ml	Estimated herbicide used
Area_m2	Area covered
Mission_Status	Completed / Aborted
⚙️ Integration Workflow
1️⃣ Authentication

Google Service Account is used

Credentials stored securely (not in GitHub)

2️⃣ Python Logging Logic (Concept)
import gspread
from oauth2client.service_account import ServiceAccountCredentials


Steps:

Authenticate using service account

Open target Google Sheet

Append a new row after each mission

3️⃣ Example Log Entry
Mission_ID: FX_2025_001
Timestamp: 2025-01-15 14:30
Field_Name: Maize Plot A
Weeds_Detected: 37
Sprays_Executed: 35
Herbicide_ml: 12.4
Mission_Status: Completed

🔁 Role in FarmX Pipeline
Drone Mission Execution
        ↓
AI Weed Detection
        ↓
Spray Action
        ↓
Mission Summary
        ↓
Google Sheets Logging
# Mini Information System Proposal: Banana Farmers in Panabo City

## Recommended Theme

**Agriculture — Banana Farm Monitoring and Assistance System**

Agriculture is the better choice for this project because banana production is strongly associated with Panabo City and Davao del Norte, while documented local concerns include banana diseases, production losses, financial difficulties, and limited access to support and training. Panabo's City Agriculture Office has also conducted local efforts to address Fusarium wilt in banana farms. 

## Suggested System Title

**BananaCare: A Banana Farm Monitoring and Farmer Assistance Information System for Panabo City**

### One-sentence title summary
A simple information system that helps banana farmers in selected areas of Panabo City record farm conditions, monitor banana problems, and keep track of assistance or recommended actions.

## Target Location

The project should be limited to **Panabo City, Davao del Norte**.

For a manageable study area, you can focus on selected banana-growing barangays such as:

- **Barangay Kasilak** — local records identify Cavendish banana as a major agricultural crop, with individual growers and planters.
- **Barangay Little Panay** — the Panabo City Agriculture Office conducted a Fusarium wilt mitigation trial involving Cavendish banana.
- **Barangay Tibungol** — a local study documented banana growers dealing with the financial costs and challenges associated with Sigatoka disease.

You do not need to cover the entire city; choosing one or two barangays would make the mini-system easier to develop and test.

## Main Problem

**One-sentence problem summary:** Banana farmers may have difficulty keeping organized records of farm conditions, disease incidents, production information, and assistance needs, making it harder to monitor problems and respond systematically.

Local evidence supports the relevance of this problem: studies involving Panabo banana growers report difficulties related to disease, weather, soil conditions, production, and financial costs, while regional stakeholders identify Fusarium wilt, rising production costs, and difficulty replacing affected farm areas as major banana-industry challenges.

## Proposed 3 Functions

Keep the system small so it remains realistic for a student information-system project.

### 1. Farm and Farmer Record Management
- Register farmer information.
- Record farm location/barangay.
- Record farm size and banana variety.
- Store basic planting and production information.
- View and update farmer/farm records.

**Function summary:** Maintains a centralized digital record of banana farmers and their basic farm information.

### 2. Disease and Farm Condition Monitoring
- Record disease or pest observations.
- Select the observed problem, such as Fusarium wilt, Sigatoka, pest infestation, or other farm issues.
- Record date, affected area, and notes.
- Set a simple status such as **Reported, Under Monitoring, or Resolved**.
- View previous reports for a farmer/farm.

**Function summary:** Allows farmers or authorized staff to document and monitor banana diseases and other farm problems.

### 3. Assistance and Recommendation Tracking
- Record assistance requested or provided.
- Examples: seedlings, fertilizer, training, disease-control support, or farm visits.
- Record the date and status of the request.
- Add basic recommendations or follow-up actions.
- View pending and completed assistance.

**Function summary:** Tracks farmer requests, agricultural assistance, and recommended follow-up actions in one place.

## Three Objectives

### General Objective
**To develop a simple information system that improves the recording, monitoring, and management of banana-farming information for selected banana farmers in Panabo City.**

### Specific Objectives

1. **To develop a farmer and farm record module** that stores organized information about selected banana farmers, their farms, and basic production details.

2. **To develop a disease and farm-condition monitoring module** that allows users to record, update, and track banana diseases, pests, and other reported farm problems.

3. **To develop an assistance and recommendation tracking module** that records farmer requests, agricultural support, and follow-up actions provided by authorized personnel.

## Objective Summaries for Later Development

| Objective | One-sentence development summary |
|---|---|
| Objective 1 | Create a module for registering and managing banana farmer and farm information. |
| Objective 2 | Create a module for recording and monitoring banana diseases, pests, and farm conditions. |
| Objective 3 | Create a module for tracking farmer assistance requests, support provided, and follow-up recommendations. |

## Suggested Users

- **Farmer** — records farm information and reports farm problems or assistance needs.
- **Agriculture Staff/Admin** — manages farmer records, reviews reports, records assistance, and monitors cases.

For a mini-system, you can limit the roles to **Farmer** and **Admin**.

## Suggested Basic Data

### Farmer
- Farmer ID
- Full Name
- Contact Number
- Barangay
- Farm Location
- Farm Size
- Banana Variety

### Farm/Disease Report
- Report ID
- Farmer ID
- Date Reported
- Problem Type
- Affected Area
- Description
- Status
- Remarks

### Assistance
- Assistance ID
- Farmer ID
- Request/Assistance Type
- Date Requested
- Date Provided
- Status
- Recommendation/Remarks

## Recommended System Scope

To keep this appropriate for a **mini information system**, do **not** include complex features such as live weather APIs, online banana-price prediction, AI disease detection, GPS mapping, online payments, or IoT sensors.

The core workflow can simply be:

**Register Farmer → Record Farm → Report Farm Problem → Monitor Status → Record Assistance/Recommendation**

## Why This Topic Is Strong

Panabo City is a practical study area because banana production is well established in the city and local sources specifically document banana-growing communities and disease-management activities. A 2025 study of small-scale banana growers across Davao del Norte, including Panabo, also reported substantial effects from Panama disease on yield and income and identified gaps in formal training and government assistance.

This gives your project a clear real-world problem while keeping the proposed system small enough to develop within a school project.

## Possible Final Title

**BananaCare: A Banana Farm Monitoring and Farmer Assistance Information System for Selected Banana Farmers in Panabo City, Davao del Norte**

### Very Short Version

**Problem:** Banana farmers need a more organized way to record farm information, report diseases, and track assistance.

**Title:** BananaCare is a mini information system for monitoring banana farms and managing farmer assistance in selected areas of Panabo City.

**Objectives:** The system will manage farmer/farm records, monitor disease and farm conditions, and track assistance and recommendations.

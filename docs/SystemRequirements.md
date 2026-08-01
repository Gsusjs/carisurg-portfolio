# System Requirements - Inputs, Outputs, and Integration Notes

## Inputs

### HCI - ED Triage Desk
- Manually entered vital signs (heart rate, blood pressure, respiratory rate, oxygen saturation, temperature, and blood glucose where available).
- Chief complaint selected during triage.
- Manual data entry only during the MVP stage to avoid dependence on hospital EHR integration.

### HRI - Observation Unit
- Continuous vital-sign measurements from the robot-assisted monitoring station.
- Chief complaint entered through the kiosk touchscreen.

## Outputs

### HCI - ED Triage Desk
- Predicted ESI level (1-5).
- Colour-coded urgency indicator.
- Confidence score.
- Brief explanation showing the main factors influencing the prediction.

### HRI - Observation Unit
- Colour-coded alert and notification for nurses when high-risk patterns are detected.
- On-screen guidance for patients while waiting for staff assistance.

## Human Response

### HCI - ED Triage Desk
The nurse reviews the AI recommendation alongside their own assessment. Where the recommendations differ, the explanation panel is reviewed before the nurse confirms or overrides the suggestion. All overrides are recorded for future audit and quality improvement.

### HRI - Observation Unit
The nurse responds to alerts by reviewing the patient's observations, reassessing the patient if necessary, and determining the appropriate course of action. The kiosk never makes clinical decisions independently.

## Integration Requirements
- Integrate with the existing ED triage workflow while allowing nurses to continue assigning the ESI manually.
- Display AI recommendations within two seconds of completing data entry.
- Clearly indicate when AI recommendations are unavailable because of missing data or network failures.
- Record confirmations and overrides for audit purposes.
- Require human approval before any recommendation influences patient care.

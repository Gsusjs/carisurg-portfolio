
# HCI-Specific (ED Triage Desk)

## 1. Alarm Fatigue

**Concern:**  
Frequent AI notifications may cause important alerts to be ignored if they occur too often.

**Mechanism:**  
The AI indicator only visually escalates (colour change, **"Review Now"** prompt) when the AI recommendation and the nurse's own ESI disagree, particularly toward a more urgent level. Matching cases are shown quietly, with no escalation, so the desk is not generating a constant stream of alerts for agreement cases.

---

## 2. Display Readability Under Pressure

**Concern:**  
Information must remain clear and easy to interpret during busy, high-noise, high-glare shifts.

**Mechanism:**  
Urgency is shown with both colour and a text/number label together, never colour alone; minimum 16 to 18 point font size; high-contrast palette; touch and click targets sized for use while wearing gloves.

---

## 3. Automation Bias

**Concern:**  
Nurses may place too much trust in AI recommendations during high workload periods.

**Mechanism:**  
There is no default **"accept"** action. Confirming the AI recommendation and keeping the nurse's own assessment are presented as two equally weighted buttons, and any override is a normal, unpenalised, logged action rather than an exception path.

---

# HRI-Specific (Observation Unit)

## 1. Physical Safety

**Concern:**  
Equipment operating near patients must not pose a physical risk, especially to frail or confused patients.

**Mechanism:**  
The MVP kiosk is stationary with no autonomous movement. Any future mobile version is explicitly scoped as a later phase requiring dedicated safety validation aligned to personal-care robot standards (ISO 13482) before deployment.

---

## 2. Reliable Interaction in a Noisy or Difficult Environment

**Concern:**  
Voice or touchscreen input must remain usable despite background noise, patient distress, or limited mobility.

**Mechanism:**  
Touch input is the default and required path; voice input, if added later, must degrade gracefully back to touch on recognition failure rather than blocking the interaction. A large-text, simplified mode is available, plus a nurse-assisted entry path for patients who cannot self-operate the kiosk.

---

## 3. Graceful Degradation on Sensor Failure

**Concern:**  
If a sensor fails or a reading cannot be collected, the system must not silently generate an unreliable recommendation.

**Mechanism:**  
A missing or out-of-range sensor reading is shown explicitly as **"no data"** on the nurse-station alert rather than being defaulted or substituted, and no ESI recommendation is generated from an incomplete reading set.

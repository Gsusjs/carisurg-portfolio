
## 1. Deployment Vision

The system is designed to give ED and Observation Unit nurses a second opinion at the point of triage, without ever making a decision on its own. Every prediction is shown alongside the nurse's own assessment, not in place of it, and every output requires a human to act on it before it affects a patient.

Deployment is phased by setting:

### Phase 1 (Primary): HCI, ED Triage Desk

A screen-based panel added to the existing triage workflow. This is the preferred first deployment because it requires no new hardware and integrates into a workflow nurses already use.

### Phase 2 (Secondary): HRI, Observation Unit

A stationary kiosk with attached vitals sensors, feeding the same underlying model. This is scoped for a later phase because it introduces physical equipment and continuous data capture, both of which carry additional safety and governance requirements beyond the HCI setting (see `docs/safety-considerations.md`).

Both settings share the same model and the same core principle:

> **The AI recommends, the nurse decides.**

---

## 2. System Requirements for Human-Machine Interfacing

- The AI recommendation must always be shown alongside the human's own assessment, never in place of it.
- The interface must make disagreement at least as easy as agreement. There is no default **"accept"** action.
- A recommendation must always be accompanied by its confidence score and a short rationale. A number with no explanation is not acceptable at any point in the interface.
- The interface must clearly and visibly state when a recommendation is unavailable (missing data, network failure, sensor fault), rather than silently omitting it.
- Confirmations and overrides must be logged, including the reason for an override.
- On the Observation Unit kiosk specifically, the patient-facing screen must never show a raw ESI number or an urgency colour code directly to the patient. Only the nurse station shows the recommendation.
- A recommendation must appear within approximately two seconds of the triggering input (manual entry completion on the ED desk, or a new vitals reading on the kiosk), so it does not add a perceptible delay to the clinical workflow.

---

## 3. Inputs and Outputs

### HCI – ED Triage Desk

**Inputs**

- Manually entered vital signs:
  - Heart rate
  - Blood pressure
  - Respiratory rate
  - Oxygen saturation
  - Temperature
  - Blood glucose (where available)
- Chief complaint selected during triage.

Manual entry only at this stage, to avoid a dependency on hospital EHR integration.

**Outputs**

- Predicted ESI level (1–5)
- Colour-coded urgency indicator
- Confidence score
- Brief explanation of the main contributing factors

### HRI – Observation Unit

**Inputs**

- Continuous vital-sign measurements from the robot-assisted monitoring station:
  - Blood pressure (BP)
  - Oxygen saturation (SpO₂)
  - Pulse
  - Temperature
- Chief complaint entered through the kiosk touchscreen

**Outputs**

- Colour-coded alert and confidence score sent to the nurse station when a high-risk pattern is detected
- Separate, calm status message shown to the patient on the kiosk screen itself

### Human Response (Both Settings)

The nurse reviews the AI recommendation alongside their own assessment or the patient's live readings. Where the two differ, the explanation panel or alert detail is reviewed before the nurse confirms or overrides. Every confirmation and override is logged for audit and quality improvement. The kiosk never initiates a care decision or patient movement on its own.

---

## 4. Build Path Choice and Justification

**Chosen build path:** Web-based interface, embedded in the existing hospital triage software (HCI), plus a kiosk touchscreen for the Observation Unit (HRI).

A native mobile app was considered and rejected for the primary deployment: triage happens at a fixed desk with an existing shared workstation, so a phone or tablet app would add a second device to manage rather than fitting into what's already there.

A fully physical/robotic prototype was considered for the Observation Unit but scoped down to a stationary kiosk for the same reason the co-design canvas gives: introducing patient-proximate mobility carries safety requirements (ISO 13482-aligned proximity safety, fail-safe stopping) that need dedicated validation before they belong in an MVP.

A web-based panel was chosen over a standalone desktop application because it can be embedded directly into the existing EHR/triage software the nurse already has open, rather than requiring a window switch during a time-pressured assessment.

---

## 5. Integration Requirements

- Integrate into the existing ED triage workflow while allowing nurses to continue assigning the ESI manually.
- Display AI recommendations within two seconds of the triggering input.
- Clearly indicate when AI recommendations are unavailable because of missing data or network failures.
- Record confirmations and overrides for audit purposes.
- Require human approval before any recommendation influences patient care, in both settings.

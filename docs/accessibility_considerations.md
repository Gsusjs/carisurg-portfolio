# Accessibility Considerations

Three accessibility concerns for the urgency-tier alert design and how the current prototype addresses each.

## 1. Colour Blindness

**Concern:** The four tiers use colour-coded chips. A nurse with red-green colour blindness could struggle to distinguish **Critical** (muted red) from **Medium** (muted mustard) by colour alone.

**Design response:** Colour is a secondary cue and is never the sole indicator of urgency. Every chip pairs colour with a text label, while the alert banner and message wording state the tier and required timeframe in text regardless of colour.

**Gap:** The four colours have not yet been validated using a colour-blindness simulator.

## 2. Cognitive Load at End of Shift

**Concern:** The target scenario is a tired nurse on a night shift with roughly ten seconds to act. Long or ambiguous wording presents a genuine risk under these conditions.

**Design response:** All four messages are **12 words or fewer**, share a single sentence structure, and lead with the tier name.

**Gap:** The wording has not yet been stress-tested against a tired-reader scenario.

## 3. Alarm Fatigue

**Concern:** If every case in the queue escalates visually in the same way, nurses may begin to disregard the banner, including for cases that require immediate attention.

**Design response:** The alert banner shows only the **single highest-priority unaddressed case**. Matching or lower-tier cases remain visible in the queue without banner escalation.

**Gap:** Behaviour when two **Critical** cases occur simultaneously has not yet been designed.

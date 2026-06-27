# Algorithmic Equity Failure in Population Health Management

## Primary Source

Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). *Dissecting racial bias in an algorithm used to manage the health of populations*. Science, 366(6464), 447–453.

DOI: https://doi.org/10.1126/science.aax2342

## 1. What happened?

A commercially developed risk stratification algorithm was used across the United States to identify patients eligible for high risk care management programmes.

Researchers discovered an equity failure: the algorithm systematically assigned lower risk scores to Black patients compared with White patients who had the same level of illness severity. As a result, the system reduced the number of Black patients identified for additional care support by more than half.

---

## 2. Why did it happen?

The failure was caused by the use of an inappropriate proxy variable.

Because developers did not have a direct digital measurement of healthcare need, they used future healthcare costs as a substitute. Although the algorithm accurately predicted healthcare costs, those costs reflected unequal patterns of healthcare access rather than true differences in clinical need.

The model therefore learned that lower healthcare spending meant lower healthcare need, even when patients had similar health conditions.

---

## 3. What did the system fail to anticipate?

The developers failed to account for structural socioeconomic inequities within healthcare systems.

The algorithm reproduced existing disparities because healthcare spending is influenced by access barriers, availability of care, and historical inequalities. Black patients with similar levels of illness often had lower healthcare costs due to reduced access to healthcare services.

The system incorrectly interpreted lower spending as lower clinical need.

---

## 4. Was the failure technical or human?

This was a combined technical and governance failure.

From a technical perspective, the main issue was proxy bias. The model used healthcare cost as a representation of health need, even though cost does not accurately measure disease severity.

From a governance perspective, the organisations deploying the system failed to perform adequate fairness testing before implementation. Disaggregated evaluation across demographic groups could have identified unequal performance.

---

## 5. What would have prevented the harm?

The harm could have been prevented by using direct clinical measures of disease burden rather than financial proxies.

Additional safeguards should have included:

* Fairness testing before deployment
* Evaluation of performance across demographic groups
* Monitoring differences in recall and error rates
* Continuous governance throughout the AI lifecycle

For example, comparing recall at threshold values across racial groups would have revealed the disparity before the system was used in clinical decision making.

---

## Key Lesson

This case demonstrates that predictive accuracy alone is not enough for safe clinical AI.

Reliable AI systems require fairness testing, transparency, continuous monitoring, and strong governance processes to ensure that automated decisions do not reinforce existing healthcare inequalities.




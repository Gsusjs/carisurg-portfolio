# Algorithmic Equity Failure in Population Health Management

## Primary Source

Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019).  
*Dissecting racial bias in an algorithm used to manage the health of populations*.  
Science, 366(6464), 447–453.

DOI: https://doi.org/10.1126/science.aax2342

---

## 1. What happened?

A commercially developed risk-stratification algorithm was used across the United States to identify patients eligible for high-risk care management programmes. These programmes provided additional healthcare resources, such as dedicated nursing support and care coordination, to patients predicted to benefit most.

Researchers discovered an equity failure: the algorithm systematically assigned lower risk scores to Black patients compared with White patients who had similar levels of illness. As a result, fewer Black patients were identified as needing additional support, reducing access to potentially beneficial healthcare resources.

---

## 2. Why did it happen?

The failure was caused by the use of an inappropriate proxy variable. Developers did not have a direct measure of patient health need, so they used future healthcare costs as a substitute.

The model accurately predicted future healthcare spending, but spending was not a neutral measure of health. Healthcare costs reflected differences in access, healthcare utilisation, insurance coverage and wider socioeconomic conditions.

As a result, the algorithm learned patterns from unequal healthcare access rather than true differences in clinical need.

---

## 3. What did the system fail to anticipate?

The developers failed to recognise that historical healthcare inequalities were embedded within the training data.

Lower healthcare spending did not necessarily indicate that patients were healthier. Some groups experienced lower spending because of reduced access to healthcare services. The system therefore interpreted lower spending as lower need.

The algorithm reproduced existing structural inequities because the data used for prediction reflected unequal healthcare opportunities.

---

## 4. Was the failure technical or human?

This was a hybrid failure involving both technical design and governance.

The technical failure was proxy bias: healthcare cost was used as a representation of health need, even though it contained existing social and healthcare inequalities.

The governance failure was insufficient validation before deployment. The organisations using the system did not conduct adequate fairness testing to determine whether performance was consistent across different patient groups.

---

## 5. What would have prevented the harm?

The harm could have been reduced by selecting direct clinical measures of disease burden rather than financial proxies.

Additional safeguards should have included:

- Testing model performance across demographic groups before deployment
- Monitoring subgroup recall and error rates
- Conducting regular equity audits after implementation
- Reviewing variables influencing model decisions
- Ensuring human oversight of AI-supported decisions

This case demonstrates that predictive accuracy alone is insufficient for safe healthcare AI. Fairness testing, transparency and continuous governance are essential safeguards throughout the AI lifecycle.

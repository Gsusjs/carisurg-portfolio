# Algorithmic Equity Failure in Population Health Management

## Primary Source

Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019).  
*Dissecting racial bias in an algorithm used to manage the health of populations*.  
Science, 366(6464), 447–453.

DOI: https://doi.org/10.1126/science.aax2342

---

## 1. What happened?

Health systems utilized a commercial risk-stratification algorithm to identify patients with complex needs for "high-risk care management" programs (Obermeyer et al., 2019, p. 1). Researchers identified a significant equity failure: at any given risk score, Black patients were considerably sicker than White patients (Obermeyer et al., 2019, p. 2). This meant sicker Black patients were assigned the same risk level as healthier White patients, leading to fewer Black patients being auto-identified for necessary additional support (Obermeyer et al., 2019, p. 2)If this bias were removed, the percentage of Black patients identified for these programs would have risen from 17.7% to 46.5%.


---

## 2. Why did it happen?

The failure was rooted in the choice of the proxy variable used for prediction. Instead of predicting health needs directly, the algorithm was designed to predict future healthcare costs (Obermeyer et al., 2019, p. 3). While the algorithm was highly accurate at predicting cost, cost is not a neutral proxy for health (Obermeyer et al., 2019, p. 3). Because of systemic barriers, Black patients generate lower healthcare costs than White patients even when they have the same level of clinical need (Obermeyer et al., 2019, p. 4). The algorithm therefore learned patterns based on unequal healthcare access and utilization rather than actual clinical severity (Obermeyer et al., 2019, p. 4).


---

## 3. What did the system fail to anticipate?

The developers failed to account for structural and historical healthcare inequalities embedded in the training data (Obermeyer et al., 2019, p. 6). They did not anticipate that the "wedge" between needing care and receiving care would be so strongly correlated with race (Obermeyer et al., 2019, p. 4). Factors causing this discrepancy include socioeconomic barriers like transportation issues, systemic clinical biases resulting in lower medical spending for Black patients regardless of need, and the misinterpretation of lower spending as a sign of health rather than reduced access to specialized care (Obermeyer et al., 2019, p. 4).


---

## 4. Was the failure technical or human?

This was a hybrid failure of technical design and institutional governance.

* Technical Failure: This is categorized as "label bias" or "proxy bias" (Obermeyer et al., 2019, p. 6). The technical decision to use total medical expenditures as the target variable directly introduced racial bias because the relationship between health and cost differs by race (Obermeyer et al., 2019, p. 4,7).

* Human/Governance Failure: There was a failure in problem formulation and validation (Obermeyer et al., 2019, p. 5). The industry standard prioritized cost prediction as the primary metric for accuracy (Obermeyer et al., 2019, p. 5). Deploying organizations failed to conduct sufficient fairness audits or clinical validation to ensure risk scores accurately reflected illness burden across demographic groups (Obermeyer et al., 2019, p. 7).


---

## 5. What would have prevented the harm?

The harm could have been significantly reduced by choosing direct clinical measures of health instead of financial ones (Obermeyer et al., 2019, p. 5). When the researchers experimented with an algorithm trained to predict the number of active chronic conditions instead of cost, the racial composition of the highest-risk group shifted to include sicker Black patients, reducing bias by 84% (Obermeyer et al., 2019, p. 5,7). Pre-deployment fairness audits comparing model recall across demographic groups would have identified the disparity before the algorithm was used at scale (Obermeyer et al., 2019, p. 7.

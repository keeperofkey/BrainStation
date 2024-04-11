<div class="title">
    <div>Third-Party Risk</div>
    <div>Liam Dodd</div>
    <div>April 8, 2024</div>
</div>

<style>
    .title {
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(3, 1fr);
        height: 842pt;
        font-size: 36pt;
        text-align: center;
        font-weight: bold;
    }
</style>

# 

Identify third-party vendors or services and update the risk register if needed to include third parties. Develop a shared responsibility model for cloud infrastructure that supports the chosen processes, threat model, and network and data security solutions.

Deliverable: Write a Third-Party Risk Report

# Risk Register for VISION

## Strategic Risks

- **Risk:** VISION's AI and algorithms may demonstrate bias and unfairness towards certain groups, resulting in legal liability and reputation damage.

  - **Mitigation:** Continuously test models and algorithms for bias. Create an ethics review board.

- **Risk:** Competitors may develop superior AI technology, eroding VISION's market position.

  - **Mitigation:** Invest heavily in R&D and recruit top AI talent. Pursue strategic acquisitions.

## Financial Risks

- **Risk:** Cloud costs may escalate rapidly as data storage and computing needs increase.

  - **Mitigation:** Negotiate discounts with cloud providers. Monitor usage regularly and optimize costs.

- **Risk:** Customers may default on payments due to economic downturn.

  - **Mitigation:** Perform credit checks on new customers. Pursue insurance on receivables.

## Operational Risks

- **Risk:** Prolonged outage at cloud providers disrupts services and causes data loss.

  - **Mitigation:** Use multiple cloud providers. Replicate data across availability zones.

- **Risk:** A cyber attack results in data breach and theft of intellectual property.

  - **Mitigation:** Harden security posture. Implement multi-factor authentication. Perform penetration testing.

- **Risk:** Key employees leave the company, resulting in loss of critical knowledge.

  - **Mitigation:** Incentivize retention with stock options. Cross-train employees. Document processes thoroughly.

## Compliance Risks

- **Risk:** Non-compliance with GDPR results in heavy fines.

  - **Mitigation:** Appoint Data Protection Officer. Implement mandatory data privacy training.

- **Risk:** Lax controls around PII data leads to privacy violations.

  - **Mitigation:** Classify data by sensitivity. Limit access to PII data. Implement encryption and data masking.

# Third-Party Risk Assessment for VISION

## Data Privacy and Security Risks

- VISION's training data library contains large amounts of data that may include sensitive information. There is a risk of data leakage or misuse if proper access controls and security measures are not in place.

- VISION utilizes third-party cloud providers like AWS to store data. There is a risk of data breach if these providers have vulnerabilities or misconfigurations.

- VISION should have comprehensive data governance policies and procedures in place to properly handle sensitive data. Lack of data governance could lead to compliance violations.

## Vendor and Supply Chain Risks

- VISION relies on many third-party vendors for services like cleaning, food, accounting etc. Proper due diligence should be conducted to validate these vendors.

- VISION utilizes an overseas cybersecurity monitoring team. There are risks of data exfiltration and lack of visibility into their activities.

- VISION should have a vendor risk management program to assess and monitor third-party vendors on an ongoing basis.

## Business Continuity Risks

- As a tech company, VISION is highly dependent on its IT infrastructure and cloud providers. Any outages could significantly impact operations.

- VISION should have redundancy built into critical systems and a tested business continuity plan. Reliance on any single vendor or system is a risk.

## Compliance and Legal Risks

- VISION must comply with data privacy regulations like GDPR if handling EU citizen data. Fines for non-compliance can be substantial.

- VISION's AI systems should be tested for bias to avoid legal issues or reputational damage.

- VISION should implement a compliance program with policies, training, and auditing to adhere to relevant laws and regulations.

# Executive Summary: Brief introduction to the scope and purpose of the third-party risk analysis.

# Third-Party Risk Register: A detailed register of risks associated with any third-party vendors or services

# Shared Responsibility Model: Explanation of the shared responsibility in the cloud infrastructure models (Saas, IaaS, etc.).

# Shared Responsibility Model

The shared responsibility model defines the division of responsibilities between cloud providers and customers when using cloud services. It helps understand security and compliance obligations for both parties.

## Key Points

- In cloud computing, responsibilities for security and compliance are shared between the cloud provider and the customer. The division depends on the service model used.

- In SaaS (Software as a Service), the provider manages most aspects of the application and infrastructure. The customer is responsible for their data, user access, and application-level security.

- In IaaS (Infrastructure as a Service), the provider manages the physical infrastructure and virtualization. The customer handles OS, network, data, and application security.

- In PaaS (Platform as a Service), the provider manages the infrastructure, OS, and middleware. The customer is responsible for the deployed apps and data security.

- Understanding the shared model is crucial to set up proper security controls, meet compliance needs, and determine liability in case of a breach or outage.

- The shared responsibility model creates interdependence between the provider and customer. Close cooperation is needed to ensure end-to-end security.

# Risk Management Strategies: Strategies and methods for managing third-party risks.

# Conclusion: Overall findings and the importance of managing third-party risks.

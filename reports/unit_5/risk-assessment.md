<div class="title">
    <div>Cybersecurity Risk Assessment: VISION</div>
    <div>Liam Dodd</div>
    <div>April 8, 2024</div>
</div>

# Cybersecurity Risk Assessment:

Based on your chosen scenario, identify two core processes presented. These processes should be sufficiently complicated enough to conduct a detailed analysis for this project. Understanding the core processes is crucial for identifying cybersecurity threats and vulnerabilities.

# Process Flow Chart

Put together the flow charts detailing each step of the process.

## A Data Collection, Ingestion, & Management Interface

If customers need to train for specific use cases, VISION has made comprehensive software that allows its customers to upload, organize, and manage image or video data used to train an artificial intelligence model.

There are a number of considerations here including file size and type, number of files, content of data being uploaded (e.g. intellectual property), storage location of the data, and more.

## A Data Annotation & Labeling Interface

AI systems don’t inherently "know" what the data being presented is. Humans need to point out those patterns by leaving annotations or labels, among other supporting data/metadata.

The provided interface helps make that process easy and scalable by allowing users to provide examples or leverage the company’s proprietary software to help speed up the data annotation and labeling process.

## Training Data Library & Model Library

VISION has solutions tailored to different levels of effort and involvement
desired by customers. Their training data library houses a vast amount of
different image and video data that can be used to train a computer vision
model. Rather than having clients search, organize and manage all the training
data, they can obtain a massive amount of value by using collections already
curated by VISION. It’s important to note there are privacy, security,
intellectual property and other considerations to consider for VISION’s library
along with how that data is being used.

If clients don’t want to train their own artificial intelligence model, they
can use a pre-trained one provided by VISION. While this is an added cost, it
is also an added value to clients, simplifying their process to build a
solution. The downside here is that pre-trained models lack the same level of
customization and control given to custom-developed models.

# People, Processes, and Technology

Next identify the people, and technology supporting the processes identified. It is important to recognize these elements to understand the ecosystem where cybersecurity measures will be applied.

## People

- 200 Bay Area Employees
- Numerous vendors and contractors
  - maintenance
  - infrastructure
- 24h cybersecurity monitoring team in India

## Technology

- maintain highly efficient infrastructure
- remain secure but accessible

# Data Flow Chart

Now that you’ve put together the processes flow chart, create a data flow diagram. This is essential for visualizing how data moves through the system, which is critical for threat modeling.

# Asset List and Register

Compile an asset list and create a risk register. Identifying assets and potential risk is the first step in any cybersecurity defense strategy.

Note: all deliverables are to be based specifically on these 4 items identified

Deliverable: Write a Risk Assessment Report:

# Asset List

## Company Assets

- Employee data (PII, credentials, etc.)
- Intellectual property (algorithms, models, code, etc.)
- Physical assets (servers, computers, office equipment)
- Vendor/contractor data
- Financial data

## Client Assets

- Patient data (PII, medical records, imaging, etc.)
- Employee data
- Physical assets (servers, computers, medical equipment)
- Financial data

# Risk Register

## Strategic Risks

- Competitors stealing IP
- Legal issues around data sourcing/usage (Copyright)
- Failure to innovate and keep pace with competition
- Damage to reputation from security breach

## Financial Risks

- Theft of funds via cybercrime
- Fines for regulatory non-compliance
- Lawsuits from data breaches
- Ransomeware

## Operational Risks

- Service disruption from DDoS, ransomware, or other cyber attacks
- Leak of intellectual property
- Insider threat from malicious employee or contractor
- Vendor management issues leading to breach

## Compliance Risks

- Failing to meet regulatory requirements around PII and medical data
- Violating laws around AI/algorithm usage
- Non-compliance with medical device standards

## Third Party Risks

- Breach of client systems leading to breach of company systems
- Vendor negligence leads to breach of company systems
- Contractors mishandle sensitive data

## Data Risks

- Leak of employee or patient PII
- Theft of medical records or images
- Inaccurate AI output sent to wrong party

## Data Privacy and Compliance

- Healthcare data is highly sensitive and there are strict regulations around its use, storage, and transmission.
  - Need to comply with regulations like HIPAA, GDPR, etc.
- Only collect, process, and store minimum necessary data.
  - Delete when no longer needed.
- Encrypt data in transit and at rest.
  - Use TLS for connections.
- Get legal signoff on data processing activities.
- Implement access controls and auditing to track data access.

## Secure Architecture

- Isolate client data from VISION systems.
  - Use separate cloud environments.
- Authenticate connections between VISION and client systems.
- No caching of client data in VISION systems unless absolutely necessary.
- Use microservices and API gateways to limit access to backend systems.

## Operations Security

- Harden cloud environments, VMs, containers, etc.
- Continuously monitor for threats, attacks, or unauthorized access.
- Perform penetration testing and code audits regularly.
- Have an incident response plan ready in case of a breach.

## AI Model Training

- Carefully manage training data.
- Check for bias in training data and model outputs.
- Continuously evaluate model performance on diverse datasets.
- Have human oversight on model outputs before clinical use.

## Secure Communications

- Encrypt all data transfers externally. Don't send sensitive data in cleartext.
- Authenticate recipients before sending data.
- Carefully manage credentials and API keys. Rotate periodically.
- Notify patients/doctors if incorrect results are sent out.

## Endpoints and Accounts

- Enforce MFA for all user and admin accounts.
- Use least privilege model for user roles and access.
- Automatically lock accounts after periods of inactivity.
- Patch and secure all client endpoints and apps.

## Physical Security

- Secure physical facilities where data is processed and stored.
- Dispose of old equipment and media securely.

## Business Continuity

- Have redundancy for critical systems.
- Regularly backup data and configurations.
- Test disaster recovery procedures periodically.

# Executive Summary

> A concise overview of the risk assessment findings, tailored for quick understanding by senior leadership.

# High Impact Risk Overview

> Detailed analysis of the most significant risks identified during the risk assessment.

# Recommendations

> Suggested actions or strategies to mitigate or manage identified risks.

# Conclusion

> A wrap of the findings and overall implications for the organization.

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

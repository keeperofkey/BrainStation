<div class="title">
    <div>Threat Modeling</div>
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

# Executive Summary

This threat modeling report identifies potential security threats to the
computer vision system under development and suggests mitigations to address
them. Key threats include spoofing of credentials or data, tampering with
training data or models, denial of service attacks, and unauthorized access due
to misconfiguration. Implementing authentication, encryption, immutable
storage, audit logging, and access controls are highlighted as key mitigations.
Ongoing threat modeling as the system architecture evolves is recommended.

# Threat Modeling Overview

The STRIDE methodology was used to categorize threats for the computer vision
system. STRIDE stands for Spoofing, Tampering, Repudiation, Information
Disclosure, Denial of Service, and Elevation of Privilege. Each component of
the system architecture was analyzed in the context of how it could be
threatened in each of these categories. Potential mitigations were proposed for
the identified threats.

# Threat Model

This document outlines potential threats and mitigations for the computer vision system being developed by VISION for the healthcare client using the STRIDE methodology.

## Spoofing Threats

- An attacker could spoof login credentials to gain unauthorized access to patient data or system functions.

  - Mitigation: Implement multi-factor authentication for all user accounts.

- An attacker could spoof the origin of malicious data sent to the AI model for training.

  - Mitigation: Authenticate all connections to the training data pipeline. Verify the source of all training data.

- An attacker could spoof system components to intercept or alter data.

  - Mitigation: Encrypt all data in transit and at rest. Authenticate all internal system connections.

## Tampering Threats

- An attacker could alter training data to degrade model accuracy.

  - Mitigation: Store training data in an immutable, append-only data store.

- An attacker could modify system logs or alerts to cover their tracks.

  - Mitigation: Send logs to a SIEM in real-time. Alert on log tampering.

- An attacker could modify model parameters or outputs.

  - Mitigation: Store models in an immutable data store. Alert on unexpected changes.

## Repudiation Threats

- Users could deny having accessed patient data.

  - Mitigation: Implement detailed audit logging for all data access.

- Actions taken by the system could be denied later.

  - Mitigation: Immutable and detailed logging of all system actions.

## Information Disclosure Threats

- Patient data could be exposed in transit over the network.

  - Mitigation: Encrypt all connections with TLS.

- Patient data could be exposed due to misconfigured storage permissions.

  - Mitigation: Implement least privilege permissions on all data.

- Credentials or API keys could be exposed.

  - Mitigation: Store secrets in a secrets vault with limited access.

## Denial of Service Threats

- Attackers could flood the public API with requests.

  - Mitigation: Implement rate limiting on the API.

- Attackers could consume all training compute resources.

  - Mitigation: Enforce resource quotas per user.

- The AI system could be overwhelmed with invalid data.

  - Mitigation: Input validation and anomaly detection.

## Elevation of Privilege Threats

- A user could escalate privileges through compromised credentials.

  - Mitigation: Enforce role-based access control. Rotate credentials regularly.

- An attacker could exploit a vulnerability to gain system access.

  - Mitigation: Harden systems and keep software patched and updated.

- Weak permissions could allow unauthorized data access.

  - Mitigation: Implement least privilege permissions.

This covers some high level threats and mitigations to consider. Further analysis should be performed once system architecture and components are finalized. Threat modeling is an iterative process that should be repeated as the system evolves.

# Compensating Controls: Identification of controls that can mitigate the identified threats.

# Recommendations: Suggestions for improving security based on the threat modeling outcomes.

# Conclusion: Final assessment and overall significance of the threat modeling for the organization.

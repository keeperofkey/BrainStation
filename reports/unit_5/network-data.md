# 

<div class="title">
    <div>Network and Data Security</div>
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

Develop a network topology diagram that would be required to support the chosen processes. A network topology diagram helps in identifying potential vulnerabilities in the network structure.

Deliverable: Write a Network and Data Security Report

# Title: Report title, student’s name, and date.

# Executive Summary: A summarized overview of the network and data security analysis, suitable for executives.

The network and data security analysis identified several areas for improvement to strengthen protections and reduce risk:

- Implement multi-factor authentication for all user accounts to prevent unauthorized access. Require strong passwords and enforce regular password changes.

- Deploy next-generation firewalls and intrusion detection/prevention systems to monitor network traffic, block malicious activity, and alert on anomalies. Keep all security software up-to-date.

- Encrypt sensitive data in transit and at rest. Ensure proper key management procedures.

- Institute least privilege and separation of duties access controls. Limit users to only the systems and data necessary for their role.

- Perform regular vulnerability scanning and penetration testing to identify and remediate vulnerabilities before they can be exploited.

- Implement a security information and event management (SIEM) system for log collection, correlation, and alerting on suspicious activity. Monitor the SIEM.

- Provide ongoing security awareness training to educate employees on cyber risks, phishing, and other threats. Test employees with simulated phishing emails.

- Develop an incident response plan with defined procedures for detecting, responding to, and recovering from security incidents. Conduct response exercises.

- Back up critical data regularly. Store backups offline and encrypted. Test restoration.

- Consider cyber insurance to help offset costs of breach response, legal services, fines, and damages.

Implementing these best practices will improve the organization's security posture against modern cyber threats, preventing breaches and reducing potential impacts. Ongoing training, testing, and adaptation to the evolving threat landscape are essential.

# Data & Network Architecture: Detailed diagram of the current data and network architecture.

# Data & Network Architecture

## Current Architecture

### Overview

The current data and network architecture consists of:

- On-premises data center
  - Application servers
  - Database servers
  - Network devices (routers, switches, firewalls)
- Cloud infrastructure
  - Virtual machines
  - Object storage
  - Load balancers
- Connectivity between on-prem and cloud
  - Site-to-site VPN
  - Direct Connect

### On-Premises

The on-premises data center contains:

- Application servers
  - 2 web servers (Apache)
  - 3 app servers (Tomcat)
  - 2 cache servers (Memcached)
- Database servers
  - 2 MySQL primary servers
  - 1 MySQL read replica
  - 1 PostgreSQL server
- Network
  - Core routers and switches
  - Firewall appliances
  - Load balancers

The servers are connected via a 10Gbps network. Internet access is provided via dual 1Gbps connections.

### Cloud Infrastructure

The cloud infrastructure on AWS contains:

- Virtual machine fleet
  - 3 web servers
  - 5 app servers
- S3 buckets for storage
- Elastic Load Balancers for traffic distribution
- Auto Scaling Groups to scale VM fleet

The cloud resources are spread across multiple Availability Zones.

### Connectivity

The on-prem data center connects to the cloud via:

- Site-to-site IPsec VPN with 500Mbps capacity
- AWS Direct Connect 1Gbps dedicated connection

Traffic is routed between environments based on policy rules.

## Network Diagram

![Network Architecture Diagram](http://www.example.com/diagram.png)

# Security Concerns: Identification and discussion of specific security concerns within the network and data architecture.

# Process-Driven Solution: Solutions and strategies based on the security concerns. Don’t forget to include vulnerability management, penetration testing, logging & monitoring, and threat intelligence as part of your solution.

# Process-Driven Solution:

## Vulnerability Management

- Perform regular vulnerability scans on all systems and infrastructure using tools like Nessus. Remediate any critical or high severity vulnerabilities.
- Subscribe to vulnerability mailing lists like US-CERT to stay up to date on new vulnerabilities.
- Patch systems regularly, prioritizing based on severity and exploitability of vulnerabilities.

## Penetration Testing

- Conduct annual penetration tests on all external facing systems and infrastructure.
- Perform internal penetration tests at least every 2 years.
- Remediate all findings from pentests based on severity and exploitability.

## Logging & Monitoring

- Send logs from all systems to a central SIEM for analysis and correlation.
- Monitor logs and alerts for anomalous activity that could indicate compromise.
- Enable file integrity monitoring on critical systems.

## Threat Intelligence

- Subscribe to threat intel feeds that provide IOCs and context on new/emerging threats.
- Incorporate IOCs from threat intel into IDS/IPS and SIEM to detect known bad actors.
- Perform lookups against threat intel when investigating potential incidents.

# Recommendations: Strategic advice for enhancing network and data security.

# Recommendations

Here are some recommendations for enhancing your organization's network and data security:

## Implement strong access controls

- Require strong passwords and enable multi-factor authentication for all users.
- Limit access to sensitive data and systems to only those who need it.
- Implement the principle of least privilege.

## Keep systems and software up-to-date

- Maintain up-to-date operating systems, software, and security patches on all devices.
- Automate patch management processes to ensure timely patching.
- Replace end-of-life systems that are no longer supported.

## Secure the network perimeter

- Use firewalls to limit traffic between network zones and filter out malicious traffic.
- Disable remote access to devices that don't require it.
- Implement VPNs for secure remote access into your network when needed.

## Encrypt sensitive data

- Encrypt data in transit and at rest wherever possible.
- Enforce encryption policies through technology controls.
- Properly manage and store encryption keys.

## Monitor, log, and analyze activity

- Implement security information and event management (SIEM) solutions.
- Log and monitor user and system activity to identify anomalies.
- Perform penetration tests and vulnerability scans regularly.

## Provide security training

- Educate employees on cybersecurity best practices through training and simulated phishing tests.
- Ensure security policies are clearly communicated.

## Maintain backups and incident response plans

- Regularly back up critical data with both onsite and offsite storage.
- Develop and test incident response plans for security events.

## Work with qualified security partners

- Leverage qualified vendors like managed security service providers.
- Obtain regular guidance from qualified cybersecurity consultants.

# Conclusion: Final assessment and overarching implications for network and data security

---
id: SOCAutomation
aliases: []
tags: []
---

______________________________________________________________________

## id: SOCAutomation aliases: \[\] tags: \[\]

# SOC & Automation Report

## Overview of the Selected IOC

### Introduction

Provide a concise overview of the selected Indicator of Compromise (IOC), emphasizing its relevance and significance to the organization's security landscape.

### Key Characteristics

Outline the key characteristics of the IOC, including the types of threats it represents, its origin, and any specific attributes that make it noteworthy.

## Setting up Wazuh and Creating a Rule

### Installation and Configuration

Detail the steps taken to install and configure Wazuh within the environment, including any specific settings tailored to your organization's needs.

### Rule Creation

Explain the process of creating a custom rule in Wazuh, specifying the parameters and conditions used to detect the identified threat intelligence.

## Shuffler.io Configuration for Automated Response

### Integration with Wazuh

Utilizing the Wazuh web dashboard we were able to add the shuffler.io integration to the ossec.conf file. When using the dashboard to restart the manager everything behaved normally. However if the Docker images were restarted the changes were lost.

### Automated Response Setup

Outline the automation rules configured in Shuffler.io to respond to the identified threat, specifying the actions taken in response to different scenarios.

## Results and Observations from Threat Simulation

### Threat Simulation Scenario

Describe the specific threat scenario simulated for testing the integration of Wazuh and Shuffler.io.

### Detection and Response

Present the results of the threat simulation, including details on how Wazuh detected the threat based on the custom rule and how Shuffler.io automated responses were triggered.

### Observations and Improvements

Provide insights gained during the simulation, any challenges faced, and recommendations for improving the threat detection and response process.

## Conclusion

Summarize the key findings, lessons learned, and the overall effectiveness of the integrated threat intelligence, Wazuh, and Shuffler.io solution.

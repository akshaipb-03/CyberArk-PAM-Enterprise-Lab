# CyberArk PAM Enterprise Lab

> A hands-on Privileged Access Management (PAM) lab demonstrating account onboarding, privileged password lifecycle operations, reconciliation, target health validation, and operational audit reporting.

## Project Overview

This project simulates the operational lifecycle of privileged accounts managed through an enterprise PAM program.

The lab combines:

- Real AWS EC2 infrastructure
- Linux and Windows privileged targets
- CyberArk-inspired Safe and platform design
- PAM account onboarding workflows
- Password rotation simulation
- Rotation failure troubleshooting
- Reconciliation workflows
- Retry-based onboarding validation
- Target health checks
- Centralized PAM operations audit reporting

The objective is to demonstrate how a PAM engineer approaches privileged account management from onboarding through operational validation.

## Architecture

```text
                    ┌─────────────────────┐
                    │    PAM Operator     │
                    │      (Mac)          │
                    └──────────┬──────────┘
                               │
                    PAM Operations Automation
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
   ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
   │   Onboarding │      │   Pre-Check │      │ Audit Report │
   │  Automation  │      │ + Health    │      │ Aggregation  │
   └──────┬───────┘      └──────┬──────┘      └──────┬───────┘
          │                     │                     │
          └──────────────┬──────┴──────────────┬──────┘
                         │                     │
              ┌──────────▼─────────┐   ┌──────▼───────────┐
              │   Linux EC2        │   │   Windows EC2     │
              │                    │   │                   │
              │  pamadmin          │   │  winadmin         │
              │  SSH / TCP 22      │   │  RDP / TCP 3389   │
              └────────────────────┘   └───────────────────┘

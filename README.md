# SecureCorp Enterprise PAM Lab

## Project Overview

This project demonstrates the design and simulation of an enterprise Privileged Access Management (PAM) implementation based on CyberArk PAM concepts.

The lab includes real Windows and Linux cloud targets, dedicated privileged accounts, PAM Safe design, account onboarding workflows, and Python automation that simulates account onboarding and password-management incident handling.

## Lab Architecture

```text
PAM User
   |
   v
CyberArk PAM
   |
   +------------------+
   |                  |
   v                  v
UNIX-ADMIN-SAFE   WIN-ADMIN-SAFE
   |                  |
   v                  v
pamadmin          winadmin
   |                  |
   v                  v
Linux EC2          Windows EC2

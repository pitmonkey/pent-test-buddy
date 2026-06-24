# Rules of Engagement / Scope — {{ENGAGEMENT_NAME}}

> This file is the authority for what is permitted in this engagement. Fill it with the
> `grill-scope` skill. `scope-check` reads it before every plan. Do not act on anything that is
> not explicitly in scope and authorized.

## Engagement
- **Name:** {{ENGAGEMENT_NAME}}
- **Client / system owner:** <owner>
- **Operator / tester:** <your name>
- **Created:** {{DATE}}

## Authorization (REQUIRED)
- **Written authorization on file:** NO
- **Authorization reference:** <contract / email / ticket id>
- **Authorizing party:** <name + role>

> `scope-check` treats the engagement as UNAUTHORIZED until "Written authorization on file" is
> YES with a real reference. While unauthorized, no action against any target is permitted.

## In scope — targets that MAY be tested
> One per line. IPs, CIDRs, hostnames, domains, URLs. Be exact.
- <ip / cidr / host / domain / url>

## Out of scope — NEVER touch
> Exclusions override everything. If a target matches here, it is a hard stop.
- <exclusions: hosts, subnets, third-party services, anything off-limits>

## Engagement window
- **Start:** <YYYY-MM-DD HH:MM TZ>
- **End:** <YYYY-MM-DD HH:MM TZ>
- **Permitted hours:** <e.g. business hours only / 24x7 / outside 09:00-17:00>

## Rules / allowed action classes
- **Denial of service / stress testing allowed:** NO
- **Social engineering allowed:** NO
- **Phishing allowed:** NO
- **Data exfiltration allowed:** NO
- **Production systems in scope:** NO
- **Lateral movement allowed:** NO
- **Password / credential attacks allowed:** NO
- **Exploitation (gaining access) allowed:** NO
- **Other constraints:** <rate limits, no-touch systems, change windows, ...>

## Contacts / emergency stop
- **Primary contact:** <name, phone, email>
- **Secondary contact:** <name, phone, email>
- **Emergency stop signal:** <how the client calls it off, and what we do>

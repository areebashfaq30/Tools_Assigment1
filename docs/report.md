# Job Market Analysis Report

## Executive Summary
Analyzed ~27k Stripe jobs (scraped via refactored pipeline). Key insights:

### Top Findings
- **Dominant locations**: Singapore (35%), San Francisco (25%), Toronto/Dublin
- **Popular roles**: Backend/API Engineers, Account Executives, Data Scientists
- **Entry-level**: ~5% (Junior/Intern roles sparse)
- **Tech stack**: Heavy Python/JavaScript/SQL, cloud (AWS), ML/Docker rising

### Charts (analysis/plots/)
![Top Titles](../analysis/plots/top_titles.png)
![Top Locations](../analysis/plots/top_locations.png)
![Skills](../analysis/plots/top_skills.png)

## Methodology
1. Multi-source Selenium → job_links.csv
2. Scrapy ItemLoader parse → jobs.csv (title, loc, dept, skills)
3. Pandas/Matplotlib → stats/plots

Pipeline tested end-to-end, output preserved post-refactor.

Generated: `date`


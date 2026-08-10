"""
AEP × Snowflake — Customer Innovation Hub
Living document: add new content by editing the DATA LAYER sections below.
Deploy: Streamlit in Snowflake (SiS) — upload this file to a Snowflake stage
        or paste directly into Snowsight > Streamlit > Create app.
"""

import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AEP × Snowflake | Innovation Hub",
    page_icon="❄️",
    layout="wide",
)

# ─────────────────────────────────────────────────────────────────────────────
# BRAND STYLES
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700;900&display=swap');

  html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; }

  /* Hero */
  .hero {
    background: linear-gradient(135deg, #1A1A1A 0%, #8B0A1E 50%, #C41230 100%);
    border-radius: 16px;
    padding: 48px 40px;
    margin-bottom: 8px;
    color: white;
  }
  .hero h1 { font-size: 2.6rem; font-weight: 900; margin: 0 0 8px 0; color: white; }
  .hero p  { font-size: 1.1rem; opacity: 0.9; margin: 0; max-width: 680px; }
  .hero .tag {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    margin-bottom: 16px;
    color: rgba(255,255,255,0.85);
  }

  /* Stat pills in hero */
  .stat-row { display: flex; gap: 24px; margin-top: 28px; flex-wrap: wrap; }
  .stat-pill {
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 12px;
    padding: 12px 20px;
    text-align: center;
    min-width: 110px;
  }
  .stat-pill .num { font-size: 1.8rem; font-weight: 900; color: #FFFFFF; line-height: 1; }
  .stat-pill .lbl { font-size: 0.72rem; color: rgba(255,255,255,0.75); margin-top: 4px; text-transform: uppercase; letter-spacing: 0.06em; }

  /* Section headers */
  .section-header {
    font-size: 1.4rem; font-weight: 700; color: #1A1A1A;
    border-left: 4px solid #C41230;
    padding-left: 12px; margin: 0 0 4px 0;
  }
  .section-sub { color: #8A999E; font-size: 0.9rem; margin-bottom: 20px; }

  /* Customer cards */
  .cust-card {
    background: white;
    border: 1px solid #FADDDD;
    border-radius: 12px;
    padding: 20px;
    height: 100%;
    border-top: 4px solid #C41230;
    transition: box-shadow .2s;
  }
  .cust-card:hover { box-shadow: 0 4px 20px rgba(196,18,48,0.15); }
  .cust-name { font-size: 1.05rem; font-weight: 700; color: #1A1A1A; margin-bottom: 4px; }
  .cust-tag  {
    display: inline-block; background: #FFF0F0; color: #C41230;
    border-radius: 8px; padding: 2px 10px; font-size: 0.72rem;
    font-weight: 700; margin-bottom: 10px;
  }
  .cust-desc { color: #24323D; font-size: 0.88rem; line-height: 1.55; }
  .cust-metric {
    margin-top: 12px; padding-top: 12px;
    border-top: 1px solid #FADDDD;
    font-size: 0.82rem; color: #8A999E;
  }
  .cust-metric b { color: #C41230; }

  /* Innovation cards */
  .innov-card {
    background: linear-gradient(135deg, #1A1A1A, #C41230);
    border-radius: 12px; padding: 20px; color: white; height: 100%;
  }
  .innov-icon { font-size: 1.8rem; margin-bottom: 8px; }
  .innov-title { font-size: 1rem; font-weight: 700; margin-bottom: 6px; color: #FFD5D5; }
  .innov-badge {
    display: inline-block; background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.45); border-radius: 6px;
    padding: 1px 8px; font-size: 0.68rem; font-weight: 700;
    color: #FFFFFF; margin-bottom: 8px; text-transform: uppercase;
  }
  .innov-desc { font-size: 0.85rem; opacity: 0.88; line-height: 1.5; }

  /* DS resource links */
  .res-card {
    background: #FAFAFA; border: 1px solid #F0DEDE;
    border-radius: 10px; padding: 16px 18px;
    margin-bottom: 10px;
  }
  .res-title { font-weight: 700; color: #1A1A1A; font-size: 0.95rem; }
  .res-desc  { color: #8A999E; font-size: 0.82rem; margin: 2px 0 6px 0; }
  .res-link  { color: #C41230; font-size: 0.82rem; text-decoration: none; font-weight: 600; }
  .res-link:hover { text-decoration: underline; }

  /* Footer */
  .footer {
    background: #1A1A1A; border-radius: 12px;
    padding: 20px 28px; color: rgba(255,255,255,0.65);
    font-size: 0.8rem; margin-top: 32px;
    display: flex; justify-content: space-between; align-items: center;
  }
  .footer a { color: #FFB3B3; text-decoration: none; }

  /* Changelog */
  .changelog-item {
    border-left: 3px solid #C41230; padding-left: 14px;
    margin-bottom: 14px;
  }
  .changelog-date { color: #C41230; font-weight: 700; font-size: 0.82rem; }
  .changelog-text { color: #24323D; font-size: 0.88rem; }

  /* Medallion architecture */
  .medallion-flow {
    display: flex; gap: 0; align-items: stretch;
    margin: 20px 0 32px 0; border-radius: 12px; overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.14);
  }
  .medallion-tier { flex: 1; padding: 24px 20px; }
  .medallion-tier.bronze { background: linear-gradient(160deg, #4A2508, #8B4513); }
  .medallion-tier.silver { background: linear-gradient(160deg, #2C3E50, #4A5568); }
  .medallion-tier.gold   { background: linear-gradient(160deg, #7B5E00, #C9A227); }
  .medallion-arrow {
    display: flex; align-items: center; justify-content: center;
    width: 32px; flex-shrink: 0; background: rgba(0,0,0,0.3);
    color: rgba(255,255,255,0.55); font-size: 1.1rem;
  }
  .medallion-tier-label { font-size: 0.68rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: rgba(255,255,255,0.6); margin-bottom: 4px; }
  .medallion-tier-name  { font-size: 1.3rem; font-weight: 900; color: #FFFFFF; margin-bottom: 8px; }
  .medallion-tier-desc  { font-size: 0.82rem; color: rgba(255,255,255,0.85); line-height: 1.5; margin-bottom: 12px; }
  .medallion-tag {
    display: inline-block; background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.3); border-radius: 6px;
    padding: 2px 8px; font-size: 0.68rem; font-weight: 600;
    color: rgba(255,255,255,0.9); margin: 2px 2px 0 0;
  }

  /* Approach cards */
  .approach-card {
    background: white; border: 1px solid #FADDDD; border-radius: 12px;
    padding: 20px; height: 100%; border-top: 4px solid #C41230;
  }
  .approach-icon  { font-size: 1.6rem; margin-bottom: 8px; }
  .approach-name  { font-size: 1rem; font-weight: 700; color: #1A1A1A; margin-bottom: 4px; }
  .approach-badge {
    display: inline-block; background: #FFF0F0; color: #C41230;
    border-radius: 8px; padding: 2px 10px; font-size: 0.72rem;
    font-weight: 700; margin-bottom: 10px;
  }
  .approach-desc  { color: #24323D; font-size: 0.85rem; line-height: 1.55; }
  .approach-tiers { margin-top: 12px; padding-top: 10px; border-top: 1px solid #FADDDD; font-size: 0.78rem; color: #8A999E; }
  .approach-tiers b { color: #C41230; }

  /* CoCo section */
  .coco-intro {
    background: linear-gradient(135deg, #1A1A1A 0%, #C41230 100%);
    border-radius: 14px; padding: 32px 36px; margin-bottom: 28px; color: white;
  }
  .coco-intro h2 { font-size: 1.7rem; font-weight: 900; margin: 0 0 8px 0; color: white; }
  .coco-intro p  { font-size: 0.95rem; opacity: 0.88; margin: 0; max-width: 680px; line-height: 1.6; }
  .coco-eyebrow  { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: rgba(255,255,255,0.55); margin-bottom: 8px; }

  .coco-feature-card {
    background: white; border: 1px solid #FADDDD; border-radius: 12px;
    padding: 20px; height: 100%; border-left: 4px solid #C41230;
  }
  .coco-feature-icon  { font-size: 1.5rem; margin-bottom: 8px; }
  .coco-feature-name  { font-size: 0.95rem; font-weight: 700; color: #1A1A1A; margin-bottom: 6px; }
  .coco-feature-desc  { color: #24323D; font-size: 0.84rem; line-height: 1.55; }

  .coco-prompt-card {
    background: #1A1A1A; border-radius: 10px; padding: 16px 20px; margin-bottom: 10px;
  }
  .coco-prompt-label { font-size: 0.68rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: rgba(255,255,255,0.45); margin-bottom: 6px; }
  .coco-prompt-text  { font-size: 0.88rem; color: #FFFFFF; font-style: italic; line-height: 1.5; }
  .coco-prompt-tag   {
    display: inline-block; background: rgba(196,18,48,0.25); border: 1px solid rgba(196,18,48,0.5);
    border-radius: 6px; padding: 2px 8px; font-size: 0.68rem; font-weight: 700;
    color: #FFB3B3; margin-top: 8px;
  }

  /* Hide default Streamlit elements */
  #MainMenu, footer, header { visibility: hidden; }
  .block-container { padding-top: 1.5rem; }
</style>
""", unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
#  ▼▼▼  DATA LAYER — EDIT HERE TO UPDATE THE LIVING DOCUMENT  ▼▼▼
# ═════════════════════════════════════════════════════════════════════════════

# ── AEP-specific use cases ────────────────────────────────────────────────────
AEP_USE_CASES = [
    {
        "icon": "👥",
        "title": "Customer 360 & C&I Analytics",
        "partner": "Reference: EDF",
        "partner_color": "#1B5E20",
        "desc": (
            "Unify AMI meter data, CRM records, billing history, and outage events into a "
            "single governed Customer 360 view for each of AEP's 5.6M customers. "
            "Powers personalized energy advisory for residential customers, segment analytics "
            "for C&I accounts, churn risk scoring, and account manager tools — all without "
            "moving data outside Snowflake's security perimeter. EDF demonstrated this pattern "
            "at scale across 7 source systems."
        ),
        "link": "https://www.snowflake.com/en/customers/all-customers/case-study/edf/",
        "link_label": "EDF case study ↗",
    },
    {
        "icon": "⚡",
        "title": "Distribution Grid Planning",
        "partner": "Partner: Itron",
        "partner_color": "#0D47A1",
        "desc": (
            "Itron and Snowflake are collaborating to bring AI-powered grid planning to "
            "distribution utilities. Feeder load forecasting, DER integration modeling, "
            "and capital investment prioritization run on top of AMI and SCADA data in "
            "Snowflake — enabling AEP distribution engineers to model grid scenarios and "
            "right-size infrastructure investments for electrification and EV load growth."
        ),
        "link": "https://investors.itron.com/news-releases/news-release-details/itron-and-snowflake-collaborate-advance-grid-planning-ai-powered",
        "link_label": "Itron + Snowflake announcement ↗",
    },
    {
        "icon": "🔌",
        "title": "Transmission Grid Planning & Operations",
        "partner": "Partner: Siemens",
        "partner_color": "#1565C0",
        "desc": (
            "Snowflake and Siemens are partnering on transmission grid operations and planning "
            "solutions — combining Siemens' grid modeling expertise with Snowflake's data "
            "platform for real-time operational analytics, asset health scoring, and outage "
            "risk prediction across high-voltage transmission infrastructure. "
            "Contact Pugal for details on the specific AEP transmission use cases in scope."
        ),
        "link": None,
        "link_label": None,
    },
    {
        "icon": "🏭",
        "title": "Power Plant Predictive Maintenance",
        "partner": "Pattern: Industrial Manufacturing",
        "partner_color": "#4A148C",
        "desc": (
            "Vibration, temperature, pressure, and efficiency sensor data from AEP's coal, "
            "gas, and nuclear generation fleet can feed the same ML patterns proven in "
            "industrial manufacturing on Snowflake. Anomaly detection models flag developing "
            "equipment faults days before failure — enabling planned maintenance windows, "
            "avoiding forced outages, and reducing O&M costs across the generation portfolio. "
            "Snowpark ML handles model training and Snowflake Tasks schedule scoring runs."
        ),
        "link": None,
        "link_label": None,
    },
    {
        "icon": "📈",
        "title": "Energy Trading, Hedging & Risk Management",
        "partner": "Reference: Uniper",
        "partner_color": "#B71C1C",
        "desc": (
            "Uniper replaced overnight batch P&L reporting with a real-time trading analytics "
            "platform built on Snowflake — ingesting market prices, position data, and "
            "counterparty exposure to optimize hedging and meet EMIR/REMIT reporting obligations. "
            "AEP's trading and risk teams can apply the same pattern: intraday VaR dashboards, "
            "mark-to-market positions, and automated regulatory extracts — all governed and "
            "auditable from a single Snowflake platform."
        ),
        "link": "https://www.snowflake.com/en/customers/all-customers/case-study/uniper/",
        "link_label": "Uniper case study ↗",
    },
]

# ── Cortex Code (CoCo) features ───────────────────────────────────────────────
COCO_FEATURES = [
    {
        "icon": "💬",
        "name": "AI Code Generation",
        "desc": (
            "Describe what you need in plain English — CoCo writes SQL, Python, or Snowpark "
            "for you. From simple queries to full pipeline scaffolding, with awareness of your "
            "actual Snowflake objects and schemas."
        ),
    },
    {
        "icon": "📊",
        "name": "Cortex Analyst",
        "desc": (
            "Ask business questions in natural language and get accurate SQL back, grounded in "
            "a semantic view over your governed data. No SQL knowledge required — built for "
            "analysts and business users who need self-serve answers."
        ),
    },
    {
        "icon": "🗂",
        "name": "Semantic Views",
        "desc": (
            "Define your business data model once — metrics, dimensions, joins, synonyms — "
            "and CoCo can build, validate, and optimize it for you. Powers Cortex Analyst "
            "and ensures consistent definitions across every query."
        ),
    },
    {
        "icon": "📓",
        "name": "Notebook Generation",
        "desc": (
            "Scaffold full Snowflake Notebooks from a prompt — with SQL cells, Python cells, "
            "and Snowpark DataFrame code pre-wired to your data. Eliminates the blank-canvas "
            "problem for exploratory analysis and ML experiments."
        ),
    },
    {
        "icon": "🤖",
        "name": "Cortex Agent Building",
        "desc": (
            "Design and deploy multi-step AI agents that can query data, call tools, search "
            "documents, and synthesize answers — all within Snowflake's security perimeter. "
            "CoCo walks you through tool selection, system prompts, and testing."
        ),
    },
    {
        "icon": "⚙️",
        "name": "Skills & Workflows",
        "desc": (
            "Pre-built expert workflows for Snowflake tasks — Dynamic Tables, Iceberg, "
            "data governance, ML model deployment, cost analysis, and more. Invoke with a "
            "single command; CoCo handles the step-by-step execution."
        ),
    },
]

COCO_PROMPTS = [
    {
        "text": "Write a Dynamic Table pipeline that aggregates AEP smart meter reads from Bronze to a Silver layer, deduplicating by meter_id and read_timestamp.",
        "tag": "Medallion pipeline",
    },
    {
        "text": "Build a semantic view over our outage_events and asset_registry tables so analysts can ask questions like 'which substations had the most outages last quarter?'",
        "tag": "Cortex Analyst",
    },
    {
        "text": "Create a Snowpark Python function that classifies work order descriptions into equipment failure categories using Cortex AI_CLASSIFY.",
        "tag": "AI enrichment",
    },
    {
        "text": "Generate a Snowflake Notebook for load forecasting: pull hourly demand from our Gold layer, train a time-series model with Snowflake ML, and register it in the Model Registry.",
        "tag": "ML pipeline",
    },
]

# ── Medallion architecture approaches ────────────────────────────────────────
MEDALLION_APPROACHES = [
    {
        "icon": "⚡",
        "name": "Dynamic Tables",
        "badge": "Recommended",
        "desc": (
            "Declare your target SQL once — Snowflake automatically computes incremental "
            "refreshes and manages the pipeline DAG. No scheduler code, no merge logic. "
            "The simplest way to keep Bronze, Silver, and Gold in sync continuously."
        ),
        "tiers": "Bronze → Silver → Gold",
        "link": "https://docs.snowflake.com/en/user-guide/dynamic-tables-intro",
    },
    {
        "icon": "🔄",
        "name": "Streams + Tasks",
        "badge": "CDC Pattern",
        "desc": (
            "Streams capture row-level inserts, updates, and deletes on any table. "
            "Tasks execute your transformation logic on a schedule or when a stream has data. "
            "Ideal for event-driven pipelines and complex procedural transformation logic."
        ),
        "tiers": "Bronze → Silver (CDC-driven)",
        "link": "https://docs.snowflake.com/en/user-guide/streams-intro",
    },
    {
        "icon": "🐍",
        "name": "Snowpark (Python)",
        "badge": "Data Science",
        "desc": (
            "Write DataFrame transformations in Python — running directly on Snowflake "
            "compute, inside your security perimeter. Ideal for AEP's data science team "
            "building feature pipelines, custom parsers, and ML-ready Gold layer datasets."
        ),
        "tiers": "Silver → Gold (ML features)",
        "link": "https://docs.snowflake.com/en/developer-guide/snowpark/python/index",
    },
    {
        "icon": "🧊",
        "name": "Apache Iceberg Tables",
        "badge": "Open Format",
        "desc": (
            "Land raw data in open Iceberg format on your own cloud storage — readable by "
            "Spark, Flink, and Trino — while Silver and Gold remain native Snowflake tables. "
            "Eliminates vendor lock-in at the Bronze layer without sacrificing governed analytics."
        ),
        "tiers": "Bronze (raw landing)",
        "link": "https://docs.snowflake.com/en/user-guide/tables-iceberg",
    },
    {
        "icon": "🛠",
        "name": "dbt on Snowflake",
        "badge": "SQL-First",
        "desc": (
            "SQL-first transformation framework with built-in data testing, column-level lineage, "
            "and auto-generated documentation. Runs transformations as Snowflake views or tables. "
            "Strong fit for governance-heavy environments and existing SQL-fluent teams."
        ),
        "tiers": "Bronze → Silver → Gold",
        "link": "https://docs.getdbt.com/docs/core/connect-data-platform/snowflake-setup",
    },
    {
        "icon": "🤖",
        "name": "Cortex AI in the Pipeline",
        "badge": "AI Enrichment",
        "desc": (
            "Run AI_CLASSIFY, AI_EXTRACT, AI_SENTIMENT, and AI_COMPLETE natively inside your "
            "Silver-to-Gold transformation — no external API calls, no data leaving Snowflake. "
            "Enrich outage records, classify work orders, or extract fields from unstructured docs."
        ),
        "tiers": "Silver → Gold (AI-enriched)",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-ai-functions",
    },
]

# ── Utility customer success stories ─────────────────────────────────────────
# To add a new customer: copy one block and append to this list.
UTILITY_CUSTOMERS = [
    {
        "name": "Duke Energy",
        "tag": "Grid Modernization",
        "desc": (
            "Duke Energy built a unified data platform on Snowflake to consolidate "
            "grid operations, customer, and financial data across six states. "
            "Snowflake's scalable compute enabled real-time analytics on smart meter "
            "data — reducing grid outage response time and improving demand forecasting accuracy."
        ),
        "metric": "Consolidated 14 data silos into a single governed platform",
        "link": "https://www.snowflake.com/customers/",
    },
    {
        "name": "Pacific Gas & Electric (PG&E)",
        "tag": "Safety & Wildfire Risk",
        "desc": (
            "PG&E leverages Snowflake as the backbone for its wildfire risk analytics "
            "program — ingesting weather, vegetation, and asset condition data at scale. "
            "Machine learning models trained on Snowflake predict high-risk ignition zones, "
            "enabling targeted inspection and de-energization decisions."
        ),
        "metric": "~70% reduction in data preparation time for safety models",
        "link": "https://www.snowflake.com/customers/",
    },
    {
        "name": "National Grid",
        "tag": "Operational Efficiency",
        "desc": (
            "National Grid migrated its enterprise analytics to Snowflake to support "
            "regulatory reporting across the US and UK. The platform provides a single "
            "source of truth for FERC, Ofgem, and state PUC filings, with full audit "
            "lineage from source system to submitted report."
        ),
        "metric": "3× faster regulatory report generation vs. legacy EDW",
        "link": "https://www.snowflake.com/customers/",
    },
    {
        "name": "Eversource Energy",
        "tag": "Renewable Forecasting",
        "desc": (
            "Eversource built its renewable energy forecasting pipeline on Snowflake, "
            "integrating ISO-NE market data, solar generation telemetry, and weather APIs. "
            "Snowpark for Python enables data scientists to train and deploy forecasting "
            "models without moving data outside the governed platform."
        ),
        "metric": "Real-time renewable dispatch optimization across 4M+ customers",
        "link": "https://www.snowflake.com/customers/",
    },
    {
        "name": "Southern Company",
        "tag": "Enterprise Data Platform",
        "desc": (
            "Southern Company standardized its enterprise analytics on Snowflake across "
            "Georgia Power, Alabama Power, and Mississippi Power subsidiaries. "
            "A shared data platform with subsidiary-level RBAC enables cross-entity "
            "benchmarking while maintaining strict data access controls."
        ),
        "metric": "Single platform serving 5 subsidiaries with isolated data access",
        "link": "https://www.snowflake.com/customers/",
    },
    {
        "name": "Avangrid",
        "tag": "Wind & Solar Operations",
        "desc": (
            "Avangrid (a subsidiary of Iberdrola) uses Snowflake to manage operational "
            "and financial data across its 8GW renewables portfolio. Real-time turbine "
            "telemetry feeds into Snowflake for predictive maintenance modeling, reducing "
            "unplanned downtime and maximizing generation output."
        ),
        "metric": "Predictive maintenance across 4,000+ wind turbines",
        "link": "https://www.snowflake.com/customers/",
    },
    {
        "name": "EDF (Électricité de France)",
        "tag": "Customer 360",
        "desc": (
            "EDF built a unified Customer 360 on Snowflake, consolidating AMI data, CRM, "
            "billing, and outage history into a single governed view of each customer. "
            "This powers personalized energy advisory, C&I segment analytics, and churn "
            "prediction models — a directly replicable pattern for AEP's 5.6M customers."
        ),
        "metric": "Single customer view unified across 7 source systems",
        "link": "https://www.snowflake.com/en/customers/all-customers/case-study/edf/",
    },
    {
        "name": "Uniper",
        "tag": "Energy Trading & Risk",
        "desc": (
            "Uniper, one of Europe's largest energy traders, built a real-time trading analytics "
            "platform on Snowflake — ingesting market prices, position data, and risk metrics "
            "to optimize hedging decisions and meet regulatory reporting requirements. "
            "Replaced overnight batch P&L with intraday dashboards and automated risk alerts."
        ),
        "metric": "Real-time P&L and VaR dashboards replacing overnight batch reporting",
        "link": "https://www.snowflake.com/en/customers/all-customers/case-study/uniper/",
    },
]

# ── Data Scientist resources ───────────────────────────────────────────────
# To add a new resource: copy one block and append to the appropriate category.
DS_RESOURCES = {
    "Getting started": [
        {
            "title": "Snowpark for Python — Quick Start",
            "desc": "Write Python, Pandas, and scikit-learn workflows that run natively inside Snowflake.",
            "link": "https://quickstarts.snowflake.com/guide/getting_started_with_snowpark_for_python/",
            "badge": "Quickstart",
        },
        {
            "title": "Snowflake Notebooks — Getting Started",
            "desc": "Interactive cell-based development directly in Snowsight. No infra to manage.",
            "link": "https://docs.snowflake.com/en/user-guide/ui-snowsight/notebooks",
            "badge": "Docs",
        },
        {
            "title": "Snowflake ML — Overview",
            "desc": "End-to-end ML platform: Feature Store, Model Registry, Cortex AI, and MLOps.",
            "link": "https://docs.snowflake.com/en/developer-guide/snowflake-ml/overview",
            "badge": "Docs",
        },
    ],
    "Cortex AI (LLMs & GenAI)": [
        {
            "title": "Cortex AI Functions Reference",
            "desc": "AI_COMPLETE, AI_EXTRACT, AI_CLASSIFY, AI_SENTIMENT, AI_REDACT, AI_TRANSLATE — all in SQL.",
            "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql",
            "badge": "Docs",
        },
        {
            "title": "Cortex Analyst — Natural Language to SQL",
            "desc": "Let business users ask questions in plain English. Build semantic models with YAML.",
            "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst",
            "badge": "Docs",
        },
        {
            "title": "Cortex Search — RAG in Snowflake",
            "desc": "Hybrid semantic + keyword search over enterprise documents. No external vector DB needed.",
            "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview",
            "badge": "Docs",
        },
        {
            "title": "Cortex Agents — Multi-step AI Workflows",
            "desc": "Orchestrate AI tasks across structured and unstructured data with full RBAC enforcement.",
            "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents",
            "badge": "Docs",
        },
        {
            "title": "Build a GenAI App with Cortex AI — Quickstart",
            "desc": "End-to-end walkthrough: ingest documents, create a search service, and build a chat UI.",
            "link": "https://quickstarts.snowflake.com/guide/getting_started_with_cortex_search/",
            "badge": "Quickstart",
        },
    ],
    "ML & model development": [
        {
            "title": "Snowflake Model Registry",
            "desc": "Version, govern, and deploy ML models. Track metrics, lineage, and reproducibility.",
            "link": "https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview",
            "badge": "Docs",
        },
        {
            "title": "Snowflake Feature Store",
            "desc": "Create reusable feature pipelines for model training and batch/online inference.",
            "link": "https://docs.snowflake.com/en/developer-guide/snowflake-ml/feature-store/overview",
            "badge": "Docs",
        },
        {
            "title": "Cortex Fine-tuning",
            "desc": "Fine-tune LLMs on your own data. Account-scoped — models never leave Snowflake.",
            "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-finetuning",
            "badge": "Docs",
        },
        {
            "title": "ML Functions (AutoML)",
            "desc": "Forecasting, anomaly detection, classification — no ML expertise required.",
            "link": "https://docs.snowflake.com/en/guides-overview-ml-functions",
            "badge": "Docs",
        },
    ],
    "Best practices": [
        {
            "title": "Data Engineering Best Practices",
            "desc": "Dynamic Tables, Streams/Tasks, Snowpipe, and cost-efficient pipeline design.",
            "link": "https://docs.snowflake.com/en/user-guide/data-pipelines-intro",
            "badge": "Guide",
        },
        {
            "title": "Performance Optimization Guide",
            "desc": "Clustering, query profiling, caching, warehouse sizing, and cost monitoring.",
            "link": "https://docs.snowflake.com/en/user-guide/warehouses-overview",
            "badge": "Guide",
        },
        {
            "title": "Security & Data Governance Best Practices",
            "desc": "RBAC, Masking Policies, Row Access Policies, classification, and audit.",
            "link": "https://docs.snowflake.com/en/user-guide/security-access-control-overview",
            "badge": "Guide",
        },
        {
            "title": "Snowflake Quickstarts Library",
            "desc": "100+ hands-on labs covering data engineering, ML, GenAI, and Streamlit apps.",
            "link": "https://quickstarts.snowflake.com/",
            "badge": "Labs",
        },
    ],
}

# ── New innovations ────────────────────────────────────────────────────────
# To add a new innovation: copy one block and append to this list.
INNOVATIONS = [
    {
        "icon": "🤖",
        "title": "Cortex AI Guardrails",
        "badge": "GA — Enterprise",
        "desc": (
            "Runtime protection against prompt injection and jailbreak attacks. "
            "Centrally enabled via ALTER ACCOUNT — covers Cortex Code, CoWork, and Agents."
        ),
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-ai-guardrails",
    },
    {
        "icon": "🔌",
        "title": "Snowflake-managed MCP Server",
        "badge": "GA",
        "desc": (
            "Connect Claude, ChatGPT, Cursor, and any MCP client directly to Snowflake. "
            "Expose Cortex Search, Cortex Analyst, and custom tools via a standards-based interface."
        ),
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp",
    },
    {
        "icon": "🏔️",
        "title": "Apache Iceberg Tables",
        "badge": "GA",
        "desc": (
            "Open table format with full read/write support. Own your data in S3/Azure/GCS "
            "while querying it with Snowflake's governed engine — no vendor lock-in."
        ),
        "link": "https://docs.snowflake.com/en/user-guide/tables-iceberg",
    },
    {
        "icon": "⚡",
        "title": "Dynamic Tables",
        "badge": "GA",
        "desc": (
            "Declarative data pipelines that auto-refresh on a configurable lag target. "
            "Replace complex Streams + Tasks chains with a single SQL SELECT statement."
        ),
        "link": "https://docs.snowflake.com/en/user-guide/dynamic-tables-intro",
    },
    {
        "icon": "🧠",
        "title": "Snowflake CoWork",
        "badge": "GA",
        "desc": (
            "Enterprise AI assistant for business users. Ask questions in natural language, "
            "get answers grounded in your governed Snowflake data — no SQL required."
        ),
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/snowflake-cowork",
    },
    {
        "icon": "🔬",
        "title": "Cortex Fine-tuning",
        "badge": "GA",
        "desc": (
            "Train domain-specific LLMs on your own data entirely within Snowflake. "
            "Fine-tuned models are account-scoped and never available to other customers."
        ),
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-finetuning",
    },
    {
        "icon": "🌐",
        "title": "Cortex Agents + Tool Orchestration",
        "badge": "GA",
        "desc": (
            "Multi-step AI workflows that coordinate across Cortex Search, Cortex Analyst, "
            "web search, and custom stored procedures — with full RBAC at every step."
        ),
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents",
    },
    {
        "icon": "📊",
        "title": "AI Observability",
        "badge": "GA",
        "desc": (
            "Evaluate and monitor GenAI app quality using LLM-as-a-judge metrics: "
            "groundedness, context relevance, answer relevance, and correctness."
        ),
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability",
    },
]

# ── Changelog (most recent first) ─────────────────────────────────────────
# To log an update: add a new entry at the TOP of this list.
CHANGELOG = [
    {
        "date": "August 2026",
        "text": "Initial launch — utility success stories, Data Scientists hub, and innovations hub.",
    },
    # ADD NEW ENTRIES ABOVE THIS LINE
    # {"date": "Month YYYY", "text": "Description of what was added or changed."},
]


# ═════════════════════════════════════════════════════════════════════════════
#  ▲▲▲  END OF DATA LAYER  ▲▲▲
# ═════════════════════════════════════════════════════════════════════════════


# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR NAVIGATION
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 8px 0 16px 0;'>
      <span style='font-size:2rem;'>❄️</span><br>
      <span style='font-weight:900; color:#1A1A1A; font-size:1.1rem;'>Snowflake, the AEP Data Platform</span><br>
      <span style='color:#8A999E; font-size:0.75rem;'>Innovation Hub</span>
    </div>
    """, unsafe_allow_html=True)

    nav = st.radio(
        "Navigate",
        [
            ":material/home: Overview",
            ":material/bolt: Utility success stories",
            ":material/lightbulb: AEP use cases",
            ":material/layers: Medallion architecture",
            ":material/science: Data scientists hub",
            ":material/rocket_launch: New innovations",
            ":material/code: Cortex Code (CoCo)",
            ":material/history: Changelog",
        ],
        label_visibility="collapsed",
    )

    st.space("large")
    st.markdown("""
    <div style='background:#FAFAFA; border-radius:10px; padding:12px 14px; border:1px solid #F0DEDE;'>
      <div style='font-weight:700; color:#1A1A1A; font-size:0.85rem; margin-bottom:6px;'>
        🤝 Your Snowflake team
      </div>
      <div style='color:#8A999E; font-size:0.78rem; line-height:1.6;'>
        <strong>Elyse Youngs</strong> · Account Executive<br>
        <strong>Bryan Christ</strong> · Sales Engineer<br>
        <span style='color:#C41230; font-weight:600;'>✉ Contact your AE to add content</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.space(16)
    st.caption("Last updated: August 2026")
    st.caption("[trust.snowflake.com](https://trust.snowflake.com) · [docs.snowflake.com](https://docs.snowflake.com)")


# ─────────────────────────────────────────────────────────────────────────────
# HERO (shown on all pages)
# ─────────────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
  <h1>❄️ &nbsp;Snowflake, the AEP Data Platform</h1>
  <p>Your living resource for Snowflake platform innovation, utility industry success stories,
     and everything your Data Science team needs to build faster on Snowflake.</p>
</div>
""", unsafe_allow_html=True)

st.space("small")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: OVERVIEW
# ─────────────────────────────────────────────────────────────────────────────
if "Overview" in nav:
    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown('<div class="section-header">Why Snowflake for utilities</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">The data platform built for regulated, complex, multi-entity enterprises.</div>', unsafe_allow_html=True)

        pillars = [
            ("🔒", "Security-first architecture",
             "Row Access Policies, Column Masking, Tri-Secret Secure encryption, and AI-specific access controls — governance that extends automatically to every AI workload."),
            ("🔗", "Single platform for all data",
             "Structured operational data, unstructured documents, streaming telemetry, and AI models — all in one governed platform. No data silos, no separate vector databases."),
            ("⚡", "AI that stays inside your perimeter",
             "Cortex AI runs LLM inference entirely within Snowflake's security boundary. No external API calls, no data sent to third parties. ISO 42001:2023 AI governance certified."),
            ("📋", "Regulatory & compliance ready",
             "SOC 2 Type II, ISO 27001, HITRUST r2, PCI-DSS 4.0, FedRAMP High. Full audit trail in QUERY_HISTORY and ACCESS_HISTORY for SOX, PUCO, and FERC filings."),
            ("🏭", "Built for utilities",
             "Smart meter analytics, grid reliability, wildfire risk modeling, renewable forecasting, rate case data management — proven across 40+ utility customers worldwide."),
        ]
        for icon, title, desc in pillars:
            with st.container(border=True):
                c1, c2 = st.columns([1, 12])
                with c1:
                    st.markdown(f"<div style='font-size:1.4rem; padding-top:2px;'>{icon}</div>",
                                unsafe_allow_html=True)
                with c2:
                    st.markdown(f"**{title}**")
                    st.caption(desc)

    with col2:
        st.markdown('<div class="section-header">Quick links</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Key resources for AEP&#39;s Cyber & EA review.</div>', unsafe_allow_html=True)

        quick_links = [
            ("✅", "AI Trust & Safety FAQ",
             "https://www.snowflake.com/en/legal/compliance/snowflake-ai-trust-and-safety/"),
            ("🛡️", "Compliance Center (SOC 2, ISO 42001, FedRAMP)",
             "https://trust.snowflake.com"),
            ("📄", "Data Processing Addendum",
             "https://www.snowflake.com/en/legal/addenda/data-processing-addendum/"),
            ("👥", "Sub-processors & Affiliates",
             "https://www.snowflake.com/en/legal/privacy/snowflake-sub-processors/"),
            ("📚", "Full AI & ML Documentation",
             "https://docs.snowflake.com/en/guides-overview-ai-features"),
            ("🚀", "Snowflake Quickstarts",
             "https://quickstarts.snowflake.com"),
            ("📡", "Platform Status",
             "https://status.snowflake.com"),
        ]
        for icon, label, url in quick_links:
            st.markdown(f"{icon} &nbsp; [{label}]({url})", unsafe_allow_html=True)
            st.space(4)

        st.space("small")
        st.info(
            "All compliance reports are available for self-service download at "
            "[trust.snowflake.com](https://trust.snowflake.com) — no NDA required.",
            icon=":material/download:",
        )

        st.space("small")
        st.markdown('<div class="section-header">Workiva integration</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">AEP&#39;s regulatory filing innovation.</div>', unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("**Snowflake + Workiva** = governed data foundation + filing execution")
            st.caption(
                "Snowflake serves as the single source of truth for FERC, PUCO, and SOX filings. "
                "The Workiva connector pulls from governed Snowflake views via OAuth — "
                "masking policies apply before any data reaches Workiva."
            )
            st.markdown("[Workiva + Snowflake connector →](https://app.snowflake.com/marketplace/providers/GZSTZJ2FPN/Workiva)")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: AEP USE CASES
# ─────────────────────────────────────────────────────────────────────────────
elif "AEP use cases" in nav:
    st.markdown('<div class="section-header">AEP use cases on Snowflake</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Five high-value platform use cases — grounded in real customer evidence and active Snowflake partnerships.</div>',
        unsafe_allow_html=True,
    )

    for uc in AEP_USE_CASES:
        partner_badge = (
            f"<span style='display:inline-block; background:{uc['partner_color']}1A; "
            f"color:{uc['partner_color']}; border:1px solid {uc['partner_color']}40; "
            f"border-radius:6px; padding:2px 10px; font-size:0.72rem; font-weight:700; "
            f"margin-bottom:12px;'>{uc['partner']}</span>"
        )
        link_html = (
            f"<br><a class='res-link' href='{uc['link']}' target='_blank'>{uc['link_label']}</a>"
            if uc["link"] else ""
        )
        st.markdown(f"""
<div class="approach-card" style="margin-bottom:16px; border-left:4px solid #C41230; border-top:none;">
  <div style="font-size:1.6rem; margin-bottom:8px;">{uc['icon']}</div>
  <div class="approach-name" style="font-size:1.05rem;">{uc['title']}</div>
  {partner_badge}
  <div class="approach-desc">{uc['desc']}{link_html}</div>
</div>
""", unsafe_allow_html=True)

    st.space("large")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: MEDALLION ARCHITECTURE
# ─────────────────────────────────────────────────────────────────────────────
elif "Medallion" in nav:
    st.markdown('<div class="section-header">Medallion architecture on Snowflake</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">A three-tier data refinement pattern — and the native Snowflake capabilities to build it.</div>',
        unsafe_allow_html=True,
    )

    # Tier flow diagram
    st.markdown("""
<div class="medallion-flow">
  <div class="medallion-tier bronze">
    <div class="medallion-tier-label">Tier 1</div>
    <div class="medallion-tier-name">🥉 Bronze</div>
    <div class="medallion-tier-desc">Raw data ingested as-is — full fidelity, append-only. The system of record for everything that entered the platform.</div>
    <span class="medallion-tag">Smart meter reads</span>
    <span class="medallion-tag">SCADA telemetry</span>
    <span class="medallion-tag">Weather feeds</span>
    <span class="medallion-tag">Outage events</span>
    <span class="medallion-tag">CIS exports</span>
    <span class="medallion-tag">Work orders</span>
  </div>
  <div class="medallion-arrow">&#9658;</div>
  <div class="medallion-tier silver">
    <div class="medallion-tier-label">Tier 2</div>
    <div class="medallion-tier-name">🥈 Silver</div>
    <div class="medallion-tier-desc">Validated, deduplicated, and schema-conformed. Business rules applied, formats standardized, bad records quarantined.</div>
    <span class="medallion-tag">Validated meter data</span>
    <span class="medallion-tag">Cleansed customer records</span>
    <span class="medallion-tag">Standardized asset data</span>
    <span class="medallion-tag">Enriched outage records</span>
    <span class="medallion-tag">Conformed grid events</span>
  </div>
  <div class="medallion-arrow">&#9658;</div>
  <div class="medallion-tier gold">
    <div class="medallion-tier-label">Tier 3</div>
    <div class="medallion-tier-name">🥇 Gold</div>
    <div class="medallion-tier-desc">Business-ready aggregates, domain marts, and ML feature stores. Optimized for analytics, dashboards, and AI model training.</div>
    <span class="medallion-tag">Load forecasting features</span>
    <span class="medallion-tag">Customer usage aggregates</span>
    <span class="medallion-tag">Grid health KPIs</span>
    <span class="medallion-tag">Regulatory reporting</span>
    <span class="medallion-tag">ML training datasets</span>
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="section-header">Native Snowflake approaches</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Pick the pattern that fits your team and pipeline requirements — or combine them.</div>',
        unsafe_allow_html=True,
    )

    # Approach cards — 3 per row
    approach_chunks = [MEDALLION_APPROACHES[i:i+3] for i in range(0, len(MEDALLION_APPROACHES), 3)]
    for chunk in approach_chunks:
        cols = st.columns(len(chunk))
        for col, approach in zip(cols, chunk):
            with col:
                st.markdown(f"""
<div class="approach-card">
  <div class="approach-icon">{approach['icon']}</div>
  <div class="approach-name">{approach['name']}</div>
  <div class="approach-badge">{approach['badge']}</div>
  <div class="approach-desc">{approach['desc']}</div>
  <div class="approach-tiers">Best for: <b>{approach['tiers']}</b> &nbsp;·&nbsp;
    <a class="res-link" href="{approach['link']}" target="_blank">Docs ↗</a>
  </div>
</div>
""", unsafe_allow_html=True)
        st.space("small")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: UTILITY SUCCESS STORIES
# ─────────────────────────────────────────────────────────────────────────────
elif "Utility success" in nav:
    st.markdown('<div class="section-header">Utility customer success stories</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Snowflake powers the data platforms of leading electric, gas, and renewable utilities worldwide.</div>',
        unsafe_allow_html=True,
    )

    # Render cards in rows of 3
    for i in range(0, len(UTILITY_CUSTOMERS), 3):
        row = UTILITY_CUSTOMERS[i : i + 3]
        cols = st.columns(len(row), gap="medium")
        for col, c in zip(cols, row):
            with col:
                st.markdown(f"""
                <div class="cust-card">
                  <div class="cust-name">{c['name']}</div>
                  <div class="cust-tag">{c['tag']}</div>
                  <div class="cust-desc">{c['desc']}</div>
                  <div class="cust-metric">📈 &nbsp;<b>{c['metric']}</b></div>
                </div>
                """, unsafe_allow_html=True)
        st.space("small")

    st.space("medium")
    st.success(
        "**Want to add a new customer story?** Edit the `UTILITY_CUSTOMERS` list "
        "at the top of this file and redeploy — takes under 2 minutes.",
        icon=":material/add_circle:",
    )
    st.markdown(
        "View the full customer gallery: [snowflake.com/customers](https://www.snowflake.com/customers/)",
    )

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: DATA SCIENTISTS HUB
# ─────────────────────────────────────────────────────────────────────────────
elif "Data scientists" in nav:
    st.markdown('<div class="section-header">🔬 Data scientists hub</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Everything AEP&#39;s data science team needs — best practices, new capabilities, and hands-on labs.</div>',
        unsafe_allow_html=True,
    )

    # Platform at a glance
    cap1, cap2, cap3, cap4 = st.columns(4, gap="small")
    caps = [
        ("🐍", "Snowpark Python", "Run Python, Pandas & sklearn inside Snowflake"),
        ("📓", "Notebooks", "Interactive cells directly in Snowsight"),
        ("🤖", "Cortex AI", "25+ LLMs. SQL interface. No infra."),
        ("🏗️", "Model Registry", "Version, govern & deploy ML models"),
    ]
    for col, (icon, title, desc) in zip([cap1, cap2, cap3, cap4], caps):
        with col:
            with st.container(border=True):
                st.markdown(f"<div style='font-size:1.6rem; text-align:center;'>{icon}</div>",
                            unsafe_allow_html=True)
                st.markdown(f"**{title}**", help=desc)
                st.caption(desc)

    st.space("medium")

    # Resource tabs by category
    categories = list(DS_RESOURCES.keys())
    tabs = st.tabs([f":material/folder: {c}" for c in categories])

    for tab, category in zip(tabs, categories):
        with tab:
            resources = DS_RESOURCES[category]
            for r in resources:
                badge_color = {
                    "Quickstart": "blue", "Docs": "green",
                    "Guide": "orange", "Labs": "violet",
                }.get(r["badge"], "gray")
                st.markdown(f"""
                <div class="res-card">
                  <div class="res-title">
                    {r['title']}
                    &nbsp; <span style="background:{'#E8F5E9' if badge_color=='green' else '#FFF3E0' if badge_color=='orange' else '#EDE7F6' if badge_color=='violet' else '#E3F2FD'}; color:{'#1B5E20' if badge_color=='green' else '#E65100' if badge_color=='orange' else '#311B92' if badge_color=='violet' else '#0D47A1'}; border-radius:6px; padding:2px 8px; font-size:0.7rem; font-weight:700;">{r['badge']}</span>
                  </div>
                  <div class="res-desc">{r['desc']}</div>
                  <a class="res-link" href="{r['link']}" target="_blank">
                    ↗ Open documentation
                  </a>
                </div>
                """, unsafe_allow_html=True)

    st.space("medium")

    # Energy / utility ML use cases
    st.markdown('<div class="section-header">Utility-specific ML use cases</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Common patterns AEP can implement using Snowflake ML and Cortex AI.</div>', unsafe_allow_html=True)

    use_cases = [
        ("⚡", "Outage prediction & grid reliability",
         "Train anomaly detection models on AMI meter data, transformer load, and weather signals. "
         "Deploy via Snowpark UDFs for real-time scoring at scale."),
        ("🌿", "Renewable generation forecasting",
         "Combine ISO-NE/MISO market data, satellite irradiance, and wind data in Snowflake. "
         "Train and serve time-series forecasting models using ML Functions or Snowpark."),
        ("🔥", "Wildfire & vegetation risk modeling",
         "Spatial ML on LiDAR, vegetation proximity, and asset condition data. "
         "AI_CLASSIFY for automated inspection report triage and risk scoring."),
        ("👥", "Customer churn & satisfaction",
         "AI_SENTIMENT on customer interaction text. Predictive churn models on billing and outage history. "
         "Served directly to Cognos/Power BI via governed Snowflake views."),
        ("📄", "Regulatory document intelligence",
         "AI_EXTRACT and AI_PARSE_DOCUMENT for FERC filings, rate case exhibits, and compliance PDFs. "
         "AI_COMPLETE for QA and consistency checks before Workiva submission."),
        ("💡", "Energy theft & revenue protection",
         "Anomaly detection on AMI consumption patterns. "
         "ML models trained on historical theft cases, deployed as Snowpark UDFs on streaming meter data."),
        ("🚨", "AMI anomaly detection — life & property safety",
         "Streaming AMI and operational telemetry ingested via Snowpipe Streaming feeds "
         "Snowflake ML anomaly detection models that flag patterns indicative of gas leak signatures, "
         "electrical faults, or dangerous over-consumption — enabling near-real-time dispatch alerts "
         "before incidents escalate. Notification integrations route alerts directly to field crews. "
         "The same infrastructure protects medically vulnerable customers on baseline programs."),
    ]
    for i in range(0, len(use_cases), 2):
        pair = use_cases[i : i + 2]
        cols = st.columns(len(pair), gap="medium")
        for col, (icon, title, desc) in zip(cols, pair):
            with col:
                with st.container(border=True):
                    st.markdown(f"**{icon} &nbsp; {title}**")
                    st.caption(desc)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: NEW INNOVATIONS
# ─────────────────────────────────────────────────────────────────────────────
elif "New innovations" in nav:
    st.markdown('<div class="section-header">🚀 New Snowflake innovations</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Recent platform releases most relevant to AEP&#39;s data strategy and Cortex AI adoption.</div>',
        unsafe_allow_html=True,
    )

    for i in range(0, len(INNOVATIONS), 4):
        row = INNOVATIONS[i : i + 4]
        cols = st.columns(len(row), gap="small")
        for col, item in zip(cols, row):
            with col:
                st.markdown(f"""
                <div class="innov-card">
                  <div class="innov-icon">{item['icon']}</div>
                  <div class="innov-badge">{item['badge']}</div>
                  <div class="innov-title">{item['title']}</div>
                  <div class="innov-desc">{item['desc']}</div>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(f"[Learn more →]({item['link']})")
        st.space("small")

    st.space("medium")
    st.info(
        "**Stay current:** Subscribe to Snowflake's What's New at "
        "[docs.snowflake.com/release-notes/new-features](https://docs.snowflake.com/release-notes/new-features) "
        "for weekly platform updates.",
        icon=":material/notifications:",
    )

    st.space("small")
    st.markdown('<div class="section-header">AI model landscape (June 2026)</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">All models run inside Snowflake\'s security perimeter — no external API calls.</div>', unsafe_allow_html=True)

    model_data = {
        "Provider": ["Anthropic", "Anthropic", "OpenAI", "OpenAI", "Meta", "Meta", "Mistral", "DeepSeek", "Google", "Snowflake"],
        "Model family": ["Claude Opus 4.x", "Claude Sonnet/Haiku 4.x", "GPT-5 / GPT-5.1 / GPT-5.2", "GPT-5-mini / GPT-4.1", "Llama 4 (Maverick, Scout)", "Llama 3.1 (8B, 70B, 405B)", "Mistral Large2 / Mixtral", "DeepSeek R1", "Gemini 3.1 Pro", "Snowflake-Llama 3.3-70B"],
        "Context window": ["1M tokens", "200K–1M tokens", "272K tokens", "128–272K tokens", "128K tokens", "128K tokens", "32–128K tokens", "32K tokens", "1M tokens", "128K tokens"],
        "Status": ["GA / Preview", "GA", "GA", "GA", "GA", "GA", "GA", "GA", "Preview", "GA"],
    }
    import pandas as pd
    df = pd.DataFrame(model_data)
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Status": st.column_config.TextColumn("Status"),
        },
    )

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: CORTEX CODE (COCO)
# ─────────────────────────────────────────────────────────────────────────────
elif "Cortex Code" in nav:
    # Intro banner
    st.markdown("""
<div class="coco-intro">
  <div class="coco-eyebrow">Snowflake Native · No Setup Required</div>
  <h2>⚡ Cortex Code (CoCo)</h2>
  <p>Snowflake's AI-powered IDE — built directly into your Snowflake account. Write SQL and
     Python with AI assistance, build semantic views, generate notebooks, deploy Cortex Agents,
     and execute expert workflows, all without leaving your data platform or moving data outside
     your security perimeter.</p>
</div>
""", unsafe_allow_html=True)

    # Feature cards — 3 per row
    st.markdown('<div class="section-header">What CoCo can do</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Six core capabilities available to AEP today.</div>',
        unsafe_allow_html=True,
    )
    feature_chunks = [COCO_FEATURES[i:i+3] for i in range(0, len(COCO_FEATURES), 3)]
    for chunk in feature_chunks:
        cols = st.columns(len(chunk))
        for col, feat in zip(cols, chunk):
            with col:
                st.markdown(f"""
<div class="coco-feature-card">
  <div class="coco-feature-icon">{feat['icon']}</div>
  <div class="coco-feature-name">{feat['name']}</div>
  <div class="coco-feature-desc">{feat['desc']}</div>
</div>
""", unsafe_allow_html=True)
        st.space("small")

    st.space("small")

    # Example prompts
    st.markdown('<div class="section-header">AEP example prompts</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Copy any of these into CoCo to get started immediately.</div>',
        unsafe_allow_html=True,
    )
    for prompt in COCO_PROMPTS:
        st.markdown(f"""
<div class="coco-prompt-card">
  <div class="coco-prompt-label">Try this in CoCo</div>
  <div class="coco-prompt-text">"{prompt['text']}"</div>
  <span class="coco-prompt-tag">{prompt['tag']}</span>
</div>
""", unsafe_allow_html=True)

    st.space("large")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: CHANGELOG
# ─────────────────────────────────────────────────────────────────────────────
elif "Changelog" in nav:
    st.markdown('<div class="section-header">📋 Changelog</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">A record of every update to this living document.</div>',
        unsafe_allow_html=True,
    )

    for entry in CHANGELOG:
        st.markdown(f"""
        <div class="changelog-item">
          <div class="changelog-date">📅 &nbsp; {entry['date']}</div>
          <div class="changelog-text">{entry['text']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.space("large")
    st.markdown('<div class="section-header">✏️ How to update this document</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">This page is designed to be maintained by the Snowflake account team.</div>', unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("**To add a new utility customer story:**")
        st.code("""
# In the UTILITY_CUSTOMERS list, add a new entry:
{
    "name": "Company Name",
    "tag": "Use Case Category",
    "desc": "2-3 sentence description of what they built and the outcome.",
    "metric": "Key result or metric",
    "link": "https://www.snowflake.com/customers/...",
}
        """, language="python")

    with st.container(border=True):
        st.markdown("**To add a new resource to the Data Scientists hub:**")
        st.code("""
# In DS_RESOURCES, append to the relevant category:
{
    "title": "Resource title",
    "desc": "One-line description.",
    "link": "https://docs.snowflake.com/...",
    "badge": "Docs",  # Options: Docs, Quickstart, Guide, Labs
}
        """, language="python")

    with st.container(border=True):
        st.markdown("**To add a new innovation card:**")
        st.code("""
# In INNOVATIONS, add a new entry:
{
    "icon": "🆕",
    "title": "Feature name",
    "badge": "GA",  # or "Preview" or "New"
    "desc": "2-3 sentence description.",
    "link": "https://docs.snowflake.com/...",
}
        """, language="python")

    with st.container(border=True):
        st.markdown("**To log an update in the changelog:**")
        st.code("""
# At the TOP of CHANGELOG (most recent first):
{"date": "Month YYYY", "text": "What was added or changed."},
        """, language="python")

    st.space("medium")
    st.success(
        "**Deploying updates:** Upload the updated `.py` file to your Snowflake stage, "
        "or paste directly into Snowsight > Streamlit > your app. "
        "Changes are live instantly — no restart required.",
        icon=":material/cloud_upload:",
    )


# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <div>
    ❄️ &nbsp; <strong>Snowflake, the AEP Data Platform</strong> &nbsp;·&nbsp;
    Prepared by the Snowflake Account Team &nbsp;·&nbsp;
    Confidential
  </div>
  <div>
    <a href="https://trust.snowflake.com">Trust Center</a> &nbsp;·&nbsp;
    <a href="https://docs.snowflake.com">Documentation</a> &nbsp;·&nbsp;
    <a href="https://status.snowflake.com">Status</a>
  </div>
</div>
""", unsafe_allow_html=True)

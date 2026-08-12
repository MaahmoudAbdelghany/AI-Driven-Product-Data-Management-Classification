# Task Tracker

## Sprint 1: Core Pipeline — Local Development

- [x] **Step 1:** Set up repository structure, pyproject.toml, .gitignore ✅
- [x] **Step 2:** Generate synthetic demo dataset (`sample_products_raw.csv`)
- [ ] **Step 3:** Define taxonomy tree (`taxonomy.json`)
- [ ] **Step 4:** Build `schema.py` — Pydantic models
- [ ] **Step 5:** Build `config.py` — Pipeline configuration
- [ ] **Step 6:** Build `utils.py` — Shared utilities
- [ ] **Step 7:** Build `taxonomy.py` — Taxonomy loading/validation
- [ ] **Step 8:** Build `preprocessor.py` — Data cleaning functions
- [ ] **Step 9:** Build `llm_classifier.py` — Bedrock integration with few-shot prompts
- [ ] **Step 10:** Build `agentic_enricher.py` — Missing field inference
- [ ] **Step 11:** Build `scraper.py` — Basic web scraper demo
- [ ] **Step 12:** Write unit tests
- [ ] **Step 13:** Run pipeline locally on full demo dataset, verify output quality

## Sprint 2: AWS Infrastructure

- [ ] **Step 14:** Build CDK stacks (storage, pipeline, app)
- [ ] **Step 15:** Write Lambda function handlers
- [ ] **Step 16:** Deploy infrastructure with `cdk deploy`
- [ ] **Step 17:** Test end-to-end: S3 → Lambda → Step Functions → DynamoDB

## Sprint 3: Streamlit App + Polish

- [ ] **Step 18:** Build Streamlit app with all 4 pages
- [ ] **Step 19:** Build embedded analytics dashboard (Plotly)
- [ ] **Step 20:** Dockerize Streamlit app
- [ ] **Step 21:** Deploy to ECS via CDK
- [ ] **Step 22:** Write README with architecture diagram
- [ ] **Step 23:** Integration tests against deployed infrastructure

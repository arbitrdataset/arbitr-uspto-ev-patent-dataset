# Arbitr USPTO EV Patent Dataset for Electric Vehicles (EV)

This repository contains the **documentation and examples** for the
**Arbitr USPTO EV Patent Dataset** – a curated subset of USPTO patents and applications
focused on **Electric Vehicles (EV), batteries, charging and power electronics**.

The actual data is hosted on **Hugging Face**:
👉 Sample: https://huggingface.co/datasets/arbitrdatasets/arbitr-uspto-ev-sample
👉 Full commercial dataset: *available on request (see below)*

---

## 1. What is this dataset?

The **Arbitr USPTO EV Dataset** is a cleaned and structured patent dataset built from
USPTO bulk data (PTGRDT + APPDT). It focuses on technologies related to:

- Electric vehicles (EV)
- Batteries and energy storage
- Charging infrastructure
- Power electronics and motor control
- EV propulsion and powertrain systems

Key features:

- USPTO **patents + applications** in the EV domain
- CPC focus on classes such as **Y02T, B60L, B60K, B60W, H02J, H02P, H02K, H01M**
- Normalized fields (dates, assignees, IDs, classifications)
- Parquet + JSONL format, ready for **Python, pandas, Spark, DuckDB, LLM pipelines**
- Designed for **ML, NLP, LLM training, innovation analytics and IP strategy**

---

## 2. Where is the data?

This GitHub repository does **not** store the full dataset.
Instead, it provides documentation and code examples.

✅ **Public sample** (small preview, free):
  https://huggingface.co/datasets/arbitrdatasets/arbitr-uspto-ev-sample

  💼 **Full commercial dataset** (large, production-ready):
  Available directly from Arbitr Inc. – see [How to get access](#5-how-to-get-access).

The sample on Hugging Face has the **same schema** as the full dataset,
so any code written against the sample will work on the full data (subject to license).

---

## 3. Typical use cases

This dataset is useful for:

- **EV and battery OEMs** – tracking competitors and technology trends
- **VC / PE investors** – mapping EV innovation and IP risk
- **Consulting firms** – technology and market-intelligence projects
- **Data science & ML teams** – training models on patent texts and metadata
- **Academic and policy research** – studying EV innovation patterns

Example tasks:

- Long-term trend analysis of EV patents by CPC class
- Mapping assignees and new entrants in the EV ecosystem
- Building prior-art search tools and semantic search over EV patents
- Training domain-specific LLMs or embedding models on EV patent text

---
## 4. Quick start with the sample (Python)

Below is a minimal example showing how to load the sample data from Hugging Face.

```bash
pip install datasets pandas pyarrow

from datasets import load_dataset
import pandas as pd

# Load the sample dataset from Hugging Face
ds = load_dataset("arbitrdatasets/arbitr-uspto-ev-sample")

# Access the Parquet files locally if you cloned the repo from HF
patents = pd.read_parquet("data/patents/patents_2025-10.parquet")
applications = pd.read_parquet("data/applications/applications_2025-10.parquet")

print(patents.head())
print(applications.head())

More examples are available in the examples/ folder.

Great — ab main tumhare liye **FINAL, upload-ready, cleaned README.md** bana rahi hoon.
Tumhein sirf email aur website add karni hogi.
Baaki sab **already perfect format** mein hai.

---

# ⭐ **FINAL README.md (copy–paste as-is)**

👇 Isay full copy karo → GitHub → README.md → Edit → Poora paste → Save.
Sirf email + website replace karna hai.

````
# Arbitr USPTO EV Patent Dataset for Electric Vehicles (EV)

This repository provides documentation and usage examples for the 
Arbitr USPTO EV Patent Dataset — a curated subset of USPTO patents and applications 
focused on Electric Vehicles (EV), batteries, charging systems, and power electronics.

The dataset itself is hosted externally on Hugging Face:

👉 Public Sample (free):  
https://huggingface.co/datasets/arbitrdatasets/arbitr-uspto-ev-sample  

👉 Full commercial dataset:  
Available on request (see “How to get access”).

---

## 1. What is this dataset?

The dataset is built from USPTO bulk data (PTGRDT + APPDT) and filtered to EV-related CPC classes.  
It includes:

- Electric vehicles and propulsion systems  
- Batteries and energy storage  
- Charging infrastructure  
- Power electronics and motor control  
- EV powertrain subsystems  

### Key Features
- USPTO patents + applications (2015–2025)  
- CPC focus: Y02T, B60L, B60K, B60W, H02J, H02P, H02K, H01M  
- Cleaned, normalized, and aligned fields  
- Delivered in Parquet + JSONL  
- Ready for analytics, ML, NLP, LLM training, semantic search  

---

## 2. Where is the data?

This repository does not include the full dataset.  
It provides documentation and examples only.

- Public Sample (free):  
  https://huggingface.co/datasets/arbitrdatasets/arbitr-uspto-ev-sample  

- Full Commercial Dataset:  
  Request access from Arbitr Inc (details below).  

The sample uses the same schema as the full dataset, so you can develop on the sample and 
run at scale on the commercial version.

---

## 3. Typical use cases

- Tracking EV & battery innovation  
- Modeling trends across CPC classes  
- Competitor and assignee mapping  
- Building semantic search tools  
- Training domain-specific embeddings or LLMs  
- Prior-art and landscape analysis  
- Academic and policy research  

---

## 4. Quick start with the sample (Python)

```bash
pip install datasets pandas pyarrow
````

```python
from datasets import load_dataset
import pandas as pd

# Load directly from Hugging Face
ds = load_dataset("arbitrdatasets/arbitr-uspto-ev-sample")

# Example local usage (if sample is downloaded)
patents = pd.read_parquet("data/patents/patents_2025-10.parquet")
applications = pd.read_parquet("data/applications/applications_2025-10.parquet")

print(patents.head())
print(applications.head())
```

More examples are available in the `examples/` folder.

---

## 5. How to get access to the full dataset

The full Arbitr USPTO EV Dataset (2015–2025, hundreds of thousands of records)
is available under a commercial license.

**Price:** USD 4,990 (one-time, perpetual internal use)

To request access, contact:

**Email:** <arbitrinc.com/datasets>
**Website:** <arbitrinc.com/datasets>

Include:

* Name + organization
* Expected use case (analytics, ML, consulting, etc.)
* Whether you want one-time access or recurring updates

You will receive a response within 24 hours.

---

## 6. Licensing (summary)

This dataset is derived from public-domain USPTO sources and then:

* filtered to the EV domain
* cleaned and normalized
* packaged into analytics-ready formats
* distributed under the Arbitr Inc Commercial Dataset License

Short usage summary:

* You may use the dataset internally for research, analytics, model building
* You may use derived models/insights in commercial products
* You may not resell or redistribute the raw dataset

Full license text is available on Hugging Face (`LICENSE_Arbitr_Commercial.txt`).

© Arbitr Inc, 2025. Not affiliated with USPTO.

---

## 7. Related links

* Hugging Face sample: [https://huggingface.co/datasets/arbitrdatasets/arbitr-uspto-ev-sample](https://huggingface.co/datasets/arbitrdatasets/arbitr-uspto-ev-sample)  
* Website: <arbitrinc.com/datasets>
* Contact: <Arbitrdataset@gmail.com>


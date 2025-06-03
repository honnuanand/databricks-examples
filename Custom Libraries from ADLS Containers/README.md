# Custom Libraries in Databricks (DBR 15.x and Above)

This example demonstrates the **prescribed, supported approach** to loading custom Python libraries in Databricks starting with **Databricks Runtime (DBR) 15.x** and beyond.

---

## 🚀 Core Intent

Starting with DBR 15.x, Databricks **no longer allows**:
- `%pip install` at the cluster level  
- `dbutils.library.install()` or `installPyPI()`  
- Direct `conda install` or `pip install` on clusters

To ensure consistency, reproducibility, and stability,  
the supported methods are now:

✅ **Notebook-scoped `%pip install`** → affects only the notebook session  
✅ **Cluster or workspace libraries** → attach prebuilt `.whl` or `.egg` files via UI or cluster config  
✅ **Init scripts (advanced)** → for automated, team-wide setups

> ✅ Instead, Databricks **prescribes two supported methods** for loading custom libraries:
> 1. **Workspace Files**
> 2. **External Storage (e.g., ADLS) with `%pip install` from `.whl` files**


| **Feature / Aspect**            | **Workspace Files**                                 | **ADLS (Azure Data Lake Storage)**                                                |
|-------------------------------|-----------------------------------------------------|-----------------------------------------------------------------------------------|
| 🛠️ Setup Complexity            | ✅ Simple — upload via UI or CLI                    | ⚠️ Moderate — requires secret scope, no mounts in Azure Gov                       |
| 🔐 Security & Access Control    | ✅ Workspace ACLs                                   | ✅ Better — uses Azure IAM + secret scopes                                        |
| 📦 Library Packaging            | ✅ Use raw `.py` files or folders                   | ✅ Supports `.whl`, `.egg` for structured, versioned deployment                   |
| 🔄 Version Control              | ✅ Git-backed Repos possible                        | ❌ Manual — but supports CI/CD pipelines                                          |
| ♻️ Reusability Across Notebooks | ✅ Yes, within workspace                            | ✅ Yes — portable across clusters/workspaces                                      |
| 🚀 Deployment Speed             | ✅ Fast for dev/test                                | ⚠️ Copy required (no mounts in Azure Gov)                                        |
| 💾 Persistence                  | ✅ Tied to workspace                                | ✅ Long-term, survives workspace/cluster changes                                  |
| 🧪 Best for                     | Dev/test, quick iterations                         | ✅ Production, secure CI/CD, Gov cloud compliant                                  |
| ⚠️ Limitations                 | ❌ Workspace bloat, no clean versioning             | ❌ Needs file copy (no mount), more setup overhead                                |
| 🔌 External Access / Automation | ✅ Via UI, API, or Git integration                  | ✅ Excellent for automated externalized pipelines                                 |
| 🧠 DBR Compatibility (15.x+)    | ✅ Fully supported                                  | ✅ Fully supported — use copy approach (mount not supported in Gov)              |


| **Use Case**                             | **Preferred Method**                          |
|------------------------------------------|-----------------------------------------------|
| Dev/test (any cloud)                     | ✅ Workspace Files                             |
| Production (Azure Gov or Commercial)     | ✅ ADLS with secret-based access (no mount)    |
| Secure deployment pipelines              | ✅ ADLS + `.whl` packaging                     |
| Quick script reuse within a notebook     | ✅ Workspace Files                             |
---
## Option 1 - **Workspace Files**
📦 Upload your .py or .whl files to:
	•	Workspace Files (/Workspace/Users/<your_email>/lib_folder/)
	•	These files are version-controlled, accessible via notebooks, and secure
	•	Supports both .py and .whl modules
```Python
import sys
sys.path.append("/Workspace/Users/your.name@databricks.com/lib_folder")
import mylib
mylib.greet("Anand")
```
---
## Option 2 - **External Storage (e.g., ADLS) with `%pip install` from `.whl` files**
---
## 📦 What This Example Covers

This example shows how to:
1. Build a **custom Python library** (`mylib`) as a proper, versioned package  
2. Upload the `.whl` file to Databricks (via DBFS or ADLS)  
3. Install the library **notebook-scoped** using `%pip install`  
4. Import and use it inside notebooks **without relying on deprecated methods**

---

✅ **Notebooks included:**
### 📔 Notebooks in This Folder

This folder includes Databricks notebooks that:
- Walk through the setup steps interactively  
- Show how to configure Spark for ADLS access  
- Demonstrate uploading `.py` files, mounting ADLS paths, and reading from them  
- Provide end-to-end flows for using the packaged library inside notebooks

✅ **Notebooks included:**
- `00_Setup and Access-ADLS-Container from the Notebook.ipynb` → Create Databricks secret, set up ADLS access, and verify connectivity  
- `01_ADLS_Library_Setup.ipynb` → Prepare the custom Python library and upload it to ADLS  
- `02_ADLS_Library_Usage.ipynb` → Use the uploaded library inside Databricks notebooks


✅ These notebooks act as **step-by-step guides** and are the primary reference for running the examples in Databricks.
---

## 📁 Repository Structure

```text
mylib_package/
├── mylib/
│   ├── __init__.py      # Makes the package importable
│   └── core.py          # Contains example functions (greet, add, multiply)
├── setup.py             # Packaging config for setuptools
└── README.md            # This documentation
```

---

## 💡 Why This Matters

✅ Aligns with Databricks’ modern library management best practices  
✅ Avoids manual file drops or `sys.path` hacks  
✅ Enables reproducible, versioned deployments  
✅ Prepares teams for cluster-wide installation via workspace libraries or automation

---

## 📚 Usage Workflow (Summary)

1️⃣ On your local machine:
```bash
pip install --upgrade setuptools wheel
python setup.py bdist_wheel
```

2️⃣ Upload the generated `.whl` (in `dist/`) to:
- **DBFS** (e.g., `dbfs:/tmp/mylib-0.1-py3-none-any.whl`)  
- **OR ADLS container**

3️⃣ In the Databricks notebook:
```python
%pip install /dbfs/tmp/mylib-0.1-py3-none-any.whl
```

4️⃣ Restart the kernel:
```python
%restart_python
```

5️⃣ Import and use:
```python
import mylib
print(mylib.greet("Anand"))
```

---

## ⚙️ Notes for Cluster-Wide Installation

If you want the library available across all notebooks and jobs on a cluster:
- Go to **Workspace → Libraries → Install New → Upload**
- Upload the `.whl` file
- Attach it to the desired cluster

---

## 🔗 References

- [Databricks: Managing Libraries](https://learn.microsoft.com/en-us/azure/databricks/libraries/object-storage-libraries)
- [Databricks Runtime 15.x Release Notes](https://docs.databricks.com/release-notes/runtime/15.x.html)

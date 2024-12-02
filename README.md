# Python Strings /  Bonus - A1 Class
> **`Algo-S1-3-Python`**

You can generate the presentation of this notebook with 2 **different** methods.
1. Jupyter Extension via Visual Studio Code ![](https://api.iconify.design/devicon-plain:vscode.svg?color=%23ffffff) 
2. Jupyter Notebook × RISE ![](https://api.iconify.design/devicon-plain:jupyter.svg?color=%23ffffff) 

> [!CAUTION]
> **DO NOT** mix these 2 installation, unless if you want to lose your time and your storage space...

## ![](https://api.iconify.design/devicon-plain:vscode.svg?color=%23ffffff) Visual Studio Code (recommended)
Install **[Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)** on your Visual Studio Code and run
```bash
# Generate the presentation
jupyter nbconvert presentation.ipynb --to slides --post serve
```
---

## ![](https://api.iconify.design/devicon-plain:jupyter.svg?color=%23ffffff) Jupyter Notebook × RISE

### ![](https://api.iconify.design/devicon-plain:linux.svg?color=%23ffffff) Linux / ![](https://api.iconify.design/ic:baseline-apple.svg?color=%23ffffff) macOS installation
```bash
# Create a new virtual environment
python -m venv .venv

# Activate a virtual environment
source .venv/bin/activate

# Install packages
python3 -m pip install -r requirements.txt
```

### ![](https://api.iconify.design/bi:windows.svg?color=%23ffffff) Windows installation
```bash
# Create a new virtual environment
python -m venv .venv

# Activate a virtual environment
.venv\Scripts\activate

# Install packages
python -m pip install -r requirements.txt
```

### ![](https://api.iconify.design/devicon-plain:jupyter.svg?color=%23ffffff) Jupyter Notebook execution
```bash
# Run Jupyter Notebook
jupyter notebook
```

2. Open **`presentation.ipynb`**
3. Click on ![](https://api.iconify.design/lucide:bar-chart-3.svg?color=%23ffffff) RISE Slideshow button

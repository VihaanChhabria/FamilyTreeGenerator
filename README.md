# FamilyTreeGenerator

## Setting Up the Development Environment
This section outlines the steps to get you started working on this project. It includes instructions for cloning the Git repository, creating a virtual environment to isolate project dependencies, and installing required packages.

### Prerequisites
- Git installed on your system (download from https://git-scm.com/)
- Python installed on your system (download from https://www.python.org/)

### Steps
1. Clone the Repository
```
git clone https://github.com/VihaanChhabria/FamilyTreeGenerator.git
```

2. Create a Virtual Environment
```
cd FamilyTreeGenerator  # Navigate to the project directory
python -m venv env  # Create a virtual environment named 'env'
```

3. Activate the Virtual Environment
```
source venv/bin/activate  # Linux/macOS (activate the environment)
# OR
venv\Scripts\activate.bat  # Windows (activate the environment)
```

4. Install Dependencies
```
pip install -r requirements.txt
```

## Todo
- separate people into generations
- find way to draw family tree
- make gui
- add a info system (you hover/click a person and it tells birth, death, full name, ...)

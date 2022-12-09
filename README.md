# Automated Testing Toy Example

In this project, we'll practice using Pytest to automatically test the functionality of three kinds of files:
  - **Python Modules**: Can we import the functions?  Do they behave as expected?
  - **Python Scripts**: Does the script run without error?  Does it behave as expected?
  - **Jupyter Notebooks**: Does the notebook run without error?  Does it behave as expected?
  


## Toy Dataset: Titanic Survival Analysis

Did passenger class, sex, and age have an effect of who survived the Titanic disaster of 1912?  This analysis says yes!

### Directions

  1. `tests/test_utils.py`
  
  - Test that the `titanic_utils.is_adult()` function behaves correctly on three different ages.
    
  -  For example, `assert is_adult(11) == False`
    
  2. `tests/test_data_download_script.py`
  
  - Test that the `scripts/download_data.py` file runs without errors (for extra credit, that it creates the `data/raw/titanic.csv` file)
    
  - The `runpy.run_path()` function is particularly helpful for this.  
    
  - `os.path.exists()`, `os.remove()`, and `shutils.rmtree()` can also be helpful here.
    
  3. `tests/test_analysis_notebook.py`
  
  - Test that the `notebooks/anlayze_data.ipynb` file runs without errors (for extra credit, that it creates the `results/survival_rate.jpg` file)
  
  - `subprocess.check_output()` is a useful function here, when used to call `jupyter nbconvert --to notebook --execute my_notebook.ipynb`
  
  - `os.path.exists()`, `os.remove()`, and `shutils.rmtree()` can also be helpful here.
    


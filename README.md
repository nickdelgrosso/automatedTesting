# Automated Testing Toy Example

In this project, we'll practice using Pytest to automatically test the functionality of three kinds of files:
  - **Python Modules**: Can we import the functions?  Do they behave as expected?
  - **Python Scripts**: Does the script run without error?  Does it behave as expected?
  - **Jupyter Notebooks**: Does the notebook run without error?  Does it behave as expected?
  


## Toy Dataset: Titanic Survival Analysis

Did passenger class, sex, and age have an effect of who survived the Titanic disaster of 1912?  This analysis says yes!


### Directions

#### Write Automated tests for each python code file

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
    

#### Push your changes to a new fork of this repository


#### Add a GitHub Action that runs the tests on push

Do this in the web browser.  Use the `Python Package using Anaconda` or `Python Application` templates under the `GitHub Actions` tab to get started.

*Tip*: Start with a small number of tests, re-running the pipeline stepwise to ensure that it continues to work.



## Packaging and Publishing

### Publishing on PyPI

| Step | Description |
| :-- | :-- | 
| `pyproject.toml`| [Make the file in the root directory that contains the build instructions and project metadata](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-pyproject-toml)
| `pip install build; python -m build` | Builds distribution files in a venv using the `pyproject.toml` file | 
| `pip install twine; twine check dist/*` | Check that the dist files have the needed metadata |
| `twine upload --repository-url=https://test.pypi.org/legacy/ dist/*` | [Upload the dist files](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives).  Make sure you have an account on the test.pypi.org site. |


### Github Actions: Deploy on Tagged Push or Release

| Step | Description |
| :-- | :-- |
| `git tag -a v1.4 -m "my version 1.4";` | [Make an annotated tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
| `git push origin --tags` | Push tags |
| `  if: github.event_name == 'push' && startsWith(github.ref, 'refs/tags')` | [In the GA step, only does the step if there was a tag](https://github.com/pypa/gh-action-pypi-publish#usage) |
| `  release:    types: [ created ]` | Run workflow on GH release creation |





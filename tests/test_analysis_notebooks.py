from subprocess import check_output


def test_notebook_runs_without_error():
    check_output([
        'jupyter',
        'nbconvert',
        '--to',
        'notebook',
        '--execute',
        'notebooks/analyze_data.ipynb',
    ])
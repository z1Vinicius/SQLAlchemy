import warnings
from sqlalchemy import exc

# for warnings not included in regex-based filter below, just log
warnings.filterwarnings("always", category=exc.RemovedIn20Warning)

# for warnings related to execute() / scalar(), raise
for msg in [
    r"The (?:Executable|Engine)\.(?:execute|scalar)\(\) function",
    r"The current statement is being autocommitted using implicit autocommit,",
    r"The connection.execute\(\) method in SQLAlchemy 2.0 will accept "
    "parameters as a single dictionary or a single sequence of "
    "dictionaries only.",
    r"The Connection.connect\(\) function/method is considered legacy",
    r".*DefaultGenerator.execute\(\)",
]:
    warnings.filterwarnings(
        "error",
        message=msg,
        category=exc.RemovedIn20Warning,
    )
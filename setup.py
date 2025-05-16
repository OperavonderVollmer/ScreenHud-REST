from setuptools import setup, find_packages

setup(
    name="ScreenHUD-REST",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "dotenv",
        "setuptools",
        "fastapi",
        "uvicorn",
        "OperaPowerRelay @ git+https://github.com/OperavonderVollmer/OperaPowerRelay@main",
        "ScreenHud-Forecast @ git+https://github.com/OperavonderVollmer/ScreenHud-Forecast@main"
    ],
    python_requires=">=3.7",
    author="Opera von der Vollmer",
    description="Forecast plugin for Opera's ScreenHUD",
    url="https://github.com/OperavonderVollmer/ScreenHUD-Forecast", 
    license="MIT",
)

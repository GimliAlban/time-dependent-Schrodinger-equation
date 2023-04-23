# Solving the Time Dependent Schrodinger Equation

This Project originate in 2017, when I was in my last year of Physic bachelor in University of Cergy-Pontoise.

During my last year of bachelor, I had a end of study internship where I was asked to solve the Time Dependent
Schrodinger Equation using the Finite Difference method.

At that time, I developed the algorithm using Fortran90 and since then I acquired a lot of knowledge in python
and wanted to challenge myself into redoing the project with python.

The article followed to develop this project is the following:

[A fast explicit algorithm for the time-dependent Schrodinger equation - P.B. Visscher](AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAApowggKWBgkqhkiG9w0BBwagggKHMIICgwIBADCCAnwGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMenxh1bc_2KXuatFHAgEQgIICTZAivFwXfeeaImUaqsSSh2ZzJWOh2hMZHiJ_06lmS4OYh1X9p18L9EQDLGjiHYkhGDgwmN34J60g50D7JwVFyIEumiCw_ZqGQxWGSJMXS4RnlxPjPaKzPTNe0vIoimV0G)

On the other hand, I though it could be a good idea to showcase my python knowledge and good practice.

# Running The Project

I used python 3.11.3 for this project.
```
python -m venv venv
```

Windows:
```
.\venv\Scripts\activate
```

Linux:
```
source .\venv\bin\activate.csh
```

Install dependencies:
```
pip install -r requirements.txt
pip install -r tests/requirements.txt
pip install -r docs/requirements.txt
```

# Run Tests

Source the virtual environment and simply run pytest:
```
(venv) ... > pytest
```

# Documentation

I used sphinx to generate the documentation. The documentation will be separated mainly into 2 parts.

The first one will be a review and overview of the method used (Finite Difference) and how it is applied to the Schrodinger Equation.

The Second part will focus on the documentation of each class or function of the project.

## Generate the documentation

```
cd docs
```

Windows:
```
.\make.bat html
```

Linux:
```
make html
```




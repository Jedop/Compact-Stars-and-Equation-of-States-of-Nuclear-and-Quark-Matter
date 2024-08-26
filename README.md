# Introduction
This is a summer project that I did in the summer of 2024 under Dr. Saumen Datta from TIFR. In this project, I learnt about Compact Stars and Dense Matter, equations of states of various models of a neutron star, and how to compute mass vs radius
relations for various initial conditions. The models vary from simple to fairly involved. I used **Newtonian equations** for the models, hence they don't have actually accurate values. Although, it is not a very complicated matter to simply replace the equations 
with the appropriate relativistic versions.

## Non Interacting Nuclear Matter
This is a simple nuclear matter model for the neutron star. The details are in my [Summer project report](Summer_Project_Report.pdf). The non-relativistic approximation is programmed [here](non_relativistic_nuclear.py). The full model is programmed 
[here](full_EoS_nuclear.py).

## Non Interacting Quark Matter
This is a quark matter model for the neutron star. The model with massless quarks is programmed [here](massless_quark_model.py). The model with strange quark mass is programmed [here](strange_quark_model.py)

### Full Equation of State for non interacting nuclear matter
The full equation of state used in the [program](full_EoS_nuclear.py) is actually an approximation obtained by curve fitting the actual solution to the pressure and energy density equations to a rational expression involving $$\overline{p}$$ 
and $$\overline{\epsilon}$$. It is done in this [python program]().

# Results
Now it is time to show the results. To obtain the results for a range of initial pressure values, I simply ran the program for a range of pressure values, saved it to a csv file and then plotted it. This is a very trivial matter hence I have not 
included the program in this repository. Anyway, here are the results for the models
| **Model**                         | **Image**                     | **Number** |
|-----------------------------------|--------------------------------|------------|
| **Non-relativistic Nuclear Matter** | ![Non-relativistic Nuclear Matter](Results/output1.png) | 1          |
| **Full Nuclear Matter**           | ![Full Nuclear Matter](Results/output3.png) | 2          |
| **Massless Quark Model**          | ![Massless Quark Model](Results/output4.png) | 3          |
| **Strange Quark Model**           | ![Strange Quark Model](Results/output5.png) | 4          |




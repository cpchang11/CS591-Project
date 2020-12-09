import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
 
#seaborn style
sns.set()


# creating a data frame for COVID-19 cases per state
df = pd.read_csv("../CSV/united_states_covid19_cases_and_deaths_by_state.csv") 

#makes the chart
plt.figure(figsize=(13, 15))
plt.bar(x = df["State/Territory"], height = df["Total Cases"])
plt.xticks(rotation = 90)

# To get rid of scientific notation on the Y axis
# plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)

plt.tick_params(axis='both', which='major', labelsize=10)
plt.tick_params(axis='both', which='minor', labelsize=8)
plt.title('Total Cases by State/Territory', fontsize=25)
plt.xlabel('State/Territory', fontsize=14)
plt.ylabel('Total Cases', fontsize=14)
plt.savefig('Total_Cases_by_State_Territory.pdf')



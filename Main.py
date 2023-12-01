import os
import pandas as pd
import csv
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster


#Umfrage in data_matrix einlesen
file_path = 'Umfrage_Ergebnis_OT.csv'
data_matrix = []

with open(file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        data_matrix.append(row)

# Display the data matrix
for row in data_matrix:
    print(row)

#Clustering and exlude first row
linkage_data = linkage(data_matrix[1:], method='ward', metric='euclidean')
cluster = fcluster(linkage_data, criterion = 'distance', t = 10)
dendrogram(linkage_data)
plt.show()
#Count which Cluster is bigger to select Persona and Second Persona
counter1 = 0
counter2 = 0

for int in cluster:
    if int == 1:
        counter1 += 1
    if int == 2:
        counter2 += 1

print("Cluster 1:" + str(counter1))
print("Cluster 2:" + str(counter2))
print(cluster)

# Convert the matrix to a DataFrame
df = pd.DataFrame(data_matrix[1:], columns=data_matrix[0])

# Filter rows with clusterID = 1
clusterPersona_df = df[cluster == 1]
# Write Cluster 1 to CVS File
clusterPersona_df.to_csv("Persona.csv", index=False)
# Filter rows with clusterID = 2
clusterPersona2_df = df[cluster == 2]
clusterPersona2_df.to_csv("SecondPersona.csv", index=False)

# Create two matrices for cluster 1 and 2
cluster1_matrix = df[cluster == 1].to_numpy()
cluster2_matrix = df[cluster == 2].to_numpy()

# Display matrices
print("Persona")
for row in cluster1_matrix:
    print(row)
print("Second Persona")
for row in cluster2_matrix:
    print(row)

# Directories for graphics
folder_path1 = 'Group1'
folder_path2 = 'Group2'
# Functions to build graphics for cluster 1 and cluster 2
def count_occurrences(matrix, column_index):
    count = 0
    for row in matrix:
        if row[column_index] == '1':
            count += 1
    return count

def plot_distribution(labels, counts, x, title, filename, folder_path):
    plt.bar(labels, counts)
    plt.ylabel('Number of People')
    plt.xlabel(x)
    plt.title(title)
    plt.savefig(os.path.join(folder_path, filename))
    plt.close()

# Age
ageLabels = ['j', 'm', 'a']
#Group1
ageCounts = [count_occurrences(cluster1_matrix, 0), count_occurrences(cluster1_matrix, 1),
             count_occurrences(cluster1_matrix, 2)]
plot_distribution(ageLabels, ageCounts, 'Age Distribution', 'Age Distribution Group 1', 'AgeGroup1.png', folder_path1)
#Group2
ageCounts = [count_occurrences(cluster2_matrix, 0), count_occurrences(cluster2_matrix, 1),
             count_occurrences(cluster2_matrix, 2)]
plot_distribution(ageLabels, ageCounts, 'Age Distribution', 'Age Distribution Group 2', 'AgeGroup2.png', folder_path2)

# Gender
gender_labels = ['male', 'female']
# Group 1
gender_counts = [count_occurrences(cluster1_matrix, 3), count_occurrences(cluster1_matrix, 4)]
plot_distribution(gender_labels, gender_counts, 'Gender Distribution', 'Gender Distribution Group 1', 'Gender.png', folder_path1)
# Gender
#Group 2
gender_counts = [count_occurrences(cluster2_matrix, 3), count_occurrences(cluster2_matrix, 4)]
plot_distribution(gender_labels, gender_counts, 'Gender Distribution', 'Gender Distribution Group 2', 'Gender.png', folder_path2)

# Working column 5
working = 0
notWorking = 0
for row in cluster1_matrix:
    if row[5] == '1':
        working += 1
    if row[5] == '0':
        notWorking += 1

# Graphic for Working Group 1
columns = ['employed', 'unemployed']
counts = [working, notWorking]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Employed Group 1')
file_path = os.path.join(folder_path1,'EmployedGroup1.png')
plt.savefig(file_path)
plt.close()

# Working column 5
working = 0
notWorking = 0
for row in cluster2_matrix:
    if row[5] == '1':
        working += 1
    if row[5] == '0':
        notWorking += 1

# Graphic for Working Group 2
columns = ['employed', 'unemployed']
counts = [working, notWorking]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Employed Group 2')
file_path = os.path.join(folder_path2,'Employed.png')
plt.savefig(file_path)
plt.close()

# Pensum
pensum_labels = ['80 -100%','60 -79%', '40 - 59%']
# Group 1
pensum_counts = [count_occurrences(cluster1_matrix, 6), count_occurrences(cluster1_matrix, 7),
                 count_occurrences(cluster1_matrix, 8)]
plot_distribution(pensum_labels, pensum_counts, 'Work Pensum', 'Pensum Group 1', 'PensumGroup1.png', folder_path1)
# Group 2
pensum_counts = [count_occurrences(cluster2_matrix, 6), count_occurrences(cluster2_matrix, 7),
                 count_occurrences(cluster2_matrix, 8)]
plot_distribution(pensum_labels, pensum_counts, 'Work Pensum', 'Pensum Group 2','PensumGroup2.png', folder_path2)


# Education
# column 9 none
# column 10 matur
# column 11 EBA
# column 12 EFZ
# column 13 BSc
# column 14 MSc
# column 15 PhD
education_labels = ['No Education', 'Matura', 'EBA', 'EFZ', 'BSc', 'MSc', 'PhD']
# Group 1
education_counts = [
    count_occurrences(cluster1_matrix, 9),
    count_occurrences(cluster1_matrix, 10),
    count_occurrences(cluster1_matrix, 11),
    count_occurrences(cluster1_matrix, 12),
    count_occurrences(cluster1_matrix, 13),
    count_occurrences(cluster1_matrix, 14),
    count_occurrences(cluster1_matrix, 15)
]
plot_distribution(education_labels, education_counts, 'Education Level', 'Education Group 1', 'EducationGroup1.png', folder_path1)
# Group 2
education_counts = [
    count_occurrences(cluster2_matrix, 9),
    count_occurrences(cluster2_matrix, 10),
    count_occurrences(cluster2_matrix, 11),
    count_occurrences(cluster2_matrix, 12),
    count_occurrences(cluster2_matrix, 13),
    count_occurrences(cluster2_matrix, 14),
    count_occurrences(cluster2_matrix, 15)
]
plot_distribution(education_labels, education_counts, 'Education Level', 'Education Group 2', 'EducationGroup2.png', folder_path2)

# Work
# column 16 none
# column 17 Landwirtschaft
# column 18 Produktion
# column 19 Dienstleistungen
work_labels = ['No Work', 'Agriculture', 'Craft / Production', 'Service']
# Group 1
work_counts = [
    count_occurrences(cluster1_matrix, 16),
    count_occurrences(cluster1_matrix, 17),
    count_occurrences(cluster1_matrix, 18),
    count_occurrences(cluster1_matrix, 19)
]
plot_distribution(work_labels, work_counts, 'Field of Work', 'Work Group 1','WorkGroup1.png', folder_path1)
# Group 2
work_counts = [
    count_occurrences(cluster2_matrix, 16),
    count_occurrences(cluster2_matrix, 17),
    count_occurrences(cluster2_matrix, 18),
    count_occurrences(cluster2_matrix, 19)
]
plot_distribution(work_labels, work_counts, 'Field of Work', 'Work Group 2','WorkGroup2.png', folder_path2)

# HomeofficeDays
# column 20 1 day
# column 21 2 days
# column 22 3 days or more
office_labels = ['One', 'Two ', 'Three or More']
# Group 1
office_counts = [
    count_occurrences(cluster1_matrix, 20),
    count_occurrences(cluster1_matrix, 21),
    count_occurrences(cluster1_matrix, 22)
]

plot_distribution(office_labels, office_counts, 'Days in Homeoffice','Homeoffice Group 1', 'HomeofficeGroup1.png', folder_path1)
#Group 2
office_counts = [
    count_occurrences(cluster2_matrix, 20),
    count_occurrences(cluster2_matrix, 21),
    count_occurrences(cluster2_matrix, 22)
]

plot_distribution(office_labels, office_counts, 'Days in Homeoffice','Homeoffice Group 2','HomeofficeGroup2.png', folder_path2)

# Living Arrangement
# column 23 renting
# column 24 property
# column 25 other
living_labels = ['Renting', 'Property', 'Other']
#Group 1
living_counts = [
    count_occurrences(cluster1_matrix, 23),
    count_occurrences(cluster1_matrix, 24),
    count_occurrences(cluster1_matrix, 25)
]

plot_distribution(living_labels, living_counts, 'Arrangement', 'Living Situation Group 1','LivingArrangementGroup1.png', folder_path1)
# Group 2
living_counts = [
    count_occurrences(cluster2_matrix, 23),
    count_occurrences(cluster2_matrix, 24),
    count_occurrences(cluster2_matrix, 25)
]

plot_distribution(living_labels, living_counts, 'Arrangement', 'Living Situation Group 2', 'LivingArrangementGroup2.png', folder_path2)


#Rooms
# column 26 2
# column 27 3
# column 28 4
# column 29 5
# column 30 6
room_labels = ['Two', 'Three', 'Four', 'Five', 'Six']
# Group1
room_counts = [
    count_occurrences(cluster1_matrix, 26),
    count_occurrences(cluster1_matrix, 27),
    count_occurrences(cluster1_matrix, 28),
    count_occurrences(cluster1_matrix, 29),
    count_occurrences(cluster1_matrix, 30)
]

plot_distribution(room_labels, room_counts, 'Number of Rooms',
                  'Number of Rooms Group1', 'RoomNrGroup1.png', folder_path1)

# Group 2
room_counts = [
    count_occurrences(cluster2_matrix, 26),
    count_occurrences(cluster2_matrix, 27),
    count_occurrences(cluster2_matrix, 28),
    count_occurrences(cluster2_matrix, 29),
    count_occurrences(cluster2_matrix, 30)
]

plot_distribution(room_labels, room_counts, 'Number of Rooms','Number of Rooms Group 2', 'RoomNrGroup2.png', folder_path2)

#Household
# column 31 alone
# column 32 Partner / Flatshare
# column 33 family

houseHold_labels = ['Alone', 'Partner or Community', 'Family']
# Group 1
houseHold_counts = [
    count_occurrences(cluster1_matrix, 31),
    count_occurrences(cluster1_matrix, 32),
    count_occurrences(cluster1_matrix, 33)
]

plot_distribution(houseHold_labels, houseHold_counts, 'Household','Household Situation Group 1', 'HouseholdGroup1.png', folder_path1)
# Group 2
houseHold_counts = [
    count_occurrences(cluster2_matrix, 31),
    count_occurrences(cluster2_matrix, 32),
    count_occurrences(cluster2_matrix, 33)
]

plot_distribution(houseHold_labels, houseHold_counts, 'Household','Household Situation Group 2', 'HouseholdGroup2.png', folder_path2)
#Children
# column 34 none
# column 35 1
# column 36 2
# column 37 3
# column 38 4+

children_labels = ['No Children', 'One', 'Two', 'Three', 'Four or More']
# Group 1
children_counts = [
    count_occurrences(cluster1_matrix, 34),
    count_occurrences(cluster1_matrix, 35),
    count_occurrences(cluster1_matrix, 36),
    count_occurrences(cluster1_matrix, 37),
    count_occurrences(cluster1_matrix, 38)
]

plot_distribution(children_labels, children_counts, 'Amount of Children','Children Group 1', 'ChildrenGroup1.png', folder_path1)
# Group 2
children_counts = [
    count_occurrences(cluster2_matrix, 34),
    count_occurrences(cluster2_matrix, 35),
    count_occurrences(cluster2_matrix, 36),
    count_occurrences(cluster2_matrix, 37),
    count_occurrences(cluster2_matrix, 38)
]

plot_distribution(children_labels, children_counts, 'Amount of Children','Children Group 2', 'ChildrenGroup2.png', folder_path2)
# Hobby
# column 39 sport
# column 40 read
# column 41 cinema gaming
# column 42 other

hobbies_labels = ['Sport', 'Reading', 'Cinema or Gaming', 'Other Things']
# Group 1
hobbies_count = [
    count_occurrences(cluster1_matrix, 39),
    count_occurrences(cluster1_matrix, 40),
    count_occurrences(cluster1_matrix, 41),
    count_occurrences(cluster1_matrix, 42)
]

plot_distribution(hobbies_labels, hobbies_count, 'Hobbies', 'Hobbies Group 1','HobbiesGroup1.png', folder_path1)
# Group 2
hobbies_count = [
    count_occurrences(cluster2_matrix, 39),
    count_occurrences(cluster2_matrix, 40),
    count_occurrences(cluster2_matrix, 41),
    count_occurrences(cluster2_matrix, 42)
]

plot_distribution(hobbies_labels, hobbies_count, 'Hobbies', 'Hobbies Group 2','HobbiesGroup2.png', folder_path2)
# Environmental Awareness
# column 43 small
# column 44 middle
# column 45 big

awareness_labels = ['Small', 'Middle', 'Big']
# Group 1
awareness_counts = [
    count_occurrences(cluster1_matrix, 43),
    count_occurrences(cluster1_matrix, 44),
    count_occurrences(cluster1_matrix, 45)
]

plot_distribution(awareness_labels, awareness_counts, 'Environmental Awareness','Environmental Awareness Group 1 ', 'EnvironmentGroup1.png', folder_path1)
# Group 2
awareness_counts = [
    count_occurrences(cluster2_matrix, 43),
    count_occurrences(cluster2_matrix, 44),
    count_occurrences(cluster2_matrix, 45)
]

plot_distribution(awareness_labels, awareness_counts, 'Environmental Awareness','Environmental Awareness Group 2', 'EnvironmentGroup2.png', folder_path2)
# Cost Awareness
# column 46 small
# column 47 middle
# column 48 big
cost_labels = ['Small', 'Middle', 'Big']
# Group 1
cost_counts = [
    count_occurrences(cluster1_matrix, 46),
    count_occurrences(cluster1_matrix, 47),
    count_occurrences(cluster1_matrix, 48)
]
plot_distribution(cost_labels, cost_counts, 'Cost Awareness','Cost Awareness Group 1', 'CostsGroup1.png', folder_path1)
# Group 2
cost_counts = [
    count_occurrences(cluster2_matrix, 46),
    count_occurrences(cluster2_matrix, 47),
    count_occurrences(cluster2_matrix, 48)
]
plot_distribution(cost_labels, cost_counts, 'Cost Awareness','Cost Awareness Group 2', 'CostsGroup2.png', folder_path2)


# Interessted in Electricity Consumption
# column 49 yes or No
# Group 1
interested = 0
notInterested = 0
for row in cluster1_matrix:
    if row[49] == '1':
        interested += 1
    if row[49] == '0':
        notInterested += 1

columns = ['interested ', 'not interested']
counts = [interested, notInterested]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Interested in Electricity Consumption Group 1')
file_path = os.path.join(folder_path1, 'ElectricityGroup1.png')
plt.savefig(file_path)
plt.close()

# Group 2
interested = 0
notInterested = 0
for row in cluster2_matrix:
    if row[49] == '1':
        interested += 1
    if row[49] == '0':
        notInterested += 1

columns = ['interested ', 'not interested']
counts = [interested, notInterested]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Interested in Electricity Consumption Group 1')
file_path = os.path.join(folder_path2,'ElectricityGroup1.png' )
plt.savefig(file_path)
plt.close()

# Too much Electricity Consumption
# column 50 yes or No
# Group 1
yes = 0
no = 0
for row in cluster1_matrix:
    if row[50] == '1':
        yes += 1
    if row[50] == '0':
        no += 1

columns = ['yes ', 'no']
counts = [yes, no]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Feeling to consume to much Electricity Group 1')
file_path = os.path.join(folder_path1, 'ConsumptionGroup1.png' )
plt.savefig(file_path)
plt.close()

# Group 2

yes = 0
no = 0
for row in cluster2_matrix:
    if row[50] == '1':
        yes += 1
    if row[50] == '0':
        no += 1

columns = ['yes ', 'no']
counts = [yes, no]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Feeling to consume to much Electricity Group 2')
file_path = os.path.join(folder_path2,'ConsumptionGroup1.png' )
plt.savefig(file_path)
plt.close()


# Electricity Costs
# column 51 low
# column 52 ok
# column 53 to high

eCost_labels = ['low', 'ok', 'to high']
#Group 1
eCost_counts = [
    count_occurrences(cluster1_matrix, 51),
    count_occurrences(cluster1_matrix, 52),
    count_occurrences(cluster1_matrix, 53)
]
plot_distribution(eCost_labels, eCost_counts, 'Electricity Costs','Electricity Costs Group 1', 'ElectricityCostsGroup1.png', folder_path1)
#Group 2
eCost_counts = [
    count_occurrences(cluster2_matrix, 51),
    count_occurrences(cluster2_matrix, 52),
    count_occurrences(cluster2_matrix, 53)
]
plot_distribution(eCost_labels, eCost_counts, 'Electricity Costs', 'Electricity Costs Group 2', 'ElectricityCostsGroup2.png', folder_path2)


# Knowlege which devices consume a lot of electricity
# column 54 yes or no
# Group 1
yes = 0
no = 0
for row in cluster1_matrix:
    if row[54] == '1':
        yes += 1
    if row[54] == '0':
        no += 1

columns = ['yes ', 'no']
counts = [yes, no]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Knowledge which devices consume a lot of electricity')
file_path = os.path.join(folder_path1, 'KnowledgeGroup1.png')
plt.savefig(file_path)
plt.close()

yes = 0
no = 0
for row in cluster2_matrix:
    if row[54] == '1':
        yes += 1
    if row[54] == '0':
        no += 1

columns = ['yes ', 'no']
counts = [yes, no]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Knowledge which devices consume a lot of electricity')
file_path = os.path.join(folder_path2, 'KnowledgeGroup2.png')
plt.savefig(file_path)
plt.close()

#Proficient in energy-related matters.
# column 55 yes or no
#Group 1
yes = 0
no = 0
for row in cluster1_matrix:
    if row[55] == '1':
        yes += 1
    if row[55] == '0':
        no += 1

columns = ['yes ', 'no']
counts = [yes, no]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Proficient in Energy-Related Matters Group 1')
file_path = os.path.join(folder_path1,'ProficientGroup1 .png' )
plt.savefig(file_path)
plt.close()

#Group2
yes = 0
no = 0
for row in cluster2_matrix:
    if row[55] == '1':
        yes += 1
    if row[55] == '0':
        no += 1

columns = ['yes ', 'no']
counts = [yes, no]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Proficient in Energy-Related Matters Group 1')
file_path = os.path.join(folder_path2,'ProficientGroup1 .png')
plt.savefig(file_path)
plt.close()

#Motivations
# column 56 costs
#column 57 Environmental Reasons

motivation_labels = ['Cost', 'Environmental Reasons']
#Group 1
motivation_counts = [
    count_occurrences(cluster1_matrix, 56),
    count_occurrences(cluster1_matrix, 57),
]
plot_distribution(motivation_labels, motivation_counts, 'Motivation','Motivation Group 1', 'MotivationGroup1.png', folder_path1)
# Group 2
motivation_counts = [
    count_occurrences(cluster2_matrix, 56),
    count_occurrences(cluster2_matrix, 57),
]
plot_distribution(motivation_labels, motivation_counts, 'Motivation','Motivation Group 2', 'MotivationGroup2.png', folder_path2)
# Car
# column 58 yes or no
# column 59 electric
def count_Has_Cars(matrix, column_index):
    count_yes = 0
    count_no = 0

    for row in matrix:
        if row[column_index] == '1':
            count_yes += 1
        elif row[column_index] == '0':
            count_no += 1

    return count_yes, count_no

# Group 1
Ecar_count = count_occurrences(cluster1_matrix, 59)

Car_counts = count_Has_Cars(cluster1_matrix, 58)

columns = ['yes', 'no', 'electric car']
car_counts_values = list(Car_counts)
electric_car_counts_values = [0, Ecar_count]

# Creating separate bars for counts of 'yes' and 'no' for 'has cars' and 'electric cars'
plt.bar(columns[:2], car_counts_values, label='Has Cars')
plt.bar(columns[2], electric_car_counts_values, label='Electric Cars')

plt.ylabel('Number of People')
plt.title('Car Group 1')
plt.legend()

file_path = os.path.join(folder_path1, 'CarGroup1.png')
plt.savefig(file_path)
plt.close()

#Group 2
Ecar_count = count_occurrences(cluster2_matrix, 59)

Car_counts = count_Has_Cars(cluster2_matrix, 58)

columns = ['yes', 'no', 'electric car']
car_counts_values = list(Car_counts)
electric_car_counts_values = [0, Ecar_count]

# Creating separate bars for counts of 'yes' and 'no' for 'has cars' and 'electric cars'
plt.bar(columns[:2], car_counts_values, label='Has Cars')
plt.bar(columns[2], electric_car_counts_values, label='Electric Cars')

plt.ylabel('Number of People')
plt.title('Car Group 2')
plt.legend()

file_path = os.path.join(folder_path2, 'CarGroup2.png')
plt.savefig(file_path)
plt.close()
# Solaranlage
#column 60 yes or no
# Group 1
yes = 0
no = 0
for row in cluster1_matrix:
    if row[60] == '1':
        yes += 1
    if row[60] == '0':
        no += 1

columns = ['yes ', 'no']
counts = [yes, no]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Solaranlage Group 1')
file_path = os.path.join(folder_path1, 'SolaranlageGroup1 .png')
plt.savefig(file_path)
plt.close()

# Group 2
yes = 0
no = 0
for row in cluster2_matrix:
    if row[60] == '1':
        yes += 1
    if row[60] == '0':
        no += 1

columns = ['yes ', 'no']
counts = [yes, no]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Solaranlage Group 2')
file_path = os.path.join(folder_path2,'SolaranlageGroup2 .png' )
plt.savefig(file_path)
plt.close()

# Smartphone
# column 61 yes or no
# Group 1
yes = 0
no = 0
for row in cluster1_matrix:
    if row[61] == '1':
        yes += 1
    if row[61] == '0':
        no += 1

columns = ['yes ', 'no']
counts = [yes, no]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Smartphone Group 1')
file_path = os.path.join(folder_path1,'SmartphoneGroup1 .png')
plt.savefig(file_path)
plt.close()

# Group 2

yes = 0
no = 0
for row in cluster2_matrix:
    if row[61] == '1':
        yes += 1
    if row[61] == '0':
        no += 1

columns = ['yes ', 'no']
counts = [yes, no]
plt.bar(columns, counts)
plt.ylabel('Number of People')
plt.title('Smartphone Group 2')
file_path = os.path.join(folder_path2, 'SmartphoneGroup2 .png')
plt.savefig(file_path)
plt.close()
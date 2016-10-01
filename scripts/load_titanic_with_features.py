import pandas as pd
import operator
import re


def merge_titles(title):
    if title in ("Capt", "Sir", "Don",
                "Col", "Major", "Rev",
                "Jonkheer","Dr"):
        return "Mr"
    elif title in ("the Countess", "Mlle", "Mme", "Lady", "Ms"):
        return "Mrs"
    else:
        return title


def parse_title(name):
    return name.split(',')[1].split('.')[0].strip()

# A function to get the title from a name.
def get_title(name):
    # Use a regular expression to search for a title.
    # Titles always consist of capital and lowercase letters, and end with a period.
    title_search = re.search(' ([A-Za-z]+)\.', name)
    # If the title exists, extract and return it.
    if title_search:
        return title_search.group(1)
    return ""


def load_titanic(train_path, test_path):
    # A function to get the id given a row
    def get_family_id(row):
        # Find the last name by splitting on a comma
        last_name = row["Name"].split(",")[0]
        # Create the family id
        family_id = "{0}{1}".format(last_name, row["FamilySize"])
        # Look up the id in the mapping
        if family_id not in family_id_mapping:
            if len(family_id_mapping) == 0:
                current_id = 1
            else:
                # Get the maximum id from the mapping and
                # add one to it if we don't have an id
                current_id = (max(family_id_mapping.items(),
                                  key=operator.itemgetter(1))[1] + 1)
            family_id_mapping[family_id] = current_id
        return family_id_mapping[family_id]

    titanic = pd.read_csv(train_path)
    titanic_test = pd.read_csv(test_path)

    # process train set attributes
    titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
    titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
    titanic.loc[titanic["Sex"] == "female", "Sex"] = 1
    titanic["Embarked"] = titanic["Embarked"].fillna('S')
    titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
    titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
    titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2

    # process test set attributes
    titanic_test['Age'] = titanic_test['Age'].fillna(titanic['Age'].median())
    titanic_test.loc[titanic_test["Sex"] == "male", "Sex"] = 0
    titanic_test.loc[titanic_test["Sex"] == "female", "Sex"] = 1
    titanic_test["Embarked"] = titanic_test["Embarked"].fillna('S')
    titanic_test.loc[titanic_test["Embarked"] == "S", "Embarked"] = 0
    titanic_test.loc[titanic_test["Embarked"] == "C", "Embarked"] = 1
    titanic_test.loc[titanic_test["Embarked"] == "Q", "Embarked"] = 2
    titanic_test['Fare'] = titanic_test['Fare'].fillna(titanic['Fare'].median())

    # Generating a familysize column
    titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"]
    # The .apply method generates a new series
    titanic["NameLength"] = titanic["Name"].apply(lambda x: len(x))
    titanic_test["FamilySize"] = titanic_test["SibSp"] + titanic_test["Parch"]
    titanic_test['NameLength'] = titanic_test['Name'].apply(lambda x: len(x))

    # Get all the titles and print how often each one occurs.
    titles = titanic["Name"].apply(get_title)
    test_titles = titanic_test["Name"].apply(get_title)
    # Map each title to an integer.  Some titles are very rare,
    # and are compressed into the same codes as other titles.
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6,
                     "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10,
                     "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2,
                     "Dona":3}
    for k,v in title_mapping.items():
        titles[titles == k] = v
        test_titles[test_titles == k] = v
    # Add in the title column.
    titanic["Title"] = titles
    titanic_test["Title"] = test_titles

    # A dictionary mapping family name to id
    family_id_mapping = {}

    # Get the family ids with the apply method
    family_ids = titanic.apply(get_family_id, axis=1)
    # There are a lot of family ids, so we'll compress all
    # of the families under 3 members into one code.
    family_ids[titanic["FamilySize"] < 3] = -1
    test_family_ids = titanic_test.apply(get_family_id, axis=1)
    test_family_ids[titanic_test["FamilySize"] < 3] = -1
    titanic["FamilyId"] = family_ids
    titanic_test["FamilyId"] = test_family_ids

    predictors = ["Pclass", "Sex", "Age", "Fare", "Embarked",
                  "FamilySize", "Title", "FamilyId"]
    return titanic[predictors], titanic["Survived"], titanic_test[predictors]

if __name__ == "__main__":
    X_train, y, X_test, = load_titanic("../data/titanic_train.csv",
                                       "../data/titanic_test.csv")
    print(X_train)
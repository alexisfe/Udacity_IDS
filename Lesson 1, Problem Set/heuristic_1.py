import pandas
import warnings
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder

def encode(ds):
    le = LabelEncoder()
    le.fit(ds)
    return le.transform(ds)

def preprocess(df, predictors):
    imp = Imputer(axis=1)
    for c in df[predictors].columns:
        if df[c].dtype == 'object':
            df[c] = encode(df[c])
        elif c in ['Age', 'SibSp', 'Parch', 'Fare']:
            df[c] = imp.fit_transform(df[c]).T
    df.fillna(0)

def custom_heuristic(file_path):
    warnings.filterwarnings("ignore")
    '''
    In this exercise, we will perform some rudimentary practices similar to those of
    an actual data scientist.

    Part of a data scientist's job is to use her or his intuition and insight to
    write algorithms and heuristics. A data scientist also creates mathematical models
    to make predictions based on some attributes from the data that they are examining.

    We would like for you to take your knowledge and intuition about the Titanic
    and its passengers' attributes to predict whether or not the passengers survived
    or perished. You can read more about the Titanic and specifics about this dataset at:
    http://en.wikipedia.org/wiki/RMS_Titanic
    http://www.kaggle.com/c/titanic-gettingStarted

    In this exercise and the following ones, you are given a list of Titantic passengers
    and their associated information. More information about the data can be seen at the
    link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data.

    For this exercise, you need to write a simple heuristic that will use
    the passengers' gender to predict if that person survived the Titanic disaster.

    You prediction should be 78% accurate or higher.

    Here's a simple heuristic to start off:
       1) If the passenger is female, your heuristic should assume that the
       passenger survived.
       2) If the passenger is male, you heuristic should
       assume that the passenger did not survive.

    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger['Sex'] will return a string "female".

    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associated value should be 1 if the
    passenger survied or 0 otherwise.

    For example, if a passenger is predicted to have survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    And if a passenger is predicted to have perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0

    You can also look at the Titantic data that you will be working with
    at the link below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv
    '''


    df = pandas.read_csv(file_path)

    id = 'PassengerId'
    predictive = 'Survived'
    predictors_exc = ['Name', 'Ticket', 'Cabin', 'Survived']
    predictors_inc = df.drop([id] + predictors_exc + [predictive], axis=1).columns

    preprocess(df, predictors_inc)

    X_train, X_test, y_train, y_test = train_test_split(df[predictors_inc], df[predictive], test_size=0.2, random_state=0)

    rfc = RandomForestClassifier(n_estimators=120, min_samples_split=5, min_samples_leaf=5)

    rfc.fit(X_train, y_train)

    df[predictive] = rfc.predict(df[predictors_inc])

    #print "Prediction score on test set: ", rfc.score(X_test, y_test)

    predictions = dict(zip(df[id], df[predictive]))

    return predictions

res = complex_heuristic("https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv")
print res
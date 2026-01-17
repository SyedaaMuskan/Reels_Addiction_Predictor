import pandas as pd
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
df=pd.read_csv("reels_data.csv")
x=df.drop("addiction_level",axis=1)
y=df['addiction_level']
numerical_feature=[
    "reels_per_day",
    "avg_session_min",
    "night_sleep",
    "phone_pickup"
]
ordinal_feature=[
    'attention_span','breaks_taken'
]
ordinal_ct=[
    ['low','medium','high'],
    ['rare','sometimes','frequent']
]
nominal_features = ["night_scrolling", "mood_after_reels"]
tranformer=ColumnTransformer(
    transformers=[
        ('num','passthrough',numerical_feature),
        ('ord',OrdinalEncoder(categories=ordinal_ct),ordinal_feature),
        ('nom',OneHotEncoder(handle_unknown='ignore'),nominal_features)

    ]
)
Pipeline=Pipeline(steps=[
    ('transformer',tranformer),
    ('model',LogisticRegression(max_iter=1000))
])
x_tr,x_te,y_tr,y_te=train_test_split(x,y,test_size=0.2,random_state=42)
Pipeline.fit(x_tr,y_tr)
y_ped=Pipeline.predict(x_te)
print(classification_report(y_te,y_ped))
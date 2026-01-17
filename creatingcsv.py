import pandas as pd
import random
random.seed(42)
rows=[]
for i in range (300):
    reels_per_day=random.randint(10,150)
    avg_session_min=random.randint(2,90)
    phone_pickup=random.randint(10,120)
    night_sleep=round(random.uniform(4,9),1)
    night_scrolling=random.choice(['yes','no'])
    mood_after_reels=random.choice(['happy','numb','anxious'])
    attention_span=random.choice(['low','medium','high'])
    breaks_taken=random.choice(['rare','sometimes','frequent'])

    if reels_per_day <= 20 and night_sleep >= 6 and breaks_taken in ['frequent', 'sometimes']:
        addiction_level = 0  # Normal
    elif reels_per_day <= 35 and night_sleep >= 4 and breaks_taken in ['sometimes', 'rare']:
        addiction_level = 1  # Addicted
    else:
        addiction_level = 2  # Severely Addicted


    rows.append([
        reels_per_day,avg_session_min,phone_pickup,night_scrolling,mood_after_reels,attention_span,breaks_taken,night_sleep,addiction_level
    ])
columns=['reels_per_day','avg_session_min','phone_pickup','night_scrolling','mood_after_reels','attention_span','breaks_taken','night_sleep',
         'addiction_level'

    ]
df=pd.DataFrame(rows,columns=columns)   
df.to_csv("reels_data.csv",index=False)
print("csv generated")



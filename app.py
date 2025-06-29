import streamlit as st
import pandas as pd

def cronbach_alpha(df):
    df = df.dropna(axis=1, how='any')  # מוחק עמודות עם ערכים חסרים
    k = df.shape[1]
    variances = df.var(axis=0, ddof=1)
    total_var = df.sum(axis=1).var(ddof=1)
    if k <= 1 or total_var == 0:
        return 0
    alpha = (k / (k - 1)) * (1 - variances.sum() / total_var)
    return alpha

# הגדרות עיצוב כלליות
st.set_page_config(page_title="Cronbach Alpha Calculator", layout="wide")
st.title("חישוב מהימנות: אלפא קרונבאך")

# העלאת קובץ
uploaded_file = st.file_uploader("העלה קובץ Excel או CSV", type=["csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.write("תצוגה מקדימה של הנתונים:")
        st.dataframe(df)

        # סינון עמודות מספריות בלבד
        numeric_df = df.select_dtypes(include='number')

        if numeric_df.empty:
            st.warning("לא נמצאו עמודות מספריות לחישוב.")
        else:
            alpha = cronbach_alpha(numeric_df)
            st.success(f"אלפא קרונבאך: {alpha:.3f}")

    except Exception as e:
        st.error(f"שגיאה בקריאת הקובץ: {e}")

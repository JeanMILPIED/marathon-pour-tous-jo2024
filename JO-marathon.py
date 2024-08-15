import streamlit as st
import pandas as pd

#data
df=pd.read_csv("scrapped_raw_results.csv", index_col=0)
# Function to get rank based on bib number
def get_rank(bib_number):
    participant = df[df['bib_number'] == bib_number]
    if not participant.empty:
        return participant
    else:
        return None

# Streamlit App
st.set_page_config(page_title="Paris Marathon Pour Tous - Rank 🥇")

# 1. Display an image of the Paris Olympics games
st.image("./image/marathon.jpg", use_column_width=True)

# 2. Title
st.title("Your Rank in the Marathon Pour Tous - JO PARIS - 2024")

# 3. Form input for the participant's number
col1,col2, col3 = st.columns([2,5, 10])
col1.image("./image/maillot.JPG")
col2.header("Your Number")
with col3.form(key='rank_form'):
    bib_number = st.number_input('Enter your number', min_value=1, max_value=100000)
    submit_button = st.form_submit_button(label='Get Your Rank')

# 4. Display the rank based on the input
if submit_button:
    participant = get_rank(bib_number)
    if participant is not None:
        try:
            st.success('Your rank is: {}'.format(participant['rank'].values[0]))
        except:
            st.error('Your number is not found or no valid time recorded.')
            pass
        st.write("Your info")
        st.table(participant)
    else:
        st.error('Your number is not found or no valid time recorded.')

#5
st.image("./image/marathon.jpg", use_column_width=True)
#6
st.caption("The results are based on the official website from JO PARIS 2024")
st.caption("https://marathonpourtous.paris2024.org/fr/actus/2024/retrouve-tes-photos-ton-resultat/59")
import streamlit as st
import pandas as pd

#data
df=pd.read_csv("scrapped_results_good.csv", index_col=0)
df_ranked=df[["name","api_number","finish_time_brut","finish_time_net","rank_net","rank_brut"]]
# Function to get rank based on bib number
def get_rank(bib_number):
    participant = df_ranked[df_ranked['api_number'] == bib_number]
    if not participant.empty:
        return participant
    else:
        return None

# Streamlit App
st.set_page_config(page_title="Paris Marathon Pour Tous - Rank 🥇")

# 1. Display an image of the Paris Olympics games
st.image("./image/marathon.jpg", use_column_width=True)

# 2. Title
st.title("Marathon Pour Tous - JO PARIS - 2024")
st.write("**Get Your (unofficial) Rank**)
st.caption("warning - this is an unofficial Paris 2024 JO website")
st.divider()

# 3. Form input for the participant's number
col2, col3 = st.columns([5,5])
#col1.image("./image/maillot.JPG")
col2.header("🏃‍♂️Your Number")
with col3.form(key='rank_form'):
    bib_number = st.number_input('Input Your Number', min_value=1, max_value=100000)
    submit_button = st.form_submit_button(label='Get Your Rank')

# 4. Display the rank based on the input
if submit_button:
    participant = get_rank(bib_number)
    if participant is not None:
        try:
            st.success('Based on your **net time**, Your rank is **{}** on 20136 participants (names registered at the start)'.format(int(participant['rank_net'].values[0])))
            st.success('Based on your **brut time**, Your rank is **{}** on 20136 participants (names registered at the start)'.format(
                int(participant['rank_brut'].values[0])))
        except:
            st.error('Your number is not found or no valid time recorded.')
            pass
        st.write("Your info")
        st.table(participant)
    else:
        st.error('Your number is not found or no valid time recorded.')


#5
st.divider()
st.write('''
#### The stats  
- 20136 names on the start  
- 2814 did not finish or did not start the race 
- fastest time net: '02:12:24'  
- fastest time brut: '02:24:43'  
''')
st.divider()
st.image("./image/marathon.jpg", use_column_width=True)
#6
st.caption("These (unofficial) rank results are based on the official website from JO PARIS 2024")
st.caption("link here: https://marathonpourtous.paris2024.org/fr/actus/2024/retrouve-tes-photos-ton-resultat/59")

#6
st.divider()
st.write("**Credits**")
st.write("If you like the site, you can click on the ⭐ on top of page ⤴️")


"""Streamlit hosting for the Aura capstone website and completed analysis."""
from pathlib import Path
from io import BytesIO
import zipfile
import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="Aura | Healthcare Capstone", page_icon="📊", layout="wide")
st.markdown('<style>.block-container{padding-top:1rem}iframe{border:0}</style>', unsafe_allow_html=True)
views = ['Healthcare website', 'Full analysis', 'Project downloads']
requested = st.query_params.get('view', 'site')
view = st.sidebar.radio('Aura · Healthcare Capstone', views, index={'report':1,'downloads':2}.get(requested,0))
st.sidebar.caption('Applied Data Science with Python · Incremental Capstone')
st.sidebar.link_button('GitHub repository', 'https://github.com/JohnCorbinCorona/aura-healthcare-capstone')
if view == views[0]:
    components.html((ROOT/'website.html').read_text(), height=3100, scrolling=True)
elif view == views[1]:
    components.html((ROOT/'Aura_Capstone.html').read_text(), height=1600, scrolling=True)
else:
    st.title('Project downloads')
    st.write('Download the complete project, or choose an individual file. Keep the original CSV beside the notebook when running it.')
    archive = ROOT/'Aura_Capstone_Submission.zip'
    st.download_button('Download complete capstone',archive.read_bytes(),file_name=archive.name,mime='application/zip')
    with zipfile.ZipFile(archive) as z:
        names = {p.removeprefix('Aura_Capstone/'):p for p in z.namelist() if not p.endswith('/')}
        selected = st.selectbox('Choose a project file', sorted(names))
        payload = z.read(names[selected])
        st.download_button('Download selected file',payload,file_name=Path(selected).name)
    st.subheader('Required CSV exports')
    for filename in ['NSMES1988new.csv','NSMES1988updated.csv','NSMES1988_Dummy.csv']:
        st.download_button(filename,(ROOT/filename).read_bytes(),file_name=filename,mime='text/csv')

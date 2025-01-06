import streamlit as st
from io import StringIO
from app3 import DatamapperDocumentParser
obj = DatamapperDocumentParser()
st.title("File Converter to CSV")

    # Upload file

options = ['Targa','IACX','Producers Midstream']
selected_option = st.selectbox("select company",options)

uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", 'xls', 'xlsx'])
if uploaded_file is not None:
    if selected_option in ['IACX' , 'Producers Midstream']:
            
                    if uploaded_file.type == "application/pdf":
                        csv_output, csv_file = obj.take_files(uploaded_file)
                    elif uploaded_file.type in ["application/vnd.ms-excel", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
                
                        csv_output , csv_file  = obj.take_files(uploaded_file)
    if selected_option in ['Targa']:
            #if uploaded_file is not None:
                csv_output ,csv_file = obj.convert_targa_file(uploaded_file)

        # Download button for CSV
        #print("CSV OUT",csv_output)
    
    if csv_output and csv_file :
        st.download_button(
                label="Download CSV",
                data=csv_output.getvalue().encode('utf-8'),
                file_name=csv_file,
                mime="text/csv"
            )


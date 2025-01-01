from astrapy import DataAPIClient
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()

endpoint = os.getenv("ASTRA_DB_API_KEY")
token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")


@st.cache_resource
def get_db():
    client = DataAPIClient(token)
    db = client.get_database_by_api_endpoint(endpoint)
    return db


database = get_db()
collection_names = ["personal_data","notes"]

for collection in collection_names:
    try:
        database.create_collection(collection)

    except:
        pass


personal_data_collection = database.get_collection("personal_data")
notes_collection = database.get_collection("notes")

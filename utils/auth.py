# Authentication utilities
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import vertexai
import streamlit as st
import json
import tempfile
import os

from config import PROJECT_ID, LOCATION

def setup_google_auth(key_path=None):
    """Set up Google Cloud authentication and initialize Vertex AI."""
    # Try to get credentials from Streamlit secrets first
    if hasattr(st, 'secrets') and 'google_credentials' in st.secrets:
        try:
            # Create a temporary file for the credentials
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp:
                # Parse JSON string from secrets and write to temp file
                json.dump(json.loads(st.secrets.google_credentials.json), temp)
                temp_key_path = temp.name
            
            # Use the temporary credentials file
            credentials = Credentials.from_service_account_file(
                temp_key_path,
                scopes=['https://www.googleapis.com/auth/cloud-platform']
            )
            
            # Clean up the temporary file
            os.unlink(temp_key_path)
            
            # Initialize Vertex AI with credentials
            vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)
            st.sidebar.success("✅ Authenticated using Streamlit secrets")
            return credentials
            
        except Exception as e:
            st.sidebar.error(f"Error using secret credentials: {str(e)}")
            # Continue to fallback methods if secrets failed
    
    # Fall back to file-based credentials if specified
    if key_path:
        try:
            credentials = Credentials.from_service_account_file(
                key_path,
                scopes=['https://www.googleapis.com/auth/cloud-platform']
            )
            
            if credentials.expired:
                credentials.refresh(Request())
                
            # Initialize Vertex AI with credentials
            vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)
            return credentials
        except Exception as e:
            st.sidebar.error(f"Error using credentials file: {str(e)}")
    
    # Use application default credentials as last resort
    try:
        vertexai.init(project=PROJECT_ID, location=LOCATION)
        return None
    except Exception as e:
        st.sidebar.error(f"Failed to authenticate: {str(e)}")
        st.error("Authentication failed. Please check your credentials.")
        return None
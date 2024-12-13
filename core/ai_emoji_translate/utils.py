
import google.generativeai as genai
from django.conf import settings
import logging

class GenerativeAIManager:
    _model = None

    @staticmethod
    def get_model():
        if GenerativeAIManager._model is None:
            # Configure the API (only once)
            try:
                genai.configure(api_key=settings.GOOGLE_GEMINI_API_KEY)
                GenerativeAIManager._model = genai.GenerativeModel("gemini-1.5-flash")
                logging.info("Google GenerativeAI Model configured successfully.")
            except Exception as e:
                logging.error(f"Error initializing GenerativeAI model: {e}")
                raise e
        
        return GenerativeAIManager._model
from django.conf import settings
import logging

class GenerativeAIManager:
    _model = None

    @staticmethod
    def get_model():
        if GenerativeAIManager._model is None:
            # Configure the API (only once)
            try:
                genai.configure(api_key=settings.GOOGLE_GEMINI_API_KEY)
                GenerativeAIManager._model = genai.GenerativeModel("gemini-1.5-flash")
                logging.info("Google GenerativeAI Model configured successfully.")
            except Exception as e:
                logging.error(f"Error initializing GenerativeAI model: {e}")
                raise e
        
        return GenerativeAIManager._model

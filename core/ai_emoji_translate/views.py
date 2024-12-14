from django.shortcuts import render
import google.generativeai as genai
from django.conf import settings
from django.http import HttpResponse
import logging

from .utils import GenerativeAIManager


def home(request):
    return render(request, "home.html")


def translate_to_emoji(request):
    if request.method != "POST":
        return HttpResponse("Only POST requests are allowed", status=405)

    try:
        print("here")
        sentence = request.POST.get("sentence", "").strip()

        if not sentence:
            return HttpResponse("No sentence provided", status=400)

        # Get the shared Generative AI model instance
        model = GenerativeAIManager.get_model()

        prompt = f"Translate the following sentence into emojis use only emojis when possible: '{sentence}'"

        try:
            response = model.generate_content(prompt)
            emoji_text = response.text.strip()

            if not emoji_text:
                return HttpResponse(
                    f"""
                    <div class="text-red-500">
                        <p class="text-xl font-bold">Original: {sentence}</p>
                        <p>Unable to generate emoji translation</p>
                    </div>
                    """
                )

            return HttpResponse(
                f"""
                <div>
                    <p class="text-xl font-bold">Original: {sentence}</p>
                    <p class="text-3xl">{emoji_text}</p>
                </div>
                """
            )

        except Exception as api_error:
            logging.error(f"Gemini API Error: {str(api_error)}")
            return HttpResponse(
                f"""
                <div class="text-red-500">
                    <p class="text-xl font-bold">Error</p>
                    <p>Failed to translate: API request error</p>
                </div>
                """,
                status=500,
            )

    except Exception as e:
        logging.error(f"Unexpected error in emoji translation: {str(e)}")
        return HttpResponse(
            f"""
            <div class="text-red-500">
                <p class="text-xl font-bold">Error</p>
                <p>An unexpected error occurred</p>
            </div>
            """,
            status=500,
        )

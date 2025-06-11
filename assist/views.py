import sys
import os

# Add grandparent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from traveller.lang_chain_code.main_p import get_assistant_response
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def travel_assistant(request):
    chat_log = request.session.get("chat_log", [])
    error = ""
    if request.method == "POST":
        question = request.POST.get("question")
        result = get_assistant_response(question)

        if result.get("quit"):
            request.session.flush()  # clears session
            return render(request, "travel_assistant.html", {
                "chat_log": chat_log + [{"user": question, "bot": result["response"]}],
                "quit": True
            })

        chat_log.append({"user": question, "bot": result["response"] or "\n".join(result["documents"])})
        request.session["chat_log"] = chat_log

    return render(request, "index.html", {
        "chat_log": chat_log,
        "quit": False
    })

from flask import Flask, render_template, request

app = Flask(__name__)

faq_data = {
    "What is Recall Network?":
        "Recall Network is a personal AI memory platform that connects your apps, data, and memories in one place.",
    "How do I create an account?":
        "Go to https://app.recall.network and sign up using your wallet or email.",
    "Is Recall free?":
        "Yes, there’s a free plan with basic features, plus premium options for advanced users.",
    "How does Recall use AI?":
        "Recall lets you ask natural language questions about your stored data using AI models.",
    "Is my data private?":
        "Yes. Your data is encrypted, and you decide what’s shared or kept private.",
    "Can I connect my Google account?":
        "Yes, Recall supports integrations with Google, Notion, Telegram, and more.",
    "What can I do with Recall memories?":
        "You can search, organize, and use them in apps or chat with your memory through Recall AI.",
    "Does Recall have an API?":
        "Yes, developers can use the Recall API to read and write user memories programmatically.",
    "Where can I find the API documentation?":
        "You can find it at https://docs.recall.network.",
    "What languages does Recall support?":
        "Currently, the interface is in English. Other languages are planned for the future.",
    "Does Recall store my chats?":
        "Yes, if you connect chat apps, messages can be stored securely as part of your memory.",
    "Can I delete my data?":
        "Absolutely. You can remove any or all of your data anytime in account settings.",
    "Can I export my data?":
        "Yes, you can export your memory data in standard formats.",
    "What blockchain does Recall use?":
        "Recall integrates with Ethereum-compatible wallets, using decentralized identity principles.",
    "Can I use Recall without crypto?":
        "Yes. You can log in with email only — crypto wallets are optional.",
    "What’s the Recall browser extension?":
        "It allows you to capture and save memories directly from any website.",
    "Can I build apps on Recall?":
        "Yes. Developers can create Recall-powered apps using its SDK and API.",
    "Is Recall open source?":
        "Some parts of Recall’s ecosystem are open source — check their GitHub for details.",
    "How do I contact support?":
        "You can reach support through https://discord.gg/recallnetwork.",
    "Where can I find updates or roadmap?":
        "Follow the official blog and community for news and updates: https://recall.network/blog."
}


@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")
        answer = faq_data.get(question, "Sorry, I don't have an answer for that yet.")
    return render_template("index.html", questions=list(faq_data.keys()), answer=answer)


if __name__ == "__main__":
    app.run(debug=True)

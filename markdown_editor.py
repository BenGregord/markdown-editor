import os
import markdown
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Path to save the Markdown file
SAVE_PATH = "saved_markdown.md"

@app.route("/", methods=["GET", "POST"])
def editor():
    """Render the Markdown editor and handle form submissions."""
    if request.method == "POST":
        markdown_text = request.form.get("markdown_text", "")
        with open(SAVE_PATH, "w") as file:
            file.write(markdown_text)
        return redirect(url_for("preview"))
    return render_template("editor.html")

@app.route("/preview")
def preview():
    """Render the Markdown preview."""
    if os.path.exists(SAVE_PATH):
        with open(SAVE_PATH, "r") as file:
            markdown_text = file.read()
        html_content = markdown.markdown(markdown_text)
        return render_template("preview.html", html_content=html_content)
    return redirect(url_for("editor"))

if __name__ == "__main__":
    app.run(debug=True)

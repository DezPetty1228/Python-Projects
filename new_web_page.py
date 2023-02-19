import tkinter as tk
import webbrowser

def generate_web_page():
    # Get the user's input text
    body_text = body_text_input.get("1.0", "end-1c")

    # Create the HTML page
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Generated Web Page</title>
    </head>
    <body>
        {body_text}
    </body>
    </html>
    """

    # Write the HTML page to a file named "generated_web_page.html"
    with open("generated_web_page.html", "w") as f:
        f.write(html)

    # Open the generated web page in a new tab in the browser
    webbrowser.open_new_tab("generated_web_page.html")

# Create the GUI
root = tk.Tk()
root.title("Web Page Generator")

# Create the text input widget
body_text_input = tk.Text(root, height=10, width=50)
body_text_input.pack()

# Create the button widget
generate_button = tk.Button(root, text="Generate Web Page", command=generate_web_page)
generate_button.pack()

# Start the GUI event loop
root.mainloop()

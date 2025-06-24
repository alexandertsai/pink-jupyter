"""
🌸 Pink Jupyter Theme - Project-Level Styling 🌸

A beautiful pink color theme for Jupyter Notebook that can be applied to individual notebooks
without requiring global installation. Perfect for shared projects!

Usage:
    1. Drop this file into your project folder
    2. In your notebook, run:
       import pink_theme
       pink_theme.apply()
    3. Enjoy your pink-themed notebook! 💕

Author: Pink Jupyter Theme Project
License: MIT
"""

def apply():
    """Apply the pink theme to the current Jupyter notebook."""
    
    from IPython.display import HTML, display
    
    # All CSS embedded as a string - identical to theme/custom.css
    PINK_CSS = """
/* Pink Jupyter Theme - A beautiful pink color scheme for Jupyter Notebooks */

/* Root variables for consistency */
:root {
    --pink-light: #FFF0F5;
    --pink-lighter: #FFF5FB;
    --pink-soft: #FFE4E1;
    --pink-medium: #FFB6C1;
    --pink-hot: #FF69B4;
    --pink-deep: #FF1493;
    --pink-violet: #C71585;
    --burgundy: #8B1538;
    --indigo: #4B0082;
}

/* Main body and container backgrounds */
body {
    background-color: var(--pink-light) !important;
}

#notebook {
    background-color: var(--pink-lighter) !important;
}

#notebook-container {
    background-color: var(--pink-lighter) !important;
    width: 95% !important;
    margin: auto !important;
    padding: 2em !important;
    box-shadow: 0 0 20px rgba(255, 182, 193, 0.3) !important;
}

/* Header */
#header {
    background-color: var(--pink-medium) !important;
    box-shadow: 0 2px 4px rgba(255, 182, 193, 0.3) !important;
}

#header-container {
    background-color: var(--pink-medium) !important;
}

/* Menu bar */
#menubar {
    background-color: var(--pink-medium) !important;
}

#menubar .navbar-nav > li > a {
    color: var(--burgundy) !important;
}

#menubar .navbar-nav > li > a:hover {
    background-color: var(--pink-hot) !important;
    color: white !important;
}

/* Notebook name */
#notebook_name {
    color: var(--pink-violet) !important;
    font-weight: bold !important;
}

/* Toolbar */
.toolbar {
    background-color: var(--pink-soft) !important;
    border-bottom: 1px solid var(--pink-medium) !important;
}

#maintoolbar {
    background-color: var(--pink-soft) !important;
    border-bottom: 1px solid var(--pink-medium) !important;
    padding: 5px !important;
}

/* All cells - general styling */
.cell {
    background-color: white !important;
    border: 1px solid var(--pink-soft) !important;
    border-radius: 5px !important;
    margin: 8px 0 !important;
    padding: 5px !important;
}

/* Selected cells */
.cell.selected {
    border: 2px solid var(--pink-hot) !important;
    box-shadow: 0 0 10px rgba(255, 105, 180, 0.3) !important;
    background-color: #FFFAFA !important;
}

.cell.selected:before {
    background: var(--pink-hot) !important;
    width: 5px !important;
}

/* Code cells specific */
.code_cell {
    background-color: white !important;
}

.code_cell .input {
    background-color: transparent !important;
}

/* Input area */
.input_area {
    background: var(--pink-lighter) !important;
    border: 1px solid var(--pink-soft) !important;
    border-radius: 3px !important;
    padding: 5px !important;
}

/* CodeMirror editor */
.CodeMirror {
    background-color: var(--pink-lighter) !important;
    color: var(--indigo) !important;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', monospace !important;
}

.CodeMirror-gutters {
    background-color: var(--pink-soft) !important;
    border-right: 1px solid var(--pink-medium) !important;
}

.CodeMirror-linenumber {
    color: #DB7093 !important;
}

.CodeMirror-cursor {
    border-left: 2px solid var(--pink-hot) !important;
}

/* Output area */
.output_wrapper {
    background: white !important;
}

.output_area {
    background: white !important;
}

.output_area pre {
    color: var(--indigo) !important;
    background-color: white !important;
    padding: 10px !important;
}

.output_subarea {
    background: white !important;
    padding: 5px !important;
}

/* Markdown cells */
.text_cell {
    background-color: white !important;
}

.text_cell_render {
    color: var(--indigo) !important;
    background-color: var(--pink-lighter) !important;
    padding: 15px !important;
    border-radius: 5px !important;
    font-family: 'Inter', 'Dancing Script', 'Playfair Display', serif !important;
    line-height: 1.6 !important;
    font-size: 16px !important;
}

.text_cell_render h1,
.text_cell_render h2,
.text_cell_render h3,
.text_cell_render h4,
.text_cell_render h5,
.text_cell_render h6 {
    color: var(--pink-violet) !important;
    font-weight: bold !important;
    font-family: 'Playfair Display', 'Georgia', 'Times New Roman', serif !important;
    letter-spacing: 0.5px !important;
}

.text_cell_render h1 {
    border-bottom: 2px solid var(--pink-medium) !important;
    padding-bottom: 10px !important;
}

/* Links in markdown */
.text_cell_render a {
    color: var(--pink-deep) !important;
}

.text_cell_render a:hover {
    color: var(--pink-hot) !important;
    text-decoration: underline !important;
}

/* Cell prompts */
.prompt {
    min-width: 14ex !important;
}

.input_prompt {
    color: var(--pink-violet) !important;
    font-weight: bold !important;
}

.output_prompt {
    color: #DB7093 !important;
}

/* Running indicator */
.running .prompt {
    background-color: var(--pink-hot) !important;
    color: white !important;
}

/* Syntax highlighting */
.cm-keyword { color: var(--pink-deep) !important; font-weight: bold !important; }
.cm-def { color: var(--pink-violet) !important; }
.cm-variable { color: var(--indigo) !important; }
.cm-variable-2 { color: #8B008B !important; }
.cm-variable-3 { color: #9400D3 !important; }
.cm-string { color: #DB7093 !important; }
.cm-operator { color: var(--pink-hot) !important; }
.cm-comment { color: #BC8F8F !important; font-style: italic !important; }
.cm-number { color: #FF6347 !important; }
.cm-atom { color: var(--pink-deep) !important; }
.cm-builtin { color: var(--pink-violet) !important; }
.cm-bracket { color: var(--burgundy) !important; }

/* Buttons */
.btn-default {
    background-color: var(--pink-medium) !important;
    border-color: var(--pink-hot) !important;
    color: var(--burgundy) !important;
}

.btn-default:hover {
    background-color: var(--pink-hot) !important;
    border-color: var(--pink-deep) !important;
    color: white !important;
}

/* Modal dialogs */
.modal-content {
    background-color: var(--pink-lighter) !important;
    border: 1px solid var(--pink-medium) !important;
}

.modal-header {
    background-color: var(--pink-medium) !important;
    color: var(--burgundy) !important;
    border-bottom: 1px solid var(--pink-hot) !important;
}

/* File browser */
#tab_content {
    background-color: var(--pink-lighter) !important;
}

.list_container {
    background-color: white !important;
}

.list_item:hover {
    background-color: var(--pink-soft) !important;
}

.list_item.selected {
    background-color: var(--pink-medium) !important;
}

/* Tables in output */
.rendered_html table {
    border: 1px solid var(--pink-medium) !important;
}

.rendered_html th {
    background-color: var(--pink-medium) !important;
    color: var(--burgundy) !important;
    padding: 8px !important;
}

.rendered_html tr:nth-child(even) {
    background-color: var(--pink-light) !important;
}

.rendered_html td {
    padding: 8px !important;
}

/* Scrollbars */
::-webkit-scrollbar {
    width: 12px !important;
    height: 12px !important;
}

::-webkit-scrollbar-track {
    background: var(--pink-soft) !important;
}

::-webkit-scrollbar-thumb {
    background: var(--pink-medium) !important;
    border-radius: 6px !important;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--pink-hot) !important;
}

/* Status bar / notification area */
#notification_area {
    background-color: transparent !important;
}

.notification_widget {
    color: var(--pink-violet) !important;
}

/* Command mode indicator */
.command_mode_icon:before {
    color: var(--pink-hot) !important;
}

.edit_mode_icon:before {
    color: var(--pink-violet) !important;
}

/* Kernel indicator */
#kernel_indicator {
    color: var(--pink-violet) !important;
}

/* Tooltips */
.tooltip-inner {
    background-color: var(--pink-hot) !important;
    color: white !important;
}

.tooltip.top .tooltip-arrow {
    border-top-color: var(--pink-hot) !important;
}

/* Make sure images and plots have proper background */
.output_png,
.output_jpeg {
    background-color: white !important;
    padding: 10px !important;
    border-radius: 3px !important;
    display: inline-block !important;
}

/* DataFrame styling */
.dataframe {
    border: 1px solid var(--pink-medium) !important;
}

.dataframe thead {
    background-color: var(--pink-medium) !important;
}

.dataframe tbody tr:nth-child(even) {
    background-color: var(--pink-light) !important;
}

/* Error output */
.output_stderr {
    background-color: #FFE4E1 !important;
    color: #8B0000 !important;
}

.output_stderr pre {
    background-color: #FFE4E1 !important;
    color: #8B0000 !important;
    border-left: 3px solid var(--pink-hot) !important;
    padding: 10px !important;
}

/* Error traceback */
.output_subarea.output_error {
    background-color: #FFE4E1 !important;
}

.output_subarea.output_error pre {
    background-color: #FFE4E1 !important;
    color: #8B0000 !important;
}

div.output_area div.output_subarea.output_stderr {
    background-color: #FFE4E1 !important;
}

/* ANSI color codes in error output */
.ansi-red-fg { color: var(--pink-hot) !important; }
.ansi-red-intense-fg { color: var(--pink-deep) !important; font-weight: bold !important; }
.ansi-cyan-fg { color: var(--pink-violet) !important; }
.ansi-cyan-intense-fg { color: var(--burgundy) !important; }
.ansi-green-fg { color: var(--pink-medium) !important; }
.ansi-green-intense-fg { color: #DB7093 !important; }

/* Python traceback styling */
.output_area .output_subarea.output_text.output_error {
    background-color: #FFE4E1 !important;
    padding: 10px !important;
    border-radius: 3px !important;
}

.output_text.output_error pre {
    background-color: transparent !important;
    color: #8B0000 !important;
}

/* Jupyter error messages */
div.output_stderr {
    background-color: #FFE4E1 !important;
}

div.output_stderr pre {
    color: #8B0000 !important;
    background-color: transparent !important;
}

/* Make all error text visible */
.output_area .output_text pre {
    color: var(--indigo) !important;
}

.output_area .output_error pre {
    color: #8B0000 !important;
    background-color: #FFE4E1 !important;
    border-radius: 3px !important;
    padding: 10px !important;
}

/* Additional nbclassic specific fixes */
div#notebook {
    border-top: none !important;
}

.container {
    width: 98% !important;
}

/* Ensure cell content is visible */
.inner_cell {
    background-color: transparent !important;
}

.input_area > .highlight {
    background-color: transparent !important;
}

.output_area .output_subarea {
    max-width: 100% !important;
}
"""
    
    # Inject the CSS into the notebook
    display(HTML(f"<style>{PINK_CSS}</style>"))
    
    # Show success message
    print("🌸 Pink theme applied successfully! Your notebook is now beautifully pink! 💕")


def remove():
    """Remove the pink theme from the current notebook (resets to default)."""
    from IPython.display import HTML, display
    
    # This will remove our custom styles by overriding them with defaults
    reset_css = """
    <style>
    /* Reset to default Jupyter styles */
    :root {
        --pink-light: unset;
        --pink-lighter: unset;
        --pink-soft: unset;
        --pink-medium: unset;
        --pink-hot: unset;
        --pink-deep: unset;
        --pink-violet: unset;
        --burgundy: unset;
        --indigo: unset;
    }
    
    body { background-color: white !important; }
    #notebook { background-color: white !important; }
    #notebook-container { background-color: white !important; width: auto !important; }
    </style>
    """
    
    display(HTML(reset_css))
    print("🌸 Pink theme removed. Notebook restored to default styling.")


if __name__ == "__main__":
    # If run as a script, apply the theme automatically
    apply()
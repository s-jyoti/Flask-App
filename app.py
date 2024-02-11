from flask import Flask, render_template, request
import traceback

app = Flask(__name__)

@app.route('/file_viewer/file1.txt', methods=['GET'])
def view_file(filename='file1.txt'):
    try:
        start_line = request.args.get('start_line', type=int)
        end_line = request.args.get('end_line', type=int)

        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if start_line is not None and end_line is not None:
            lines = lines[start_line - 1:end_line]
        elif start_line is not None:
            lines = lines[start_line - 1:]

        content = ''.join(lines)

        return render_template('file_viewer.html', filename=filename, content=content)

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        traceback_str = traceback.format_exc()
        return render_template('error.html', error_message=error_message, traceback_str=traceback_str)

if __name__ == '__main__':
    app.run(debug=True)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CarX Cleaner</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background: #eee;
            padding: 10px;
            border-radius: 5px;
        }
        code {
            background: #eee;
            padding: 2px 4px;
            border-radius: 3px;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        ol {
            list-style-type: decimal;
            margin-left: 20px;
        }
        .checkbox {
            margin-left: 20px;
        }
        .logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 150px; /* Adjust the width as needed */
        }
    </style>
</head>
<body>
    <img src="images/logo/carx_cleaner_logo.png" alt="CarX Cleaner Logo" class="logo">
    <h1>CarX Cleaner</h1>
    <p>CarX Cleaner is a tool that is designed to remove mods from CarX eliminating the requirement to do some manually. This tool ensures that only un-original (modded) files and directories are removed, preserving the integrity of the original game files.</p>
    
    <h2>Features</h2>
    <ul>
        <li>Removes un-original files and directories</li>
        <li>Preserves original files and directories</li>
        <li>User-friendly PyQt5 GUI</li>
        <li>Supports relative paths for universal compatibility</li>
    </ul>
    
    <h2>Installation</h2>
    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.x</li>
        <li>PyQt5</li>
    </ul>
    
    <h3>Steps</h3>
    <ol>
        <li><strong>Clone the repository:</strong>
            <pre><code>git clone https://github.com/Elixir-Elf/CarX-Cleaner.git
cd CarX-Cleaner</code></pre>
        </li>
        <li><strong>Install the required dependencies:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Run the application:</strong>
            <pre><code>python main.py</code></pre>
        </li>
    </ol>
    
    <h2>Usage</h2>
    <ol>
        <li><strong>Input the game directory path:</strong>
            <p>Open the application and input the full directory path of the game installation in the provided text box.</p>
        </li>
        <li><strong>Start the cleaning process:</strong>
            <p>Click the "Start Cleaning" button to begin the cleaning process. The progress bar will update to show the progress, and the status label will indicate the current status (Ready, In-Progress, Completed, Error).</p>
        </li>
    </ol>
    
    <h2>TODO</h2>
    <ul class="checkbox">
        <li>[ ] Add a mod file backup feature</li>
    </ul>
    
    <h2>Contributing</h2>
    <p>Contributions are welcome! Please follow these steps to contribute:</p>
    <ol>
        <li>Fork the repository</li>
        <li>Create a new branch (<code>git checkout -b feature-branch</code>)</li>
        <li>Commit your changes (<code>git commit -am 'Add new feature'</code>)</li>
        <li>Push to the branch (<code>git push origin feature-branch</code>)</li>
        <li>Create a new Pull Request</li>
    </ol>
    
    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the LICENSE file for details.</p>
    
    <h2>Acknowledgements</h2>
    <p>Special thanks to <a href="https://github.com/pepe-wizard">pepe-wizard</a> for providing massive amounts of support and code snippets!</p>
</body>
</html>

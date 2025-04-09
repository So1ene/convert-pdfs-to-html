
<hr />
<details>
<summary><b>Linux / Windows-WSL installation</b></summary>
<hr />

#### 1. Check if python is installed

```
python3 --version
```

If not, `sudo apt install python3`

---

#### 2. Ensure your package list is updated, then install the necessary dependencies:

```
sudo apt update
```

```
sudo apt install -y libfontconfig1 libcairo2 libjpeg-turbo8
```

---

#### 3: Install pdf2htmlEX

Download the latest .deb package of pdf2htmlEX from its [GitHub releases page](https://github.com/pdf2htmlEX/pdf2htmlEX/releases). Navigate inside the downloaded release and install it:

```
sudo apt install ./pdf2htmlEX.deb
```

If you encounter any dependency issues like I did, resolve them with:
```
sudo apt --fix-broken install
```
Confirm that pdf2htmlEX is installed correctly:
```
pdf2htmlEX -v
```
<br />
<br />
<br />
</details>
<hr />
<details> <summary><b>MacOS Installation</b></summary>
<hr />

(I didn't test it myself, but I found some instructions that might work:)

• Install MacPorts:
```
xcode-select --install
```
- After isntalling xcode-select, Visit the [MacPorts Download Page](https://www.macports.org/install.php) to find the appropriate installer for your macOS version, then run the .pkg file installer.
Check if installed correctly with `port version`
<br />


<br />
• Install pdf2htmlex via MacPorts:

```
sudo port install pdf2htmlex
```

- Confirm that pdf2htmlEX is installed correctly using: `pdf2htmlEX -v`
- If all else fails, run a linux box and follow the instructions above instead
<br />
<br />
<br />
</details>
<hr />
<br />
<br />
<br />

## How to use ##
- Add the pdf files to be converted in the "pdfs_input" folder
- Open this directory in a terminal and run the python script, for example:

```
python3 convert_pdfs_to_html.py
```

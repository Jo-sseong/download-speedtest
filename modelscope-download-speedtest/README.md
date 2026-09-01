# ModelScope Download Speed Test

A small command-line tool that measures how much of a ModelScope dataset is
downloaded during a fixed time window.

Each run creates its own temporary directory under `--work-dir`. When the run
finishes or is interrupted, only that temporary directory is deleted. Existing
files in the parent directory are not removed.

## Install

```bash
git clone https://github.com/YOUR_NAME/modelscope-download-speedtest.git
cd modelscope-download-speedtest
python -m venv .venv
```

Activate the virtual environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# Linux/macOS
source .venv/bin/activate
```

Then install the dependency:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python speedtest.py \
  --dataset DiffSynth-Studio/Qwen-Image-Self-Generated-Dataset \
  --duration 120 \
  --work-dir /tmp/ms_speedtest \
  --label on_kr \
  --log-file ./speedtest_results.txt
```

PowerShell also accepts the command on one line:

```powershell
python speedtest.py --dataset "DiffSynth-Studio/Qwen-Image-Self-Generated-Dataset" --duration 120 --work-dir "E:\ms_speedtest" --label "on_kr" --log-file "E:\ms_speedtest_results.txt"
```

Only `--dataset` is required. The defaults are:

| Option | Default |
| --- | --- |
| `--duration` | `120` seconds |
| `--work-dir` | `./speedtest_runs` |
| `--label` | dataset ID |
| `--log-file` | `./speedtest_results.txt` |

Example result:

```text
[on_kr] elapsed=120.0s  bytes=771,467,639  speed=6.13 MiB/s
```

## Measurement notes

- Use the same dataset, duration, disk, and network conditions when comparing runs.
- Choose a dataset large enough that it does not finish before the time limit.
- The result includes all files written into the temporary download directory.
- Cached data outside that directory is not counted.

## Publish on GitHub

Create an empty GitHub repository, replace `YOUR_NAME` in the clone URL above,
and run:

```bash
git init
git add .
git commit -m "Add ModelScope download speed test"
git branch -M main
git remote add origin https://github.com/YOUR_NAME/modelscope-download-speedtest.git
git push -u origin main
```

## License

[MIT](LICENSE)

# ModelScope Download Speed Test

정해진 시간 동안 데이터셋이 얼마나 다운로드되는지 측정하는
간단한 도구입니다.

실행할 때마다 `--work-dir` 아래에 전용 임시 폴더를 생성합니다. 측정이
끝나거나 중단되면 해당 임시 폴더만 삭제하며, 상위 폴더에 원래 있던
파일은 삭제하지 않습니다.

## Install

```bash
git clone https://github.com/YOUR_NAME/modelscope-download-speedtest.git
cd modelscope-download-speedtest
python -m venv .venv
```

가상환경을 활성화합니다.

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# Linux/macOS
source .venv/bin/activate
```

필요한 패키지를 설치합니다.

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

PowerShell에서는 다음과 같이 한 줄로 실행할 수도 있습니다.

```powershell
python speedtest.py --dataset "DiffSynth-Studio/Qwen-Image-Self-Generated-Dataset" --duration 120 --work-dir "E:\ms_speedtest" --label "on_kr" --log-file "E:\ms_speedtest_results.txt"
```

`--dataset`만 필수 옵션이며, 나머지 옵션의 기본값은 다음과 같습니다.

| Option | Default |
| --- | --- |
| `--duration` | `120`초 |
| `--work-dir` | `./speedtest_runs` |
| `--label` | 데이터셋 ID |
| `--log-file` | `./speedtest_results.txt` |

결과 예시는 다음과 같습니다.

```text
[on_kr] elapsed=120.0s  bytes=771,467,639  speed=6.13 MiB/s
```

## Measurement notes

- 여러 결과를 비교할 때는 데이터셋, 측정 시간, 디스크, 네트워크 조건등을 동일하게 유지하세요.
- 제한 시간 전에 다운로드가 끝나지 않을 만큼 충분히 큰 데이터셋을 사용하세요.
- 해당 폴더 외부에 저장된 캐시 데이터는 측정에 포함되지 않습니다.

## License

[MIT](LICENSE)

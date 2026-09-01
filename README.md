# Download Speed Test

정해진 시간 동안 ModelScope 데이터셋이 얼마나 다운로드되는지 측정하는
간단한 명령줄 도구입니다.

실행할 때마다 `--work-dir` 아래에 전용 임시 폴더를 생성합니다. 측정이
끝나거나 중단되면 해당 임시 폴더만 삭제하며, 상위 폴더에 원래 있던
파일은 삭제하지 않습니다.

## Install

저장소를 내려받고 가상환경을 생성합니다.

```bash
git clone https://github.com/Jo-sseong/download-speedtest.git
cd download-speedtest
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

Linux 또는 macOS에서는 다음과 같이 실행합니다.

```bash
python speedtest.py \
  --dataset DiffSynth-Studio/Qwen-Image-Self-Generated-Dataset \
  --duration 120 \
  --work-dir /tmp/ms_speedtest \
  --label on_kr \
  --log-file ./speedtest_results.txt
```

Windows PowerShell에서는 다음과 같이 실행합니다.

```powershell
python speedtest.py --dataset "DiffSynth-Studio/Qwen-Image-Self-Generated-Dataset" --duration 120 --work-dir "E:\ms_speedtest" --label "on_kr" --log-file "E:\ms_speedtest_results.txt"
```

`--dataset`만 필수 옵션이며, 나머지 옵션의 기본값은 다음과 같습니다.

| Option | Description | Default |
| --- | --- | --- |
| `--dataset` | ModelScope 데이터셋 ID | 필수 |
| `--duration` | 측정 시간(초) | `120` |
| `--work-dir` | 임시 다운로드 폴더를 생성할 상위 경로 | `./speedtest_runs` |
| `--label` | 결과를 구분할 이름 | 데이터셋 ID |
| `--log-file` | 결과를 누적할 로그 파일 | `./speedtest_results.txt` |

결과는 화면에 출력되고 로그 파일에도 추가됩니다.

```text
[on_kr] elapsed=120.0s  bytes=771,467,639  speed=6.13 MiB/s
```

| Field | Description |
| --- | --- |
| `elapsed` | 측정을 시작한 뒤 실제로 흐른 시간(초) |
| `bytes` | 임시 다운로드 폴더에 기록된 전체 바이트 수 |
| `speed` | `bytes / elapsed`로 계산한 평균 다운로드 속도(MiB/s) |

## Measurement notes

- 여러 결과를 비교할 때는 데이터셋, 측정 시간, 디스크, 네트워크 조건 등을 동일하게 유지하세요.
- 제한 시간 전에 다운로드가 끝나지 않을 만큼 충분히 큰 데이터셋을 사용하세요.
- 임시 다운로드 폴더 외부에 저장된 캐시 데이터는 측정에 포함되지 않습니다.
- `--work-dir` 자체는 삭제하지 않으며, 프로그램이 생성한 `run_...` 임시 폴더만 삭제합니다.

## License

[MIT](LICENSE)

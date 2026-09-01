import argparse
import multiprocessing as mp
import shutil
import tempfile
import time
from pathlib import Path


MIB = 1024**2


def download(dataset, target):
    from modelscope import dataset_snapshot_download

    dataset_snapshot_download(dataset, local_dir=str(target))


def dir_size(path):
    return sum(file.stat().st_size for file in path.rglob("*") if file.is_file())


def positive_number(value):
    value = float(value)
    if value <= 0:
        raise argparse.ArgumentTypeError("must be greater than 0")
    return value


def parse_args():
    parser = argparse.ArgumentParser(
        description="Measure ModelScope dataset download speed for a fixed time."
    )
    parser.add_argument("--dataset", required=True, help="ModelScope dataset ID")
    parser.add_argument(
        "--duration",
        type=positive_number,
        default=120,
        help="measurement time in seconds (default: 120)",
    )
    parser.add_argument(
        "--work-dir",
        type=Path,
        default=Path("speedtest_runs"),
        help="parent directory for temporary downloads",
    )
    parser.add_argument("--label", help="name shown in the result")
    parser.add_argument(
        "--log-file",
        type=Path,
        default=Path("speedtest_results.txt"),
        help="file to append results to",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    label = args.label or args.dataset

    args.work_dir.mkdir(parents=True, exist_ok=True)
    run_dir = Path(tempfile.mkdtemp(prefix="run_", dir=args.work_dir))
    process = mp.Process(target=download, args=(args.dataset, run_dir))

    print(f"[{label}] Downloading for {args.duration:g}s ...", flush=True)
    print("Temporary directory:", run_dir, flush=True)

    try:
        start = time.perf_counter()
        process.start()

        try:
            time.sleep(args.duration)
        except KeyboardInterrupt:
            print("\nStopped by user.")
            return 130
        finally:
            elapsed = time.perf_counter() - start
            finished_early = not process.is_alive()
            if process.is_alive():
                process.terminate()
            process.join()

        if finished_early and process.exitcode != 0:
            print("Download failed. Check the error message above.", flush=True)
            return 1

        bytes_downloaded = dir_size(run_dir)
        speed = bytes_downloaded / MIB / elapsed
        line = (
            f"[{label}] elapsed={elapsed:.1f}s  "
            f"bytes={bytes_downloaded:,}  speed={speed:.2f} MiB/s"
        )

        print(f"\n=== RESULT ===\n{line}")
        args.log_file.parent.mkdir(parents=True, exist_ok=True)
        with args.log_file.open("a", encoding="utf-8") as file:
            file.write(line + "\n")

        print("Log appended to", args.log_file)
        return 0
    finally:
        if process.is_alive():
            process.terminate()
            process.join()
        shutil.rmtree(run_dir)
        print("Cleaned up temporary directory:", run_dir)


if __name__ == "__main__":
    mp.freeze_support()
    raise SystemExit(main())

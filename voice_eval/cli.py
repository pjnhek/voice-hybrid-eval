# Command line interface for voice evaluation system
from pathlib import Path

from dotenv import load_dotenv
import typer

from .reporters.markdown import write_markdown_report
from .simulator import run_directory

app = typer.Typer()


@app.callback()
def main() -> None:
    """Voice evaluation command group."""
    load_dotenv()


@app.command()
def scenarios(
    path: str = typer.Argument(..., help="Path to scenarios directory"),
    report: str = typer.Option("out/report.md", help="Output report path"),
    audio_dir: str = typer.Option("out/audio", help="Audio output directory"),
    real_audio: str = typer.Option(
        None,
        help="Directory with pre-recorded user audio files (.wav, .m4a, .mp3, .ogg, .flac)",
    ),
    model: str = typer.Option("tiny", help="ASR model size"),
    judge: str = typer.Option("rules", help="Evaluation judge: rules | claude"),
):
    """Run voice evaluation scenarios."""
    Path(report).parent.mkdir(parents=True, exist_ok=True)
    Path(audio_dir).mkdir(parents=True, exist_ok=True)

    results = run_directory(
        Path(path),
        Path(audio_dir),
        model_size=model,
        judge=judge,
        real_audio_dir=real_audio,
    )
    write_markdown_report(results, Path(report))

    total_scenarios = len(results)
    passed_scenarios = sum(1 for r in results if r["scenario_pass"])

    print(f"{passed_scenarios}/{total_scenarios} scenarios passed")
    print(f"Report written to: {report}")


if __name__ == "__main__":
    app()

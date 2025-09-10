# Command line interface for voice evaluation system
import typer
from pathlib import Path

from .simulator import run_directory
from .reporters.markdown import write_markdown_report

app = typer.Typer()


@app.command()
def scenarios(
    path: str = typer.Argument(..., help="Path to scenarios directory"),
    report: str = typer.Option("out/report.md", help="Output report path"),
    audio_dir: str = typer.Option("out/audio", help="Audio output directory"),
    model: str = typer.Option("tiny", help="ASR model size"),
    judge: str = typer.Option("rules", help="Evaluation method: 'rules' or 'llm'")
):
    """Run voice evaluation scenarios."""
    # Ensure out dirs exist
    Path(report).parent.mkdir(parents=True, exist_ok=True)
    Path(audio_dir).mkdir(parents=True, exist_ok=True)
    
    # Call run_directory
    results = run_directory(Path(path), Path(audio_dir), model_size=model, judge=judge)
    
    # Write markdown report
    write_markdown_report(results, Path(report))
    
    # Print summary "X/Y passed" and report path
    total_scenarios = len(results)
    passed_scenarios = sum(1 for r in results if r["scenario_pass"])
    
    print(f"{passed_scenarios}/{total_scenarios} scenarios passed")
    print(f"Report written to: {report}")


if __name__ == "__main__":
    app()
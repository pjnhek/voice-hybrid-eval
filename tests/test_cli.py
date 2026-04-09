from pathlib import Path

from typer.testing import CliRunner

from voice_eval import cli


def test_main_loads_dotenv(mocker):
    load_dotenv = mocker.patch("voice_eval.cli.load_dotenv")

    cli.main()

    load_dotenv.assert_called_once_with()


def test_scenarios_passes_real_audio_option_to_run_directory(mocker, tmp_path):
    runner = CliRunner()
    scenarios_dir = tmp_path / "scenarios"
    scenarios_dir.mkdir()
    report_path = tmp_path / "out" / "report.md"
    audio_dir = tmp_path / "audio"
    real_audio_dir = tmp_path / "real-audio"

    run_directory = mocker.patch(
        "voice_eval.cli.run_directory",
        return_value=[
            {
                "scenario_pass": True,
                "intent_detected": True,
            }
        ],
    )
    write_report = mocker.patch("voice_eval.cli.write_markdown_report")

    result = runner.invoke(
        cli.app,
        [
            "scenarios",
            str(scenarios_dir),
            "--report",
            str(report_path),
            "--audio-dir",
            str(audio_dir),
            "--real-audio",
            str(real_audio_dir),
        ],
    )

    assert result.exit_code == 0
    assert "1/1 scenarios passed" in result.stdout
    assert "Intent detection: 1/1 correct" in result.stdout
    run_directory.assert_called_once_with(
        Path(scenarios_dir),
        Path(audio_dir),
        model_size="tiny",
        judge="rules",
        real_audio_dir=str(real_audio_dir),
        real_audio_only=False,
    )
    write_report.assert_called_once_with(
        [{"scenario_pass": True, "intent_detected": True}],
        Path(report_path),
    )

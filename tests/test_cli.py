from voice_eval import cli


def test_main_loads_dotenv(mocker):
    load_dotenv = mocker.patch("voice_eval.cli.load_dotenv")

    cli.main()

    load_dotenv.assert_called_once_with()

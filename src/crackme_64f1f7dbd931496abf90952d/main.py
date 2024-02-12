import typer

app = typer.Typer()


@app.command()
def keygen() -> None:
    typer.echo("Implement your keygen for crackme_64f1f7dbd931496abf90952d here.")


if __name__ == "__main__":
    app()

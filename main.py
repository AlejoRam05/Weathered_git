from app.comandos import obtener_comandos
from app.lectura import Wheather


def run_command():
    args = obtener_comandos()

    Wheather.data(args.name)

    if args.c == "csv":
        Wheather.export_csv(args.name)

    elif args.c == "json":
        Wheather.ver_json(args.name)

    elif args.c == "txt":
        Wheather.txt(args.name)


if __name__ == "__main__":
    run_command()

import os

import click

@click.group()
def main():
    pass

@main.command()
@click.option('--sql-alchemy-connection')
@click.option('--bind-host', default='0.0.0.0')
@click.option('--bind-port', default='5000', type=int)
@click.pass_context
def server(sql_alchemy_connection, bind_host, bind_port):
    connection_string = sql_alchemy_connection or os.getenv('SQL_ALCHEMY_CONNECTION')

    app = create_app(taskflow, connection_string=connection_string)

    if prod:
        options = {
            'bind': '{}:{}'.format(bind_host, bind_port),
            'workers': number_of_workers(),
            'worker_class': worker_class
        }
        StandaloneApplication(app, options).run()
    else:
        app.run(host=bind_host, port=bind_port)

#!/usr/bin/env python2
import click


@click.group(name="mua")
def cli():
    pass

# Init subcommands
import ya_disk_publish.publish
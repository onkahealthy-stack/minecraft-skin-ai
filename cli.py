#!/usr/bin/env python
"""Command Line Interface for Minecraft Skin AI Generator"""

import click
import logging
from core.generator import SkinGenerator
from core.config import Config

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.group()
def cli():
    """Minecraft Skin AI Generator CLI"""
    pass


@cli.command()
@click.argument('prompt')
@click.option('--style', default='fantasy', help='Generation style')
@click.option('--output', '-o', default=None, help='Output file path')
def generate(prompt, style, output):
    """Generate a new Minecraft skin"""
    try:
        click.echo(f"🎨 Generating skin: {prompt}")
        click.echo(f"Style: {style}")
        
        generator = SkinGenerator()
        skin = generator.generate(prompt, style)
        
        path = skin.save(output)
        click.echo(f"✅ Skin saved: {path}")
        click.echo(f"ID: {skin.id}")
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        exit(1)


@cli.command()
@click.option('--style', default=None, help='Generation style')
@click.option('--count', '-c', default=1, type=int, help='Number of skins')
def random(style, count):
    """Generate random skins"""
    try:
        click.echo(f"🎲 Generating {count} random skin(s)...")
        
        generator = SkinGenerator()
        for i in range(count):
            skin = generator.random_generate(style)
            path = skin.save()
            click.echo(f"✅ Skin {i+1} saved: {path}")
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        exit(1)


@cli.command()
@click.argument('skin_id')
@click.argument('modification')
@click.option('--output', '-o', default=None, help='Output file path')
def edit(skin_id, modification, output):
    """Edit existing skin"""
    try:
        click.echo(f"✏️ Editing skin {skin_id}")
        click.echo(f"Modification: {modification}")
        
        generator = SkinGenerator()
        skin = generator.edit(skin_id, modification)
        
        path = skin.save(output)
        click.echo(f"✅ Edited skin saved: {path}")
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        exit(1)


@cli.command()
def styles():
    """List available styles"""
    click.echo("📋 Available Styles:")
    click.echo()
    
    for style, description in Config.STYLES.items():
        click.echo(f"• {style:15} - {description}")


@cli.command()
def version():
    """Show version"""
    click.echo("Minecraft Skin AI Generator v1.0.0")


if __name__ == '__main__':
    cli()

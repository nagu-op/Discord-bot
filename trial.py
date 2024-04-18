import discord
from discord.ext import commands
import csv
from PIL import Image, ImageDraw, ImageFont
import datetime

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

# Function to draw text onto an image at specified coordinates with formatting
def draw_text(image, text, coordinates, font_path, font_size, fill_color, bold=False):
    draw = ImageDraw.Draw(image)
    if bold:
        font = ImageFont.truetype(font_path, font_size, encoding="unic")
    else:
        font = ImageFont.truetype(font_path, font_size)
    draw.text(coordinates, text, fill=fill_color, font=font)

@bot.command()
async def scoreboard(ctx):
    csv_file = 'test.csv'
    coordinates_file = 'coordinates.csv'
    image_path = 'sample.jpg'
    font_path = 'nameFont.ttf'
    font_size = 36
    
    image = Image.open(image_path)
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        
        for idx, row in enumerate(reader):
            name = row['name']
            
            # Open the coordinates CSV file and read its contents
            with open(coordinates_file, 'r') as coord_file:
                coord_reader = csv.reader(coord_file)
                # Read the coordinates corresponding to the current index
                coordinates = list(coord_reader)[idx]
                
            draw_text(image, name, (int(coordinates[0]), int(coordinates[1])), font_path, font_size, fill_color=(0, 0, 0), bold=True)
    
    output_image_path = 'output_image.jpeg'
    image.save(output_image_path)
    
    await ctx.send(file=discord.File(output_image_path))

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f"Last update was: {current_time}")

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual bot token
bot.run('MTIzMDQ0Njc2ODQ3OTY3MDI3Mg.GKgm9h.oNcFXBJ3Kuuf6DpmHFT1Hs4QtvBtQ1cCZr2rp8')

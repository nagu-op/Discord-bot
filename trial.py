# import discord
# from discord.ext import commands
# import csv

# intents = discord.Intents.all()

# bot = commands.Bot(command_prefix='$', intents=intents)

# @bot.command()
# async def scoreboard(ctx):
#     # Replace 'your_csv_file.csv' with the path to your updated CSV file
#     csv_file = 'test.csv'
    
#     # Create an empty list to store the player data
#     player_data = []
    
#     # Open the CSV file and read its contents
#     with open(csv_file, 'r') as file:
#         reader = csv.DictReader(file)
        
#         # Iterate over each row in the CSV
#         for row in reader:
#             # Extract rank, name, and score from the row
#             rank = row['rank']
#             name = row['name']
#             score = row['score']
            
#             # Append player data to the list
#             player_data.append((rank, name, score))
    
#     # Create an embed object
#     embed = discord.Embed(title="Scoreboard", color=discord.Color.blue())
    
#     # Add player data to the embed
#     for rank, name, score in player_data:
#         # Add rank with larger font size and bold styling
#         embed.add_field(name=f"**Rank {rank}**", value=f"Name: {name}\nScore: {score}", inline=False)
    
#     # Send the embed to the Discord channel
#     await ctx.send(embed=embed)

# # Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual bot token
import discord
from discord.ext import commands
import csv
from PIL import Image, ImageDraw, ImageFont

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

# Function to draw text onto an image at specified coordinates
def draw_text(image, text, coordinates, font, fill_color):
    draw = ImageDraw.Draw(image)
    draw.text(coordinates, text, fill=fill_color, font=font)

@bot.command()
async def scoreboard(ctx):
    # Replace 'your_csv_file.csv' with the path to your updated CSV file
    csv_file = 'test.csv'
    # Replace 'name_coordinates.csv' with the path to your coordinates CSV file
    coordinates_file = 'coordinates.csv'
    
    # Load the image onto which the details will be displayed
    image_path = 'sample.jpeg'  # Replace with the path to your image
    image = Image.open(image_path)
    
    # Load the font
    font_path = 'Aaargh.ttf'  # Replace with the path to your font
    font_size = 24
    font = ImageFont.truetype(font_path, font_size)
    
    # Open the CSV file and read its contents
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        
        # Iterate over each row in the CSV
        for row in reader:
            # Extract name from the row
            name = row['name']
            
            # Open the coordinates CSV file and read its contents
            with open(coordinates_file, 'r') as coord_file:
                coord_reader = csv.reader(coord_file)
                # Read the first row which contains the coordinates
                coordinates = next(coord_reader)
            
            # Draw name onto the image using coordinates from the CSV
            draw_text(image, name, (int(coordinates[0]), int(coordinates[1])), font, fill_color=(0, 0, 0))
    
    # Save the modified image
    output_image_path = 'output_image.jpeg'  # Replace with the path to save the output image
    image.save(output_image_path)
    
    # Send the image as an attachment to the Discord channel
    await ctx.send(file=discord.File(output_image_path))

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual bot token

bot.run('MTIzMDQ0Njc2ODQ3OTY3MDI3Mg.GKgm9h.oNcFXBJ3Kuuf6DpmHFT1Hs4QtvBtQ1cCZr2rp8')



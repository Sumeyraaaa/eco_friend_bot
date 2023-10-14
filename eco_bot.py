import discord
from discord.ext import commands
from settings import settings

intents = discord.Intents.default()
intents.message_content = True

# Botunuzu oluşturun
bot = commands.Bot(command_prefix='!', intents=intents)

# Yardım komutunu oluşturun
@bot.command()
async def yardim(ctx):
    yardim_mesaji = """
    Selam! Ben sizin çevreyi korumaniz icin önerilerde bulunacagim. Bu komutlari kullanın:
    
    !bilgi - Çevreyi korumak temiz bir gelecek için çok önemlidir. Bunun hakkında bilgi alın.
    !geri_donusum - Geri dönüşüm insanların kullandığı şeylerin geri dönüştürülmesiyle olur. Geri dönüşüm kaynakların aşırı kullanımını önlemektedir. Bunun için bilgi alın.
    !enerji_tasarrufu - Enerji tasarrufu enerji kaynaklarının azalmasına yol açar. Enerji tüketimini azaltmak için yapılan her türlü çabaya verilen isimdir. Bunun için bilgi alın.
    """
    await ctx.send(yardim_mesaji)

# Bilgi komutunu oluşturun
@bot.command()
async def bilgi(ctx):
    bilgi_mesaji =  "Çevre temizliği ve sürdürülebilirlik konusunda bilgi almak için çevre kuruluşlarının web sitelerini ziyaret edebilirsiniz."
    await ctx.send(bilgi_mesaji)

# Geri dönüşüm komutunu oluşturun
@bot.command()
async def geri_donusum(ctx):
    geri_donusum_mesaji = "Geri dönüşüm, atıkları yeniden kullanarak yapılır. Çevreyi koruma konusunda önemli bir adımdır. Atıkları ayrıştırarak ve geri dönüşüm kutularını kullanarak geri dönüşüme katkıda bulunabilirsiniz ve daha fazla bilgi için web sitelerini ziyaret edebilirzzZ"
    await ctx.send(geri_donusum_mesaji)

# Enerji tasarrufu komutunu oluşturun
@bot.command()
async def enerji_tasarrufu(ctx):
    enerji_tasarrufu_mesaji = "Enerji tasarrufu yapmak için gereksiz yanan lambalar kapatılmalı. Elektrik fişleri fişte bırakılmamalı. Daha fazla bilgi için web sitelerinden yararlanabilirsiniz."
    await ctx.send(enerji_tasarrufu_mesaji)

# Botunuzu çalıştırın
bot.run(your token)

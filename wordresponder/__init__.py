from .wordresponder import WordResponder

__red_end_user_data_statement__ = (
    "This cog responds to any message containing a specified keyword with a specified response"
)

def setup(bot):
    bot.add_cog(WordResponder(bot))

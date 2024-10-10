from pydantic_settings import BaseSettings, SettingsConfigDict
from aiogram import F
class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False)
    bot_token: str
settings = Settings()


admin_group_id = -1002123850090  # Айди вашего чата
admin_id = (6751720805, 1851081467, 1570652377, 1398573474)  #Айди админов бота


prefixs=('$', '!', '.', '%', '&', ':', '|', '+', '-', '/', '~')


media_types = ["animation", "sticker", "video", "GIF"]
types_media = ("types.ContentType.PHOTO", "types.ContentType.STICKER", "types.ContentType.ANIMATION", "types.ContentType.VOICE", "types.ContentType.VIDEO", "types.ContentType.AUDIO", "types.ContentType.DOCUMENT", "types.ContentType.CONTACT")


any_media_F = F.photo | F.video | F.document | F.GIF | F.animation
any_media_F_caption = F.photo | F.video | F.document, F.caption


log_file_path = "BotInfo/bot_log.txt"
info_file_path = "BotInfo/bot_info.txt"
user_info_file_path = "BotInfo/user_info_data.txt"

base_path = 'BotReceivedMedia'
photo_path = "BotReceivedMedia/Photo"
video_path = "BotReceivedMedia/Video"
GIF_path = "BotReceivedMedia/GIF"
document_path = "BotReceivedMedia/Document"
videonote_path = "BotReceivedMedia/VideoNote"
voice_path = "BotReceivedMedia/Voice"

youtube_path = "BotReceivedMedia/Video/YouTube"
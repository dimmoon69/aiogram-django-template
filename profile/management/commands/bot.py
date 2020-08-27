from django.core.management.base import BaseCommand


async def on_startup(dp):
    import telegram_config.filters
    import telegram_config.middlewares
    telegram_config.filters.setup(dp)
    telegram_config.middlewares.setup(dp)

    from telegram_config.utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


class Command(BaseCommand):
    help = 'Телеграм бот'

    def handle(self, *args, **options):
        from aiogram import executor
        from telegram_config.handlers import dp

        executor.start_polling(dp, on_startup=on_startup)
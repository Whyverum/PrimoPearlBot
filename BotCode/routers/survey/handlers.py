from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown

from BotLibrary import BotVariables
from email_validators import valid_email
from keyboards.reply_kb.survey_yesno_kb import get_survey_email_kb
from .states import Survey

router = Router(name=__name__)

@router.message(Command("survey", prefix=BotVariables.prefixs))
async def handler_survey(message: types.Message, state: FSMContext):
    await state.set_state(Survey.full_name)
    await message.answer(
        text="Приветствую тебя в нашем маленьком раю! Подожди, я кажется не знаю твоего имени.. Как тебя зовут?",
        reply_markup=types.ReplyKeyboardRemove(),
    )


@router.message(Survey.full_name, F.text)
async def handler_survey_user_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer(
        f"Привет, {markdown.hbold(message.text)}! Скажи свою почту)",
    )
    await state.set_state(Survey.email)


@router.message(Survey.full_name)
async def handler_survey_user_name_invalid(message: types.Message):
    await message.answer(
        f"Извините, но кажется я вас не понимаю.. Повторите свое имя, пожалуйста!!!",
    )


@router.message(Survey.email, F.text.cast(valid_email).as_("email"))
async def handler_survey_email(message: types.Message, state: FSMContext, email: str):
    await state.update_data(email=email)
    await message.answer(
        text=f"Отличная почта: {markdown.hcode(message.text)}! "
        f"\nХочешь ли получать письма от меня?",
        reply_markup=get_survey_email_kb()
    )
    await state.set_state(Survey.email_newsletter)


async def send_survey_results(message: types.Message, data: dict) -> None:
    text = markdown.text(
       "Ваши результаты: \n",
        markdown.text(f"Имя: {markdown.hbold(data['full_name'])}"),
        markdown.text(f"Почта: {markdown.hcode(data['email'])}"),
        (
            "Отлично, теперь ждите новых сообщений)"
            if data["news_letter"]
            else "Что-ж, мы не будем писать вам!"
        ),
        sep='\n'
   )
    await message.answer(text=text, reply_markup=types.ReplyKeyboardRemove())


@router.message(Survey.email)
async def handler_survey_email_invalid(message: types.Message):
    await message.answer(
        text="Почта не подошла, попробуйте еще раз!",
    )


@router.message(Survey.email_newsletter, F.text.casefold() == "да")
async def handle_survey_email_newsletter_ok(message: types.Message, state: FSMContext):
    data = await state.update_data(news_letter=True)
    await state.clear()
    await send_survey_results(message, data)


@router.message(Survey.email_newsletter, F.text.casefold() == "нет")
async def handle_survey_email_newsletter_no(message: types.Message, state: FSMContext):
    data = await state.update_data(news_letter=False)
    await state.clear()
    await send_survey_results(message, data)


@router.message(Survey.email_newsletter)
async def handle_survey_email_newsletter_not_understand(message: types.Message, state: FSMContext):
    await message.answer(
        text=f"Простите, я не понимаю пожалуйста ответьте {markdown.hcode("да")} или {markdown.hcode("нет")}!"
    )

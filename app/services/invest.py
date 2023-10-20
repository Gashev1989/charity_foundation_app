from datetime import datetime

from sqlalchemy import select
from sqlalchemy.sql.expression import false
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


async def get_not_completed(
        session: AsyncSession,
        obj_in: CharityProject or Donation
) -> list[CharityProject or Donation]:
    """Функция получения незавершенных объектов."""
    not_completed_obj = await session.execute(
        select(obj_in).where(
            obj_in.fully_invested == false()
        ).order_by('create_date')
    )
    return not_completed_obj.scalars().first()


def get_balance(
        obj_in: CharityProject or Donation
):
    return obj_in.full_amount - obj_in.invested_amount


def sum_money(
        project: CharityProject,
        donation: Donation,
        money: int
) -> None:
    """Функция сложения денег."""
    project.invested_amount += money
    donation.invested_amount += money


def complete_object(
        obj_in: CharityProject or Donation
) -> None:
    """Функция, меняющая статус объекта на завершенный."""
    obj_in.close_date = datetime.now()
    obj_in.fully_invested = True


async def invest_money(
        session: AsyncSession,
        obj_in: CharityProject or Donation
) -> CharityProject or Donation:
    """Функция процесса инвестирования."""
    free_donation = await get_not_completed(session, Donation)
    opened_project = await get_not_completed(session, CharityProject)
    if not free_donation or not opened_project:
        await session.commit()
        await session.refresh(obj_in)
        return obj_in
    free_money = get_balance(free_donation)
    need_money = get_balance(opened_project)
    if free_money > need_money:
        sum_money(opened_project, free_donation, free_money)
        complete_object(opened_project)
    elif free_money < need_money:
        sum_money(opened_project, free_donation, free_money)
        complete_object(free_donation)
    else:
        sum_money(opened_project, free_donation, free_money)
        complete_object(opened_project)
        complete_object(free_donation)
    session.add(free_donation)
    session.add(opened_project)
    await session.commit()
    await session.refresh(free_donation)
    await session.refresh(opened_project)
    return await invest_money(session, obj_in)

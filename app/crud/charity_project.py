from datetime import datetime
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import true

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return db_project_id.scalars().first()

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> list[dict[str, datetime, str]]:
        projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == true()
            )
        )
        projects = projects.scalars().all()
        projects_to_repr = []
        for project in projects:
            projects_to_repr.append(
                {
                    'name': project.name,
                    'timedelta': project.close_date - project.create_date,
                    'description': project.description
                }
            )
        return sorted(projects_to_repr, key=lambda x: x['timedelta'])


charity_project_crud = CRUDCharityProject(CharityProject)

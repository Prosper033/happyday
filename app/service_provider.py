from dependency_injector import containers, providers
from app.repositories.basic_repository import BasicRepository, DjangoORMBasicRepository
from app.services.basic_management_service import BasicManagementService, DefaultBasicManagementService
from app.repositories.session_repository import SessionRepository, DjangoORMSessionRepository
from app.services.session_management_service import SessionManagementService, DefaultSessionManagementService
from app.repositories.student_repository import StudentRepository, DjangoORMStudentRepository
from app.services.student_management_service import StudentManagementService, DefaultStudentManagementService
from app.repositories.subject_repository import SubjectRepository, DjangoORMSubjectRepository
from app.services.subject_management_service import SubjectManagementService, DefaultSubjectManagementService
from app.repositories.application_repository import ApplicationRepository, DjangoORMApplicationRepository
from app.services.application_management_service import ApplicationManagementService, \
    DefaultApplicationManagementService

from typing import Callable


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    basic_repository: Callable[[], BasicRepository] = providers.Factory(
        DjangoORMBasicRepository
    )

    basic_management_service: Callable[[], BasicManagementService] = providers.Factory(
        DefaultBasicManagementService,
        repository=basic_repository
    )

    session_repository: Callable[[], SessionRepository] = providers.Factory(
        DjangoORMSessionRepository
    )

    session_management_service: Callable[[], SessionManagementService] = providers.Factory(
        DefaultSessionManagementService, repository=session_repository
    )

    student_repository: Callable[[], StudentRepository] = providers.Factory(
        DjangoORMStudentRepository
    )

    student_management_service: Callable[[], StudentManagementService] = providers.Factory(
        DefaultStudentManagementService, repository=student_repository
    )

    subject_repository: Callable[[], SubjectRepository] = providers.Factory(
        DjangoORMSubjectRepository
    )

    subject_management_service: Callable[[], SubjectManagementService] = providers.Factory(
        DefaultSubjectManagementService, repository=subject_repository
    )

    application_repository: Callable[[], ApplicationRepository] = providers.Factory(
        DjangoORMApplicationRepository
    )

    application_management_service: Callable[[], ApplicationManagementService] = providers.Factory(
        DefaultApplicationManagementService, repository=application_repository
    )


app_service_provider = Container()

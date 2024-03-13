from aiogram import Router

from src.middleware.role import AdminRoleMiddleware

admin_router = Router()

admin_router.message.middleware(AdminRoleMiddleware())
admin_router.callback_query.middleware(AdminRoleMiddleware())

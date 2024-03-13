from aiogram import Router

from src.middleware.role import DeliveryRoleMiddleware

delivery_router = Router()

delivery_router.message.middleware(DeliveryRoleMiddleware())
delivery_router.callback_query.middleware(DeliveryRoleMiddleware())

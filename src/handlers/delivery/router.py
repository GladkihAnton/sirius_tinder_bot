from aiogram import Router

from src.middleware.role import DeliveryRoleMiddleware

from .order.router import order_router

delivery_router = Router()

delivery_router.include_router(order_router)

delivery_router.message.middleware(DeliveryRoleMiddleware())
delivery_router.callback_query.middleware(DeliveryRoleMiddleware())

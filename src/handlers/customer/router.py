from aiogram import Router

from src.middleware.role import CustomerRoleMiddleware

from .products.router import products_router

customer_router = Router()

customer_router.include_router(products_router)

customer_router.message.middleware(CustomerRoleMiddleware())
customer_router.callback_query.middleware(CustomerRoleMiddleware())

from typing import Sequence

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.products.schemas import ProductCreate, ProductUpdate, ProductUpdatePartial
from core.models import Product


async def get_products(session: AsyncSession) -> Sequence[Product]:
    stmt = select(Product).order_by(Product.id)
    results: Result = await session.execute(stmt)

    products = results.scalars().all()
    return products


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(
    session: AsyncSession, product: ProductCreate
) -> Product | None:
    product_in = Product(**product.model_dump())
    session.add(product_in)
    await session.commit()
    await session.refresh(product_in)
    return product_in


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductUpdate | ProductUpdatePartial,
    partial: bool = False,
) -> Product:
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
        await session.commit()
    return product


async def delete_product(session: AsyncSession, product: Product) -> None:
    await session.delete(product)
    await session.commit()

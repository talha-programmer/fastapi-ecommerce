import random
from datetime import datetime
from sqlalchemy.orm import Session

from db.models.inventory import Inventory
from pydantic_schemas.inventory import InventoryCreate
from pydantic_schemas.product import Product
from ..products import get_products
from helper import generate_random_time



def seed_inventory(db: Session):
    products = get_products(db, 0, 1000);
    for product in products:
        generate_inventories(db, product)



# Generate 100 inventory records for each product by default
def generate_inventories(db:Session, product: Product, entries:int = 100):
    all_quantities = []
    for i in range(entries):
        quantity = random.randint(-20, 30)
        all_quantities.append(quantity)
        update_time = generate_random_time(datetime(2020, 1, 1), datetime.now())
        inventory = InventoryCreate(quantity=quantity, product_id=product.id, created_at=update_time, updated_at=update_time)
        create_inventory(db, inventory, product)



def create_inventory(db: Session, inventory: InventoryCreate, product: Product):
    db_inventory = Inventory(
        quantity=inventory.quantity,
        product_id=inventory.product_id,
        created_at = inventory.created_at,
        updated_at = inventory.updated_at
    )
    db.add(db_inventory)

    product.stock = sum([product.stock, inventory.quantity])
    db.add(product)

    db.commit()
    db.refresh(db_inventory)

    return db_inventory 


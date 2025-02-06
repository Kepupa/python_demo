import psycopg2

from partners_type import Product, Partner, Sale

# Press the green button in the gutter to run the script.
def connect_db():
    return psycopg2.connect(
        dbname="demo",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

def fetch_data():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        # Мне кажется, что так будет проще создать объект, а то вот так вот через x[..], выглядит страшно...
        cursor.execute("SELECT product_type_id, product_name, minimum_cost_for_partner FROM products")
        product_data = [Product(*row) for row in cursor.fetchall()]


        cursor.execute("SELECT partner_type, partner_name, director, partner_email, partner_phone, partner_adress, inn, rating FROM partners")
        partners_data = [Partner(*row) for row in cursor.fetchall()]


        cursor.execute("SELECT partner_id, product_id, quantity_of_production FROM partner_products")
        sale_data = [Sale(*row) for row in cursor.fetchall()]

        cursor.close()
        connection.close()
        return product_data, partners_data, sale_data

    except psycopg2.Error as e:
        print("Ошибка подключения к базе данных!", e)



if __name__ == "__main__":
    products, partners, sales = fetch_data()


    for sale in sales:
        discount = sale.calculate_discount()
        print(f"Партнер {sale.partner_id} купил продукт {sale.product_id} → скидка {discount}%")
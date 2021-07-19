from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
STATE_CHOICES = (("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"), ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"), ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "), ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"), ("Nagaland", "Nagaland"), ("Odisha", "Odisha"),
                 ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"), ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"), ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"), ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"), ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"), ("Puducherry", "Puducherry"))

Category_Choice = (
    ('M', 'Mobile'),
    ('L', 'Laptops'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
    ('BG', 'Bag'),
    ('HP', 'HeadPhone'),
    ('W', 'Watches'),
    ('S', 'Shoes'),
)

BANK_CHOICES = (
    ('State Bank of India (SBI)', 'State Bank of India (SBI)'),
    ('Punjab National Bank', 'Punjab National Bank'),
    ('Bank of Baroda', 'Bank of Baroda'),
    ('Canara Bank', 'Canara Bank'),
    ('Union Bank of India', 'Union Bank of India'),
    ('Bank of India', 'Bank of India'),
    ('Indian Bank', 'Indian Bank'),
    ('Central Bank of India', 'Central Bank of India'),
    ('Indian Overseas Bank', 'Indian Overseas Bank'),
    ('UCO Bank', 'UCO Bank'),
    ('Bank of Maharashtra', 'Bank of Maharashtra'),
    ('Punjab & Sindh Bank', 'Punjab & Sindh Bank'),
    ('Axis', 'Axis'),
    ('Bandhan', 'Bandhan'),
    ('HDFC', 'HDFC'),
    ('ICICI', 'ICICI'),
    ('IDBI', 'IDBI'),
    ('Kotak Mahindra', 'Kotak Mahindra'),
    ('South Indian Bank', 'South Indian Bank'),
    ('Yes Bank', 'Yes Bank'),
    ('IndusInd Bank', 'IndusInd Bank'),
)

CANCLE_CHOICES = (
    ('ORDER_MISTAKE', 'ORDER_CREATED_BY_MISTAKE'),
    ('NOT_ARRIVED_TIME', 'ITEM NOT ARRIVED ON TIME'),
    ('S_HIGH_COST', 'SHIPPING COST TOO HIGH'),
    ('I_HIGH_COST', 'ITEM COST TOO HIGH'),
    ('FOUND_CHEAPER', 'FOUND CHEAPER SOMEWHERE ELSE'),
    ('CHANGE_S_ADDRESS', 'NEED TO CHANGE SHIPPING ADDRESS'),
    ('CHANGE_S_SPEED', 'NEED TO CHANGE SHIPPING SPEED'),
    ('CHANGE_BILLING_ADDRESS', 'NEED TO CHANGE BILLING ADDRESS'),
    ('CHANGE_PAYMETHOD', 'NEED TO CHANGE PAYMENT METHOD'),
    ('OTHER', 'OTHER'),
)

RETURN_CHOICES = (
    ('BAD_QUALITY', 'ORDER_CREATED_BY_MISTAKE'),
    ('PRODUCT_DAMAGE', 'ITEM NOT ARRIVED ON TIME'),
    ('MISSING_PART', 'SHIPPING COST TOO HIGH'),
    ('PRODUCT_AND_BOX_DAMAGE', 'ITEM COST TOO HIGH'),
    ('WRONG_ITEM_SEND', 'FOUND CHEAPER SOMEWHERE ELSE'),
    ('ITEM_DEFECTIVE', 'NEED TO CHANGE SHIPPING ADDRESS'),
    ('OTHER', 'OTHER'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Customer'


class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=Category_Choice, max_length=2)
    product_image = models.ImageField(upload_to='productImg')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Product'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Cart'

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price


STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancled', 'Cancled'),
    ('Return', 'Return'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'OrderPlaced'

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price


class CancledOrders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderplaced = models.ForeignKey(OrderPlaced, on_delete=models.CASCADE)
    reason = models.CharField(choices=CANCLE_CHOICES,
                              max_length=50)
    cancle_date = models.DateTimeField(auto_now_add=True)
    bank_name = models.CharField(
        choices=BANK_CHOICES, max_length=50,)
    bank_acc = models.CharField(max_length=50)
    bank_ifsc = models.CharField(max_length=20, blank=True, null=True)
    holder_name = models.CharField(max_length=150, blank=True, null=True)
    upi_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Order_Cancled'


class ReturnOrders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderplaced = models.ForeignKey(OrderPlaced, on_delete=models.CASCADE)
    rreason = models.CharField(
        choices=RETURN_CHOICES, max_length=150)
    return_date = models.DateTimeField(auto_now_add=True)
    bank_name = models.CharField(
        choices=BANK_CHOICES, max_length=50)
    bank_acc = models.CharField(max_length=50)
    bank_ifsc = models.CharField(max_length=20, blank=True, null=True)
    holder_name = models.CharField(max_length=150, blank=True, null=True)
    upi_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Order_Return'

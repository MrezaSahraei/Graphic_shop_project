# مرحله اول: استفاده از یک تصویر پایه
FROM python:3.10-slim

# تعیین دایرکتوری کاری
WORKDIR /usr/src/app

# کپی کردن فایل نیازمندی‌ها و نصب آن‌ها
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن بقیه کدهای پروژه
COPY . .

# اگر پورت 8000 را استفاده می‌کنید
EXPOSE 8000

# دستور اجرای برنامه (بسته به پروژه شما ممکن است فرق کند)
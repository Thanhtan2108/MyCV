from weasyprint import HTML
import os

# Đường dẫn đến file HTML
html_file_path = 'index.html'  # Thay đổi nếu file HTML của bạn nằm ở vị trí khác

# Đường dẫn đến file PDF đầu ra
output_pdf_path = 'output/resume.pdf'  # Thư mục và tên file PDF đầu ra

# Đảm bảo thư mục đầu ra tồn tại
os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)

# Đọc nội dung file HTML
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Chuyển HTML thành PDF
HTML(string=html_content, base_url=os.path.dirname(html_file_path)).write_pdf(output_pdf_path)

print(f"File PDF đã được lưu tại: {output_pdf_path}")
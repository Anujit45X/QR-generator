import qrcode

def generate_instagram_qr(leomessi):
    # Construct the Instagram profile URL
    instagram_url = f'https://www.instagram.com/{leomessi}/'

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(instagram_url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image or display it
    img.save(f'{leomessi}_instagram_qr.png')
    print(f"Instagram QR code for {leomessi} generated and saved.")

if __name__ == "__main__":
    # Replace 'messi' with the desired Instagram username
    generate_instagram_qr('leomessi')

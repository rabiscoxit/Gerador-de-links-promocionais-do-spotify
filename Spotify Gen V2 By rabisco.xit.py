import random
import string

def generate_random_code(length=9):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_links(num_links=10):
    base_url = "https://www.spotify.com/br-pt/ppt/microsoft/?code="
    for _ in range(num_links):
        code = generate_random_code()
        print(f"{base_url}{code}")

def main():
    print("Gerador de Links Spotify by rabisco.xit")
    num_links = int(input("Quantos links você quer gerar? "))
    generate_links(num_links)
    input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()

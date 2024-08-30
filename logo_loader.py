from PIL import Image, ImageTk

def load_logo(image_path, size=(50, 50)):
    """
    Carrega e redimensiona uma imagem de logo.

    Args:
        image_path (str): Caminho para a imagem do logo.
        size (tuple): Novo tamanho para redimensionar a imagem (largura, altura).

    Returns:
        ImageTk.PhotoImage: Imagem redimensionada pronta para uso no Tkinter.
    """
    logo = Image.open(image_path)
    logo = logo.resize(size)
    logo = ImageTk.PhotoImage(logo)
    return logo

def load_logos():
    """
    Carrega e redimensiona múltiplos logos.

    Returns:
        dict: Um dicionário contendo os logos redimensionados.
    """
    logos = {
        "cadastrar": load_logo("cadastrar.png"),
        "deletar": load_logo("deletar.png"),
        "update": load_logo("update.png"),
        "save": load_logo("save.png"),
        "adicionar": load_logo("adicionar.png")
    }
    return logos

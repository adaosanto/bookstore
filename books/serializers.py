from django.utils import timezone
from rest_framework import serializers

from .models import Book


class BookModelSerializer(serializers.ModelSerializer):
    """Serializador para o modelo Book."""

    class Meta:
        """Metaclasse para configurar o serializador."""

        model = Book  # Define o modelo associado ao serializador.
        fields = (
            "__all__"  # Especifica todos os campos do modelo para serem serializados.
        )

    def validate_publication_year(self, value):
        """
        Valida o ano de publicação do livro.

        Verifica se o ano de publicação está dentro de limites razoáveis.

        Args:
            value (int): O ano de publicação a ser validado.

        Returns:
            int: O ano de publicação, se for válido.

        Raises:
            serializers.ValidationError: Se o ano de publicação for anterior a 1900 ou maior que o ano atual.
        """
        if value < 1900:
            raise serializers.ValidationError(
                "A data de publicação não pode ser anterior a 1900."
            )

        if value > timezone.now().year:
            raise serializers.ValidationError(
                "A data de publicação não pode ser maior que o ano atual."
            )

        return value

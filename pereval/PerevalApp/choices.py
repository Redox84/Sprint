
# Список уровней сложности
LEVELS_CHOICES = (
    ('1a', '1А'),
    ('1b', '1Б'),
    ('2a', '2А'),
    ('2b', '2Б'),
    ('3a', '3А'),
    ('3b', '3Б'),
)

# Список статусов
NEW = 'NW'
PENDING = 'PN'
ACCEPTED = 'AC'
REJECTED = 'RJ'
STATUS_CHOICES = (
    ('NW', 'Новый'),
    ('AC', 'На модерации'),
    ('PN', 'Принят'),
    ('RJ', 'Отклонён'),
)
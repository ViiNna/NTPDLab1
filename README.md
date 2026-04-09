Odopwiedzi na zadanie 5: 

Różnice we wdrażaniu modelu ML w środowisku produkcyjnym a deweloperskim:
środowisko developerskie:
-jest mniejsze i statyczne, z naszego PC
-możemy używać dowolnych bibliotek
-jeśli wystąpi błąd to jest to nasz problem
-wdrażany u nas ręcznie 
-nie ma domyślnego monitorowania
-retraining jest ręczny 


środowisko produkcyjne:
-jest dużo większe i strumieniowe
-ma z góry określone biblioteki w requirements
-błędy nie mogą występować bo musi działać ciągle
-wdrażany z użyciem np kontenerów dockera itd
-możliwe jest monitorowanie przez tracking danych
-retraining wykonuje się automatycznie



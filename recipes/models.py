from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class RecipeIngredients(models.Model):
    # 레시피 코드
    recipe_id = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10000000)]
    )
    # 재료 순번
    irdnt_sn = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10000000)]
    )
    # 재료명
    irdnt_nm = models.CharField(max_length=20)
    # 재료용량
    irdnt_cpcty = models.CharField(max_length=20)
    # 재료타입 코드
    irdnt_ty_code = models.CharField(max_length=10)
    # 재료타입명
    irdnt_ty_nm = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.recipe_id} - {self.irdnt_sn} - {self.irdnt_nm} - {self.irdnt_cpcty} - {self.irdnt_ty_code} - {self.irdnt_ty_nm}'

class RecipeInfo(models.Model):
    # 레시피 코드
    recipe_id = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10000000)]
    )
    # 레시피 이름
    recipe_nm_ko = models.CharField(max_length=15)
    # 간략(요약)소개
    sumry = models.CharField(max_length=100)
    # 유형코드
    nation_code = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10000000)]
    )
    # 유형분류
    nation_nm = models.CharField(max_length=10)
    # 음식분류코드
    ty_code = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10000000)]
    )
    # 음식분류
    ty_nm = models.CharField(max_length=10)
    # 조리시간
    cooking_time = models.CharField(max_length=10)
    # 칼로리
    calorie = models.CharField(max_length=10)
    # 분량
    qnt = models.CharField(max_length=10)
    # 난이도
    level_nm = models.CharField(max_length=10)
    # 재료별 분류명
    irdnt_code = models.CharField(max_length=10)
    # 가격별 분류
    pc_nm = models.CharField(max_length=10)

    def __str__(self):
        return (f'''{self.recipe_id}-{self.recipe_nm_ko}-{self.sumry}-
                {self.nation_code}-{self.nation_nm}-{self.ty_code}-
                {self.ty_nm}-{self.cooking_time}-{self.calorie}-
                {self.qnt}-{self.level_nm}-{self.irdnt_code}-{self.pc_nm}''')

class RecipeCourse(models.Model):
    # 레시피 코드
    recipe_id = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10000000)]
    )
    # 요리설명순서
    cooking_no = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)]
    )
    # 요리 설명
    cooking_dc = models.CharField(max_length=300)
    # 과정팁
    step_tip = models.CharField(max_length=100)
    def __str__(self):
        return(f'{self.recipe_id}-{self.cooking_no}-{self.cooking_dc}-{self.step_tip}')


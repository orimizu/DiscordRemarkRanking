## �f�B���N�g���\��

```
DiscordRemarkRanking
  +-- log
  | +-- 20230410
  | +-- yyyymmdd
  +-- python_auto
    +-- result
    | +-- 20230410
    +-- discord_log_analysis.bat
    +-- discord_log_analysis.py
    +-- reaction_image_csv2html.py
    +-- sort_remark_ranking.py
    +-- UTF-8_BOM.txt
```

## �����L���O�쐬�菇

1. DiscordChatExporter �Ń��O���_�E�����[�h���܂��B

* Discord�̃��O�́ADiscordChatExporter �Ń_�E�����[�h���邱�Ƃ�z�肵�Ă��܂�
  * DiscordChatExporter���̂́AGitHub�Ō��J����Ă���A�ȉ���URL��Readme.md��Download�̃Z�N�V�����̃����N��Ń_�E�����[�h�ł��܂�
  * https://github.com/Tyrrrz/DiscordChatExporter
  * �h�L�������g�͈ȉ����Q�Ƃ��Ă�������
  * https://github.com/Tyrrrz/DiscordChatExporter/tree/master/.docs
* Discord\log �̉��ɁAyyyymmdd�`���̃t�H���_���쐬���܂��B(�Ⴆ�΁A20230410�Ȃ�)
  * �Ⴆ�΁A20230410�t�H���_�̏ꍇ�A�ȉ��̃t�@�C���ɂȂ�悤�Ƀ_�E�����[�h���܂��B
  * Discord\log\20230410\�}������2022�a�����L�OLIVE�T�[�o�[ - Text Channels - �G�k�R�[�i�[ [1015156495366762533].json

2. discord_log_analysis.bat ��ҏW���ăp�����[�^���X�V���܂�

* LOG_SUB_DIR
  * ���O�p�̃t�H���_���ł��B��{�A�_�E�����[�h�����g���Ă��܂��B�ȉ���json�t�@�C�������݂���l�ɐݒ肵�Ă�������
  * DiscordRemarkRanking\log\%LOG_SUB_DIR%\�}������2022�a�����L�OLIVE�T�[�o�[ - Text Channels - �G�k�R�[�i�[ [1015156495366762533].json
  * �ȉ��A�ݒ��ł�
    * set LOG_SUB_DIR=20230410
* B_YEAR B_MONTH
  * 2023�N3���̌��ԏW�v�A�T�[�o�J�n����2023�N3�����܂ł̏W�v������ꍇ
  * B_YEAR=2023  B_MONTH=03 �ƂȂ�܂��B
  * �ȉ��A�ݒ��ł�
    * set B_YEAR=2023
    * set B_MONTH=3
* B_M_ENG 
  * B_MONTH�̉p��\�L�����܂� Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
  * �R�}���h�v�����v�g�ł́A�z�񂪎g���Ȃ��悤�Ȃ̂ŁA�蓮�����ɂԂ񓊂��Ă��܂�
  * �ȉ��A�ݒ��ł�
    * set B_M_ENG=Mar

3. �o�b�`�����s���܂�

* python�Ƀp�X���ʂ��Ă���R�}���h�v�����v�g���J���܂�
* Discord\python_auto �t�H���_�� cd ���܂�
* discord_log_analysis.bat �����s���܂�

4. �쐬�t�@�C���̊m�F

* DiscordRemarkRanking\python_auto\result\%LOG_SUB_DIR% �ɁAcsv�t�@�C�����Q�Ahtml�t�@�C�����Q�o���Ă���̂Œ��g���m�F���Ă�������(�ȉ��́AB_YEAR=2023  B_MONTH=3  B_M_ENG=Mar �Őݒ肵���Ƃ��̗�ł��j
  * reaction_emoji_ranking_20230401.html
  * reaction_emoji_ranking_2023Mar.html
  * remark_ranking_20230401.csv
  * remark_ranking_2023Mar.csv

csv�́Aexcel�Œ��ڊJ���܂�
�������́Agoogle �X�v���b�h�V�[�g��import�\�ł�


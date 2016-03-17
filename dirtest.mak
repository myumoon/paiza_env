# 
# �w��f�B���N�g���ɑ��݂���e�X�g�t�@�C����S�ăe�X�g���܂��B
# 
# -- ���� --
# TEST_PROG : ���s�v���O����(python)
# TEST_DIR  : �e�X�g�t�@�C�����i�[����Ă���f�B���N�g���ւ̃p�X
#             �e�t�@�C���̓t�@�C���������s���ʂłȂ���΂Ȃ�Ȃ��B
# 


TEST_FILES=${notdir ${shell find $(TEST_DIR)/ -maxdepth 1 -type f}}

.PHONY: all clear
.SECONDARY:

all:$(TEST_FILES)
	@echo all done
	
clear:
	@echo clear done


%: $(TEST_DIR)/test_work/%.test $(TEST_DIR)/test_work/%.ans
	python test.py -e $(TEST_PROG) -if $(TEST_DIR)/test_work/$*.test -af $(TEST_DIR)/test_work/$*.ans

$(TEST_DIR)/test_work/%.test:
	@mkdir -p $(TEST_DIR)/test_work
	@sed -e '$$d' $(TEST_DIR)/$* > $(TEST_DIR)/test_work/$*.test

$(TEST_DIR)/test_work/%.ans:
	@mkdir -p $(TEST_DIR)/test_work
	@sed -n -e '$$p' $(TEST_DIR)/$* > $(TEST_DIR)/test_work/$*.ans

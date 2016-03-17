# 
# 指定ディレクトリに存在するテストファイルを全てテストします。
# 
# -- 引数 --
# TEST_PROG : 実行プログラム(python)
# TEST_DIR  : テストファイルが格納されているディレクトリへのパス
#             各ファイルはファイル名が実行結果でなければならない。
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

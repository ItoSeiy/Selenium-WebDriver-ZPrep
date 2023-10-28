# chrome設定

# 同意チェック項目
AGREEMENT_ELEMENTS = ['/html/body/div[5]/div/div/div/form/div[1]/div/div/div[1]/input',
                    '/html/body/div[5]/div/div/div/form/div[1]/div/div/div[2]/input',
                    '/html/body/div[5]/div/div/div/form/div[1]/div/div/div[3]/input',
                    '/html/body/div[5]/div/div/div/form/div[1]/div/div/div[4]/input',
                    '/html/body/div[5]/div/div/div/form/div[1]/div/div/div[5]/input']
AGREEMENT_BUTTON = '/html/body/div[5]/div/div/div/form/div[2]/button'

# 必修教材のみボタン
ONLY_REQUIRED_SUBJECT_BUTTON = '/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[1]/div[1]/div[2]/div/div[2]/button[1]'

# 動画エレメントの格納場所
VIDEO_ELEMENTS_CONTAINER = '//*[@id="root"]/div/div[2]/div[2]/main/div[2]/div/div[1]/ul'
# 動画エレメントのタグ
VIDEO_ELEMENT_TAG = 'li'
# 不変な動画エレメントのクラス名
VIDEO_ELEMENT_CLASS_NAME = 'sc-aXZVg sc-gEvEer sc-lcfvsp-11 dKubqp fteAEG hZhBzF'

# 動画エレメントが開かれている時のクラス名
OPENING_VIDEO_ELEMENT_CLASS_NAME = 'sc-aXZVg sc-gEvEer hYNtMZ fteAEG sc-1otp79h-0 sc-35qwhb-0 evJGlU crtNbk'
# 動画エレメントが解放されている時のクラス名
OPEND_VIDEO_ELEMENT_CLASS_NAME = 'sc-aXZVg sc-gEvEer hYNtMZ fteAEG sc-1otp79h-0 sc-35qwhb-0 evJGlU cpELFc'
# 動画が未開放の時のクラス名
CLOSED_VIDEO_ELEMENT_CLASS_NAME = 'sc-aXZVg sc-gEvEer hYNtMZ fteAEG sc-1otp79h-0 sc-35qwhb-0 evJGlU hoWVG'
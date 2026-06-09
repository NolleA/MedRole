import uuid
import json

CASES = [
    # ============================================================
    # Case 01: 纤维肌痛综合征 (Fibromyalgia) - 模块2/第七周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "纤维肌痛综合征",
        "department": "风湿免疫科",
        "difficulty": "intermediate",
        "chief_complaint": "医生们已经拿我没办法了。哪里都疼！我尝试了所有方法，但都无济于事。",
        "patient_profile": json.dumps({
            "name": "杨扬",
            "age": 42,
            "gender": "女",
            "occupation": "园丁主管",
            "marital_status": "未婚",
            "education": "本科（历史学）"
        }),
        "symptoms_description": (
            "全身多处慢性疼痛，髋部和背部关节疼痛评分8/10，纤维肌痛压痛评分6/10。"
            "背部疼痛呈间歇性尖锐痛伴刺痛和肌肉痉挛，纤维肌痛压痛为持续性钝痛。"
            "坐15分钟、站5分钟、行走1.6公里后疼痛加剧。举起14kg以上重量困难。"
            "大学滑雪时右髋受伤后出现关节炎，之后驾驶割草机翻倒致背部受伤。一年前诊断为纤维肌痛，一个月前因无法忍受疼痛停止工作。"
            "目前服用萘普生、对乙酰氨基酚、维可丁、愈创甘油醚、舒筋灵，并以利多卡因局部封闭。"
            "儿童时代有多次损伤史：7岁锁骨骨折，14岁因反复下腹痛行腹部探查术（未发现异常）。"
            "因与男友分手感到更加压抑，入睡和维持睡眠均困难，偶用安定。经常头痛，偶有复视。"
            "注意力、回忆能力下降，自称'笨拙'，过去几个月体重增加4.5kg。否认自杀想法但感觉生命正'从身边溜走'。"
            "十几岁时曾尝试可卡因、安非他命和LSD。父母酗酒。"
        ),
        "physical_exam": json.dumps({
            "general": "身高168cm，体重54.4kg",
            "vitals": "BP 130/68mmHg，P 76次/分",
            "musculoskeletal": "背部两侧、右髋部、右小腿和左肩部明显弥散性压痛，无肌萎缩，四肢肌力正常，反射正常",
            "neurological": "反射正常，四肢肌力正常"
        }),
        "emotional_state": "anxious",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问疼痛的具体部位和分布", "weight": 1},
                {"id": "2", "category": "chief_complaint", "text": "询问疼痛的性质（尖锐/钝痛）和强度评分", "weight": 1},
                {"id": "3", "category": "chief_complaint", "text": "询问疼痛的诱发和缓解因素（坐、站、行走）", "weight": 1},
                {"id": "4", "category": "associated_symptoms", "text": "询问伴随症状：头痛、复视、睡眠障碍、疲劳、注意力下降", "weight": 1},
                {"id": "5", "category": "pmh", "text": "询问童年损伤史：骨折、手术、运动损伤", "weight": 1},
                {"id": "6", "category": "pmh", "text": "询问纤维肌痛的诊断过程及之前治疗效果", "weight": 1},
                {"id": "7", "category": "medications", "text": "详细询问当前所有用药情况，特别是阿片类药物（维可丁）的使用时长和剂量", "weight": 2},
                {"id": "8", "category": "social_history", "text": "询问心理社会因素：情绪状态、压力、人际关系、药物滥用史", "weight": 1},
                {"id": "9", "category": "differential", "text": "询问有无晨僵、关节肿胀、皮疹等提示炎症性关节病的症状", "weight": 1},
                {"id": "10", "category": "red_flag", "text": "评估阿片类药物成瘾风险和自杀意念", "weight": 2},
                {"id": "11", "category": "red_flag", "text": "评估抑郁程度及是否需要心理科会诊", "weight": 1}
            ],
            "total_items": 11,
            "total_weight": 13
        }),
        "key_questions": json.dumps([
            "疼痛的具体部位在哪里？什么情况下会加重？",
            "您每天服用哪些药物？每种药的剂量是多少？",
            "您现在睡眠情况怎么样？入睡困难还是容易醒？",
            "您是否有过不想活下去的念头？",
            "除了疼痛，您还注意到身体有什么其他变化吗？"
        ]),
        "red_flags": json.dumps([
            "长期使用阿片类药物（维可丁）有成瘾风险",
            "患者表达过生命'从身边溜走'，需评估抑郁和自杀风险",
            "偶有复视，需排除神经系统器质性病变",
            "多种药物联用需关注药物相互作用"
        ]),
        "diagnosis": "纤维肌痛综合征（Fibromyalgia）",
        "is_active": 1
    },

    # ============================================================
    # Case 02: 腰椎间盘突出症 (Lumbar Disc Herniation) - 模块2/第三周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "腰椎间盘突出症（L4-L5）",
        "department": "骨科",
        "difficulty": "beginner",
        "chief_complaint": "医生，我腰疼得厉害，跑着跑着就摔倒了，右脚有点拖沓，腿上像电击一样疼。",
        "patient_profile": json.dumps({
            "name": "陈钢",
            "age": 32,
            "gender": "男",
            "occupation": "军官（上尉）",
            "marital_status": "不详",
            "education": "不详"
        }),
        "symptoms_description": (
            "每天沿海滩跑步锻炼，跑步约5公里时出现下腰部和右髋发紧，后出现痉挛从腰部蔓延到髋和大腿外侧，向下延伸到膝盖。"
            "若继续跑疼痛会蔓延到小腿并持续数小时。躺下后疼痛缓解，但站起来或跑步则立刻加剧。"
            "某日跑步时右脚突然陷进沙地摔倒，被扶起后右脚拖沓，感到电击般刺痛从下腰部穿过右侧大腿传到小腿外侧面。"
            "当场被送往军区医院。既往史不详，无明确用药史。"
        ),
        "physical_exam": json.dumps({
            "general": "一步一拐走入诊室，因背痛背部活动范围受限",
            "musculoskeletal": "右侧脊柱旁部位和右髌肌肉明显压痛和痉挛。右腿直腿抬高至30度加剧腰部疼痛并放射到髋、大腿侧面及小腿外侧面。左腿直腿抬高正常（0-70度未出现疼痛）",
            "motor": "胫骨前肌肌力4/5",
            "reflexes": "深部腱反射全身2+，包括膝反射和踝反射",
            "sensory": "对轻触、针刺感觉正常，足背包括前三个脚趾出现轻微感觉减退"
        }),
        "emotional_state": "stoic",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问疼痛的放射方向（腰部-大腿-小腿外侧）", "weight": 1},
                {"id": "2", "category": "chief_complaint", "text": "询问疼痛的诱发和缓解因素（跑步加重、躺下缓解）", "weight": 1},
                {"id": "3", "category": "associated_symptoms", "text": "询问有无下肢无力、感觉异常、大小便功能障碍", "weight": 2},
                {"id": "4", "category": "pmh", "text": "询问既往外伤史、背部受伤史及类似发作史", "weight": 1},
                {"id": "5", "category": "physical_exam", "text": "了解直腿抬高试验结果和肌力检查", "weight": 1},
                {"id": "6", "category": "physical_exam", "text": "了解感觉和反射检查结果", "weight": 1},
                {"id": "7", "category": "differential", "text": "考虑腰椎间盘突出、腰椎管狭窄或梨状肌综合征的鉴别", "weight": 1},
                {"id": "8", "category": "red_flag", "text": "询问有无大小便功能障碍（马尾综合征）", "weight": 2},
                {"id": "9", "category": "red_flag", "text": "评估进行性下肢无力的程度", "weight": 2},
                {"id": "10", "category": "imaging", "text": "询问是否需要MRI或CT进一步评估", "weight": 1}
            ],
            "total_items": 10,
            "total_weight": 13
        }),
        "key_questions": json.dumps([
            "疼痛从腰部放射到哪个部位？做什么动作会加重？",
            "您有没有感觉腿或脚麻木、无力？",
            "您排尿和排便正常吗？有没有失禁或排尿困难？",
            "您以前有没有过腰部外伤或类似的疼痛发作？",
            "躺下来休息后疼痛能缓解多少？"
        ]),
        "red_flags": json.dumps([
            "足下垂或进行性下肢无力提示神经根严重受压",
            "大小便功能障碍提示马尾综合征，需紧急手术",
            "右腿直腿抬高仅30度即诱发疼痛，提示神经根明显受压"
        ]),
        "diagnosis": "腰椎间盘突出症（L4-L5，右侧）",
        "is_active": 1
    },

    # ============================================================
    # Case 03: 特发性震颤 + 帕金森病 (Essential Tremor + Parkinson's) - 模块2/第五周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "特发性震颤合并帕金森病",
        "department": "神经内科",
        "difficulty": "advanced",
        "chief_complaint": "医生，我和内人都注意到我的双手震颤不断加重，写字都写不清楚了，喝了酒之后反而会好一点。",
        "patient_profile": json.dumps({
            "name": "Langley",
            "age": 41,
            "gender": "男",
            "occupation": "前业余拳击手",
            "marital_status": "已婚",
            "education": "不详"
        }),
        "symptoms_description": (
            "5年来出现进行性双手快速震颤，写字时、喝咖啡或可乐后或端杯子时震颤加剧。"
            "双手放在膝上时震颤消失，饮酒后震颤减轻。患者父亲和叔叔有严重震颤史，父亲甚至无法端起咖啡、无法写字、自己吃饭都有困难，家人以为得了帕金森病。"
            "3年前使用治疗支气管炎的吸入式B受体激动剂后手和头出现颤动。曾用甲哌氯丙嗪（compazine）治疗恶心呕吐，导致头部僵硬如雕像面向左面，需注射药物消除。"
            "初诊后服用心得安（普萘洛尔）每日60mg，最初有效但需加大用量，后出现性功能问题和站立时头晕。"
            "数年后休息时也出现震颤，频率稍慢，伸手时震颤有所缓解，出现行动迟缓、僵硬，字迹慢慢变小。"
        ),
        "physical_exam": json.dumps({
            "mental_status": "神志清醒，定向力完整，记忆力和语言能力正常，说话声音轻，语音单调",
            "cranial_nerves": "I-XII正常，面部表情较少，眨眼明显减少",
            "motor": "所有肌群肌力正常。肌张力中度僵硬，伴明显静止性震颤，频率约3-5/秒，右手更明显。右脚轻微震颤，偶尔嘴唇抖动。紧张时震颤加剧幅度加大频率降低。保持姿势时震颤会消失一会",
            "reflexes": "肱二头肌、桡骨膜反射、肱三头肌、膝反射和跟腱反射2+。Babinski征阴性。眉间反射阳性",
            "gait": "步态不利索，转身困难速度很慢不流畅。头、躯干和胳膊姿势弯屈，走路时胳膊不会随之摆动。字迹潦草，字越写越小"
        }),
        "emotional_state": "anxious",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问震颤的具体特点：部位、频率、诱发和缓解因素", "weight": 1},
                {"id": "2", "category": "chief_complaint", "text": "询问震颤从动作性到静止性的演变过程", "weight": 1},
                {"id": "3", "category": "associated_symptoms", "text": "询问伴随运动症状：行动迟缓、僵硬、姿势改变、字迹变小（小写症）", "weight": 2},
                {"id": "4", "category": "pmh", "text": "询问既往用药史：B受体激动剂、甲哌氯丙嗪对震颤的影响", "weight": 1},
                {"id": "5", "category": "family_history", "text": "询问家族中震颤或帕金森病史", "weight": 1},
                {"id": "6", "category": "medications", "text": "询问心得安治疗效果及副作用（性功能、头晕）", "weight": 1},
                {"id": "7", "category": "physical_exam", "text": "了解静止性震颤特征、肌张力、步态、面部表情（面具脸）", "weight": 1},
                {"id": "8", "category": "differential", "text": "区分特发性震颤（动作性、饮酒减轻）与帕金森病震颤（静止性、搓丸样）", "weight": 2},
                {"id": "9", "category": "differential", "text": "考虑药物性震颤、小脑性震颤等其他类型", "weight": 1},
                {"id": "10", "category": "imaging", "text": "询问是否需要MRI或PET检查以明确诊断", "weight": 1}
            ],
            "total_items": 10,
            "total_weight": 12
        }),
        "key_questions": json.dumps([
            "您的震颤什么时候最明显？写字、端杯子还是休息的时候？",
            "喝酒之后震颤真的会减轻吗？能减轻多少？",
            "您有没有注意到自己走路变慢、转身困难或者面部表情变少？",
            "您家里人还有谁有类似的震颤？",
            "您之前用过什么药来治疗震颤？效果怎么样？"
        ]),
        "red_flags": json.dumps([
            "静止性震颤的出现提示可能合并帕金森病",
            "行动迟缓和僵硬提示疾病进展需调整治疗方案",
            "字迹逐渐变小（小写症）是帕金森病的典型表现",
            "药物副作用（性功能障碍、体位性低血压）影响生活质量"
        ]),
        "diagnosis": "特发性震颤（Essential Tremor）合并早期帕金森病（Parkinson's Disease）",
        "is_active": 1
    },

    # ============================================================
    # Case 04: 类风湿关节炎 (Rheumatoid Arthritis) - 模块2/第八周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "类风湿关节炎",
        "department": "风湿免疫科",
        "difficulty": "intermediate",
        "chief_complaint": "杜教授，我最近几个月双手又疼又僵，早上醒来特别严重，要过好几个小时才能慢慢活动开，弹琴的时候尤其难受。",
        "patient_profile": json.dumps({
            "name": "安娜",
            "age": 35,
            "gender": "女",
            "occupation": "乐队钢琴师",
            "marital_status": "未婚",
            "education": "不详"
        }),
        "symptoms_description": (
            "近几个月出现双手间歇性疼痛、僵硬，醒来时尤为严重，持续数小时才慢慢舒展开。有时温水淋浴后手部会舒适一些。"
            "演奏贝多芬第五（皇帝）协奏曲华彩乐段时特别疼痛甚至难以完成。"
            "服用朋友推荐的营养补品葡萄糖胺和硫酸软骨素。否认服用任何药物，未服用口服避孕药。"
            "月经周期规律，未怀孕过。不吸烟、不吸毒、不饮酒。"
            "去年夏天去奥地利萨尔茨堡音乐节期间在森林中远足时得过一次皮疹。"
            "近亲中无类似关节和软组织疾病患者。"
        ),
        "physical_exam": json.dumps({
            "general": "体重54.4kg，身高162.6cm",
            "vitals": "BP 110/80mmHg（两臂），P 70次/min律齐，无发热",
            "head_neck": "头皮、发际、面部皮肤无异常或脱发。无甲状腺肿大",
            "chest": "肺、乳房和心脏正常，未闻及心脏杂音和心包摩擦音",
            "abdomen": "正常，无肝脾肿大",
            "musculoskeletal": "手腕部温热、有压痛，双侧腕关节伸展范围缩小，右手更严重。两手食指、中指和无名指掌指关节和近侧指间关节温热、饱胀感，右手更严重。涉及关节弯曲能力降低，握力减小。右足侧压时患者表现痛苦",
            "neurological": "正常"
        }),
        "emotional_state": "anxious",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问关节疼痛和僵硬的具体特点：部位、对称性、晨僵持续时间", "weight": 2},
                {"id": "2", "category": "chief_complaint", "text": "询问症状对职业功能的影响（演奏钢琴的具体困难）", "weight": 1},
                {"id": "3", "category": "associated_symptoms", "text": "询问伴随全身症状：皮疹、发热、疲劳、体重变化", "weight": 1},
                {"id": "4", "category": "pmh", "text": "询问近期感染史、旅行史（奥地利远足后皮疹的意义）", "weight": 1},
                {"id": "5", "category": "family_history", "text": "询问家族中关节病、自身免疫病史", "weight": 1},
                {"id": "6", "category": "medications", "text": "询问营养补品使用情况（葡萄糖胺、硫酸软骨素）", "weight": 1},
                {"id": "7", "category": "physical_exam", "text": "了解关节检查结果：受累关节分布（对称性）、有无畸形、握力情况", "weight": 1},
                {"id": "8", "category": "differential", "text": "考虑类风湿关节炎与骨关节炎、银屑病关节炎、感染后关节炎的鉴别", "weight": 2},
                {"id": "9", "category": "differential", "text": "询问有无口干眼干、脱发、光敏等提示其他结缔组织病的症状", "weight": 1},
                {"id": "10", "category": "labs", "text": "询问应做哪些实验室检查：RF、抗CCP抗体、ESR、CRP", "weight": 1}
            ],
            "total_items": 10,
            "total_weight": 12
        }),
        "key_questions": json.dumps([
            "晨僵持续多长时间？有没有用过什么方法能缓解？",
            "除了手和手腕，脚、膝盖或其他关节有没有类似症状？",
            "您在奥地利远足时出现的皮疹是什么样子的？持续了多久？",
            "您有没有口干、眼干或者脱发的情况？",
            "最近有没有感冒、发烧或其他感染的症状？"
        ]),
        "red_flags": json.dumps([
            "对称性多关节受累伴晨僵提示类风湿关节炎可能",
            "右足侧压时患者表现痛苦提示其他关节受累",
            "双侧腕关节伸展范围缩小可能造成永久性功能损伤",
            "需尽早干预以保护钢琴师的职业生涯"
        ]),
        "diagnosis": "类风湿关节炎（Rheumatoid Arthritis）",
        "is_active": 1
    },

    # ============================================================
    # Case 05: 急性缺血性脑卒中／TIA - 模块2/第六周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "短暂性脑缺血发作（TIA）／轻型急性缺血性脑卒中",
        "department": "神经内科",
        "difficulty": "beginner",
        "chief_complaint": "我刚才突然左手和左脚都动不了了，狗也掉地上了，我这是怎么了？",
        "patient_profile": json.dumps({
            "name": "马丽",
            "age": 41,
            "gender": "女",
            "occupation": "不详",
            "marital_status": "不详",
            "education": "不详"
        }),
        "symptoms_description": (
            "在超市停车场下车时突然感到无力，站立不稳需用右手抓车门把手才能保持平衡，无法控制左臂。"
            "旁观者拨打120。患者无急性创伤、无意识丧失、无阵挛性强直，意识清醒但说话有点困难。"
            "既往有高胆固醇、高血压、偶尔低血糖和心悸病史。2个月前被狗绊倒导致右额上肿块。"
            "服用口服避孕药（Loestrin），无过敏史。急救人员现场测量：P 96次/分，R 18次/分，BP 180/100mmHg，说话含混不清，血糖210mg/dL。"
            "急诊检查左侧轻偏瘫但无感觉缺失。头部CT正常。在准备注射rt-PA时患者左侧肢体功能自行迅速恢复。"
        ),
        "physical_exam": json.dumps({
            "general": "BP 180/100mmHg，P 88次/分，T 36.2°C",
            "head": "无急性创伤迹象，可疑红色面颊",
            "neck": "柔软，左颈部下颌角水平听诊闻及较大嗖嗖声（颈动脉杂音）",
            "heart": "心跳速度和节律正常，无杂音",
            "lungs": "无殊",
            "neurological": "双侧额纹对称，左鼻唇沟变浅。左上肢肌力3/5，左下肢肌力3/5。左侧感觉完好。左侧上下肢深部肌腱反射增强，左侧Babinski征阳性"
        }),
        "emotional_state": "anxious",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问发病确切时间：'最后正常时间'对溶栓决策至关重要", "weight": 2},
                {"id": "2", "category": "chief_complaint", "text": "询问神经功能缺损的具体表现：肢体无力、面部歪斜、言语障碍", "weight": 1},
                {"id": "3", "category": "associated_symptoms", "text": "询问有无复视、眩晕、平衡失调、头痛、意识改变", "weight": 1},
                {"id": "4", "category": "risk_factors", "text": "询问卒中危险因素：高血压、高胆固醇、糖尿病、心脏病、吸烟", "weight": 1},
                {"id": "5", "category": "pmh", "text": "询问近期外伤史（2个月前头部碰撞）及可能的TIA发作史", "weight": 1},
                {"id": "6", "category": "medications", "text": "询问口服避孕药使用史及抗凝/抗血小板药物使用", "weight": 1},
                {"id": "7", "category": "physical_exam", "text": "注意颈动脉听诊发现（杂音）的意义", "weight": 1},
                {"id": "8", "category": "differential", "text": "区分缺血性卒中与出血性卒中、TIA、低血糖、偏瘫型偏头痛", "weight": 2},
                {"id": "9", "category": "imaging", "text": "了解CT检查结果及溶栓治疗的适应症和禁忌症", "weight": 1},
                {"id": "10", "category": "red_flag", "text": "识别大面积脑梗死和溶栓后出血转化的风险", "weight": 2}
            ],
            "total_items": 10,
            "total_weight": 13
        }),
        "key_questions": json.dumps([
            "您能准确告诉我您是从什么时候开始感觉左手左脚无力的吗？",
            "您以前有没有过类似的发作？有没有高血压或者糖尿病？",
            "您平时吃什么药？有没有在吃避孕药？",
            "您有没有感觉到头晕、看东西重影或者走路不稳？",
            "您吸烟喝酒吗？家族里有没有人中风过？"
        ]),
        "red_flags": json.dumps([
            "症状在未溶栓时自行缓解提示可能为TIA，仍须紧急评估",
            "BP 180/100mmHg为溶栓的相对禁忌",
            "左颈动脉杂音提示可能存在大动脉狭窄",
            "血糖升高可能与应激有关，须排除糖尿病"
        ]),
        "diagnosis": "短暂性脑缺血发作（TIA）或轻型急性缺血性脑卒中",
        "is_active": 1
    },

    # ============================================================
    # Case 06: 结核性脑膜炎 (Tuberculous Meningitis) - 模块2/第四周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "结核性脑膜炎",
        "department": "神经内科",
        "difficulty": "advanced",
        "chief_complaint": "医生，我头痛一个多月了，越来越厉害，还老是恶心想吐，最近看东西也不清楚了。",
        "patient_profile": json.dumps({
            "name": "高先生",
            "age": 46,
            "gender": "男",
            "occupation": "外贸公司管理",
            "marital_status": "已婚",
            "education": "本科"
        }),
        "symptoms_description": (
            "一个多月前开始额头处阵阵胀痛，一直疲乏，体温37.5°C上下，以为是感冒。近一年收入下降不得不兼职，每天只睡4-5小时。"
            "一个月后头痛更频繁，几乎持续性头痛，常感恶心，有时呕吐。妻子带至中心医院急诊。"
            "既往平素健康，每年一次常规体检未发现特殊问题，无住院手术史，无过敏史。近期未服用任何药物。"
            "父亲患高血压，母亲患糖尿病，1个哥哥和1个妹妹健康。饮食健康，2个儿子1个女儿都健康，无特殊不良嗜好。"
            "第一次住院脑脊液检查后因经济原因坚决要求带药出院。半个月后因视力下降、头痛加重再次就诊，出现视物旋转、走路不稳。"
        ),
        "physical_exam": json.dumps({
            "general": "身高172cm，体重67.3kg。T 38.6°C/复诊38.8°C，BP 123-126/74-75mmHg",
            "lungs": "双肺呼吸音清，无干湿啰音",
            "heart": "心律齐，无病理性杂音",
            "abdomen": "腹平软，无压痛及反跳痛",
            "neurological_initial": "神清，双瞳等大等圆，对光反射灵敏，视乳头无水肿。颈项强直，克氏征阳性。四肢肌力5级，双侧指鼻试验阴性",
            "neurological_followup": "双侧视力听力下降，眼球外展受限，视乳头水肿、眼底静脉怒张、灰白色渗出及出血，闭目难立征阳性，双手指鼻欠稳准"
        }),
        "emotional_state": "anxious",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问头痛的具体特点：部位、性质、时间演变", "weight": 1},
                {"id": "2", "category": "associated_symptoms", "text": "询问有无发热、恶心呕吐、视力变化、复视", "weight": 1},
                {"id": "3", "category": "associated_symptoms", "text": "询问有无癫痫发作、意识改变、神经系统定位体征", "weight": 1},
                {"id": "4", "category": "pmh", "text": "询问既往感染史、结核接触史、免疫状态", "weight": 1},
                {"id": "5", "category": "physical_exam", "text": "了解脑膜刺激征（颈项强直、克氏征）的意义", "weight": 2},
                {"id": "6", "category": "labs", "text": "了解脑脊液检查结果：压力、细胞数、蛋白、糖、氯化物的变化规律", "weight": 2},
                {"id": "7", "category": "differential", "text": "区分化脓性、病毒性、结核性、隐球菌性脑膜炎的CSF特点", "weight": 2},
                {"id": "8", "category": "differential", "text": "考虑自身免疫性脑炎、肿瘤性脑膜炎的可能性", "weight": 1},
                {"id": "9", "category": "red_flag", "text": "评估颅内压升高程度及脑疝风险", "weight": 2},
                {"id": "10", "category": "management", "text": "讨论降颅压治疗方案及抗结核治疗的适应症", "weight": 1}
            ],
            "total_items": 10,
            "total_weight": 14
        }),
        "key_questions": json.dumps([
            "头痛从什么时候开始的？是持续性的还是阵发性的？",
            "您有没有发烧？最近有没有接触到结核病人？",
            "看东西有没有重影或者模糊？",
            "您有没有咳血、盗汗或者体重明显下降？",
            "最近有没有去过人多拥挤的地方或者接触过生病的动物？"
        ]),
        "red_flags": json.dumps([
            "脑脊液压力330-390mmH2O，提示严重颅高压",
            "视力下降和眼底改变提示视神经受压，可能导致永久性失明",
            "脑脊液糖低（1.4-1.9mmol/L）和蛋白高（620-840mg/L）高度提示结核性脑膜炎",
            "颈项强直和克氏征阳性提示脑膜受累"
        ]),
        "diagnosis": "结核性脑膜炎（Tuberculous Meningitis）",
        "is_active": 1
    },

    # ============================================================
    # Case 07: 运动员心动过缓 (Athlete's Bradycardia) - 模块3/第一周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "运动员心动过缓伴一度房室传导阻滞",
        "department": "心内科",
        "difficulty": "intermediate",
        "chief_complaint": "医生，我没什么不舒服的，是我妻子非要让我来。她说我的脉搏有时候只有二十几次，她担心不正常。",
        "patient_profile": json.dumps({
            "name": "鲁班",
            "age": 58,
            "gender": "男",
            "occupation": "玻璃工匠／业余马拉松运动员",
            "marital_status": "已婚",
            "education": "不详"
        }),
        "symptoms_description": (
            "极度活跃的业余马拉松运动员，每月至少跑一次马拉松或10公里。每天起床后做200个仰卧起坐、50个俯卧撑和50个引体向上，骑30分钟负荷运动自行车，平均每周跑48公里。"
            "周末专业潜水4-5小时。在妻子坚持下来就诊，脉搏可降至每分钟二十几次。"
            "否认心悸，但脉搏可低至28次/分（尤其坐着看电视时）。有时感觉困倦但非头晕眼花，只是有点累，摇几下头便会好一点。"
            "曾有踝关节严重骨折，钢针未取出时就恢复跑步，在最后一根钢针取出前已恢复全程马拉松训练。赢得所在年龄组每次马拉松比赛。"
            "否认气短或呼吸困难，否认胸痛。起跑时偶尔轻微头晕但继续跑后消失。"
            "偶尔用泰诺林和阿司匹林缓解肌肉疼痛。自幼父母在二战中去世无法提供家族史。"
        ),
        "physical_exam": json.dumps({
            "general": "体型偏瘦但肌肉发达，体重无明显下降",
            "vitals": "BP 130/60mmHg，P 40次/分，偶有不规则",
            "chest": "叩诊和听诊无殊",
            "heart": "心率缓慢，偶有舒张中期心音（低钝，最佳听诊在胸骨边缘，与呼吸节律无关）。轻度收缩中期杂音，胸骨左上缘最明显，不随呼吸改变，无舒张期杂音",
            "abdomen_other": "均无异常",
            "neurological": "无定位体征，肌力正常，脑神经无殊",
            "ecg": "心率45次/分，PR间期0.62秒（一度AVB），QRS电压有所增高"
        }),
        "emotional_state": "calm",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问心动过缓的最低心率和出现时机", "weight": 1},
                {"id": "2", "category": "chief_complaint", "text": "询问运动耐量：日常锻炼强度、有无气短胸痛", "weight": 1},
                {"id": "3", "category": "associated_symptoms", "text": "询问有无头晕、晕厥、疲劳等心动过缓相关症状", "weight": 1},
                {"id": "4", "category": "pmh", "text": "了解既往踝关节手术史和用药史", "weight": 1},
                {"id": "5", "category": "physical_exam", "text": "了解心脏听诊结果：额外心音和杂音的意义", "weight": 1},
                {"id": "6", "category": "ecg", "text": "了解心电图：PR间期0.62秒（一度AVB）和QRS电压增高的意义", "weight": 1},
                {"id": "7", "category": "exercise_test", "text": "询问运动时心率能否相应增加（运动负荷试验）", "weight": 1},
                {"id": "8", "category": "differential", "text": "区分生理性运动员心脏和病理性心动过缓（病窦综合征、高度房室传导阻滞）", "weight": 2},
                {"id": "9", "category": "imaging", "text": "询问是否需要Holter监测和超声心动图检查", "weight": 1}
            ],
            "total_items": 9,
            "total_weight": 10
        }),
        "key_questions": json.dumps([
            "您心率最低的时候有多少次？当时在做什么？",
            "您有没有过眼前发黑、晕倒或者严重头晕的情况？",
            "跑步时心率能升到多少？运动起来会不会觉得喘不过气？",
            "您平时吃什么药吗？有没有用过任何补充剂？",
            "有没有感到心跳突然跳一下或者不规则？"
        ]),
        "red_flags": json.dumps([
            "心率低于30次/分需排除病理性心动过缓",
            "偶有不规则心律需Holter监测排除恶性心律失常",
            "舒张中期心音和收缩期杂音需超声明确结构异常",
            "运动中头晕需评估心输出量储备"
        ]),
        "diagnosis": "运动员心动过缓伴一度房室传导阻滞（Athlete's Bradycardia with First-Degree AV Block）",
        "is_active": 1
    },

    # ============================================================
    # Case 08: COPD急性加重合并心衰 - 模块3/第七周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "慢性阻塞性肺疾病急性加重合并急性左心衰竭",
        "department": "呼吸内科",
        "difficulty": "intermediate",
        "chief_complaint": "医生，我喘不上气来！今天早上起来去洗手间就突然喘得不行，还咳出了粉红色的泡沫。",
        "patient_profile": json.dumps({
            "name": "JH",
            "age": 74,
            "gender": "女",
            "occupation": "退休芭蕾舞教师（原舞蹈演员）",
            "marital_status": "已婚",
            "education": "不详"
        }),
        "symptoms_description": (
            "进行性劳力性呼吸困难12年。最初仅在剧烈运动时出现，之后爬楼梯或上坡也会有，最近2年走不到一个街区就必须停下来喘口气。"
            "近3年因'肺炎'和严重气急入院2次，接受了抗生素和糖皮质激素治疗。"
            "入院当天早晨醒后去洗手间时突发气急，咳出粉红色泡沫样物。丈夫拨打120。"
            "无胸痛、胸闷、发热。长期吸烟约40包年，2年前戒烟。曾接受沙丁胺醇、吸入型皮质类固醇激素和异丙托溴铵治疗。"
            "有间歇性心脏杂音病史，一位医生告诫牙科手术前需服用抗生素。姐姐也有心脏杂音，68岁死于乳腺癌。"
            "很少饮酒，与丈夫一同生活，无子女。从事芭蕾舞教学30年后因呼吸不适离职。"
        ),
        "physical_exam": json.dumps({
            "general": "消瘦，急性面容，呼吸急促，神情惊恐（急性呼吸窘迫）",
            "vitals": "BP 110/80mmHg，P 106次/分律齐，R 28次/分",
            "jvp": "颈静脉压7cmH2O，颈动脉搏动正常但幅度下降",
            "lungs": "两下肺可闻及湿啰音，双肺满布低调呼气期哮鸣音",
            "heart": "锁骨中线第六肋间隙可触及强有力持久心脏搏动。S1柔和，S2生理性分裂，A2=P2。心前区全收缩期杂音，左室搏动处最明显，向腋下传导。心尖区闻及响亮S4和低钝S3",
            "abdomen": "腹部检查无异常",
            "extremities": "无紫绀，四肢无水肿，无杵状指（趾）",
            "abg": "PaO2 56mmHg，PaCO2 52mmHg"
        }),
        "emotional_state": "anxious",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问呼吸困难的具体特点：起病时间、诱因、严重程度", "weight": 1},
                {"id": "2", "category": "chief_complaint", "text": "重点询问咳粉红色泡沫痰（急性肺水肿的典型表现）", "weight": 2},
                {"id": "3", "category": "history", "text": "询问慢性呼吸困难的演变过程：12年进展速度和加重因素", "weight": 1},
                {"id": "4", "category": "pmh", "text": "询问既往急性加重次数和治疗情况", "weight": 1},
                {"id": "5", "category": "risk_factors", "text": "详细询问吸烟史（40包年）和用药史（沙丁胺醇、ICS、异丙托溴铵）", "weight": 1},
                {"id": "6", "category": "pmh", "text": "询问心脏杂音史及牙科术前用抗生素的意义", "weight": 1},
                {"id": "7", "category": "physical_exam", "text": "了解肺部听诊（湿啰音+哮鸣音）和心脏听诊（S3、S4、杂音）的临床意义", "weight": 2},
                {"id": "8", "category": "labs", "text": "了解动脉血气（PaO2 56，PaCO2 52）和胸片结果", "weight": 1},
                {"id": "9", "category": "differential", "text": "区分COPD急性加重与心源性肺水肿", "weight": 2},
                {"id": "10", "category": "red_flag", "text": "评估呼吸衰竭程度及是否需要气管插管机械通气", "weight": 2}
            ],
            "total_items": 10,
            "total_weight": 14
        }),
        "key_questions": json.dumps([
            "这次喘不上气是从什么时候开始的？和以前发作比有什么不一样？",
            "您咳出的粉红色泡沫多吗？有没有胸痛？",
            "您抽烟多少年了？什么时候戒的？",
            "您平常用什么药控制呼吸？最近有没有按时用？",
            "您有没有心脏病？以前医生有没有说过您的心脏有什么问题？"
        ]),
        "red_flags": json.dumps([
            "咳粉红色泡沫痰提示急性肺水肿",
            "R 28次/分且PaO2仅56mmHg提示呼吸衰竭",
            "S3奔马律和S4同时出现提示严重心室功能不全",
            "患者疲倦且血气恶化提示需气管插管机械通气"
        ]),
        "diagnosis": "慢性阻塞性肺疾病急性加重合并急性左心衰竭（AECOPD with Acute Left Heart Failure）",
        "is_active": 1
    },

    # ============================================================
    # Case 09: 急性下壁心肌梗死 - 模块3/第三周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "急性下壁ST段抬高型心肌梗死",
        "department": "心内科",
        "difficulty": "intermediate",
        "chief_complaint": "医生，我胸口压得难受，像有块大石头压着，一顿暴食之后开始的，还有点恶心，喘气也费劲。",
        "patient_profile": json.dumps({
            "name": "不详",
            "age": 55,
            "gender": "男",
            "occupation": "个体演员",
            "marital_status": "已婚",
            "education": "不详"
        }),
        "symptoms_description": (
            "自诉胸部有重压感约6小时，一顿暴食后开始出现，并有点恶心和深呼吸困难。妻子'强行'带至医院急诊，因为胸痛越来越严重。"
            "12岁开始吸烟，每天2包，此次胸部不适正是在抽了2支烟后发生的。"
            "已有二十多年没看过病，对血压及血脂情况都不了解。独生子，没有孩子。"
            "无重大疾病史，从未住过院，无手术史。很少饮酒，无吸毒史。"
            "急诊给予硝酸甘油后胸痛缓解，但BP从125/72降至88/50mmHg，P从74降至52bpm，出现头晕。"
            "快速滴注500ml生理盐水后BP回升至100-105/72，P仍为60bpm。"
            "心电图示II/III/AVF导联ST段明显抬高。冠脉造影显示右冠状动脉完全阻塞，行支架植入术。"
            "术后心尖区闻及全收缩期杂音并向腋下传导。"
        ),
        "physical_exam": json.dumps({
            "general": "除硝酸甘油导致的低血压和第四心音外体检一切正常",
            "heart": "闻及第四心音（S4），无心脏杂音（术后出现全收缩期杂音）",
            "vascular": "外周血管和颈动脉无异常搏动，腹主动脉听诊无异常",
            "ecg": "第II、III、AVF导联ST段明显抬高",
            "angio": "右冠状动脉锐缘处完全阻塞，左前降支无异常，回旋支较小",
            "swan_ganz": "CO 4.8L/min，RAP 14mmHg，PAP 38/22mmHg，PAWP 19mmHg"
        }),
        "emotional_state": "anxious",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问胸痛部位、性质（重压感）、持续时间和诱发因素", "weight": 1},
                {"id": "2", "category": "associated_symptoms", "text": "询问有无大汗、恶心呕吐、呼吸困难", "weight": 1},
                {"id": "3", "category": "risk_factors", "text": "详细询问吸烟史（12岁开始，每天2包，约40余年）", "weight": 2},
                {"id": "4", "category": "pmh", "text": "询问既往心血管病史、心绞痛发作史", "weight": 1},
                {"id": "5", "category": "pmh", "text": "询问高血压、高脂血症、糖尿病史", "weight": 1},
                {"id": "6", "category": "family_history", "text": "询问心血管疾病家族史（父亲44岁意外去世）", "weight": 1},
                {"id": "7", "category": "ecg", "text": "了解心电图的定位诊断：II/III/AVF导联ST段抬高=下壁心梗", "weight": 2},
                {"id": "8", "category": "management", "text": "讨论急性心梗的治疗方案：抗血小板、PCI、β受体阻滞剂使用时机", "weight": 1},
                {"id": "9", "category": "red_flag", "text": "认识硝酸甘油导致低血压和心动过缓的意义（右室梗死可能）", "weight": 2},
                {"id": "10", "category": "complication", "text": "评估术后全收缩期杂音的原因（乳头肌功能不全/二尖瓣反流）", "weight": 2}
            ],
            "total_items": 10,
            "total_weight": 14
        }),
        "key_questions": json.dumps([
            "胸痛是从什么时候开始疼的？是什么样的感觉？",
            "有没有出冷汗、恶心、呕吐或者呼吸困难？",
            "您从多大开始抽烟？每天抽多少？",
            "您以前有没有过类似的胸痛？有没有高血压、糖尿病？",
            "家里有没有人得过心脏病或者突然去世的？"
        ]),
        "red_flags": json.dumps([
            "II/III/AVF导联ST段明显抬高提示急性下壁心梗",
            "硝酸甘油导致明显低血压和心动过缓需警惕右室梗死",
            "LVEF仅45%且下后壁运动丧失",
            "术后全收缩期杂音伴向腋下传导需警惕乳头肌功能不全"
        ]),
        "diagnosis": "急性下壁ST段抬高型心肌梗死（Inferior STEMI），右冠状动脉闭塞",
        "is_active": 1
    },

    # ============================================================
    # Case 10: 血管迷走性晕厥 (Vasovagal Syncope) - 模块3/第二周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "血管迷走性晕厥",
        "department": "心内科",
        "difficulty": "intermediate",
        "chief_complaint": "医生，我已经晕倒两次了！都是在指挥乐队的时候，突然感觉人不行了，然后就倒了。我还能继续做指挥吗？",
        "patient_profile": json.dumps({
            "name": "Z先生",
            "age": 35,
            "gender": "男",
            "occupation": "杭州爱乐乐团首席指挥",
            "marital_status": "不详",
            "education": "不详（高薪海外招聘）"
        }),
        "symptoms_description": (
            "才华横溢的交响乐团首席指挥。因晕厥两次被送到急诊室。每次都在激情指挥乐队时发作。"
            "第一次在两周前排练时，未去看医生。第二次在演出时发作，演出被迫停止。"
            "近来感觉良好，每隔一天慢跑5公里已坚持1年多。最近没有发烧、咳嗽或腹泻。"
            "两次晕厥前都感到温热、汗涔涔和恶心，能预感到'人不行了快要晃倒'，但能在失去意识前弯曲膝盖。"
            "倒下时未碰到头部，无肢体抽搐，无大小便失禁。几乎在倒下的同时清醒，知道发生了什么。"
            "否认晕厥时有胸痛或心悸。有轻度高血压一年，服用利尿剂。家庭中无晕厥或猝死者。"
            "以往未发现心脏病、癫痫发作或头部外伤史。"
        ),
        "physical_exam": json.dumps({
            "general": "神志清晰，定向力正常",
            "vitals": "坐位和立位BP均为110/70mmHg，坐位HR 55次/分立位增至65次/分",
            "jvp": "颈静脉压4cmH2O，无颈静脉充盈或怒张",
            "lungs": "叩诊和听诊无殊",
            "heart": "心尖搏动无移位。S1正常，S2生理性分裂，A2高于P2。无杂音或奔马律",
            "neuro": "神经系统体格检查均正常",
            "ecg": "正常窦性心律，HR 55次/分，PR间期0.24秒，不完全性右束支传导阻滞",
            "labs": "Hb 13g/dL，血清肌酐1.2mg/dL均正常"
        }),
        "emotional_state": "anxious",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问晕厥的触发因素（激情指挥）和前驱症状（温热、出汗、恶心）", "weight": 2},
                {"id": "2", "category": "chief_complaint", "text": "询问有无抽搐、大小便失禁、舌咬伤等提示癫痫的特征", "weight": 1},
                {"id": "3", "category": "associated_symptoms", "text": "询问晕厥前后的胸痛、心悸、呼吸困难", "weight": 1},
                {"id": "4", "category": "pmh", "text": "询问高血压史、用药史（利尿剂）及心脏病或癫痫病史", "weight": 1},
                {"id": "5", "category": "family_history", "text": "询问家族中晕厥、猝死、心律失常病史", "weight": 2},
                {"id": "6", "category": "physical_exam", "text": "了解直立位血压和心率变化（排除体位性低血压）", "weight": 1},
                {"id": "7", "category": "ecg", "text": "了解PR间期延长（0.24秒）和不完全性RBBB的意义", "weight": 1},
                {"id": "8", "category": "differential", "text": "区分心源性晕厥（心律失常、流出道梗阻）与神经介导性晕厥（血管迷走性）", "weight": 2},
                {"id": "9", "category": "red_flag", "text": "评估晕厥的恶性程度及对驾驶和职业的影响", "weight": 1},
                {"id": "10", "category": "management", "text": "讨论住院观察vs门诊随访及高血压治疗调整", "weight": 1}
            ],
            "total_items": 10,
            "total_weight": 13
        }),
        "key_questions": json.dumps([
            "这两次晕倒前您有什么感觉？有没有觉得热、出汗或者恶心？",
            "晕倒后多久能醒过来？有没有大小便失禁或者咬到舌头？",
            "您家里有没有人突然去世或者在年轻时晕倒过的？",
            "您平时在吃什么药？晕倒跟吃药时间有没有关系？",
            "除了指挥的时候，在其他情况下有没有头晕过？"
        ]),
        "red_flags": json.dumps([
            "运动中（激情指挥）发生的晕厥须警惕心源性可能",
            "PR间期0.24秒（一度AVB）和不完全性RBBB提示可能存在传导系统疾病",
            "晕厥在未改变治疗方案时可能再次发作",
            "须评估是否安全驾驶和继续从事指挥工作"
        ]),
        "diagnosis": "血管迷走性晕厥（Vasovagal Syncope），排除心源性晕厥",
        "is_active": 1
    },

    # ============================================================
    # Case 11: 慢性阻塞性肺疾病 (COPD) - 模块3/第五周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "慢性阻塞性肺疾病（慢性支气管炎型）",
        "department": "呼吸内科",
        "difficulty": "beginner",
        "chief_complaint": "医生，我最近觉得自己呼吸困难，做任何体力活都会喘。我妻子催我来看病已经很久了，她说我呼吸有杂音。",
        "patient_profile": json.dumps({
            "name": "Robert Adams",
            "age": 50,
            "gender": "男",
            "occupation": "纺织工厂领班（前造船厂焊接工）",
            "marital_status": "已婚",
            "education": "高中"
        }),
        "symptoms_description": (
            "因气急就诊，在妻子催促下才来看病。妻子说他的呼吸状况比去年糟糕多了，早上散步中途都必须停下来喘口气。"
            "任何体力活动都会导致呼吸短促，安静时好点。每年冬天咳嗽很严重，感冒持续整个冬天，早上咳嗽最严重，大部分干咳偶尔咳出淡灰色痰液。"
            "去年冬天有一天早上咳嗽太严重甚至不能呼吸，不得不去急诊室，吸入药物治疗后好转回家。"
            "否认儿童时期呼吸感染或缺课情况，自称小时候很健康。无哮喘、枯草热、过敏或湿疹。"
            "从高中开始吸烟已30-35年，一天两包持续约30年。去年尝试戒烟只戒了3天。"
            "曾当造船厂焊接工20-25年，一直住在洛杉矶圣加百利谷（空气污染严重地区）25年。"
        ),
        "physical_exam": json.dumps({
            "general": "身高178cm，体重77kg",
            "vitals": "BP 138/88mmHg，P 92次/分，R 26次/分，体温正常",
            "oropharynx": "咽后壁有红斑",
            "respiratory": "呼吸费力并用辅助呼吸肌。胸部听诊整个肺野都能闻及哮鸣音，呼气相延长，胸部叩诊呈过清音",
            "heart": "心音遥远，无心脏杂音，无心脏扩大迹象",
            "other": "无外周水肿，无颈静脉扩张。心电图正常。PEF 250L/min。吸入支气管扩张剂后症状好转"
        }),
        "emotional_state": "calm",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问呼吸困难与活动的关系和进行性加重特点", "weight": 1},
                {"id": "2", "category": "chief_complaint", "text": "询问咳嗽咳痰：发作季节、痰的颜色和量", "weight": 1},
                {"id": "3", "category": "history", "text": "询问急性加重次数、诱因和治疗经过", "weight": 1},
                {"id": "4", "category": "risk_factors", "text": "详细询问吸烟史（30-35年，每天2包，约60包年）和戒烟尝试", "weight": 2},
                {"id": "5", "category": "social_history", "text": "询问职业暴露（造船厂焊接工20-25年）和环境暴露（空气污染）", "weight": 2},
                {"id": "6", "category": "pmh", "text": "询问儿童期呼吸系统疾病史和过敏史", "weight": 1},
                {"id": "7", "category": "physical_exam", "text": "了解肺部检查：哮鸣音、呼气相延长、过清音、辅助呼吸肌使用", "weight": 1},
                {"id": "8", "category": "labs", "text": "了解肺功能检查（PEF 250L/min）和支气管舒张试验结果", "weight": 1},
                {"id": "9", "category": "differential", "text": "区分COPD与哮喘：发病年龄、吸烟史、可逆性、痰液特点", "weight": 1},
                {"id": "10", "category": "management", "text": "讨论戒烟计划和支气管扩张剂使用", "weight": 1}
            ],
            "total_items": 10,
            "total_weight": 12
        }),
        "key_questions": json.dumps([
            "您从多大年龄开始吸烟？一天吸多少支？有没有尝试戒过烟？",
            "您呼吸困难是什么时候开始的？做什么事情会喘？",
            "您以前做什么工作？在造船厂工作了多少年？",
            "您咳嗽主要在什么时间？有没有痰？痰是什么颜色的？",
            "家里有没有人也有呼吸方面的毛病？"
        ]),
        "red_flags": json.dumps([
            "R 26次/分且使用辅助呼吸肌提示呼吸困难严重",
            "60包年吸烟史是COPD的极高风险因素",
            "焊接工职业暴露增加了慢性肺病风险",
            "须排除肺癌（长期吸烟史+新发呼吸道症状）"
        ]),
        "diagnosis": "慢性阻塞性肺疾病（COPD，慢性支气管炎型）",
        "is_active": 1
    },

    # ============================================================
    # Case 12: 外伤后中枢性尿崩症 - 模块3/第八周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "外伤后中枢性尿崩症",
        "department": "内分泌科",
        "difficulty": "advanced",
        "chief_complaint": "医生，我口渴得要命，不停地喝水，小便也多得吓人，一天要排7-9升尿。我这是怎么了？",
        "patient_profile": json.dumps({
            "name": "H先生",
            "age": 23,
            "gender": "男",
            "occupation": "不详",
            "marital_status": "不详",
            "education": "不详"
        }),
        "symptoms_description": (
            "因车祸转入ICU。开SUV行驶在山路上未系安全带，转弯太快导致车翻。"
            "左股骨骨折和颅底骨折（颞骨岩部骨折），但脑神经未受影响。行股骨钢针固定术。"
            "术后神志清醒定向无障碍。连日来每日静脉输注6-8升液体，但每日尿量7-9升，尿量每天超过输液量1-2升。床边水杯每天被多次加满。"
            "出事前健康状况良好，已3年未去医院。最近一次看病是上呼吸道感染用抗生素痊愈。"
            "无骨折史，无头部创伤史。此前只在压力大时偶有头痛。本次住院前从未感到如此严重口渴和大量排尿。"
            "无用药史。不吸烟，每周几次晚餐时饮葡萄酒。"
            "家族中无糖尿病或水摄入异常患者：父亲57岁患高血压需药物控制，母亲55岁曾行良性乳腺肿块摘除术。"
        ),
        "physical_exam": json.dumps({
            "general": "R 16次/分，P 82次/分律齐，BP 100/68mmHg",
            "heent": "眼球各向运动正常，瞳孔等大等圆对光反应正常。视力视野正常。口腔正常但唇部稍干",
            "chest": "因无法坐起检查受限，心音正常呼吸正常",
            "abdomen": "肠鸣音闻及，无触痛，无肿块",
            "extremities": "左腿石膏固定外其余未见异常",
            "neurological": "右腿反射正常，感觉正常，定向无障碍神志清晰",
            "labs": "血钠144mEq/L，血浆渗透压293mOsm/kg，尿渗透压90mOsm/kg（极低），BUN 5mg/dL（低）"
        }),
        "emotional_state": "calm",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问每日尿量（7-9L）、口渴程度和饮水量", "weight": 2},
                {"id": "2", "category": "history", "text": "了解外伤史：车祸类型、骨折部位（股骨+颞骨岩部）、有无头部外伤", "weight": 2},
                {"id": "3", "category": "history", "text": "询问外伤前后饮水排尿量的对比变化", "weight": 1},
                {"id": "4", "category": "pmh", "text": "了解外伤前健康状态和有无多饮多尿史", "weight": 1},
                {"id": "5", "category": "family_history", "text": "询问家族中有无糖尿病、尿崩症或内分泌疾病", "weight": 1},
                {"id": "6", "category": "labs", "text": "了解血钠（144）、血浆渗透压（293）和尿渗透压（90）的临床意义", "weight": 2},
                {"id": "7", "category": "differential", "text": "区分中枢性尿崩症与肾性尿崩症、原发性烦渴、糖尿病", "weight": 2},
                {"id": "8", "category": "pathophysiology", "text": "解释颅底骨折与ADH分泌不足之间的关系", "weight": 1},
                {"id": "9", "category": "management", "text": "讨论禁水试验的设计和去氨加压素治疗的适应症", "weight": 1},
                {"id": "10", "category": "red_flag", "text": "评估高钠血症和容量不足的风险", "weight": 1}
            ],
            "total_items": 10,
            "total_weight": 14
        }),
        "key_questions": json.dumps([
            "您什么时候开始觉得这么口渴？一天大概喝多少水？",
            "每天小便多少次？每次量多吗？是不是很清亮？",
            "您是车祸前就有这种情况，还是车祸后才出现的？",
            "车祸时有没有撞到头？有没有失去过意识？",
            "您以前有没有得过肾脏病或者糖尿病？"
        ]),
        "red_flags": json.dumps([
            "每日尿量7-9升远超正常范围（<2.5L/天）",
            "尿渗透压90mOsm/kg极低，提示肾脏浓缩功能严重障碍",
            "血钠144mEq/L处于高限，持续多尿可能导致严重高钠血症",
            "颅底骨折（颞骨岩部）是中枢性尿崩症的明确危险因素"
        ]),
        "diagnosis": "外伤后中枢性尿崩症（Post-Traumatic Central Diabetes Insipidus）",
        "is_active": 1
    },

    # ============================================================
    # Case 13: 肺结节性质待查 - 模块3/第六周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "肺结节性质待查（鉴别肺癌）",
        "department": "心胸外科",
        "difficulty": "advanced",
        "chief_complaint": "医生，我胸口疼了十几天了，社区医院的CT查出来右肺有一个小结节，我很担心是不是癌症，想请您帮我看看。",
        "patient_profile": json.dumps({
            "name": "M女士",
            "age": 58,
            "gender": "女",
            "occupation": "会计（退休）",
            "marital_status": "已婚",
            "education": "不详"
        }),
        "symptoms_description": (
            "2周前右前胸部出现持续性疼痛强度1级（最高10级），之后疼痛变得轻微但仍持续。"
            "8天前社区医院X线胸片阴性，CT血管造影无肺栓塞但发现右上肺叶1cm小结节。9个月前X线胸片阴性。"
            "6个多月来体重减轻4.5kg（患者认为与停止吃肉有关）。3周前曾有寒战，干咳一段时间。无呼吸短促、盗汗或咯血。有失眠。"
            "过敏史：青霉素和红霉素导致荨麻疹和喉头水肿气道梗阻（血管性水肿）。"
            "既往：30年前上呼吸道感染后胸膜炎。三次肺炎/支气管炎。高胆固醇血症。胆囊切除、阑尾切除、扁桃体切除。alpha-1抗胰蛋白酶缺乏症肯定携带者。"
            "家族史：父亲二战期间得过结核病，皮肤鳞状细胞癌转移至喉和肺。母亲健在83岁有2型糖尿病。儿子患有alpha-1抗胰蛋白酶缺乏症。"
            "吸烟量60包年（18-58岁每天1包半），一周前刚戒烟。每周打4次网球。"
        ),
        "physical_exam": json.dumps({
            "general": "T 36.5°C，BP 118/80mmHg，P 77次/分，R 17次/分，体重57.6kg，SpO2 98%",
            "heent": "结膜无充血，瞳孔正常。口咽无殊。气管居中，无甲状腺肿",
            "respiratory": "未使用辅助肌，听诊呼吸音清，无哮鸣音或啰音",
            "cardiovascular": "S1/S2正常，无杂音，无水肿",
            "abdomen": "腹部柔软无压痛，无明显肝脾肿大",
            "lymph": "无颈部、腋下或锁骨上淋巴结肿大",
            "skin": "无包块、无皮疹",
            "msk": "步态正常，无杵状指"
        }),
        "emotional_state": "anxious",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问胸痛特点：部位、性质、与呼吸的关系", "weight": 1},
                {"id": "2", "category": "associated_symptoms", "text": "询问干咳、寒战和体重减轻（4.5kg/6个月）", "weight": 2},
                {"id": "3", "category": "imaging", "text": "了解肺结节的特征：大小1cm、部位右上肺叶、发现过程", "weight": 1},
                {"id": "4", "category": "risk_factors", "text": "详细评估吸烟史（60包年）和肺癌风险", "weight": 2},
                {"id": "5", "category": "pmh", "text": "了解alpha-1抗胰蛋白酶缺乏症携带状态的意义", "weight": 1},
                {"id": "6", "category": "pmh", "text": "询问反复肺炎/支气管炎史和胸膜炎史", "weight": 1},
                {"id": "7", "category": "family_history", "text": "询问父亲结核病史和皮肤鳞状细胞癌转移史", "weight": 1},
                {"id": "8", "category": "differential", "text": "区分肺结节的可能病因：恶性（肺癌、转移癌）vs良性（感染性肉芽肿、错构瘤）", "weight": 2},
                {"id": "9", "category": "allergy", "text": "记录严重药物过敏史（青霉素和红霉素导致血管性水肿）", "weight": 1},
                {"id": "10", "category": "management", "text": "讨论肺结节的处理策略：随访CT vs PET-CT vs活检 vs手术", "weight": 1}
            ],
            "total_items": 10,
            "total_weight": 13
        }),
        "key_questions": json.dumps([
            "您抽烟有多少年了？每天抽多少支？什么时候戒的？",
            "这6个月体重减了多少？是刻意减肥还是不知不觉瘦下来的？",
            "您有没有咳血、夜里出汗或者发烧？",
            "您家人有没有得过肺癌、结核病或者其他癌症？",
            "您以前有没有做过胸部CT？这个结节是新出现的还是一直在的？"
        ]),
        "red_flags": json.dumps([
            "60包年吸烟史是肺癌的极高风险因素",
            "6个月体重减轻4.5kg须警惕恶性肿瘤",
            "alpha-1抗胰蛋白酶缺乏症增加了COPD和肺癌风险",
            "1cm肺结节在重度吸烟者中须高度怀疑恶性可能",
            "药物过敏史（青霉素和红霉素导致血管性水肿）影响后续治疗选择"
        ]),
        "diagnosis": "右上肺结节性质待查（Lung Nodule, Rule Out Malignancy）",
        "is_active": 1
    },

    # ============================================================
    # Case 14: 缺铁性贫血 (Iron Deficiency Anemia) - 模块3/第四周
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "缺铁性贫血（消化道隐性出血可能）",
        "department": "消化内科",
        "difficulty": "beginner",
        "chief_complaint": "医生，我最近几个月人特别容易疲劳，爬一两层楼梯就喘不上气，孩子们也说我脸色不好看。",
        "patient_profile": json.dumps({
            "name": "S先生",
            "age": 55,
            "gender": "男",
            "occupation": "银行信贷员",
            "marital_status": "不详",
            "education": "不详"
        }),
        "symptoms_description": (
            "主诉'疲劳'。没有心脏、肺或肾病病史，未曾有心绞痛或其他胸痛。不吸烟不饮酒。"
            "没有发烧、畏寒或出汗。胃口很好但近6个月体重减轻6.8kg。有时感到恶心但无呕吐、腹痛或腹泻。"
            "有时大便颜色较黑但未见便血。近几年有慢性消化不良，有胃酸过多症状，规律服用铝碳酸镁片或硫糖铝片。"
            "既往：孩童时阑尾切除手术，三十多岁时得过一次肺炎。"
            "住杭州，在银行做了25年信贷员。家里没养过宠物，最近没去任何地方旅行。无服用药物史和过敏史。"
        ),
        "physical_exam": json.dumps({
            "general": "T 36.8°C，BP 130/74mmHg，P 98次/min（临界性心动过速），R 24次/min，SpO2 97%",
            "skin": "无皮疹",
            "heent": "眼结膜苍白，无黄疸",
            "lungs": "呼吸音清",
            "heart": "律齐，II度收缩期杂音，无奔马律",
            "abdomen": "柔软，无压痛，无肿块或脏器肿大",
            "extremities": "无水肿",
            "labs": "Hb 64g/L（重度贫血），HCT 23.4%，MCV 68fL（小细胞性），MCH 18.6pg，MCHC 273g/L，网织红细胞0.5%。血清铁低，TIBC高，铁蛋白低。血红蛋白A2正常"
        }),
        "emotional_state": "calm",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问疲劳的表现：持续时间、对日常活动的影响", "weight": 1},
                {"id": "2", "category": "associated_symptoms", "text": "询问呼吸困难（爬楼气喘）和体重减轻（6.8kg/6个月）", "weight": 1},
                {"id": "3", "category": "associated_symptoms", "text": "重点询问消化系统症状：大便颜色变黑、消化不良、胃酸过多", "weight": 2},
                {"id": "4", "category": "pmh", "text": "询问慢性消化不良和服用抗酸药的历史", "weight": 1},
                {"id": "5", "category": "labs", "text": "解读Hb 64g/L（重度贫血）、MCV 68（小细胞性）、MCH 18.6（低色素性）的临床意义", "weight": 2},
                {"id": "6", "category": "labs", "text": "了解铁代谢指标：血清铁低+TIBC高+铁蛋白低=缺铁性贫血", "weight": 1},
                {"id": "7", "category": "differential", "text": "区分缺铁性贫血与其他小细胞性贫血：地中海贫血（HbA2正常）、慢性病贫血", "weight": 2},
                {"id": "8", "category": "etiology", "text": "寻找缺铁原因：消化道隐性出血（黑便+消化不良史）", "weight": 2},
                {"id": "9", "category": "red_flag", "text": "评估严重贫血（Hb 64g/L）的心血管风险", "weight": 1},
                {"id": "10", "category": "management", "text": "讨论是否需要胃镜和结肠镜检查排除消化道肿瘤", "weight": 1}
            ],
            "total_items": 10,
            "total_weight": 14
        }),
        "key_questions": json.dumps([
            "您疲劳的情况有多久了？有没有觉得爬楼梯或活动后喘不上气？",
            "您这6个月体重下降了将近7公斤，是没胃口还是自己减的？",
            "您大便颜色怎么样？有没有变黑或者看到血？",
            "您有没有胃痛、胃胀或者吃不下饭？",
            "您平时吃什么药吗？有没有在吃阿司匹林或者其他止痛药？"
        ]),
        "red_flags": json.dumps([
            "Hb 64g/L为重度贫血，须紧急评估",
            "6个月内体重减轻6.8kg须警惕消化道恶性肿瘤",
            "大便颜色变黑提示上消化道出血可能",
            "MCV仅68提示显著小细胞性贫血，缺铁为最常见原因",
            "P 98次/分和临界性心动过速反映贫血对心血管的影响"
        ]),
        "diagnosis": "缺铁性贫血（Iron Deficiency Anemia），疑消化道隐性出血",
        "is_active": 1
    },

    # ============================================================
    # Case 15: 乳糜泻 (Celiac Disease) - 模块4/week1-2
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "乳糜泻（麸质敏感性肠病）",
        "department": "消化内科",
        "difficulty": "advanced",
        "chief_complaint": "医生，我拉肚子好几年了，最近半年每天要拉7到15次，人都瘦了13公斤，脱水得不行。",
        "patient_profile": json.dumps({
            "name": "诸葛谨",
            "age": 67,
            "gender": "男",
            "occupation": "不详",
            "marital_status": "不详",
            "education": "不详"
        }),
        "symptoms_description": (
            "因腹泻、脱水和体重减轻入院。数年间歇性腹泻史，每次持续1-2天自行缓解。外院检查提示乳糖不耐受。"
            "入院7个月前胃镜检查显示消化性溃疡，服用奥美拉唑后缓解。上消化道检查显示胃窦和幽门疤痕伴胃扩张。有维生素B缺乏症。"
            "结肠镜检查发现局灶性直肠炎。入院前6个月腹泻次数增多每天7-15次。"
            "入院前30天曾因脱水在外院住院，合并代谢性酸中毒。小肠造影显示一过性小肠节段性扩张符合不完全性肠梗阻。服用头孢氨苄后腹泻改善但出院15天后复发，粪便呈白色燕麦样便。"
            "入院前4天因脱水和代谢酸中毒再次住院。粪便镜检少量白细胞，无脂肪虫卵或寄生虫。维生素B水平仍偏低。"
            "平素消瘦，6个月内体重减轻13kg。"
        ),
        "physical_exam": json.dumps({
            "general": "身高178cm，体重61kg（恶液质表现），伴焦虑",
            "vitals": "T 37°C，P 84次/分，R 20次/分，BP 100/60mmHg",
            "lungs": "两肺呼吸音清",
            "heart": "心律齐，未闻及病理性杂音",
            "abdomen": "腹平软无压痛无腹胀，无肝脾肿大，未及包块，肠鸣音无明显亢进",
            "extremities": "双下肢凹陷性水肿",
            "neuro": "无殊",
            "labs": "木糖吸收试验5小时尿排出仅0.3g（正常>23%），血清木糖3.0mg/dL"
        }),
        "emotional_state": "anxious",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问腹泻的具体特点：次数（7-15次/天）、性状（白色燕麦样）、与进食的关系", "weight": 2},
                {"id": "2", "category": "associated_symptoms", "text": "询问伴随症状：体重减轻（13kg/6个月）、脱水、腹痛、腹胀", "weight": 2},
                {"id": "3", "category": "associated_symptoms", "text": "询问营养缺乏表现：维生素B缺乏、双下肢水肿（低蛋白血症）", "weight": 1},
                {"id": "4", "category": "pmh", "text": "了解既往消化系统疾病：消化性溃疡、乳糖不耐受、直肠炎", "weight": 1},
                {"id": "5", "category": "pmh", "text": "询问既往住院史：脱水、代谢性酸中毒的发生过程", "weight": 1},
                {"id": "6", "category": "labs", "text": "了解木糖吸收试验极低（0.3g/5h）的意义——小肠吸收功能障碍", "weight": 2},
                {"id": "7", "category": "differential", "text": "区分吸收不良的病因：乳糜泻、克罗恩病、小肠细菌过度生长、胰腺功能不全", "weight": 2},
                {"id": "8", "category": "differential", "text": "考虑卓-艾综合征（胃泌素瘤）的可能性及胃泌素检测的意义", "weight": 1},
                {"id": "9", "category": "management", "text": "讨论禁食乳糖、无麸质饮食、营养支持（补铁、维生素K、电解质）", "weight": 1},
                {"id": "10", "category": "red_flag", "text": "评估严重营养不良和多发性溃疡的恶性风险", "weight": 1}
            ],
            "total_items": 10,
            "total_weight": 14
        }),
        "key_questions": json.dumps([
            "您一天大便多少次？大便是什么样子的？有没有油滴或者特别臭？",
            "腹泻跟吃东西有关系吗？吃什么会让拉肚子加重？",
            "您这半年体重下降了13公斤，胃口怎么样？",
            "您有没有觉得手麻脚麻或者记忆力下降？",
            "您家里人有没有类似的腹泻问题或者吃面食不舒服的？"
        ]),
        "red_flags": json.dumps([
            "每日7-15次腹泻导致严重脱水和代谢性酸中毒",
            "6个月内体重减轻13kg提示严重营养不良",
            "双下肢凹陷性水肿提示低蛋白血症",
            "木糖吸收试验极低（仅0.3g/5h）提示小肠吸收功能严重障碍",
            "多发性消化性溃疡须警惕卓-艾综合征"
        ]),
        "diagnosis": "乳糜泻（Celiac Disease / Gluten-Sensitive Enteropathy）",
        "is_active": 1
    },

    # ============================================================
    # Case 16: 消化性溃疡／胃癌待排 - 模块4/week3-4
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "消化性溃疡伴幽门螺杆菌感染（胃癌待排）",
        "department": "消化内科",
        "difficulty": "intermediate",
        "chief_complaint": "医生，我这两个月肚子一直胀胀的，吃不下饭，烧心得厉害，人也瘦了差不多7公斤。",
        "patient_profile": json.dumps({
            "name": "菊花",
            "age": 39,
            "gender": "女",
            "occupation": "品牌服装公司质检员",
            "marital_status": "已婚",
            "education": "不详"
        }),
        "symptoms_description": (
            "近2个月腹胀感，4年前从北京搬到杭州时也有过类似不适，钡餐造影告知患有'溃疡'，接受雷尼替丁和抗酸药治疗。当时医生建议休假戒烟戒酒，患者从3年半前戒烟后症状改善。"
            "近2个月偶尔消化不良，频繁烧心感，尤其吃太多或辛辣油腻食物后。服用碳酸钙制剂和雷尼替丁后缓解。"
            "上个月开始经常消化不良，上腹部隐隐压迫感，未放射，恶心和早饱感。"
            "每周工作6天，最近新老板想压缩工作时间感到压力大。最近体重减轻6.8kg（自认为因减少脂肪摄入）。"
            "偶尔便秘，服用氧化镁乳剂好转，现每天早上食用果汁沥燕麦麸。大便无血迹，颜色也不深。"
            "父亲三周前因肺癌去世，母亲69岁患抑郁症。外祖母54岁死于胃癌。一个兄弟患溃疡已痊愈。"
            "有频繁头痛（每周两三次），服用布洛芬后好转。2次足月妊娠，1次自然流产。"
        ),
        "physical_exam": json.dumps({
            "general": "身高165cm，体重50.3kg（BMI 18.5），紧张、烦躁不安",
            "vitals": "无发热，BP 118/64mmHg，P 85次/分",
            "neck": "无颈部淋巴结肿大，甲状腺正常",
            "lungs": "无异常",
            "breasts": "略有结节状，符合纤维囊性改变",
            "abdomen": "上腹部深度触诊有压痛，无腹胀；肝脾未及",
            "labs": "Hb 100g/L，HCT 30.1%，大便潜血试验阳性，幽门螺旋杆菌抗体IgG阳性",
            "imaging": "钡餐造影显示胃窦充盈缺损"
        }),
        "emotional_state": "anxious",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问上消化道症状：腹胀、烧心、恶心、早饱感", "weight": 1},
                {"id": "2", "category": "associated_symptoms", "text": "询问警报症状：体重减轻6.8kg、大便潜血阳性、Hb下降", "weight": 2},
                {"id": "3", "category": "history", "text": "询问症状的诱发和缓解因素：饮食、压力、药物", "weight": 1},
                {"id": "4", "category": "pmh", "text": "了解4年前溃疡病史和治疗经过", "weight": 1},
                {"id": "5", "category": "medications", "text": "询问布洛芬使用频率（每周2-3次）和抗酸药使用", "weight": 1},
                {"id": "6", "category": "social_history", "text": "了解工作压力、父亲去世的心理应激、吸烟饮酒史", "weight": 1},
                {"id": "7", "category": "family_history", "text": "询问胃癌家族史（外祖母54岁死于胃癌）对诊断的影响", "weight": 2},
                {"id": "8", "category": "differential", "text": "区分解剖性病因：消化性溃疡、胃窦充盈缺损=胃癌待排", "weight": 2},
                {"id": "9", "category": "labs", "text": "了解H.pylori阳性、潜血阳性和钡餐胃窦充盈缺损的综合意义", "weight": 1},
                {"id": "10", "category": "red_flag", "text": "评估胃窦充盈缺损的恶性风险及是否需紧急胃镜检查", "weight": 2}
            ],
            "total_items": 10,
            "total_weight": 14
        }),
        "key_questions": json.dumps([
            "您最近的烧心和腹胀跟吃什么东西有关系吗？",
            "这6.8公斤是怎么瘦下来的？是故意减肥还是吃不下饭？",
            "您大便颜色有没有变黑？最近有没有头晕或者乏力？",
            "您家里还有谁得过胃病、胃癌或者其他癌症？",
            "您最近有没有吃什么止痛药？布洛芬每周吃几次？"
        ]),
        "red_flags": json.dumps([
            "体重减轻6.8kg+大便潜血阳性+贫血高度提示消化道肿瘤",
            "外祖母死于胃癌提示遗传易感性",
            "钡餐造影显示胃窦充盈缺损必须排除胃癌",
            "H.pylori阳性+长期消化不良+胃癌家族史需要胃镜排查",
            "Hb 100g/L提示已存在缺铁性贫血"
        ]),
        "diagnosis": "消化性溃疡伴幽门螺杆菌感染（Peptic Ulcer Disease with H. pylori），胃窦充盈缺损待查排除胃癌",
        "is_active": 1
    },

    # ============================================================
    # Case 17: 股骨颈骨折／骨质疏松 - 模块4/week5-6
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "股骨颈骨折（骨质疏松性骨折）",
        "department": "骨科",
        "difficulty": "beginner",
        "chief_complaint": "医生，我在图书馆前面摔倒了，臀部疼得厉害，完全不能站起来，这条腿一点力气也没有。真是太愚蠢了！",
        "patient_profile": json.dumps({
            "name": "Richardson教授",
            "age": 70,
            "gender": "女",
            "occupation": "大学教授（退休）",
            "marital_status": "丧偶",
            "education": "博士"
        }),
        "symptoms_description": (
            "在图书馆前摔倒致臀部疼痛伴活动障碍。自述失去平衡或脚踝扭了而摔倒。臀部剧烈疼痛，不动会好一点，尝试起来时受伤侧不能站立，虚弱且疼。"
            "学生拨打911，救护车十分钟到达。两年前有一次轻微中风导致右腿比左腿虚弱，可能是摔倒原因之一。"
            "一年前在高尔夫球场下车时也摔了一跤导致腕关节骨折。讨厌用拐杖因为让她觉得自己很老。"
            "20年前查出高血压，服用降压药（B受体阻断剂+利尿剂）。有补钙史但不喜欢喝牛奶。从未接受过激素替代治疗。"
            "不吸烟（50年前吸过但戒了），偶尔喝酒一次很少超过两杯。每天喝3-6杯咖啡。"
            "母亲85岁死于中风，有过多次压缩性骨折史。父亲54岁死于心脏病。独自生活。丈夫九年前因肺癌过世。"
            "每周打一次高尔夫，抱怨腰疼。每天只能走半小时。"
        ),
        "physical_exam": json.dumps({
            "general": "T 37.5°C，HR 102次/分，R 16次/分，BP 160/90mmHg，身高157cm，体重65.8kg",
            "heent": "头部正常，瞳孔正常，眼底动脉硬化I级",
            "neck": "柔软，左颈动脉有轻微杂音",
            "lungs": "双侧清晰",
            "heart": "心率正常律齐，可闻及S4，无杂音",
            "abdomen": "柔软无压痛",
            "extremities": "左腿比右腿短，左髋向外旋转运动范围减少。髋部即使被动运动也感到极度疼痛",
            "neuro": "清醒定向正常，右腿肌力良好，双下肢远侧感觉良好",
            "xray": "股骨颈错位骨折"
        }),
        "emotional_state": "in_pain",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问摔倒的具体情况：地点、机制、受伤部位、疼痛程度", "weight": 1},
                {"id": "2", "category": "history", "text": "询问伤后功能受限：能否站立和其他损伤", "weight": 1},
                {"id": "3", "category": "risk_factors", "text": "评估摔倒危险因素：既往中风（右腿虚弱）、降压药、一年前腕关节骨折史", "weight": 2},
                {"id": "4", "category": "pmh", "text": "了解高血压史、用药史（B受体阻断剂+利尿剂）和中风史", "weight": 1},
                {"id": "5", "category": "risk_factors", "text": "询问骨质疏松危险因素：年龄、绝经、补钙情况、咖啡摄入、运动", "weight": 2},
                {"id": "6", "category": "family_history", "text": "了解母亲多次压缩性骨折史对骨质疏松遗传的影响", "weight": 1},
                {"id": "7", "category": "physical_exam", "text": "了解股骨颈骨折典型体征：左腿短缩外旋、剧烈疼痛", "weight": 1},
                {"id": "8", "category": "imaging", "text": "了解X片结果和手术治疗方案", "weight": 1},
                {"id": "9", "category": "management", "text": "讨论摔倒预防和骨质疏松治疗（钙、维生素D、双膦酸盐）", "weight": 1},
                {"id": "10", "category": "red_flag", "text": "评估骨折并发症：DVT、肺栓塞、肺炎、压疮", "weight": 1}
            ],
            "total_items": 10,
            "total_weight": 12
        }),
        "key_questions": json.dumps([
            "您是怎么摔倒的？摔倒前有没有头晕或者站不稳？",
            "您以前有过骨折吗？一年前腕关节是怎么骨折的？",
            "您平时补钙吗？喝牛奶多不多？有没有吃过防治骨质疏松的药？",
            "您两年前中风后右腿恢复得怎么样？有没有坚持做康复？",
            "您现在在吃什么降压药？吃了多久了？"
        ]),
        "red_flags": json.dumps([
            "股骨颈错位骨折须紧急手术治疗避免股骨头坏死",
            "左腿短缩外旋是股骨颈骨折的典型体征",
            "70岁女性有既往骨折史（腕关节）提示骨质疏松",
            "摔倒风险因素众多：中风后遗症+降压药+高龄",
            "母亲多次压缩性骨折史提示遗传性骨质疏松倾向"
        ]),
        "diagnosis": "左侧股骨颈骨折（Femoral Neck Fracture）继发于骨质疏松（Osteoporosis）",
        "is_active": 1
    },

    # ============================================================
    # Case 18: 多囊卵巢综合征／不孕症 - 模块4/week7-8
    # ============================================================
    {
        "id": str(uuid.uuid4()),
        "title": "多囊卵巢综合征伴不孕症",
        "department": "妇产科",
        "difficulty": "intermediate",
        "chief_complaint": "医生，我结婚3年了，一直没避孕但就是怀不上。我以前怀过两次但都流掉了，从那以后月经量少了一半，月经也越来越不准了。",
        "patient_profile": json.dumps({
            "name": "W女士",
            "age": 26,
            "gender": "女",
            "occupation": "高中英语教师",
            "marital_status": "已婚",
            "education": "本科"
        }),
        "symptoms_description": (
            "与丈夫结婚3年，夫妻性生活正常且从未避孕，但多次家庭妊娠测试均为阴性，感到非常愁闷。"
            "婚前曾怀孕2次，均在怀孕1个多月时因不想要而行人工流产，最近一次在4年前和前男友交往时。"
            "从那次人流后发现每次月经量比以前减少将近一半。本来月经还算准（一般28天一次），但最近5年来月经变得不规律，经常延后，最长需要间隔4个月才来一次月经，且体重逐渐增加。"
            "否认反复腹痛或性生活时疼痛。自觉身体健康，没生过'大病'也没'开过刀'。"
            "无药物或食物过敏史，最近未服用任何特殊药物。有性生活后每年做宫颈癌筛查结果均无问题。"
            "母亲56岁身体健康。父亲有2型糖尿病，3年前因心脏疾病去世（57岁）。姐姐37岁体型肥胖育有2个小孩。哥哥29岁身体健康。"
            "丈夫30岁，婚前女友无妊娠或生育史。因多年未怀孕夫妻双方情绪焦躁偶尔互相埋怨。丈夫男科体检：双侧睾丸大小约12ml质韧，精液常规已送检。"
            "1年前月经第21天做过子宫内膜诊刮，组织物送病理。B超：子宫正常大，内膜双层厚6mm，宫腔局部粘连可能，卵巢多囊样改变。"
        ),
        "physical_exam": json.dumps({
            "general": "外表未见异常，身高162cm，体重76kg（BMI约28.9）",
            "vitals": "无发热，BP 100/75mmHg，P 76次/分",
            "skin": "温暖干燥，毛发增多（腋毛、四肢、乳晕周围），面部有较多痤疮",
            "heent": "瞳孔等大等圆，对光反射正常",
            "neck": "柔软无结节，双侧甲状腺未触及肿大",
            "heart_lungs": "心律齐，S1/S2正常，无杂音，呼吸音正常",
            "gyn": "外阴阴毛浓密，阴道通畅少量分泌物。宫颈闭合无举痛。子宫正常大无压痛。附件区未及肿块或压痛",
            "neuro": "颅神经2-12完整，肌力感觉正常，膝反射2+",
            "extremities": "无杵状指、紫绀、水肿或震颤",
            "imaging": "子宫正常大，内膜双层厚6mm，宫腔局部粘连可能，卵巢多囊样改变"
        }),
        "emotional_state": "anxious",
        "rubric": json.dumps({
            "items": [
                {"id": "1", "category": "chief_complaint", "text": "询问不孕的具体情况：结婚3年未避孕未孕", "weight": 1},
                {"id": "2", "category": "menstrual_history", "text": "询问月经变化：人流后月经量减半、周期延长、月经稀发（最长4个月）", "weight": 2},
                {"id": "3", "category": "associated_symptoms", "text": "询问多毛和痤疮等高雄激素表现及体重增加", "weight": 2},
                {"id": "4", "category": "pmh", "text": "询问2次人工流产史对子宫内膜的影响及宫腔粘连可能", "weight": 2},
                {"id": "5", "category": "family_history", "text": "询问家族史：父亲糖尿病（胰岛素抵抗）、姐姐肥胖、PCOS的家族聚集性", "weight": 1},
                {"id": "6", "category": "physical_exam", "text": "了解多毛（腋毛、四肢、乳晕周围）、面部痤疮、肥胖（BMI 28.9）等高雄激素体征", "weight": 1},
                {"id": "7", "category": "imaging", "text": "了解B超：子宫内膜厚度6mm（偏薄）、宫腔粘连可能、卵巢多囊样改变", "weight": 2},
                {"id": "8", "category": "differential", "text": "区分PCOS与其他不孕原因：输卵管因素、子宫内膜因素（宫腔粘连）、男方因素", "weight": 2},
                {"id": "9", "category": "male_factor", "text": "询问男方精液检查的重要性和夫妻同治原则", "weight": 1},
                {"id": "10", "category": "management", "text": "讨论PCOS综合治疗：生活方式干预（减重）、排卵诱导、宫腔粘连处理", "weight": 1}
            ],
            "total_items": 10,
            "total_weight": 15
        }),
        "key_questions": json.dumps([
            "您月经一般多久来一次？最长推迟过多久？",
            "您最近体重有什么变化？有没有注意到自己体毛变多或者脸上长痘痘？",
            "您以前做的人流手术是怎么做的？术后有没有宫腔感染？",
            "您有没有查过血糖或者胰岛素？家里人有没有糖尿病的？",
            "您丈夫有没有去检查过精液？结果怎么样？"
        ]),
        "red_flags": json.dumps([
            "月经稀发（最长4个月）+高雄激素体征（多毛、痤疮）+肥胖高度提示PCOS",
            "B超提示宫腔局部粘连可能，与人流史相关",
            "子宫内膜仅6mm（偏薄）可能影响胚胎着床",
            "家族史：父亲2型糖尿病+姐姐肥胖提示胰岛素抵抗遗传",
            "须排除男方因素导致的不孕"
        ]),
        "diagnosis": "多囊卵巢综合征（Polycystic Ovary Syndrome, PCOS）伴宫腔粘连可能，原发性不孕症",
        "is_active": 1
    },
]

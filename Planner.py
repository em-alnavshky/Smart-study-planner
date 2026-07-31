# برنامج إدارة وتصنيف المهام الدراسية الذكي
# يساعد الطالب على تنظيم واجباته واختباراته وتحديد الأولويات تلقائياً

print("=== مرحباً بك في نظام إدارة المهام الدراسية الذكي ===")

tasks = []

def add_task():
    print("\n--- إضافة مهمة جديدة ---")
    task_name = input("أدخل عنوان المهمة (مثلاً: حل واجب بايثون): ")
    
    print("اختر درجة الأهمية:")
    print("1. عالية جداً (اختبار أو تسليم مشروع)")
    print("2. متوسطة (واجب منزلي عادي)")
    print("3. منخفضة (مراجعة أو قراءة جانبية)")
    
    choice = input("أدخل رقم الاختيار (1-3): ")
    
    # خوارزمية بسيطة لتصنيف الأولوية تلقائياً
    if choice == "1":
        priority = "🔴 عالية جداً (ابدأ بها فوراً)"
    elif choice == "2":
        priority = "🟡 متوسطة (مهمة عادية)"
    else:
        priority = "🟢 منخفضة (وقت الفراغ)"
        
    # حفظ المهمة في قاموس (Dictionary) داخل المصفوفة
    new_task = {"name": task_name, "priority": priority}
    tasks.append(new_task)
    print(f"✅ تم إضافة المهمة [{task_name}] بنجاح!")

def show_tasks():
    print("\n=== قائمة مهامك الدراسية الحالية ===")
    if not tasks:
        print("🎉 لا توجد مهام حالياً! أنتِ مستعدة تماماً.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task['name']} -> الأولوية: {task['priority']}")
    print("====================================")

# الحلقة التكرارية الرئيسية للبرنامج
while True:
    print("\n1. إضافة مهمة جديدة")
    print("2. عرض كل المهام وتصنيفها")
    print("3. الخروج من البرنامج")
    
    main_choice = input("اختر عملية للقيام بها (1-3): ")
    
    if main_choice == "1":
        add_task()
    elif main_choice == "2":
        show_tasks()
    elif main_choice == "3":
        print("\nبالتوفيق في دراستكِ! تم إغلاق البرنامج. ✨")
        break
    else:
        print("إدخال خاطئ، يرجى اختيار رقم من 1 إلى 3.")

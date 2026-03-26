# دليل نشر مشروع Suna المعدل 🚀

هذا المستودع يحتوي على نسخة معدلة من مشروع **Suna** مع دمج مزود **Wavespeed** (مودل `minimax-m2.7`) وإصلاحات شاملة للتبعيات.

## 1. الرفع إلى GitHub
1. قم بإنشاء مستودع جديد (New Repository) على حسابك في GitHub.
2. قم بفك ضغط الملف الذي أرسلته لك.
3. افتح الطرفية (Terminal) داخل المجلد وقم بتنفيذ الأوامر التالية:
   ```bash
   git init
   git add .
   git commit -m "Initial commit with Wavespeed integration"
   git branch -M main
   git remote add origin [رابط_مستودعك_على_جيت_هاب]
   git push -u origin main
   ```

## 2. النشر على Render
لقد قمت بإضافة ملف `render.yaml` الذي يقوم بضبط كل شيء تلقائياً.
1. اذهب إلى [Render Dashboard](https://dashboard.render.com/).
2. اضغط على **New +** ثم اختر **Blueprint**.
3. اربط حسابك بـ GitHub واختر المستودع الذي رفعته.
4. سيقوم Render تلقائياً بإنشاء خدمتين:
   - **suna-backend**: الواجهة الخلفية (FastAPI).
   - **suna-frontend**: الواجهة الأمامية (Next.js).

## 3. إعداد متغيرات البيئة (Environment Variables)
في لوحة تحكم Render، تأكد من إضافة المتغيرات التالية لكل خدمة:

### للواجهة الخلفية (suna-backend):
- `SUPABASE_URL`
- `SUPABASE_SERVICE_ROLE_KEY`
- `REDIS_URL` (الرابط الذي يبدأ بـ redis://)
- `WAVESPEED_API_KEY`
- `COMPOSIO_API_KEY`
- `DAYTONA_API_KEY`
- `FERNET_KEY` (مفتاح التشفير)

### للواجهة الأمامية (suna-frontend):
- `NEXT_PUBLIC_SUPABASE_URL`
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- `NEXT_PUBLIC_API_URL` (رابط الواجهة الخلفية الذي سيوفره لك Render)

---
**ملاحظة:** تم ضبط المشروع ليعمل بأفضل أداء (Production Mode) لضمان السرعة والاستقرار.

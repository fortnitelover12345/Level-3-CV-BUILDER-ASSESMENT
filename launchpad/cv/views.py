from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import CVProfile
import pdfplumber
import re

def templates(request):
    return render(request, 'cv/templates.html')


@login_required
def overview(request, profile_id):
    profile = get_object_or_404(CVProfile, id=profile_id, user=request.user)
    
    context = {
        'profile': profile,
    }
    return render(request, 'cv/cv_template.html', context)

@login_required
def cv_preview(request):
    profile = request.user.cvprofile
    return render(request, 'cv/cv_template.html', {'profile': profile})
@login_required
def template_gallery(request):
    return render(request, 'cv/template.html')

@login_required
def preview_template(request, template_name):

    profile = request.user.cvprofile
    if request.method == 'POST':
        profile.design_choice = template_name
        profile.save()
        return redirect('edit_profile')
        
   
    return render(request, 'cv/preview_template.html', {
        'profile': profile, 
        'preview_mode': True,
        'selected_template': template_name
    })

@login_required
def edit_profile(request):
    profile = request.user.cvprofile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('cv_template', profile_id=profile.id)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'cv/gather_info.html', {'form': form})

@login_required
def upload_cv_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('cv_file')
        
        if not uploaded_file:
            messages.error(request, "Please pick a valid file.")
            return redirect('upload_cv')

        if not uploaded_file.name.endswith('.pdf'):
            messages.error(request, "Currently, only PDF documents are supported for upload.")
            return redirect('upload_cv')

        extracted_text = ""
        try:
        
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    text_content = page.extract_text()
                    if text_content:
                        extracted_text += text_content + "\n"

            if not extracted_text.strip():
                messages.error(request, "Could not extract text. The PDF might be a scanned image.")
                return redirect('upload_cv')

         
            profile, created = CVProfile.objects.get_or_create(user=request.user)

        
            profile.summary = extracted_text.strip()
            profile.save()

            messages.success(request, "File processed successfully!")
            
        
            return redirect('template_gallery')

        except Exception as e:
            messages.error(request, f"An error occurred while reading your file: {str(e)}")
            return redirect('upload_cv')

    return render(request, 'cv/upload.html')

@login_required
def upload_cv_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('cv_file')
        
        if not uploaded_file or not uploaded_file.name.endswith('.pdf'):
            messages.error(request, "Please upload a valid PDF file.")
            return redirect('upload_cv')

        extracted_text = ""
        try:
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    text_content = page.extract_text()
                    if text_content:
                        extracted_text += text_content + "\n"

            if not extracted_text.strip():
                messages.error(request, "Could not read text from this PDF.")
                return redirect('upload_cv')

    
            lines = [line.strip() for line in extracted_text.split('\n') if line.strip()]
            
          
            full_name = ""
            phone = ""
            summary = ""
            skills = ""
            experience = ""
            education = ""

           
            if lines:
                full_name = lines[0]

        
            phone_match = re.search(r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}', extracted_text)
            if phone_match:
                phone = phone_match.group(0)


            current_section = "summary"
            
            SUMMARY_KEYWORDS = ["summary", "profile", "about me", "objective", "overview"]
            SKILLS_KEYWORDS = ["skill", "expertise", "competencies", "strengths", "capabilities"]
            EXPERIENCE_KEYWORDS = ["experience", "work history", "employment", "history", "career"]
            EDUCATION_KEYWORDS = ["education", "school", "qualification", "degree", "academic"]


            COMMON_SKILLS_LIST = ["team worker", "active listener", "customer service", "communication", 
                                  "problem solving", "leadership", "time management", "teamwork", "python", "django"]

            for line in lines[1:]:  
                lower_line = line.lower().strip()
                

                if "@" in lower_line or ".com" in lower_line or (any(char.isdigit() for char in line) and len([c for c in line if c.isdigit()]) > 7):
                    continue
                
  
                for skill_word in COMMON_SKILLS_LIST:
                    if skill_word in lower_line and skill_word not in skills.lower():
                        skills += skill_word.title() + ", "


                has_skills_kw = any(kw in lower_line for kw in SKILLS_KEYWORDS)
                has_summary_kw = any(kw in lower_line for kw in SUMMARY_KEYWORDS)
                
                if has_skills_kw and has_summary_kw:
                    skills_pos = min([lower_line.find(kw) for kw in SKILLS_KEYWORDS if lower_line.find(kw) != -1])
                    summary_pos = min([lower_line.find(kw) for kw in SUMMARY_KEYWORDS if lower_line.find(kw) != -1])
                    
                    clean_text = line
                    for phrase in ["core skills", "professional summary", "summary", "skills"]:
                        clean_text = re.sub(phrase, "", clean_text, flags=re.IGNORECASE)
                    clean_text = clean_text.strip()
                    
                    if clean_text:
                        if skills_pos < summary_pos:
                            summary += clean_text + " "
                            current_section = "summary"
                        else:
                            skills += clean_text + ", "
                            current_section = "skills"
                    continue 

 
                is_standalone_header = False
                
                if any(kw in lower_line for kw in SKILLS_KEYWORDS):
                    current_section = "skills"
                    is_standalone_header = True
                elif any(kw in lower_line for kw in SUMMARY_KEYWORDS):
                    current_section = "summary"
                    is_standalone_header = True
                elif any(kw in lower_line for kw in EXPERIENCE_KEYWORDS):
                    current_section = "experience"
                    is_standalone_header = True
                elif any(kw in lower_line for kw in EDUCATION_KEYWORDS):
                    current_section = "education"
                    is_standalone_header = True


                if is_standalone_header and len(lower_line.split()) <= 4:
                    continue

                if current_section == "summary":
                    summary += line + " "
                elif current_section == "skills":
                    skills += line + ", "
                elif current_section == "experience":
                    experience += line + "\n"
                elif current_section == "education":
                    education += line + "\n"


            if skills:
                skills = re.sub(r',\s*$', '', skills.strip()) 
                skills = re.sub(r'\s+', ' ', skills).strip()

            
            profile, created = CVProfile.objects.get_or_create(user=request.user)
            profile.full_name = full_name.strip()
            profile.phone = phone.strip()
            profile.summary = summary.strip()
            profile.skills = re.sub(r'\s+', ' ', skills).strip()
            profile.experience = experience.strip()
            profile.education = education.strip()
            profile.save()

            messages.success(request, "File parsed and fields mapped successfully!")
            return redirect('template_gallery')

        except Exception as e:
            messages.error(request, f"An error occurred while splitting fields: {str(e)}")
            return redirect('upload_cv')

    return render(request, 'cv/upload.html')

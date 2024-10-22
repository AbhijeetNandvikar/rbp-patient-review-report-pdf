from jinja2 import Environment, FileSystemLoader
import json
import asyncio
from playwright.async_api import async_playwright


env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('without-header-footer.html')

header = env.get_template('header.html')
footer = env.get_template('footer.html')

mockData = {
  "review_id": 1,
  "review_status": "review_complete",
  "completed_on": "05/29/2024",
  "exported_by": "Abhijeet Nandvikar",
  "exported_on": "08/30/2024 02:35 PM",
  "patient_name": "Mr Helensky, Adren J",
  "patient_id": "00000003",
  "patient_dob": "08/03/2000 (24 Y)",
  "patient_sex": "M",
  "patient_insurance_plan": "Company A",
  "patient_member_id": "826918101",
  "disease_type": "Cancer",
  "affected_organ": "Lung",
  "occurrence": "New Occurrence",
  "phase_of_care": "Treatment",
  "review_assessment_questions": [
    {
      "question": "This is an example of a sample question.",
      "answer": "While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner."
    },
      {
      "question": "This is an example of a sample question.",
      "answer": "While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner.While paragraphs traditionall skdhfkshfhsf shf sfh khf sdkfh skdfh sh fsd hfshf ksdhf ksjhdf ksdhf ksdhf kshf ksdhf ksdhf kshf sdjkfh skdhf ksdjfh skdjfh ksdjfh sjkdhf ksdjfh jksdfh ksjdh fksdh fsdh fhksjhfk j   djdjjjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjdjfkshfkshkfgh lsfglsdfghsldfg lsdfhgs fgsdf hjgsdf khjsgf sdghf ksjdghf skejfg sdufg kf jg sdfg f gjksd fk fjkg skfg jkasfg hjks fk fkhsg dfhjkg sdkf gksjdf gkjsdfg jsdf vbksjdf bsjdfh by consist of written text, they can also incorporate visual elements, such as bullet points, lists, or images. These visual aids can enhance the organization and clarity of the content, especially in instructional or explanatory writing. By combining textual and visual elements, authors can effectively convey information and engage readers in a more dynamic manner."
    }
  ],
  "treatment_plans": [
    {
      "name": "Treatment Plan A",
      "description": "This is a sample recommendation description as placeholder This is a sample description as placeholder This is a sample description as placeholder",
      "recommendation_groups": [
          ]
    },
     {
      "name": "Treatment Plan B",
      "description": "This is a sample recommendation description as placeholder This is a sample description as placeholder This is a sample description as placeholder",
      "recommendation_groups": [
        {
          "name": "Sample Group 1",
          "description": "This is a sample group description as placeholder This is a sample description as placeholder This is a sample description as placeholder,This is a sample group description as placeholder This is a sample description as placeholder This is a sample description as placeholder.",
          "recommendations": [
            {
              "name": "Adjuvant Hormone Therapy",
              "description": "Adjuvant hormone therapy with tamoxifen is recommended for patients with hormone receptor-positive breast cancer.",
              "reason_for_deviation": "This is a sample note for the recommendation",
              "not_applicable": False,
              "additional_notes": "",
              "is_non_standard": False,
              "code": "A0010",
              "code_description": "some medication description"
            },
            {
              "name": "Adjuvant Hormone Therapy",
              "description": "Adjuvant hormone therapy with tamoxifen is recommended for patients with hormone receptor-positive breast cancer.",
              "reason_for_deviation": "This is a sample note for the recommendation",
              "not_applicable": False,
              "additional_notes": "",
              "is_non_standard": False,
              "code": "A0010",
              "code_description": "some medication description"
            },
            {
              "name": "Adjuvant Hormone Therapy",
              "description": "Adjuvant hormone therapy with tamoxifen is recommended for patients with hormone receptor-positive breast cancer.",
              "reason_for_deviation": "This is a sample note for the recommendation",
              "not_applicable": False,
              "additional_notes": "",
              "is_non_standard": False,
              "code": "A0010",
              "code_description": "some medication description"
            },
            
          ]
        },
         {
          "name": "Sample Group 1",
          "description": "This is a sample group description as placeholder This is a sample description as placeholder This is a sample description as placeholder,This is a sample group description as placeholder This is a sample description as placeholder This is a sample description as placeholder.",
          "recommendations": [
            {
              "name": "Adjuvant Hormone Therapy",
              "description": "Adjuvant hormone therapy with tamoxifen is recommended for patients with hormone receptor-positive breast cancer.",
              "reason_for_deviation": "This is a sample note for the recommendation",
              "not_applicable": False,
              "additional_notes": "",
              "is_non_standard": False,
              "code": "A0010",
              "code_description": "some medication description"
            },
            {
              "name": "Adjuvant Hormone Therapy",
              "description": "Adjuvant hormone therapy with tamoxifen is recommended for patients with hormone receptor-positive breast cancer.",
              "reason_for_deviation": "This is a sample note for the recommendation",
              "not_applicable": False,
              "additional_notes": "",
              "is_non_standard": False,
              "code": "A0010",
              "code_description": "some medication description"
            },
            {
              "name": "Adjuvant Hormone Therapy",
              "description": "Adjuvant hormone therapy with tamoxifen is recommended for patients with hormone receptor-positive breast cancer.",
              "reason_for_deviation": "This is a sample note for the recommendation",
              "not_applicable": False,
              "additional_notes": "",
              "is_non_standard": False,
              "code": "A0010",
              "code_description": "some medication description"
            },
            
          ]
        },
         {
          "name": "Sample Group 123",
          "description": "This is a sample group description as placeholder This is a sample description as placeholder This is a sample description as placeholder,This is a sample group description as placeholder This is a sample description as placeholder This is a sample description as placeholder.",
          "recommendations": []
        },
    
      ]
    }
  ]
}

# Render the template with JSON data
html_content = template.render(mockData)

# Write the rendered HTML to a file (optional)
with open('output.html', 'w') as file:
    file.write(html_content)

async def generate_pdf(html_content, output_file):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # Set the HTML content for the page
        await page.set_content(html_content)

        pdf_config = {
            "path": 'output.pdf',
            "format": "A4",
            "print_background": True,
            "display_header_footer": True,
            "header_template": header.render(),
            "footer_template": footer.render(),
            "margin": {
                "top": "120px",
                "bottom": "100px"
            }
        }

        # Generate a PDF from the page
        await page.pdf(**pdf_config)

        # Close the browser
        await browser.close()

with open("output.html", "r") as file:
     html_content = file.read()

asyncio.run(generate_pdf(html_content, "output.pdf"))
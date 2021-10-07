from patient.models import Label, AlternateLabel
import json
import datetime


def main():
    input_data = [
        "Haemoglobin", "RBC Count", "MCV", "MCH", "TLC", "PCV", "MCHC", "MPV", "E.S.R.", "GLUCOSE", "SGOT- ASPARTTATE TRANSAMINAS E", "SGPT - ALANINE TRANSAMINAS E", "GGTP", "UIBC", "FOLATE", "GLYCOSYLATE D HEMOGLOBIN", "25-HYDROXY, VITAMIN D" ,
        "HAEMOGLOBIN", "TOTAL LEUCOCYTES COUNT","PACKED CELLS UME", "MEAN CORP VOLUME", "MEAN CORP Hb ( MCH)", "MEAN CORP Hb CONC", "PLATELETS COUNT", "E.S.R.", "Neutrophil", "Lymphocyte", "Monocyte", "Eosinophil", "Basophil", "Serum Cholestrol", "Serum Triglycerides", "HDL Cholesterol", "Serum L.D.L.Cholestrol", "Serum VLDL", "CHO / HDL Cholesterol Ratio", "LDL / HDL Cholesterol Ratio", "BLOOD UREA", "BLOOD UREA NITROGEN", "Serum Creatinine", "Serum Uric Acid ", "Calcium", "Serum Sodium", "Serum Potassium", "Serum Bilirubin", "Bilirubin (Direct)", "Bilirubin (Indirect )", "Serum G. O. T./AST", "Serum G. P. T. /ALT","Serum Alkaline Phosphatase", "GAMMA G.T.", "Serum Albumin", "Globulin", "TRI-IODO THYROXINE", "SERUM TSH", "ESTRADIOL", "(Glycated HbA1c)/ HbA1c", "VITAMIN B-12 LEVEL ", "VITAMIN D3 LEVEL", "LH", "FSH", "Total Protein", "Blood Sugar",
        "HEMOGLOBIN ", "WHITE BLOOD CELL COUNT", "RED BLOOD CELL COUNT", "HEMATOCRIT", "MCV", "MCH", "MCHC", "MPV", "PLATELET COUNT", "ERYTHROCYTE SEDIMENTATION RATE", "NEUTROPHILS ", "LYMPHOCYTES ", "MONOCYTES", "EOSINOPHILS ", "BASOPHILS ", "ABSOLUTE NEUTROPHILS", "ABSOLUTE LYMPHOCYTES", "ABSOLUTE MONOCYTES", "ABSOLUTE BASOPHILS ", "TSH",
        "HEMOGLOBIN","TLC","PACKED CELL VOLUME","MCV","MCH, Blood","MCHC","PLATELET COUNT","E.S.R","POLYMORPHS","LYMPHOCYTES", "EOSINOPHILS" ,"MONOCYTES","RDW","ABSOLUTE NEUTROPHIL COUNT" , "ABSOLUTE EOSINOPHIL COUNT BLOOD","FASTING GLUCOSE","MAGNESIUM","CHOLESTROL, SERUM","TRIGLYCERIDES","HDL CHOLESTEROL","LDL CHOLESTEROL ","VLDL CHOLESTEROL","LDL / HDL RATIO","CHOLESTEROL / HDL RATIO","UREA Serum",  "UREA NITROGEN","CREATININE SERUM","URIC ACID","SODIUM","POTASSIUM","CHLORIDE" ,"BILIRUBIN (TOTAL)","SGOT","SGPT","ALKALINE PHOSPHATASE","TOTAL PROTEINS Serum","ALBUMIN","GLOBULIN","A:G RATIO","IgE SERUM","IRON","TIBC","UIBC","FERRITIN","FT3 Serum" ,"FREE T4","TSH, Serum"," HbA1c","VITAMIN B12","VITAMIN D, 25-HYDROXY, Serum","FOLATE, Serum","INSULIN FASTING","INSULIN PP","BLOOD GLUCOSE PP",
        "Hemoglobin","WBC COUNT","RBC","Packed cell volume","Platelet Count","ESR","Neutrophils","Lymphocytes","Monocytes","Eosinophils","Basophils","CHOLESTEROL", "TRIGLYCERIDES", "HDL CHOLESTEROL", "LDL CHOLESTEROL","HDL CHOLESTROL RATIO","BILIRUBIN","BILIRUBIN CONJUGATED(DIRECT)","BILIRUBIN UNCONJUGATED (INDIRECT)","AST ","ALT","ALKALINE PHOSPHATASE","GGTP","ALBUMIN","GLOBULIN","FREE T3","FREE T4","TSH","HBA1C","VITAMIN B12","VITAMIN D TOTAL(250H vitD3 and 250H vitD2)","FASTING","INSULIN (PP)",
    ]
    input_data = list(map(str.strip, input_data))
    input_data = list(set(map(str.lower, input_data)))
    print(input_data)
    print(len(input_data))
    for label in input_data:
        print(label)
        try:    
            l, created = Label.objects.get_or_create(name=label)
            print(l, created)
            if created:
                l.save()
            a = AlternateLabel.objects.create(name=label, label=l)
            a.save()
        except Exception as identifier:
            print('error', label, identifier,)
    return 'done'

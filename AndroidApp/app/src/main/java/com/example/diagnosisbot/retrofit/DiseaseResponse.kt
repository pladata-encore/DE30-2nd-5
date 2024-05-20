package com.example.diagnosisbot.retrofit

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

data class DiseaseResponse (
    @Expose
    @SerializedName(value = "disease_id") val diseaseId: Int,

    @Expose
    @SerializedName(value = "disease_name") val diseaseName: String,

    @Expose
    @SerializedName(value = "disease_link") val diseaseLink: String,

    @Expose
    @SerializedName(value = "disease_img") val diseaseImg: String,

    @Expose
    @SerializedName(value = "symptoms") val symptoms: String,

    @Expose
    @SerializedName(value = "symptom_ids") val symptomIds: String,

    @Expose
    @SerializedName(value = "related_diseases") val relatedDiseases: String,

    @Expose
    @SerializedName(value = "related_disease_ids") val relatedDiseaseIds: String,

    @Expose
    @SerializedName(value = "department") val department: String,

    @Expose
    @SerializedName(value = "synonyms") val synonyms: String,

    @Expose
    @SerializedName(value = "detailed_symptoms") val detailedSymptoms: String,

    @Expose
    @SerializedName(value = "disease_course") val diseaseCourse: String,

    @Expose
    @SerializedName(value = "disease_specific_diet") val diseaseSpecificDiet: String,

    @Expose
    @SerializedName(value = "diet_therapy") val dietTherapy: String,

    @Expose
    @SerializedName(value = "recommended_food") val recommendedFood: String,

    @Expose
    @SerializedName(value = "caution_food") val cautionFood: String,

    @Expose
    @SerializedName(value = "other_notes") val otherNotes: String
)
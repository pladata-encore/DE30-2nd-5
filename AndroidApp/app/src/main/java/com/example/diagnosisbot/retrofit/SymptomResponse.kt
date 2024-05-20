package com.example.diagnosisbot.retrofit

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

data class SymptomResponse (
    @Expose
    @SerializedName(value = "predicted_diseases") val diseasesString: String
)
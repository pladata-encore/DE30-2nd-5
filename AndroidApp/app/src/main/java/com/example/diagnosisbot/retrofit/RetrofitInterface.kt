package com.example.diagnosisbot.retrofit

import com.google.gson.Gson
import com.google.gson.GsonBuilder
import retrofit2.Call
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Body
import retrofit2.http.POST

interface RetrofitInterface {
    @POST("api/symptom/")
    fun postSymptom(
        @Body req: SymptomRequest
    ): Call<SymptomResponse>

    @POST("api/disease/")
    fun getDisease(
        @Body req: DiseaseRequest
    ): Call<DiseaseResponse>


    companion object {
        private const val BASE_URL = "http://10.0.2.2:8000/" //
        fun create(): RetrofitInterface {
            val gson: Gson = GsonBuilder().setLenient().create()


            return Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create(gson))
                .build()
                .create(RetrofitInterface::class.java)
        }
    }
}
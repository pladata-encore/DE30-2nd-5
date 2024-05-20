package com.example.diagnosisbot

import android.os.Bundle
import android.text.method.ScrollingMovementMethod
import android.util.Log
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.diagnosisbot.retrofit.DiseaseRequest
import com.example.diagnosisbot.retrofit.DiseaseResponse
import com.example.diagnosisbot.retrofit.RetrofitInterface
import org.json.JSONObject
import org.json.JSONTokener
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response


class InfoActivity: AppCompatActivity() {
    /* InfoActivity <-> MainActivity */
    companion object {
        var infoActivity: InfoActivity? = null
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_info)

        /* infoActivity <-> MainActivity */
        infoActivity = this

        // 전역 변수
        val toFindDisease: String? = intent.getStringExtra("selectedDisease")

        // View 변수 선언 및 연결
        val txtDiseaseName: TextView = findViewById(R.id.txtDiseaseName)
        val txtSymptom: TextView = findViewById(R.id.txtSymptom)
        val txtDepartment: TextView = findViewById(R.id.txtDepartment)
        val txtProgress: TextView = findViewById(R.id.txtProgress)
        val txtTreatment: TextView = findViewById(R.id.txtTreatment)

        // scroll bar 추가
        txtSymptom.movementMethod = ScrollingMovementMethod()
        txtDepartment.movementMethod = ScrollingMovementMethod()
        txtProgress.movementMethod = ScrollingMovementMethod()
        txtTreatment.movementMethod = ScrollingMovementMethod()


        txtDiseaseName.setText(toFindDisease)

        Toast.makeText(this@InfoActivity, "데이터베이스에 없는 정보는 표시되지 않습니다.", Toast.LENGTH_LONG)
            .show()

        // 통신 시작
        val retrofitObj = RetrofitInterface.create()
        val diseaseRequest = DiseaseRequest(toFindDisease!!)
        // API 호출
        retrofitObj.getDisease(diseaseRequest).enqueue(object: Callback<DiseaseResponse> {
            override fun onResponse(call: Call<DiseaseResponse>, response: Response<DiseaseResponse>) {
                //// 통신 및 호출 성공 시
                if(response.isSuccessful) {
                    // Body 받아오기
                    val responseBody = response.body()!!

                    if (!responseBody.symptoms.isNullOrEmpty())
                        txtSymptom.setText(responseBody.symptoms)
                    else
                        txtSymptom.setText("정보가 없습니다.")

                    if (!responseBody.department.isNullOrEmpty())
                        txtDepartment.setText(responseBody.department)
                    else
                        txtDepartment.setText("정보가 없습니다.")

                    if (!responseBody.detailedSymptoms.isNullOrEmpty())
                        txtProgress.setText(responseBody.detailedSymptoms)
                    else
                        txtProgress.setText("정보가 없습니다.")

                    val diet_therapy_str: String
                    val recommended_food_str: String
                    val caution_food_str: String
                    val other_notes_str: String

                    if (!responseBody.dietTherapy.isNullOrEmpty())
                        diet_therapy_str = responseBody.dietTherapy
                    else
                        diet_therapy_str = "정보가 없습니다."

                    if (!responseBody.recommendedFood.isNullOrEmpty())
                        recommended_food_str = responseBody.recommendedFood
                    else
                        recommended_food_str = "정보가 없습니다."

                    if (!responseBody.cautionFood.isNullOrEmpty())
                        caution_food_str = responseBody.cautionFood
                    else
                        caution_food_str = "정보가 없습니다."

                    if (!responseBody.otherNotes.isNullOrEmpty())
                        other_notes_str = responseBody.otherNotes
                    else
                        other_notes_str = "정보가 없습니다."

                    val strTreatment: String = "식사요법의 실제\n" + diet_therapy_str +
                            "\n\n권장 식품\n" + recommended_food_str +
                            "\n\n주의 식품\n" + caution_food_str +
                            "\n\n그 외 주의사항\n" + other_notes_str

                    txtTreatment.setText(strTreatment)
                }

                //// 통신 성공, 호출 실패 시
                else {
                    val responseErrorBody = JSONTokener(
                        response.errorBody()?.string()!!
                    ).nextValue() as JSONObject
                    Log.e("error", responseErrorBody.toString())
                    Toast.makeText(this@InfoActivity, "에러가 발생했습니다.", Toast.LENGTH_SHORT)
                        .show()
                }
            }

            //// 통신 실패 시
            override fun onFailure(call: Call<DiseaseResponse>, t: Throwable) {
                Toast.makeText(this@InfoActivity, "서버와 연결할 수 없습니다.", Toast.LENGTH_SHORT)
                    .show()
            }
        })
    }

    // back 버튼 클릭 시, MainActivity 전환
    override fun onBackPressed() {
        super.onBackPressed()
        Toast.makeText(this@InfoActivity, "메인으로 되돌아갑니다..",
            Toast.LENGTH_LONG).show()

        // MainActivity 전환
        finish()
    }
}
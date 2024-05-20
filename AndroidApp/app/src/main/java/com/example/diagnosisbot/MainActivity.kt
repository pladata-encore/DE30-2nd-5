package com.example.diagnosisbot

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.diagnosisbot.retrofit.RetrofitInterface
import com.example.diagnosisbot.retrofit.SymptomRequest
import com.example.diagnosisbot.retrofit.SymptomResponse
import org.json.JSONArray
import org.json.JSONObject
import org.json.JSONTokener
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* InfoActivity 종료 */
        InfoActivity.infoActivity?.finish()

        // View 변수 선언 및 연결
        val edtSymptom: EditText = findViewById(R.id.edtSymptom)
        val btnSubmitSymptom: Button = findViewById(R.id.btnSubmitSymptom)
        val loResult: LinearLayout = findViewById(R.id.loResult)
        val txtDiseasesList: TextView = findViewById(R.id.txtDiseasesList)
        val edtDiseaseNo: EditText = findViewById(R.id.edtDiseaseNo)
        val btnSubmitDisease: Button = findViewById(R.id.btnSubmitDisease)

        var findedDiseases: JSONArray? = null

        // 질병 찾기 버튼 클릭 이벤트
        btnSubmitSymptom.setOnClickListener {
            // 입력이 비어있으면,
            if (edtSymptom.text.toString().isEmpty()) {
                Toast.makeText(
                    this@MainActivity,
                    "증상을 입력해주세요.",
                    Toast.LENGTH_SHORT
                ).show()
            } else {
                // 통신 시작
                val retrofitObj = RetrofitInterface.create()
                val symptomRequest = SymptomRequest(edtSymptom.getText().toString())
                retrofitObj.postSymptom(symptomRequest).enqueue(object: Callback<SymptomResponse> {
                    override fun onResponse(call: Call<SymptomResponse>, response: Response<SymptomResponse>) {
                            /// 통신 및 호출 성공 시
                            if (response.isSuccessful) {
                                val responseBody = response.body()!!
                                // 호출 성공 시 동작!!
                                //response body는 String으로 된 JSONArray 형태
                                val predictedDiseasesString: String = responseBody.diseasesString
                                findedDiseases = JSONArray(predictedDiseasesString)

                                var tmpTxt = ""
                                for (i in 0 until findedDiseases!!.length()) {
                                    val jsonObject: JSONObject = findedDiseases!!.getJSONObject(i)
                                    tmpTxt = tmpTxt + "${i+1}" + ". " + jsonObject.getString("질병") + "\n"
                                }
                                txtDiseasesList.setText(tmpTxt)

                                loResult.visibility = View.VISIBLE
                            }

                            /// 통신 성공, 호출 실패 시
                            else {
                                val responseErrorBody = JSONTokener(
                                    response.errorBody()?.string()!!
                                ).nextValue() as JSONObject
                                Log.e("error", responseErrorBody.toString())

                                Toast.makeText(this@MainActivity, "에러가 발생했습니다.: ", Toast.LENGTH_SHORT)
                                    .show()
                                loResult.visibility = View.INVISIBLE
                            }
                        }

                        /// 통신 실패 시
                        override fun onFailure(call: Call<SymptomResponse>, t: Throwable) {
                            Toast.makeText(this@MainActivity, "서버와의 연결이 끊겼거나, 입력에 쉼표(,)가 없습니다.", Toast.LENGTH_SHORT)
                                .show()
                            loResult.visibility = View.INVISIBLE
                        }
                    })
            }
            return@setOnClickListener
        }
        btnSubmitDisease.setOnClickListener {
            val selectedDiseaseNumber: Int = edtDiseaseNo.getText().toString().toInt()-1
            val selectedDisease: String = findedDiseases!!.getJSONObject(selectedDiseaseNumber).getString("질병")
            val toInfoIntent = Intent(this@MainActivity, InfoActivity::class.java)
            toInfoIntent.putExtra("selectedDisease", selectedDisease)
            startActivity(toInfoIntent)
        }
    }

    // back 버튼 더블 클릭 시, App 종료
    var backPressedTime: Long = 0
    override fun onBackPressed() {
        if (backPressedTime + 3000 > System.currentTimeMillis()) {
            super.onBackPressed()
            finish()
        }
        else {
            Toast.makeText(
                this@MainActivity,
                "한 번 더 뒤로가기 버튼을 누르면 앱을 종료합니다.",
                Toast.LENGTH_LONG
            ).show()
        }
        backPressedTime = System.currentTimeMillis()
    }
}
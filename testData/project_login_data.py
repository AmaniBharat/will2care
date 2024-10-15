class logindata:

    individual_username_data = 'vamsigrandhe123@gmail.com'

    individual_password_data = '1234567'

    business_username_data = '9700440711'

    business_password_data = '123456'
###############individual forgot password email data###########

    individual_log_forgot_email_data = 'amanibharat@gmail.com'

###############individual profile details###########

    individual_dob_data = '11/07/1993'

    individual_aadhar_data = '8117 8659 4480'

    individual_spouse_data = 'padma'

    individual_father_data = 'peraiah'

    individual_zip_data = '500001'

    individual_line2_data = 'Tarnaka'

    individual_line3_data = 'Hyderabad'

########################individual beneficiary1 details#####################

    individual_ben1_fname_data = 'vasu'

    individual_ben1_lname_data = 'grandhe'

    individual_ben1_dob_data = '23/7/1991'

    individual_ben1_email_data = 'amanibharat@gmail.com'

    individual_ben1_mobile_data = '7989872552'

    individual_ben1_zip_data = '523332'

    individual_ben1_line2_data = 'K.G.Road'

    individual_ben1_line3_data = 'Dornala'

##################adding 2nd beneficiary details##########

    individual_ben2_fname_data = 'Gayathrii'

    individual_ben2_lname_data = 'Grandhe'

    individual_ben2_dob_data = '11/7/1992'

    individual_ben2_email_data = 'amanibharat@gmail.com'

    individual_ben2_mobile_data = '7989872552'

#########################adding 3rd beneficiary############

    individual_ben3_fname_data = 'swechaa'

    individual_ben3_lname_data = 'Grandhe'

    individual_ben3_dob_data = '2/6/2022'

    individual_ben3_email_data = 'amanibharat@gmail.com'

    individual_ben3_mobile_data = '7989872552'

    individual_ben3_zip_data = '500002'

    individual_ben3_line2_data = 'Panjagutta'

    individual_ben3_line3_data = 'Hyderabad'
#########################ben4 details###########

    individual_ben4_fname_data = 'Chinmayi'

    individual_ben4_lname_data = 'Maddirala'

    individual_ben4_dob_data = '30/9/2023'

    individual_ben4_email_data = 'amanibharat@gmail.com'

    individual_ben4_mobile_data = '7989872552'

#######################new gaurdian details Data#############

    individual_gau1_fname_data = 'Pranay'

    individual_gau1_lname_data = 'Maddirala'

    individual_gau1_email_data = 'amanibharat@gmail.com'

    individual_gau1_mobile_data = '7989872552'

    individual_gau1_zip_data = '500003'

    individual_gau1_state_data = 'Telangana'

    individual_gau1_country_data = 'India'

    individual_gau1_address_data = 'Narayanaguda'

####################Editing OF BENEFICIARY DETAILS################

    individual_ben1_edit_fname = 'Vakeel'





class loginselectors:

########################## individual login selectors ######################

    individual_dropdown_id = 'loginButton'

    individual_user_id = 'email'

    individual_password_id = 'password'

    individual_login_xpath = '//*[@id="site-login-form"]/div[3]/div[1]/button'
######################## forgot password selectos############

    individual_login_forgot_click_xpath = '//*[@id="site-login-form"]/div[3]/div[2]/a'

    individual_log_email_select_xpath = '//*[@id="email"]'

    individual_log_send_pw_xpath = '//*[@id="site-forgot-password-form"]/button'



########################individual profile form############
    invidual_dob_id  = 'dob'

    individual_gender_id = 'gender'

    individual_new_will_edit = '/html/body/div/div/div[2]/div[3]/div[1]/div/div[2]/a'

################################business login selectors##################

    business_user_id = 'email'

    business_password = 'password'

    business_xpath = '//*[@id="site-login-form"]/div[3]/div[1]/button'

    individual_aadhar_change_xpath = '//*[@id="change-aadhaar"]'

    invidual_aadhar_update_id = 'change_adhar'

    individual_aadhar_update_click = '//*[@id="change-aadhaar-testator-form"]/div[3]/button[1]'

    individual_religion_xpath = '//*[@id="religion"]'

    individual_marriage_deselect = '//*[@id="testator-details-form"]/div[4]/div/div[1]/div/div/label[2]'

    individual_status_married_xpath = '//*[@id="testator-details-form"]/div[4]/div/div[1]/div/div/label[1]'

    individual_spouse_id = 'spouse_name'

    individual_father_id = 'fathers_name'

    individual_zip_id = 'zip_code'

    individual_line2_id = 'address_line_two'

    individual_line3_id = 'address_line_three'

    individual_sandc_xpath = '//*[@id="savecount"]'

##################beneficiary page details##############

    individual_bclick_xpath = '/html/body/div/div[1]/div[2]/div[2]/ul/li[3]/a'

    individual_bfname_id = 'beneficiary_firstname'

    individual_blnmae_id = 'beneficiary_lastname'

    individual_bf_dob_id = 'beneficiary_dob'

    individual_bf_gender_xpath = '//*[@id="beneficiary_gender"]'

    individual_bf_email_id = 'beneficiary_email'

    individual_bf_mobile_id = 'beneficiary_mobile'

    individual_bf_zip_id = 'beneficiary_zip_code'

    individual_bf_line2_id = 'beneficiary_address_line_two'

    individual_bf_line3_id = 'beneficiary_address_line_three'

    individual_bf_sanewb_id = 'addNew'

########################same as testator address ###################

    individual_bf_stestator_id = 'same-as-testators'

##############Gaurdian existing Deatils###############


    individual_gaurdian_existing_confirm = '/html/body/div[3]/div[7]/button'

    individual_gaurdian_select = '//*[@id="guardian-table-body"]/tr[1]/td[1]/input'

    individual_gaurdian_save = '//*[@id="guardianModal"]/div/div/div[3]/button[1]'

###################new gaurdian details###################

    individual_gaurdian_new_click_xpath = '/html/body/div[3]/div[7]/div/button'

    individual_gaurdian_firstname_id = 'firstname'

    individual_gaurdian_lastname_id = 'lastname'

    individual_gaurdian_relation_testator_id = 'testator_relationship'

    individual_gaurdian_gender_id = 'gender'

    individual_gaurdian_email_id = 'email'

    individual_gaurdian_mobile_id = 'mobile'

    individual_gaurdian_zip_id = 'zip_code'

    individual_gaurdian_state_id = 'state'

    individual_gaurdian_country_id = 'country'

    individual_gaurdian_address_id = 'address_line_one'

    individual_gaurdian_save_click_xpath = '//*[@id="add-guardian-detail-form"]/div[3]/div[2]/button'

#########################Editig OF BENEFICIARY DETAILS####################

    idividual_ben_edit_click = '//*[@id="beneficiary-325"]/div/i[1]'

    individual_ben1_edit_fname_id = 'firstname'

    individual_ben_edit_update_xpath = '//*[@id="edit-beneficiary-detail-form"]/div[3]/button[1]'

#############################deleting the beneficiary#############

    individual_ben_delete_click_xpath = '//*[@id="beneficiary-325"]/div/i[2]'

    individual_ben_delete_cancel_xpath = '/html/body/div[3]/div[7]/button'

    individual_ben_delete_button_xpath = '/html/body/div[3]/div[7]/div/button'

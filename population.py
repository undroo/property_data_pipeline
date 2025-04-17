class Population:
    def __init__(self, df):
        """Initialize Population class with a dataframe containing exactly one row of data.
        
        Args:
            df (pd.DataFrame): DataFrame containing census data
            
        Raises:
            ValueError: If DataFrame is empty or contains more than one row
        """
        if df.empty:
            raise ValueError("DataFrame is empty")
        if len(df) > 1:
            raise ValueError("DataFrame contains more than one row")
        
        self.df = df

    def _get_value(self, column):
        """Helper method to safely extract a single value from a column.
        
        Args:
            column (str): Column name to extract value from
            
        Returns:
            float: The numeric value from the specified column
        """
        return float(self.df[column].iloc[0])

    def get_total_population(self):
        """Returns total population broken down by gender"""
        return {
            'total': self._get_value('Tot_P_P'),
            'male': self._get_value('Tot_P_M'),
            'female': self._get_value('Tot_P_F')
        }

    def get_age_distribution(self):
        """Returns population distribution by age groups"""
        age_groups = {
            '0-4': {
                'total': self._get_value('Age_0_4_yr_P'),
                'male': self._get_value('Age_0_4_yr_M'),
                'female': self._get_value('Age_0_4_yr_F')
            },
            '5-14': {
                'total': self._get_value('Age_5_14_yr_P'),
                'male': self._get_value('Age_5_14_yr_M'),
                'female': self._get_value('Age_5_14_yr_F')
            },
            '15-19': {
                'total': self._get_value('Age_15_19_yr_P'),
                'male': self._get_value('Age_15_19_yr_M'),
                'female': self._get_value('Age_15_19_yr_F')
            },
            '20-24': {
                'total': self._get_value('Age_20_24_yr_P'),
                'male': self._get_value('Age_20_24_yr_M'),
                'female': self._get_value('Age_20_24_yr_F')
            },
            '25-34': {
                'total': self._get_value('Age_25_34_yr_P'),
                'male': self._get_value('Age_25_34_yr_M'),
                'female': self._get_value('Age_25_34_yr_F')
            },
            '35-44': {
                'total': self._get_value('Age_35_44_yr_P'),
                'male': self._get_value('Age_35_44_yr_M'),
                'female': self._get_value('Age_35_44_yr_F')
            },
            '45-54': {
                'total': self._get_value('Age_45_54_yr_P'),
                'male': self._get_value('Age_45_54_yr_M'),
                'female': self._get_value('Age_45_54_yr_F')
            },
            '55-64': {
                'total': self._get_value('Age_55_64_yr_P'),
                'male': self._get_value('Age_55_64_yr_M'),
                'female': self._get_value('Age_55_64_yr_F')
            },
            '65-74': {
                'total': self._get_value('Age_65_74_yr_P'),
                'male': self._get_value('Age_65_74_yr_M'),
                'female': self._get_value('Age_65_74_yr_F')
            },
            '75-84': {
                'total': self._get_value('Age_75_84_yr_P'),
                'male': self._get_value('Age_75_84_yr_M'),
                'female': self._get_value('Age_75_84_yr_F')
            },
            '85+': {
                'total': self._get_value('Age_85ov_P'),
                'male': self._get_value('Age_85ov_M'),
                'female': self._get_value('Age_85ov_F')
            }
        }
        return age_groups

    def get_indigenous_statistics(self):
        """Returns indigenous population statistics"""
        return {
            'total': {
                'total': self._get_value('Indigenous_P_Tot_P'),
                'male': self._get_value('Indigenous_P_Tot_M'),
                'female': self._get_value('Indigenous_P_Tot_F')
            },
            'aboriginal': {
                'total': self._get_value('Indigenous_psns_Aboriginal_P'),
                'male': self._get_value('Indigenous_psns_Aboriginal_M'),
                'female': self._get_value('Indigenous_psns_Aboriginal_F')
            },
            'torres_strait_islander': {
                'total': self._get_value('Indig_psns_Torres_Strait_Is_P'),
                'male': self._get_value('Indig_psns_Torres_Strait_Is_M'),
                'female': self._get_value('Indig_psns_Torres_Strait_Is_F')
            },
            'both': {
                'total': self._get_value('Indig_Bth_Abor_Torres_St_Is_P'),
                'male': self._get_value('Indig_Bth_Abor_Torres_St_Is_M'),
                'female': self._get_value('Indig_Bth_Abor_Torres_St_Is_F')
            }
        }

    def get_education_attendance(self):
        """Returns statistics about educational institution attendance by age group"""
        return {
            '0-4': {
                'total': self._get_value('Age_psns_att_educ_inst_0_4_P'),
                'male': self._get_value('Age_psns_att_educ_inst_0_4_M'),
                'female': self._get_value('Age_psns_att_educ_inst_0_4_F')
            },
            '5-14': {
                'total': self._get_value('Age_psns_att_educ_inst_5_14_P'),
                'male': self._get_value('Age_psns_att_educ_inst_5_14_M'),
                'female': self._get_value('Age_psns_att_educ_inst_5_14_F')
            },
            '15-19': {
                'total': self._get_value('Age_psns_att_edu_inst_15_19_P'),
                'male': self._get_value('Age_psns_att_edu_inst_15_19_M'),
                'female': self._get_value('Age_psns_att_edu_inst_15_19_F')
            },
            '20-24': {
                'total': self._get_value('Age_psns_att_edu_inst_20_24_P'),
                'male': self._get_value('Age_psns_att_edu_inst_20_24_M'),
                'female': self._get_value('Age_psns_att_edu_inst_20_24_F')
            },
            '25+': {
                'total': self._get_value('Age_psns_att_edu_inst_25_ov_P'),
                'male': self._get_value('Age_psns_att_edu_inst_25_ov_M'),
                'female': self._get_value('Age_psns_att_edu_inst_25_ov_F')
            }
        }

    def get_education_completion(self):
        """Returns statistics about highest level of school completed"""
        return {
            'year_12': {
                'total': self._get_value('High_yr_schl_comp_Yr_12_eq_P'),
                'male': self._get_value('High_yr_schl_comp_Yr_12_eq_M'),
                'female': self._get_value('High_yr_schl_comp_Yr_12_eq_F')
            },
            'year_11': {
                'total': self._get_value('High_yr_schl_comp_Yr_11_eq_P'),
                'male': self._get_value('High_yr_schl_comp_Yr_11_eq_M'),
                'female': self._get_value('High_yr_schl_comp_Yr_11_eq_F')
            },
            'year_10': {
                'total': self._get_value('High_yr_schl_comp_Yr_10_eq_P'),
                'male': self._get_value('High_yr_schl_comp_Yr_10_eq_M'),
                'female': self._get_value('High_yr_schl_comp_Yr_10_eq_F')
            },
            'year_9': {
                'total': self._get_value('High_yr_schl_comp_Yr_9_eq_P'),
                'male': self._get_value('High_yr_schl_comp_Yr_9_eq_M'),
                'female': self._get_value('High_yr_schl_comp_Yr_9_eq_F')
            },
            'year_8_or_below': {
                'total': self._get_value('High_yr_schl_comp_Yr_8_belw_P'),
                'male': self._get_value('High_yr_schl_comp_Yr_8_belw_M'),
                'female': self._get_value('High_yr_schl_comp_Yr_8_belw_F')
            },
            'did_not_attend': {
                'total': self._get_value('High_yr_schl_comp_D_n_g_sch_P'),
                'male': self._get_value('High_yr_schl_comp_D_n_g_sch_M'),
                'female': self._get_value('High_yr_schl_comp_D_n_g_sch_F')
            }
        }

    def get_australian_citizen_status(self):
        """Returns statistics about Australian citizen status"""
        return {
            'total': self._get_value('Australian_citizen_P'),
            'male': self._get_value('Australian_citizen_M'),
            'female': self._get_value('Australian_citizen_F')
        }
class DwellingStructure:
    def __init__(self, df):
        """Initialize Income class with a dataframe containing exactly one row of data.
        
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

    def get_ownership_summary(self):
        """Returns summary of property ownership (owned outright vs mortgaged)"""
        return {
            'owned_outright': {
                'separate_house': self._get_value('O_OR_DS_Sep_house'),
                'semi_detached': self._get_value('O_OR_DS_SemiD_ro_or_tce_h_th'),
                'flat_apartment': self._get_value('O_OR_DS_Flat_apart'),
                'other_dwelling': self._get_value('O_OR_DS_Oth_dwell'),
                'not_stated': self._get_value('O_OR_DS_not_stated'),
                'total': self._get_value('O_OR_Total')
            },
            'owned_with_mortgage': {
                'separate_house': self._get_value('O_MTG_DS_Sep_house'),
                'semi_detached': self._get_value('O_MTG_DS_SemiD_ro_or_tce_h_th'),
                'flat_apartment': self._get_value('O_MTG_DS_Flat_apart'),
                'other_dwelling': self._get_value('O_MTG_DS_Oth_dwell'),
                'not_stated': self._get_value('O_MTG_DS_not_stated'),
                'total': self._get_value('O_MTG_Total')
            }
        }

    def get_rental_by_type(self):
        """Returns detailed breakdown of rental properties by landlord type"""
        return {
            'real_estate_agent': {
                'separate_house': self._get_value('R_RE_Agt_DS_Sep_house'),
                'semi_detached': self._get_value('R_RE_Ag_DS_SemD_ro_or_tc_h_th'),
                'flat_apartment': self._get_value('R_RE_Agt_DS_Flat_apart'),
                'other_dwelling': self._get_value('R_RE_Agt_DS_Oth_dwell'),
                'not_stated': self._get_value('R_RE_Agt_DS_not_stated'),
                'total': self._get_value('R_RE_Agt_Total')
            },
            'state_housing': {
                'separate_house': self._get_value('R_ST_h_auth_DS_Sep_house'),
                'semi_detached': self._get_value('R_ST_h_au_DS_SD_ro_or_tc_h_th'),
                'flat_apartment': self._get_value('R_ST_h_auth_DS_Flat_apart'),
                'other_dwelling': self._get_value('R_ST_h_auth_DS_Oth_dwell'),
                'not_stated': self._get_value('R_ST_h_auth_DS_not_stated'),
                'total': self._get_value('R_ST_h_auth_Total')
            },
            'community_housing': {
                'separate_house': self._get_value('R_Com_Hp_DS_Sp_ho'),
                'semi_detached': self._get_value('R_Com_Hp_DS_SD_ro_t_h_t'),
                'flat_apartment': self._get_value('R_Com_Hp_DS_Flt_apt'),
                'other_dwelling': self._get_value('R_Com_Hp_DS_Ot_dwel'),
                'not_stated': self._get_value('R_Com_Hp_DS_NS'),
                'total': self._get_value('R_Com_Hp_Total')
            },
            'private_landlord': {
                'separate_house': self._get_value('R_Psn_not_in_s_hh_DS_Sep_hous'),
                'semi_detached': self._get_value('R_P_not_in_s_h_DS_SD_ro_t_h_t'),
                'flat_apartment': self._get_value('R_P_not_in_s_hh_DS_Flat_apart'),
                'other_dwelling': self._get_value('R_Psn_not_in_s_hh_DS_Oth_dwel'),
                'not_stated': self._get_value('R_Psn_not_in_s_hh_DS_NS'),
                'total': self._get_value('R_Psn_not_in_s_hh_Total')
            },
            'other_landlord': {
                'separate_house': self._get_value('R_Ot_landld_typ_DS_Sep_house'),
                'semi_detached': self._get_value('R_O_LLd_typ_DS_SD_ro_tc_h_th'),
                'flat_apartment': self._get_value('R_Ot_LLd_typ_DS_Flat_apart'),
                'other_dwelling': self._get_value('R_Ot_landld_typ_DS_Oth_dwell'),
                'not_stated': self._get_value('R_Ot_landld_typ_DS_not_stated'),
                'total': self._get_value('R_Ot_landld_typ_Total')
            }
        }

    def get_rental_totals(self):
        """Returns total rental statistics by dwelling type"""
        return {
            'separate_house': self._get_value('R_Tot_DS_Sep_house'),
            'semi_detached': self._get_value('R_Tot_DS_SemiD_ro_or_tce_h_th'),
            'flat_apartment': self._get_value('R_Tot_DS_Flat_apart'),
            'other_dwelling': self._get_value('R_Tot_DS_Oth_dwell'),
            'not_stated': self._get_value('R_Tot_DS_not_stated'),
            'total': self._get_value('R_Tot_Total')
        }

    def get_dwelling_totals(self):
        """Returns total statistics for all dwelling types regardless of tenure"""
        return {
            'separate_house': self._get_value('Total_DS_Sep_house'),
            'semi_detached': self._get_value('Total_DS_SemiD_ro_or_tce_h_th'),
            'flat_apartment': self._get_value('Total_DS_Flat_apart'),
            'other_dwelling': self._get_value('Total_DS_Oth_dwell'),
            'not_stated': self._get_value('Total_DS_not_stated'),
            'total': self._get_value('Total_Total')
        }

    def get_other_tenure_types(self):
        """Returns statistics for other tenure types and not stated categories"""
        return {
            'other_tenure': {
                'separate_house': self._get_value('Oth_ten_type_DS_Sep_house'),
                'semi_detached': self._get_value('Oth_ten_ty_DS_SD_ro_tce_h_th'),
                'flat_apartment': self._get_value('Oth_ten_type_DS_Flat_apart'),
                'other_dwelling': self._get_value('Oth_ten_type_DS_Oth_dwell'),
                'not_stated': self._get_value('Oth_ten_type_DS_not_stated'),
                'total': self._get_value('Oth_ten_type_Total')
            },
            'tenure_not_stated': {
                'separate_house': self._get_value('Ten_type_NS_DS_Sep_house'),
                'semi_detached': self._get_value('Ten_ty_NS_DS_SD_ro_tce_h_t'),
                'flat_apartment': self._get_value('Ten_ty_NS_DS_Flat_apart'),
                'other_dwelling': self._get_value('Ten_type_NS_DS_Oth_dwell'),
                'not_stated': self._get_value('Ten_type_NS_DS_not_stated'),
                'total': self._get_value('Ten_type_NS_Total')
            }
        }
class Company:
    def __init__(self,
                 company_name_id,
                 url,
                 year_founded,
                 city,
                 state,
                 country,
                 zip_code,
                 full_time_employees,
                 company_type,
                 company_category,
                 revenue_source,
                 business_model,
                 social_impact,
                 description,
                 description_short,
                 source_count,
                 data_types,
                 example_uses,
                 data_impacts,
                 financial_info,
                 last_updated):
        self.company_name_id = company_name_id
        self.url = url
        self.year_founded = year_founded
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zip_code
        self.full_time_employees = full_time_employees
        self.company_type = company_type
        self.company_category = company_category
        self.revenue_source = revenue_source
        self.business_model = business_model
        self.social_impact = social_impact
        self.description = description
        self.description_short = description_short
        self.source_count = source_count
        self.data_types = data_types
        self.example_uses = example_uses
        self.data_impacts = data_impacts
        self.financial_info = financial_info
        self.last_updated = last_updated
        self

    def __repr__(self):
        return (
            'Company ('
            f'company_name_id: {self.company_name_id}, '
            f'year_founded: {self.year_founded}, '
            f'city: {self.city}, '
            f'state: {self.state}, '
            f'country: {self.country} ,'
            f'full_time_employees: {self.full_time_employees}'
            f'zip_code: {self.zip_code}'
            f'company_type: {self.company_type}'
            f'company_category: {self.company_category}'
            f'revenue_source: {self.revenue_source}'
            f'business_model: {self.business_model}'
            f'social_impact: {self.social_impact}'
            f'description: {self.description}'
            f'description_short: {self.description_short}'
            f'source_count: {self.source_count}'
            f'data_types: {self.data_types}'
            f'example_uses: {self.example_uses}'
            f'financial_info: {self.financial_info}'
            f'last_updated: {self.last_updated})'
        )

    def to_json(self):
        return self.__dict__

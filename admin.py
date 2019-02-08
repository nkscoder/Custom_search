 def get_search_results(self, request, queryset, search_term):
      
        queryset, use_distinct = super(CustomUserAdmin, self).get_search_results(request, queryset, search_term)
  
        try:
            
            queryset |= self.model.objects.filter(pk__in=UserEmail.objects.filter(email__icontains=search_term).values_list("user_id",flat=True))
        except ValueError:
    
            pass
        else:

            pattern = re.compile('^\d{10}$')
            result = pattern.match(search_term)
            if not result is  None:
                queryset |= self.model.objects.filter(pk__in=MobileNumber.objects.filter(mobile__icontains=search_term).values_list("user_id",flat=True))
           
         
        return queryset, use_distinct

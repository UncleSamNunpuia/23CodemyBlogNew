from django import forms
from .models import InkhawmInchhiarnaBlogNew


class InkhawmInchhiarnaBlogNewForm(forms.ModelForm):
    class Meta:
        model = InkhawmInchhiarnaBlogNew
        # fields = ['inkhawm_ni']
        fields = ['inkhawm_ni',
                  'mat_grp_cmt', 'mat_members',
                  'marka_grp_cmt', 'marka_members',
                  'luka_grp_cmt', 'luka_members',
                  'johan_grp_cmt', 'johan_members', 'leader_secy',
                  'chhimtu1', 'chhimtu1_no',
                  'chhimtu2', 'chhimtu2_no',
                  'chhimtu3', 'chhimtu3_no',
                  'posted_by', 'total']
        #

from rest_framework import serializers

from B_01BaseApp.models import InkhawmInchhiarnaBlogNew


class InkhawmInchhiarnaBlogNewSerializer(serializers.ModelSerializer):
    # to make the instnance mthod or a proprty diplayed with alias
    # my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = InkhawmInchhiarnaBlogNew
        fields = [
            "pk",
            "inkhawm_ni",
            "mat_grp_cmt",
            "mat_members",
            "marka_grp_cmt",
            "marka_members",
            "luka_grp_cmt",
            "luka_members",
            "johan_grp_cmt",
            "johan_members",
            "leader_secy",
            "chhimtu1",
            "chhimtu1_no",
            "chhimtu2",
            "chhimtu2_no",
            "chhimtu3",
            "chhimtu3_no",
            "created_at",
            "updated_at",
            "posted_by",
            "total"
            # fields = [
            #     "inkhawm_ni",
            #     "mat_grp_cmt",
            #     'mat_members',
            #     'marka_grp_cmt',
            #     'marka_members',
            #     'luka_grp_cmt',
            #     'luka_members',
            #     'johan_grp_cmt',
            #     'johan_members',
            #     'leader_secy',
            #     'chhimtu1',
            #     'chhimtu1_no',
            #     'chhimtu2',
            #     'chhimtu2_no',
            #     'chhimtu3',
            #     'chhimtu3_no',
            #     'created_at',
            #     'updated_at',
            #     'posted_by',
            #     'total'
        ]

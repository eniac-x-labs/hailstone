# encoding=utf-8

import json
import uuid

from common.helpers import (
    ok_json,
    error_json
)
from airdrop.models import (
    AirdropUser,
    PointsRecord,
    ProjectInterAction,
    Questions,
    Period
)


# @check_api_token
def get_reward_info(request):
    params = json.loads(request.body.decode())
    address = params.get("address", None)
    if address is None:
        return error_json("address params is empty", 4000)
    pr_list = Period.objects.all().order_by("-id")
    pr_response = []
    for pr in pr_list:
        pr_response.append(pr.as_dict(address=address))
    return ok_json(pr_response)


# @check_api_token
def get_project_interactions(request):
    params = json.loads(request.body.decode())
    language = params.get("language", "en")
    pi_lists = ProjectInterAction.objects.filter(language=language).order_by("id").all()
    projects_ret_lists = []
    social_ret_list = []
    for pl in pi_lists:
        if pl.project_type in ["Project"]:
            projects_ret_lists.append(pl.as_dict())
        else:
            social_ret_list.append(pl.as_dict())
    data = {
        "project": projects_ret_lists,
        "social": social_ret_list
    }
    return ok_json(data)


# @check_api_token
def get_questions(request):
    params = json.loads(request.body.decode())
    language = params.get("language", "en")
    question_lists = Questions.objects.filter(language=language).order_by("id").all()
    question_ret_lists = []
    for ql in question_lists:
        question_ret_lists.append(ql.as_dict())
    return ok_json(question_ret_lists)


# @check_api_token
def get_invite_code_by_address(request):
    params = json.loads(request.body.decode())
    address = params.get("address", None)
    if address is not None:
        airdrop_user = AirdropUser.objects.filter(address__icontains=address).first()
        if airdrop_user is not None:
            data = {
                "invite_code": airdrop_user.invite_code,
            }
            return ok_json(data)
        else:
            return error_json("address is not exist", 4000)
    else:
        return error_json("address is none", 4000)


# @check_api_token
def submit_invite_info(request):
    params = json.loads(request.body.decode())
    address = params.get("address", None)
    invite_code = params.get("invite_code", None)
    if address is None or invite_code is None:
        return error_json("address or invite_code params is empty", 4000)
    invite_user = AirdropUser.objects.filter(invite_code=invite_code).first()
    if invite_user is None:
        return error_json("This user is not exist", 4000)
    address_user = AirdropUser.objects.filter(address__icontains=address).first()
    if address_user is not None:
        return error_json("address exist in system", 4000)
    AirdropUser.objects.create(
        invite_code=uuid.uuid4(),
        invite_me_uuid=invite_user.uuid,
        address=address
    )
    if invite_user.points < 10:
        invite_user.points = invite_user.points + 2
        invite_user.save()
        PointsRecord.objects.create(
            user=invite_user,
            address=invite_user.address,
            type='Invite',
            points=2
        )
    return ok_json({})


# @check_api_token
def get_points_by_address(request):
    params = json.loads(request.body.decode())
    address = params.get("address", None)
    if address is None:
        return error_json("address is empty", 4000)
    airdrop_user = AirdropUser.objects.filter(address__icontains=address).first()
    if airdrop_user is not None:
        return ok_json(airdrop_user.as_dict())
    else:
        return error_json("No this user address points", 4000)


# @check_api_token
def get_points_record_by_address(request):
    params = json.loads(request.body.decode())
    address = params.get("address", None)
    if address is None:
        return error_json("address is empty", 4000)
    page = params.get('page', 1)
    page_size = params.get('page_size', 20)
    start = (page - 1) * page_size
    end = start + page_size
    points = PointsRecord.objects.filter(address__icontains=address).order_by("-id")[start:end]
    total = PointsRecord.objects.filter(address__icontains=address).order_by("-id").count()
    point_list = []
    for point in points:
        point_list.append(point.as_dict())
    data = {
        "total": total,
        "points": point_list,
    }
    return ok_json(data)

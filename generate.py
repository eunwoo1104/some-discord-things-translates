import json


permission_translates = {
    "kick_members": "멤버 추방하기",
    "ban_members": "멤버 차단하기",
    "administrator": "관리자",
    "manage_channels": "채널 관리하기",
    "manage_guild": "서버 관리하기",
    "add_reactions": "반응 추가하기",
    "view_audit_log": "감사 로그 보기",
    "priority_speaker": "우선 발언권",
    "stream": "영상",
    "read_messages": "채널 보기",
    "view_channel": "채널 보기",  # is actually an alias
    "send_messages": "메시지 보내기",
    "send_tts_messages": "텍스트 음성 변환 메시지 전송",
    "manage_messages": "메시지 관리",
    "embed_links": "링크 첨부",
    "attach_files": "파일 첨부",
    "read_message_history": "메시지 기록 보기",
    "mention_everyone": "@everyone, @here, 모든 역할 맨션하기",
    "external_emojis": "외부 이모티콘 사용",
    "use_external_emojis": "외부 이모티콘 사용",  # is actually an alias
    "view_guild_insights": "서버 인사이트 보기",
    "connect": "연결",
    "speak": "말하기",
    "mute_members": "멤버들의 마이크 음소거하기",
    "deafen_members": "멤버의 헤드셋 음소거하기",
    "move_members": "멤버 이동",
    "use_voice_activation": "음성 감지 사용",
    "change_nickname": "별명 변경하기",
    "manage_nicknames": "별명 관리하기",
    "manage_roles": "역할 관리하기",
    "manage_permissions": "권한 관리하기",
    "manage_webhooks": "웹후크 관리하기",
    "manage_emojis": "이모티콘 및 스티커 관리",
    "use_slash_commands": "빗금 명령어 사용",
    "request_to_speak": "발언권 요청하기"
}


rtc_region_translates = {
    "amsterdam": "암스테르담",
    "brazil": "브라질",
    "dubai": "두바이",
    "eu_central": "중앙유럽",
    "eu_west": "서유럽",
    "europe": "유럽",
    "frankfurt": "프랑크푸르트",
    "hongkong": "홍콩",
    "india": "인도",
    "japan": "일본",
    "london": "런던",
    "russia": "러시아",
    "singapore": "싱가포르",
    "southafrica": "남아프리카",
    "south_korea": "대한민국",
    "us_central": "미국 중부",
    "us_east": "미국 동부",
    "us_south": "미국 남부",
    "vip_amsterdam": "VIP 암스테르담",
    "vip_us_east": "VIP 미국 동부",
    "vip_us_west": "VIP 미국 서부"
}


verification_level_translates = {
    "none": "없음",
    "low": "낮음",
    "medium": "중간",
    "high": "높음",
    "extreme": "매우 높음",
    "table_flip": "높음",
    "double_table_flip": "매우 높음",
    "very_high": "매우 높음",
}


verification_desc_translates = {
    "none": "제한 없음",
    "low": "이메일 인증이 완료된 Discord 계정이어야 해요.",
    "medium": "또한, Discord에 가입한 지 5분이 지나야 돼요.",
    "high": "또한, 이 서버의 멤버가 된 지 10분이 지나야 돼요.",
    "extreme": "휴대폰 인증이 완료된 Discord 계정이어야 해요.",
    "table_flip": "또한, 이 서버의 멤버가 된 지 10분이 지나야 돼요.",
    "double_table_flip": "휴대폰 인증이 완료된 Discord 계정이어야 해요.",
    "very_high": "휴대폰 인증이 완료된 Discord 계정이어야 해요.",
}

with open("jsons/permission_translates.json", "w", encoding="UTF-8") as f:
    json.dump(permission_translates, f, indent=4, ensure_ascii=False)
with open("jsons/rtc_region_translates.json", "w", encoding="UTF-8") as f:
    json.dump(rtc_region_translates, f, indent=4, ensure_ascii=False)
with open("jsons/verification_level_translates.json", "w", encoding="UTF-8") as f:
    json.dump(verification_level_translates, f, indent=4, ensure_ascii=False)
with open("jsons/verification_description_translates.json", "w", encoding="UTF-8") as f:
    json.dump(verification_desc_translates, f, indent=4, ensure_ascii=False)

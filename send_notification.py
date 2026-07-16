import os

from linebot.v3.messaging import (
    ApiClient,
    Configuration,
    MessagingApi,
    PushMessageRequest,
    TextMessage,
)


def main():
    channel_access_token = os.environ.get(
        "LINE_CHANNEL_ACCESS_TOKEN"
    )

    line_user_id = os.environ.get(
        "LINE_USER_ID"
    )

    if not channel_access_token:
        raise RuntimeError(
            "LINE_CHANNEL_ACCESS_TOKENが設定されていません。"
        )

    if not line_user_id:
        raise RuntimeError(
            "LINE_USER_IDが設定されていません。"
        )

    configuration = Configuration(
        access_token=channel_access_token
    )

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)

        line_bot_api.push_message(
            PushMessageRequest(
                to=line_user_id,
                messages=[
                    TextMessage(
                        text="カフェタッチができる時間になりました。"
                    )
                ]
            )
        )

    print("プッシュ送信成功")


if __name__ == "__main__":
    main()

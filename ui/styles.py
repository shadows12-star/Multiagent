import streamlit as st


def inject_global_css():
    st.markdown(
        """
        <style>
        :root {
            --bd-green: #006A4E;
            --bd-green-dark: #004D3A;
            --bd-red: #F42A41;
            --surface: #FFFFFF;
            --surface-soft: #F7F9F8;
            --text: #17211D;
            --muted: #66736D;
            --border: #E1E7E4;
        }

        .stApp {
            background: #F7F9F8;
            color: var(--text);
        }

        [data-testid="stHeader"] {
            background: rgba(247,249,248,.92);
        }

        [data-testid="stSidebar"] {
            background: #FFFFFF;
            border-right: 1px solid var(--border);
        }

        [data-testid="stSidebarNav"] span {
            font-weight: 600;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 6rem;
        }

        h1, h2, h3, h4 {
            letter-spacing: -0.02em;
        }

        .brand-wrap {
            display: flex;
            align-items: center;
            gap: .7rem;
            padding: .35rem 0 1rem 0;
        }

        .brand-mark {
            width: 42px;
            height: 42px;
            border-radius: 13px;
            display: grid;
            place-items: center;
            font-size: 1.35rem;
            background: #E8F4EF;
        }

        .brand-title {
            font-size: 1rem;
            font-weight: 800;
            color: #12332A;
            line-height: 1.15;
        }

        .brand-subtitle {
            font-size: .73rem;
            color: var(--muted);
            margin-top: .2rem;
        }

        .tool-mini {
            display: flex;
            align-items: center;
            gap: .65rem;
            padding: .65rem .7rem;
            border: 1px solid var(--border);
            border-radius: 12px;
            margin: .45rem 0;
            background: #FAFCFB;
        }

        .tool-mini span {
            font-size: 1.05rem;
        }

        .tool-mini b {
            font-size: .82rem;
            display: block;
            color: #26342F;
        }

        .tool-mini small {
            color: #16855D;
            font-size: .7rem;
        }

        .sidebar-footer {
            margin-top: 1.25rem;
            display: flex;
            align-items: center;
            gap: .6rem;
            padding: .8rem;
            border-radius: 12px;
            background: #F3F8F6;
            font-size: .8rem;
        }

        .online-dot {
            width: 9px;
            height: 9px;
            background: #25A66A;
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 0 4px rgba(37,166,106,.12);
        }

        .eyebrow {
            display: inline-flex;
            gap: .45rem;
            align-items: center;
            font-size: .78rem;
            font-weight: 700;
            color: var(--bd-green);
            background: #E8F4EF;
            border: 1px solid #CEE8DD;
            border-radius: 999px;
            padding: .35rem .65rem;
            margin-bottom: .8rem;
        }

        .hero-title {
            font-size: clamp(2rem, 4vw, 3.4rem);
            line-height: 1.05;
            font-weight: 850;
            color: #14221D;
            margin-bottom: .8rem;
            letter-spacing: -0.045em;
        }

        .hero-copy {
            max-width: 780px;
            color: var(--muted);
            font-size: 1.03rem;
            line-height: 1.65;
            margin-bottom: 1.6rem;
        }

        .header-row {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .badge-row {
            display: flex;
            gap: .5rem;
            flex-wrap: wrap;
            justify-content: flex-end;
        }

        .pill {
            display: inline-flex;
            align-items: center;
            gap: .35rem;
            border: 1px solid var(--border);
            background: #FFFFFF;
            border-radius: 999px;
            padding: .4rem .7rem;
            font-size: .75rem;
            font-weight: 700;
            color: #35433E;
        }

        .suggestion-card, .source-card, .architecture-card, .history-card {
            border: 1px solid var(--border);
            background: #FFFFFF;
            border-radius: 18px;
            padding: 1.1rem 1.15rem;
            box-shadow: 0 6px 18px rgba(33, 57, 47, .035);
        }

        .suggestion-card {
            min-height: 145px;
        }

        .card-icon {
            width: 38px;
            height: 38px;
            border-radius: 11px;
            background: #EEF7F3;
            display: grid;
            place-items: center;
            font-size: 1.05rem;
            margin-bottom: .75rem;
        }

        .card-title {
            font-weight: 800;
            color: #20302A;
            margin-bottom: .35rem;
        }

        .card-copy {
            color: var(--muted);
            font-size: .86rem;
            line-height: 1.45;
        }

        .tool-badge {
            display: inline-flex;
            align-items: center;
            border: 1px solid #D8E7E1;
            border-radius: 999px;
            padding: .28rem .55rem;
            margin: 0 .35rem .45rem 0;
            font-size: .72rem;
            font-weight: 750;
            background: #F4FAF7;
            color: #19694F;
        }

        [data-testid="stChatMessage"] {
            background: #FFFFFF;
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: .25rem .65rem;
            box-shadow: 0 5px 14px rgba(20, 47, 37, .025);
        }

        [data-testid="stChatInput"] {
            border-radius: 16px;
        }

        .chat-note {
            text-align: center;
            color: var(--muted);
            font-size: .78rem;
            margin-top: .5rem;
        }

        .section-title {
            font-size: 1.65rem;
            font-weight: 850;
            color: #16251F;
            margin-bottom: .35rem;
        }

        .section-copy {
            color: var(--muted);
            max-width: 760px;
            line-height: 1.55;
            margin-bottom: 1.4rem;
        }

        .source-card h4 {
            margin: 0 0 .25rem 0;
        }

        .source-meta {
            color: var(--muted);
            font-size: .82rem;
            margin-bottom: .8rem;
        }

        .status-chip {
            display: inline-block;
            border-radius: 999px;
            padding: .26rem .55rem;
            font-size: .7rem;
            font-weight: 750;
            background: #EAF7F1;
            color: #147650;
        }

        .warning-box {
            border-left: 3px solid #D7A719;
            padding: .7rem .8rem;
            background: #FFF9E8;
            border-radius: 8px;
            font-size: .8rem;
            color: #6A5720;
            margin-top: .8rem;
        }

        .flow-node {
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1rem;
            text-align: center;
            background: #FFFFFF;
            font-weight: 800;
        }

        .flow-arrow {
            text-align: center;
            color: #769188;
            font-size: 1.4rem;
            padding: .2rem 0;
        }

        div.stButton > button {
            border-radius: 12px;
            border: 1px solid #DCE6E2;
            font-weight: 700;
        }

        div.stButton > button[kind="primary"] {
            background: var(--bd-green);
            border-color: var(--bd-green);
        }

        [data-testid="stExpander"] {
            border-radius: 13px;
            border-color: var(--border);
            background: #FBFCFC;
        }

        @media (max-width: 760px) {
            .block-container {
                padding-top: 1.2rem;
            }

            .header-row {
                display: block;
            }

            .badge-row {
                justify-content: flex-start;
                margin-top: .8rem;
            }

            .hero-title {
                font-size: 2.2rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

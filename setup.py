from pathlib import Path

FILES = {}

FILES["settings.gradle.kts"] = r"""
pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "YTPlayer"
include(":app")
"""

FILES["build.gradle.kts"] = r"""
plugins {
    id("com.android.application") version "8.5.2" apply false
    id("org.jetbrains.kotlin.android") version "2.0.21" apply false
}
"""

FILES["gradle.properties"] = r"""
org.gradle.jvmargs=-Xmx3g -Dfile.encoding=UTF-8
android.useAndroidX=true
kotlin.code.style=official
"""

FILES["app/build.gradle.kts"] = r"""
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.example.ytplayer"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.ytplayer"
        minSdk = 26
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
        ndk { abiFilters += listOf("armeabi-v7a", "arm64-v8a") }
    }

    packaging { jniLibs { useLegacyPackaging = true } }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions { jvmTarget = "17" }
}

dependencies {
    implementation("androidx.media3:media3-exoplayer:1.4.1")
    implementation("androidx.media3:media3-session:1.4.1")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.8.1")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-guava:1.8.1")
    implementation("io.github.junkfood02.youtubedl-android:library:0.17.4")
}
"""

FILES["app/src/main/AndroidManifest.xml"] = r"""
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" />
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher"
        android:label="YT Player"
        android:extractNativeLibs="true"
        android:usesCleartextTraffic="true"
        android:theme="@style/AppTheme">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTop"
            android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
            <intent-filter>
                <action android:name="android.intent.action.SEND" />
                <category android:name="android.intent.category.DEFAULT" />
                <data android:mimeType="text/plain" />
            </intent-filter>
        </activity>

        <service
            android:name=".PlaybackService"
            android:exported="true"
            android:foregroundServiceType="mediaPlayback">
            <intent-filter>
                <action android:name="androidx.media3.session.MediaSessionService" />
            </intent-filter>
        </service>
    </application>
</manifest>
"""

FILES["app/src/main/res/values/theme.xml"] = r"""
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="bg">#0F1115</color>

    <style name="AppTheme" parent="@android:style/Theme.Material.NoActionBar">
        <item name="android:windowBackground">@color/bg</item>
        <item name="android:statusBarColor">@color/bg</item>
        <item name="android:navigationBarColor">@color/bg</item>
        <item name="android:colorAccent">#7C4DFF</item>
    </style>
</resources>
"""

FILES["app/src/main/res/drawable/ic_launcher_background.xml"] = r"""
<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:aapt="http://schemas.android.com/aapt"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <path android:pathData="M0,0h108v108h-108z">
        <aapt:attr name="android:fillColor">
            <gradient
                android:startX="0"
                android:startY="0"
                android:endX="108"
                android:endY="108"
                android:type="linear">
                <item android:offset="0" android:color="#7C4DFF" />
                <item android:offset="1" android:color="#00BCD4" />
            </gradient>
        </aapt:attr>
    </path>
</vector>
"""

FILES["app/src/main/res/drawable/ic_launcher_foreground.xml"] = r"""
<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <path
        android:fillColor="#FFFFFF"
        android:pathData="M34,70a9,9 0 1,0 18,0a9,9 0 1,0 -18,0z" />
    <path
        android:fillColor="#FFFFFF"
        android:pathData="M50,34h5v36h-5z" />
    <path
        android:fillColor="#FFFFFF"
        android:pathData="M55,34L72,41L72,52L55,45z" />
</vector>
"""

FILES["app/src/main/res/drawable/ic_notification.xml"] = r"""
<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path
        android:fillColor="#FFFFFFFF"
        android:pathData="M12,3v10.55c-0.59,-0.34 -1.27,-0.55 -2,-0.55 -2.21,0 -4,1.79 -4,4s1.79,4 4,4 4,-1.79 4,-4V7h4V3h-6z" />
</vector>
"""

FILES["app/src/main/res/mipmap-anydpi/ic_launcher.xml"] = r"""
<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background" />
    <foreground android:drawable="@drawable/ic_launcher_foreground" />
</adaptive-icon>
"""

FILES["app/src/main/java/com/example/ytplayer/PlaybackService.kt"] = r"""
package com.example.ytplayer

import android.content.Intent
import androidx.media3.common.AudioAttributes
import androidx.media3.common.C
import androidx.media3.datasource.DefaultHttpDataSource
import androidx.media3.exoplayer.ExoPlayer
import androidx.media3.exoplayer.source.DefaultMediaSourceFactory
import androidx.media3.session.DefaultMediaNotificationProvider
import androidx.media3.session.MediaSession
import androidx.media3.session.MediaSessionService

class PlaybackService : MediaSessionService() {

    private var session: MediaSession? = null

    override fun onCreate() {
        super.onCreate()

        val http = DefaultHttpDataSource.Factory()
            .setUserAgent(
                "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 " +
                    "(KHTML, like Gecko) Chrome/124.0 Mobile Safari/537.36"
            )
            .setAllowCrossProtocolRedirects(true)

        val player = ExoPlayer.Builder(this)
            .setMediaSourceFactory(DefaultMediaSourceFactory(this).setDataSourceFactory(http))
            .setAudioAttributes(
                AudioAttributes.Builder()
                    .setContentType(C.AUDIO_CONTENT_TYPE_MUSIC)
                    .setUsage(C.USAGE_MEDIA)
                    .build(),
                true
            )
            .setHandleAudioBecomingNoisy(true)
            .setWakeMode(C.WAKE_MODE_NETWORK)
            .build()

        session = MediaSession.Builder(this, player).build()

        setMediaNotificationProvider(
            DefaultMediaNotificationProvider(this).apply {
                setSmallIcon(R.drawable.ic_notification)
            }
        )
    }

    override fun onGetSession(controllerInfo: MediaSession.ControllerInfo): MediaSession? = session

    override fun onTaskRemoved(rootIntent: Intent?) {
        val player = session?.player
        if (player == null || !player.playWhenReady) stopSelf()
    }

    override fun onDestroy() {
        session?.run {
            player.release()
            release()
        }
        session = null
        super.onDestroy()
    }
}
"""

FILES["app/src/main/java/com/example/ytplayer/MainActivity.kt"] = r"""
package com.example.ytplayer

import android.Manifest
import android.app.Activity
import android.app.AlertDialog
import android.content.ComponentName
import android.content.Intent
import android.graphics.Color
import android.graphics.Typeface
import android.graphics.drawable.ColorDrawable
import android.graphics.drawable.GradientDrawable
import android.os.Build
import android.os.Bundle
import android.text.TextUtils
import android.view.Gravity
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.EditText
import android.widget.FrameLayout
import android.widget.LinearLayout
import android.widget.ListView
import android.widget.TextView
import android.widget.Toast
import androidx.media3.common.MediaItem
import androidx.media3.common.MediaMetadata
import androidx.media3.common.PlaybackException
import androidx.media3.common.Player
import androidx.media3.session.MediaController
import androidx.media3.session.SessionToken
import com.yausername.youtubedl_android.YoutubeDL
import com.yausername.youtubedl_android.YoutubeDLRequest
import kotlinx.coroutines.Deferred
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.MainScope
import kotlinx.coroutines.async
import kotlinx.coroutines.cancel
import kotlinx.coroutines.guava.await
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import org.json.JSONArray
import org.json.JSONObject

class MainActivity : Activity() {

    private val scope = MainScope()
    private var controller: MediaController? = null
    private lateinit var ytReady: Deferred<Unit>

    private val names = mutableListOf<String>()
    private val urls = mutableListOf<String>()
    private var current = -1
    private var loading = false

    private lateinit var listAdapter: SongAdapter
    private lateinit var linkInput: EditText
    private lateinit var nameInput: EditText
    private lateinit var miniTitle: TextView
    private lateinit var miniSub: TextView
    private lateinit var playBtn: TextView

    private val prefs by lazy { getSharedPreferences("songs", MODE_PRIVATE) }

    private val MATCH = ViewGroup.LayoutParams.MATCH_PARENT
    private val WRAP = ViewGroup.LayoutParams.WRAP_CONTENT

    private val bg = Color.parseColor("#0F1115")
    private val card = Color.parseColor("#1A1D24")
    private val field = Color.parseColor("#252932")
    private val accent = Color.parseColor("#7C4DFF")
    private val playingBg = Color.parseColor("#2A2150")
    private val textMain = Color.WHITE
    private val textSub = Color.parseColor("#9AA0AC")

    private val playerListener = object : Player.Listener {
        override fun onIsPlayingChanged(isPlaying: Boolean) {
            if (isPlaying) loading = false
            updateMini()
        }

        override fun onPlaybackStateChanged(playbackState: Int) {
            if (playbackState == Player.STATE_ENDED) next()
            updateMini()
        }

        override fun onPlayerError(error: PlaybackException) {
            loading = false
            toast("재생 오류: ${error.errorCodeName}")
            updateMini()
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        if (Build.VERSION.SDK_INT >= 33) {
            requestPermissions(arrayOf(Manifest.permission.POST_NOTIFICATIONS), 1)
        }

        ytReady = scope.async(Dispatchers.IO) { YoutubeDL.getInstance().init(application) }

        loadSongs()
        buildUi()
        connectPlayer()
        handleIntent(intent)
    }

    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        handleIntent(intent)
    }

    // ---------- UI ----------

    private fun dp(v: Int) = (v * resources.displayMetrics.density).toInt()

    private fun round(color: Int, radius: Int) = GradientDrawable().apply {
        setColor(color)
        cornerRadius = dp(radius).toFloat()
    }

    private fun lp(w: Int, h: Int, top: Int = 0, weight: Float = 0f) =
        LinearLayout.LayoutParams(w, h, weight).apply { topMargin = dp(top) }

    private fun input(hintText: String) = EditText(this).apply {
        hint = hintText
        setHintTextColor(textSub)
        setTextColor(textMain)
        textSize = 15f
        setSingleLine()
        background = round(field, 12)
        setPadding(dp(14), dp(12), dp(14), dp(12))
    }

    private fun pill(label: String, color: Int) = TextView(this).apply {
        text = label
        setTextColor(Color.WHITE)
        textSize = 15f
        typeface = Typeface.DEFAULT_BOLD
        gravity = Gravity.CENTER
        background = round(color, 12)
        setPadding(dp(16), dp(13), dp(16), dp(13))
    }

    private fun ctrl(label: String, onClick: () -> Unit) = TextView(this).apply {
        text = label
        textSize = 24f
        setTextColor(Color.WHITE)
        gravity = Gravity.CENTER
        setPadding(dp(12), dp(8), dp(12), dp(8))
        setOnClickListener { onClick() }
    }

    private fun buildUi() {
        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setBackgroundColor(bg)
            setPadding(dp(16), dp(12), dp(16), dp(12))
        }

        root.addView(TextView(this).apply {
            text = "내 음악"
            textSize = 28f
            typeface = Typeface.DEFAULT_BOLD
            setTextColor(textMain)
        })
        root.addView(TextView(this).apply {
            text = "유튜브 링크를 등록하고 백그라운드에서 들어요"
            textSize = 13f
            setTextColor(textSub)
        })

        val form = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            background = round(card, 16)
            setPadding(dp(14), dp(14), dp(14), dp(14))
        }
        linkInput = input("유튜브 링크 붙여넣기")
        nameInput = input("이름")
        val addBtn = pill("＋ 등록", accent)
        form.addView(linkInput, lp(MATCH, WRAP))
        form.addView(nameInput, lp(MATCH, WRAP, 8))
        form.addView(addBtn, lp(MATCH, WRAP, 10))
        root.addView(form, lp(MATCH, WRAP, 14))

        listAdapter = SongAdapter()
        val list = ListView(this).apply {
            adapter = listAdapter
            divider = null
            dividerHeight = dp(8)
            setSelector(ColorDrawable(Color.TRANSPARENT))
            isVerticalScrollBarEnabled = false
        }
        val empty = TextView(this).apply {
            text = "등록된 곡이 없어요\n위에 링크와 이름을 입력해 보세요"
            setTextColor(textSub)
            textSize = 14f
            gravity = Gravity.CENTER
        }
        val frame = FrameLayout(this)
        frame.addView(list, FrameLayout.LayoutParams(MATCH, MATCH))
        frame.addView(empty, FrameLayout.LayoutParams(MATCH, MATCH))
        list.emptyView = empty
        root.addView(frame, lp(MATCH, 0, 14, 1f))

        val mini = LinearLayout(this).apply {
            orientation = LinearLayout.HORIZONTAL
            gravity = Gravity.CENTER_VERTICAL
            background = round(Color.parseColor("#22183F"), 18)
            setPadding(dp(16), dp(8), dp(6), dp(8))
        }
        val texts = LinearLayout(this).apply { orientation = LinearLayout.VERTICAL }
        miniTitle = TextView(this).apply {
            textSize = 15f
            typeface = Typeface.DEFAULT_BOLD
            setTextColor(textMain)
            setSingleLine()
            ellipsize = TextUtils.TruncateAt.END
        }
        miniSub = TextView(this).apply {
            textSize = 12f
            setTextColor(textSub)
        }
        texts.addView(miniTitle)
        texts.addView(miniSub)
        mini.addView(texts, lp(0, WRAP, 0, 1f))
        mini.addView(ctrl("⏮") { prev() })
        playBtn = ctrl("▶") { toggle() }
        mini.addView(playBtn)
        mini.addView(ctrl("⏭") { next() })
        root.addView(mini, lp(MATCH, WRAP, 12))

        setContentView(root)

        addBtn.setOnClickListener {
            val u = linkInput.text.toString().trim()
            val n = nameInput.text.toString().trim()
            if (!u.startsWith("http")) {
                toast("올바른 링크를 입력하세요")
                return@setOnClickListener
            }
            if (n.isEmpty()) {
                toast("이름을 입력하세요")
                return@setOnClickListener
            }
            names.add(n)
            urls.add(u)
            saveSongs()
            linkInput.text.clear()
            nameInput.text.clear()
            listAdapter.notifyDataSetChanged()
            toast("등록했어요")
        }

        list.setOnItemClickListener { _, _, i, _ -> play(i) }
        list.setOnItemLongClickListener { _, _, i, _ ->
            AlertDialog.Builder(this)
                .setTitle(names[i])
                .setMessage("이 곡을 삭제할까요?")
                .setPositiveButton("삭제") { _, _ -> removeSong(i) }
                .setNegativeButton("취소", null)
                .show()
            true
        }

        updateMini()
    }

    inner class SongAdapter : BaseAdapter() {
        override fun getCount() = names.size
        override fun getItem(position: Int): Any = names[position]
        override fun getItemId(position: Int) = position.toLong()

        override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
            val isCurrent = position == current
            val row = LinearLayout(this@MainActivity).apply {
                orientation = LinearLayout.HORIZONTAL
                gravity = Gravity.CENTER_VERTICAL
                background = round(if (isCurrent) playingBg else card, 14)
                setPadding(dp(12), dp(12), dp(14), dp(12))
            }
            val badge = TextView(this@MainActivity).apply {
                text = if (isCurrent) "♫" else "♪"
                textSize = 18f
                gravity = Gravity.CENTER
                setTextColor(if (isCurrent) Color.WHITE else accent)
                background = round(if (isCurrent) accent else Color.parseColor("#2B2F3A"), 20)
            }
            val title = TextView(this@MainActivity).apply {
                text = names[position]
                textSize = 16f
                setTextColor(textMain)
                setSingleLine()
                ellipsize = TextUtils.TruncateAt.END
            }
            row.addView(badge, LinearLayout.LayoutParams(dp(40), dp(40)))
            row.addView(title, lp(0, WRAP, 0, 1f).apply { leftMargin = dp(12) })
            return row
        }
    }

    // ---------- Player ----------

    private fun connectPlayer() {
        val token = SessionToken(this, ComponentName(this, PlaybackService::class.java))
        scope.launch {
            val c = MediaController.Builder(this@MainActivity, token).buildAsync().await()
            c.addListener(playerListener)
            controller = c
            updateMini()
        }
    }

    private fun play(i: Int) {
        if (i !in names.indices) return
        current = i
        loading = true
        updateMini()

        val link = urls[i]
        val name = names[i]

        scope.launch {
            try {
                ytReady.await()
                val streamUrl = withContext(Dispatchers.IO) {
                    val req = YoutubeDLRequest(link)
                    req.addOption("-f", "bestaudio/best")
                    req.addOption("--no-playlist")
                    YoutubeDL.getInstance().getInfo(req).url
                }
                if (streamUrl.isNullOrEmpty()) throw IllegalStateException("재생 주소를 찾지 못했어요")
                if (current != i) return@launch // 그 사이 다른 곡을 눌렀으면 무시

                val c = controller ?: throw IllegalStateException("플레이어 연결 중이에요. 잠시 후 다시 눌러 주세요")
                val item = MediaItem.Builder()
                    .setUri(streamUrl)
                    .setMediaMetadata(MediaMetadata.Builder().setTitle(name).build())
                    .build()
                c.setMediaItem(item)
                c.prepare()
                c.play()
            } catch (e: Exception) {
                loading = false
                toast("실패: ${e.message}")
                updateMini()
            }
        }
    }

    private fun toggle() {
        val c = controller ?: return
        if (current !in names.indices) {
            if (names.isNotEmpty()) play(0)
            return
        }
        when {
            c.mediaItemCount == 0 -> play(current)
            c.isPlaying -> c.pause()
            else -> c.play()
        }
    }

    private fun next() {
        if (names.isEmpty()) return
        play(if (current + 1 < names.size) current + 1 else 0)
    }

    private fun prev() {
        if (names.isEmpty()) return
        play(if (current > 0) current - 1 else names.size - 1)
    }

    private fun updateMini() {
        val playing = controller?.isPlaying == true
        val hasCurrent = current in names.indices
        miniTitle.text = if (hasCurrent) names[current] else "재생 중인 곡 없음"
        miniSub.text = when {
            loading -> "불러오는 중..."
            playing -> "재생 중"
            hasCurrent -> "일시정지"
            else -> "목록에서 곡을 선택하세요"
        }
        playBtn.text = if (playing) "⏸" else "▶"
        listAdapter.notifyDataSetChanged()
    }

    // ---------- Data ----------

    private fun removeSong(i: Int) {
        names.removeAt(i)
        urls.removeAt(i)
        when {
            i == current -> {
                current = -1
                controller?.stop()
                controller?.clearMediaItems()
            }
            i < current -> current--
        }
        saveSongs()
        updateMini()
        toast("삭제했어요")
    }

    private fun loadSongs() {
        val arr = JSONArray(prefs.getString("list", "[]"))
        for (k in 0 until arr.length()) {
            val o = arr.getJSONObject(k)
            names.add(o.getString("name"))
            urls.add(o.getString("url"))
        }
    }

    private fun saveSongs() {
        val arr = JSONArray()
        for (k in names.indices) {
            arr.put(JSONObject().put("name", names[k]).put("url", urls[k]))
        }
        prefs.edit().putString("list", arr.toString()).apply()
    }

    // 유튜브 앱에서 "공유 → YT Player"로 보내면 링크 자동 입력
    private fun handleIntent(i: Intent?) {
        if (i?.action != Intent.ACTION_SEND) return
        val text = i.getStringExtra(Intent.EXTRA_TEXT) ?: return
        val link = Regex("https?://\\S+").find(text)?.value ?: text
        linkInput.setText(link)
        val subject = i.getStringExtra(Intent.EXTRA_SUBJECT)
        if (!subject.isNullOrBlank() && nameInput.text.isBlank()) nameInput.setText(subject)
        toast("링크를 채웠어요. 이름을 확인하고 등록하세요")
    }

    private fun toast(msg: String) = Toast.makeText(this, msg, Toast.LENGTH_SHORT).show()

    override fun onDestroy() {
        controller?.removeListener(playerListener)
        controller?.release()
        scope.cancel()
        super.onDestroy()
    }
}
"""


def main():
    for path, content in FILES.items():
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content.lstrip("\n"), encoding="utf-8")
        print("created:", path)
    print("done:", len(FILES), "files")


if __name__ == "__main__":
    main()

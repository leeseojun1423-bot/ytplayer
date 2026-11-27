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
        versionCode = 2
        versionName = "2.0"
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
    implementation("io.github.junkfood02.youtubedl-android:ffmpeg:0.17.4")
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

FILES["app/src/main/java/com/example/ytplayer/Models.kt"] = r"""
package com.example.ytplayer

class Song(
    val id: String,
    var title: String,
    val url: String,
    var thumb: String = "",
    var fav: Boolean = false,
    var status: Int = READY
) {
    companion object {
        const val READY = 0
        const val DOWNLOADING = 1
        const val FAILED = 2
    }
}

class Row(
    val type: Int,
    val song: Song? = null,
    val label: String = "",
    val tag: String = ""
) {
    companion object {
        const val SONG = 0
        const val PLAYLIST = 1
        const val ACTION = 2
    }
}
"""

FILES["app/src/main/java/com/example/ytplayer/PlaybackService.kt"] = r"""
package com.example.ytplayer

import android.content.Intent
import androidx.media3.common.AudioAttributes
import androidx.media3.common.C
import androidx.media3.exoplayer.ExoPlayer
import androidx.media3.session.DefaultMediaNotificationProvider
import androidx.media3.session.MediaSession
import androidx.media3.session.MediaSessionService

class PlaybackService : MediaSessionService() {

    private var session: MediaSession? = null

    override fun onCreate() {
        super.onCreate()

        val player = ExoPlayer.Builder(this)
            .setAudioAttributes(
                AudioAttributes.Builder()
                    .setContentType(C.AUDIO_CONTENT_TYPE_MUSIC)
                    .setUsage(C.USAGE_MEDIA)
                    .build(),
                true
            )
            .setHandleAudioBecomingNoisy(true)
            .setWakeMode(C.WAKE_MODE_LOCAL)
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
import android.content.res.ColorStateList
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Color
import android.graphics.Typeface
import android.graphics.drawable.ColorDrawable
import android.graphics.drawable.GradientDrawable
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.os.Environment
import android.os.Handler
import android.os.Looper
import android.text.Editable
import android.text.TextUtils
import android.text.TextWatcher
import android.view.Gravity
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.EditText
import android.widget.FrameLayout
import android.widget.ImageView
import android.widget.LinearLayout
import android.widget.ListView
import android.widget.SeekBar
import android.widget.TextView
import android.widget.Toast
import androidx.media3.common.C
import androidx.media3.common.MediaItem
import androidx.media3.common.MediaMetadata
import androidx.media3.common.PlaybackException
import androidx.media3.common.PlaybackParameters
import androidx.media3.common.Player
import androidx.media3.session.MediaController
import androidx.media3.session.SessionToken
import com.yausername.ffmpeg.FFmpeg
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
import java.io.File
import java.net.URL
import kotlin.math.abs

class MainActivity : Activity() {

    private val scope = MainScope()
    private val ui = Handler(Looper.getMainLooper())
    private var controller: MediaController? = null
    private lateinit var engineReady: Deferred<Unit>

    // ----- 데이터 -----
    private val songs = mutableListOf<Song>()
    private val playlists = linkedMapOf<String, MutableList<String>>()
    private val progress = HashMap<String, Int>()
    private val thumbCache = HashMap<String, Bitmap>()
    private var tab = 0
    private var openPlaylist: String? = null
    private var query = ""
    private var rows = listOf<Row>()
    private var sleepRunnable: Runnable? = null
    private var seeking = false
    private val speeds = listOf(0.75f, 1f, 1.25f, 1.5f, 2f)

    private val prefs by lazy { getSharedPreferences("library", MODE_PRIVATE) }
    private val musicDir: File by lazy {
        getExternalFilesDir(Environment.DIRECTORY_MUSIC) ?: filesDir
    }

    // ----- 뷰 -----
    private lateinit var listAdapter: SongAdapter
    private lateinit var form: LinearLayout
    private lateinit var linkInput: EditText
    private lateinit var nameInput: EditText
    private lateinit var searchInput: EditText
    private lateinit var tabViews: List<TextView>
    private lateinit var playerArt: ImageView
    private lateinit var playerTitle: TextView
    private lateinit var playerSub: TextView
    private lateinit var seekBar: SeekBar
    private lateinit var timeNow: TextView
    private lateinit var timeTotal: TextView
    private lateinit var shuffleBtn: TextView
    private lateinit var playBtn: TextView
    private lateinit var repeatBtn: TextView
    private lateinit var speedBtn: TextView
    private lateinit var sleepBtn: TextView

    private val MATCH = ViewGroup.LayoutParams.MATCH_PARENT
    private val WRAP = ViewGroup.LayoutParams.WRAP_CONTENT

    private val bg = Color.parseColor("#0F1115")
    private val card = Color.parseColor("#1A1D24")
    private val field = Color.parseColor("#252932")
    private val accent = Color.parseColor("#7C4DFF")
    private val playingBg = Color.parseColor("#2A2150")
    private val textMain = Color.WHITE
    private val textSub = Color.parseColor("#9AA0AC")

    private val ticker = object : Runnable {
        override fun run() {
            updateProgress()
            ui.postDelayed(this, 500)
        }
    }

    private val playerListener = object : Player.Listener {
        override fun onIsPlayingChanged(isPlaying: Boolean) = updatePlayerInfo()
        override fun onMediaItemTransition(mediaItem: MediaItem?, reason: Int) = updatePlayerInfo()
        override fun onShuffleModeEnabledChanged(shuffleModeEnabled: Boolean) = updatePlayerInfo()
        override fun onRepeatModeChanged(repeatMode: Int) = updatePlayerInfo()
        override fun onPlaybackParametersChanged(playbackParameters: PlaybackParameters) = updatePlayerInfo()
        override fun onPlaybackStateChanged(playbackState: Int) = updatePlayerInfo()
        override fun onPlayerError(error: PlaybackException) {
            toast("재생 오류: ${error.errorCodeName}")
            updatePlayerInfo()
        }
    }

    // =====================================================
    // 생명주기
    // =====================================================

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        if (Build.VERSION.SDK_INT >= 33) {
            requestPermissions(arrayOf(Manifest.permission.POST_NOTIFICATIONS), 1)
        }

        engineReady = scope.async(Dispatchers.IO) {
            YoutubeDL.getInstance().init(application)
            FFmpeg.getInstance().init(application)
            Unit
        }

        load()
        buildUi()
        refresh()
        connectPlayer()
        handleIntent(intent)
        ui.post(ticker)
    }

    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        handleIntent(intent)
    }

    override fun onDestroy() {
        ui.removeCallbacks(ticker)
        sleepRunnable?.let { ui.removeCallbacks(it) }
        controller?.removeListener(playerListener)
        controller?.release()
        scope.cancel()
        super.onDestroy()
    }

    // =====================================================
    // UI 구성
    // =====================================================

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
        setPadding(dp(8), dp(6), dp(8), dp(6))
        setOnClickListener { onClick() }
    }

    private fun buildUi() {
        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setBackgroundColor(bg)
            setPadding(dp(16), dp(10), dp(16), dp(10))
        }

        // 헤더
        val header = LinearLayout(this).apply {
            orientation = LinearLayout.HORIZONTAL
            gravity = Gravity.CENTER_VERTICAL
        }
        val title = TextView(this).apply {
            text = "내 보관함"
            textSize = 26f
            typeface = Typeface.DEFAULT_BOLD
            setTextColor(textMain)
        }
        val plusBtn = ctrl("＋") { toggleForm() }
        header.addView(title, lp(0, WRAP, 0, 1f))
        header.addView(plusBtn)
        root.addView(header, lp(MATCH, WRAP))

        // 등록 폼
        form = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            background = round(card, 16)
            setPadding(dp(14), dp(14), dp(14), dp(14))
            visibility = View.GONE
        }
        linkInput = input("유튜브 링크 붙여넣기")
        nameInput = input("이름 (비우면 영상 제목 사용)")
        val addBtn = pill("⬇ MP3로 저장하기", accent)
        form.addView(linkInput, lp(MATCH, WRAP))
        form.addView(nameInput, lp(MATCH, WRAP, 8))
        form.addView(addBtn, lp(MATCH, WRAP, 10))
        root.addView(form, lp(MATCH, WRAP, 10))
        addBtn.setOnClickListener { addSong() }

        // 탭
        val tabRow = LinearLayout(this).apply { orientation = LinearLayout.HORIZONTAL }
        val labels = listOf("전체", "♥ 즐겨찾기", "재생목록")
        tabViews = labels.mapIndexed { i, label ->
            pill(label, field).apply {
                textSize = 13f
                setPadding(dp(8), dp(9), dp(8), dp(9))
                setOnClickListener {
                    tab = i
                    openPlaylist = null
                    refresh()
                }
            }
        }
        tabViews.forEachIndexed { i, v ->
            tabRow.addView(v, lp(0, WRAP, 0, 1f).apply { if (i > 0) leftMargin = dp(8) })
        }
        root.addView(tabRow, lp(MATCH, WRAP, 12))

        // 검색
        searchInput = input("🔍 곡 검색")
        searchInput.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {}
            override fun afterTextChanged(s: Editable?) {
                query = s?.toString().orEmpty()
                refresh()
            }
        })
        root.addView(searchInput, lp(MATCH, WRAP, 10))

        // 목록
        listAdapter = SongAdapter()
        val list = ListView(this).apply {
            adapter = listAdapter
            divider = null
            dividerHeight = dp(8)
            setSelector(ColorDrawable(Color.TRANSPARENT))
            isVerticalScrollBarEnabled = false
        }
        val empty = TextView(this).apply {
            text = "곡이 없어요\n오른쪽 위 ＋ 버튼으로 유튜브 링크를 등록해 보세요"
            setTextColor(textSub)
            textSize = 14f
            gravity = Gravity.CENTER
        }
        val frame = FrameLayout(this)
        frame.addView(list, FrameLayout.LayoutParams(MATCH, MATCH))
        frame.addView(empty, FrameLayout.LayoutParams(MATCH, MATCH))
        list.emptyView = empty
        root.addView(frame, lp(MATCH, 0, 10, 1f))

        list.setOnItemClickListener { _, _, position, _ -> onRowClick(rows[position]) }
        list.setOnItemLongClickListener { _, _, position, _ ->
            onRowLongClick(rows[position])
            true
        }

        // 플레이어 패널
        val panel = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            background = round(Color.parseColor("#22183F"), 18)
            setPadding(dp(14), dp(12), dp(14), dp(6))
        }

        val top = LinearLayout(this).apply {
            orientation = LinearLayout.HORIZONTAL
            gravity = Gravity.CENTER_VERTICAL
        }
        playerArt = ImageView(this).apply {
            scaleType = ImageView.ScaleType.CENTER_CROP
            background = round(Color.parseColor("#2B2F3A"), 12)
            clipToOutline = true
        }
        playerTitle = TextView(this).apply {
            textSize = 15f
            typeface = Typeface.DEFAULT_BOLD
            setTextColor(textMain)
            setSingleLine()
            ellipsize = TextUtils.TruncateAt.END
        }
        playerSub = TextView(this).apply {
            textSize = 12f
            setTextColor(textSub)
        }
        val tcol = LinearLayout(this).apply { orientation = LinearLayout.VERTICAL }
        tcol.addView(playerTitle)
        tcol.addView(playerSub)
        top.addView(playerArt, LinearLayout.LayoutParams(dp(52), dp(52)))
        top.addView(tcol, lp(0, WRAP, 0, 1f).apply { leftMargin = dp(12) })
        panel.addView(top, lp(MATCH, WRAP))

        val seekRow = LinearLayout(this).apply {
            orientation = LinearLayout.HORIZONTAL
            gravity = Gravity.CENTER_VERTICAL
        }
        timeNow = TextView(this).apply { text = "0:00"; textSize = 11f; setTextColor(textSub) }
        timeTotal = TextView(this).apply { text = "0:00"; textSize = 11f; setTextColor(textSub) }
        seekBar = SeekBar(this).apply {
            progressTintList = ColorStateList.valueOf(accent)
            thumbTintList = ColorStateList.valueOf(accent)
        }
        seekBar.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(sb: SeekBar?, progress: Int, fromUser: Boolean) {
                if (fromUser) timeNow.text = fmt(progress.toLong())
            }

            override fun onStartTrackingTouch(sb: SeekBar?) {
                seeking = true
            }

            override fun onStopTrackingTouch(sb: SeekBar?) {
                seeking = false
                controller?.seekTo((sb?.progress ?: 0).toLong())
            }
        })
        seekRow.addView(timeNow)
        seekRow.addView(seekBar, lp(0, WRAP, 0, 1f))
        seekRow.addView(timeTotal)
        panel.addView(seekRow, lp(MATCH, WRAP, 6))

        val ctrls = LinearLayout(this).apply {
            orientation = LinearLayout.HORIZONTAL
            gravity = Gravity.CENTER
        }
        shuffleBtn = ctrl("🔀") { toggleShuffle() }
        val prevBtn = ctrl("⏮") { controller?.seekToPrevious() }
        playBtn = ctrl("▶") { togglePlay() }.apply { textSize = 32f }
        val nextBtn = ctrl("⏭") { controller?.seekToNext() }
        repeatBtn = ctrl("🔁") { cycleRepeat() }
        ctrls.addView(shuffleBtn, lp(0, WRAP, 0, 1f))
        ctrls.addView(prevBtn, lp(0, WRAP, 0, 1f))
        ctrls.addView(playBtn, lp(0, WRAP, 0, 1f))
        ctrls.addView(nextBtn, lp(0, WRAP, 0, 1f))
        ctrls.addView(repeatBtn, lp(0, WRAP, 0, 1f))
        panel.addView(ctrls, lp(MATCH, WRAP, 2))

        val extra = LinearLayout(this).apply {
            orientation = LinearLayout.HORIZONTAL
            gravity = Gravity.CENTER
        }
        speedBtn = ctrl("1.0x") { cycleSpeed() }.apply { textSize = 13f }
        sleepBtn = ctrl("⏲ 취침예약") { showSleepMenu() }.apply { textSize = 13f }
        extra.addView(speedBtn, lp(0, WRAP, 0, 1f))
        extra.addView(sleepBtn, lp(0, WRAP, 0, 1f))
        panel.addView(extra, lp(MATCH, WRAP))

        root.addView(panel, lp(MATCH, WRAP, 10))

        setContentView(root)
    }

    private fun toggleForm() {
        form.visibility = if (form.visibility == View.VISIBLE) View.GONE else View.VISIBLE
    }

    // =====================================================
    // 목록 행
    // =====================================================

    inner class SongAdapter : BaseAdapter() {
        override fun getCount() = rows.size
        override fun getItem(position: Int): Any = rows[position]
        override fun getItemId(position: Int) = position.toLong()

        override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
            val r = rows[position]
            return when (r.type) {
                Row.SONG -> songRow(r.song!!)
                Row.PLAYLIST -> textRow("♬  ${r.label}", "${r.tag}곡", false)
                else -> textRow(r.label, "", true)
            }
        }
    }

    private fun textRow(title: String, sub: String, highlight: Boolean): View {
        val row = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            background = round(if (highlight) Color.parseColor("#1F1A3A") else card, 14)
            setPadding(dp(16), dp(14), dp(16), dp(14))
        }
        val t = TextView(this).apply {
            text = title
            textSize = 15f
            typeface = Typeface.DEFAULT_BOLD
            setTextColor(if (highlight) accent else textMain)
        }
        row.addView(t)
        if (sub.isNotEmpty()) {
            val s = TextView(this).apply {
                text = sub
                textSize = 12f
                setTextColor(textSub)
            }
            row.addView(s)
        }
        return row
    }

    private fun songRow(s: Song): View {
        val playing = controller?.currentMediaItem?.mediaId == s.id
        val row = LinearLayout(this).apply {
            orientation = LinearLayout.HORIZONTAL
            gravity = Gravity.CENTER_VERTICAL
            background = round(if (playing) playingBg else card, 14)
            setPadding(dp(10), dp(10), dp(6), dp(10))
        }

        val bmp = thumb(s)
        val art: View = if (bmp != null) {
            ImageView(this).apply {
                setImageBitmap(bmp)
                scaleType = ImageView.ScaleType.CENTER_CROP
                background = round(field, 10)
                clipToOutline = true
            }
        } else {
            TextView(this).apply {
                text = if (playing) "♫" else "♪"
                textSize = 18f
                gravity = Gravity.CENTER
                setTextColor(if (playing) Color.WHITE else accent)
                background = round(if (playing) accent else Color.parseColor("#2B2F3A"), 10)
            }
        }
        row.addView(art, LinearLayout.LayoutParams(dp(44), dp(44)))

        val col = LinearLayout(this).apply { orientation = LinearLayout.VERTICAL }
        val titleView = TextView(this).apply {
            text = s.title
            textSize = 15f
            setTextColor(textMain)
            typeface = if (playing) Typeface.DEFAULT_BOLD else Typeface.DEFAULT
            setSingleLine()
            ellipsize = TextUtils.TruncateAt.END
        }
        val subText = when (s.status) {
            Song.DOWNLOADING -> "다운로드 중 ${progress[s.id] ?: 0}%"
            Song.FAILED -> "실패 · 탭해서 재시도"
            else -> if (playing) "재생 중" else "저장됨"
        }
        val subView = TextView(this).apply {
            text = subText
            textSize = 12f
            setTextColor(if (s.status == Song.FAILED) Color.parseColor("#FF6B6B") else textSub)
        }
        col.addView(titleView)
        col.addView(subView)
        row.addView(col, lp(0, WRAP, 0, 1f).apply { leftMargin = dp(12) })

        val heart = TextView(this).apply {
            text = if (s.fav) "♥" else "♡"
            textSize = 22f
            setTextColor(if (s.fav) accent else textSub)
            setPadding(dp(10), dp(6), dp(10), dp(6))
            setOnClickListener {
                s.fav = !s.fav
                save()
                refresh()
            }
        }
        row.addView(heart)
        return row
    }

    private fun thumb(s: Song): Bitmap? {
        thumbCache[s.id]?.let { return it }
        val f = thumbFile(s)
        if (!f.exists()) return null
        val opts = BitmapFactory.Options().apply { inSampleSize = 4 }
        val b = BitmapFactory.decodeFile(f.absolutePath, opts) ?: return null
        thumbCache[s.id] = b
        return b
    }

    // =====================================================
    // 목록 데이터 / 클릭
    // =====================================================

    private fun filtered(list: List<Song>) =
        if (query.isBlank()) list else list.filter { it.title.contains(query, true) }

    private fun addSongRows(out: MutableList<Row>, list: List<Song>) {
        val readyCount = list.count { it.status == Song.READY }
        if (readyCount > 0) {
            out.add(Row(Row.ACTION, label = "▶ 전체 재생 (${readyCount}곡)", tag = "playall"))
        }
        list.forEach { out.add(Row(Row.SONG, song = it)) }
    }

    private fun buildRows(): List<Row> {
        val out = mutableListOf<Row>()
        when (tab) {
            0 -> addSongRows(out, filtered(songs))
            1 -> addSongRows(out, filtered(songs.filter { it.fav }))
            else -> {
                val open = openPlaylist
                if (open == null) {
                    out.add(Row(Row.ACTION, label = "＋ 새 재생목록", tag = "new"))
                    for ((name, ids) in playlists) {
                        out.add(Row(Row.PLAYLIST, label = name, tag = ids.size.toString()))
                    }
                } else {
                    out.add(Row(Row.ACTION, label = "← 재생목록으로", tag = "back"))
                    val ids = playlists[open] ?: mutableListOf()
                    val list = ids.mapNotNull { id -> songs.firstOrNull { it.id == id } }
                    addSongRows(out, filtered(list))
                }
            }
        }
        return out
    }

    private fun refresh() {
        rows = buildRows()
        listAdapter.notifyDataSetChanged()
        tabViews.forEachIndexed { i, v ->
            v.background = round(if (i == tab) accent else field, 12)
        }
        updatePlayerInfo()
    }

    private fun visibleSongs(): List<Song> = rows.mapNotNull { it.song }

    private fun onRowClick(r: Row) {
        when (r.type) {
            Row.SONG -> {
                val s = r.song ?: return
                when (s.status) {
                    Song.READY -> playList(visibleSongs(), s)
                    Song.DOWNLOADING -> toast("다운로드 중이에요")
                    else -> startDownload(s, false)
                }
            }
            Row.PLAYLIST -> {
                openPlaylist = r.label
                refresh()
            }
            else -> when (r.tag) {
                "playall" -> playList(visibleSongs(), null)
                "back" -> {
                    openPlaylist = null
                    refresh()
                }
                "new" -> promptName("새 재생목록", "") { n ->
                    playlists.getOrPut(n) { mutableListOf() }
                    save()
                    refresh()
                }
            }
        }
    }

    private fun onRowLongClick(r: Row) {
        when (r.type) {
            Row.SONG -> {
                val s = r.song ?: return
                val items = mutableListOf<Pair<String, () -> Unit>>()
                if (s.status == Song.READY) items.add("▶ 재생" to { playList(visibleSongs(), s) })
                items.add((if (s.fav) "♡ 즐겨찾기 해제" else "♥ 즐겨찾기") to {
                    s.fav = !s.fav
                    save()
                    refresh()
                })
                items.add("♬ 재생목록에 추가" to { addToPlaylist(s) })
                val open = openPlaylist
                if (tab == 2 && open != null) {
                    items.add("재생목록에서 빼기" to {
                        playlists[open]?.remove(s.id)
                        save()
                        refresh()
                    })
                }
                items.add("이름 변경" to {
                    promptName("이름 변경", s.title) { n ->
                        s.title = n
                        save()
                        refresh()
                    }
                })
                items.add("🗑 삭제" to { confirmDelete(s) })
                showMenu(s.title, items)
            }
            Row.PLAYLIST -> {
                val name = r.label
                val items = mutableListOf<Pair<String, () -> Unit>>()
                items.add("이름 변경" to {
                    promptName("재생목록 이름", name) { n ->
                        val ids = playlists.remove(name) ?: mutableListOf()
                        playlists[n] = ids
                        save()
                        refresh()
                    }
                })
                items.add("🗑 삭제" to {
                    playlists.remove(name)
                    save()
                    refresh()
                })
                showMenu(name, items)
            }
        }
    }

    private fun showMenu(title: String, items: List<Pair<String, () -> Unit>>) {
        AlertDialog.Builder(this)
            .setTitle(title)
            .setItems(items.map { it.first }.toTypedArray()) { _, which -> items[which].second() }
            .show()
    }

    private fun promptName(title: String, initial: String, onOk: (String) -> Unit) {
        val et = EditText(this)
        et.setText(initial)
        et.setSingleLine()
        AlertDialog.Builder(this)
            .setTitle(title)
            .setView(et)
            .setPositiveButton("확인") { _, _ ->
                val t = et.text.toString().trim()
                if (t.isNotEmpty()) onOk(t)
            }
            .setNegativeButton("취소", null)
            .show()
    }

    private fun addToPlaylist(s: Song) {
        val items = mutableListOf<Pair<String, () -> Unit>>()
        for (n in playlists.keys.toList()) {
            items.add("♬ $n" to { addTo(n, s) })
        }
        items.add("＋ 새 재생목록" to {
            promptName("새 재생목록", "") { n ->
                playlists.getOrPut(n) { mutableListOf() }
                addTo(n, s)
            }
        })
        showMenu("재생목록 선택", items)
    }

    private fun addTo(name: String, s: Song) {
        val l = playlists.getOrPut(name) { mutableListOf() }
        if (!l.contains(s.id)) l.add(s.id)
        save()
        refresh()
        toast("'$name'에 추가했어요")
    }

    private fun confirmDelete(s: Song) {
        AlertDialog.Builder(this)
            .setTitle(s.title)
            .setMessage("기기에서 이 곡을 삭제할까요?")
            .setPositiveButton("삭제") { _, _ -> deleteSong(s) }
            .setNegativeButton("취소", null)
            .show()
    }

    private fun deleteSong(s: Song) {
        controller?.let { c ->
            for (i in c.mediaItemCount - 1 downTo 0) {
                if (c.getMediaItemAt(i).mediaId == s.id) c.removeMediaItem(i)
            }
        }
        audioFile(s).delete()
        thumbFile(s).delete()
        thumbCache.remove(s.id)
        songs.remove(s)
        playlists.values.forEach { it.remove(s.id) }
        save()
        refresh()
        toast("삭제했어요")
    }

    // =====================================================
    // 다운로드 (MP3)
    // =====================================================

    private fun audioFile(s: Song) = File(musicDir, s.id + ".mp3")
    private fun thumbFile(s: Song) = File(musicDir, s.id + ".jpg")

    private fun addSong() {
        val u = linkInput.text.toString().trim()
        val n = nameInput.text.toString().trim()
        if (!u.startsWith("http")) {
            toast("올바른 링크를 입력하세요")
            return
        }
        val s = Song(
            id = System.currentTimeMillis().toString(),
            title = if (n.isEmpty()) "새 곡" else n,
            url = u,
            status = Song.DOWNLOADING
        )
        songs.add(0, s)
        save()
        linkInput.text.clear()
        nameInput.text.clear()
        form.visibility = View.GONE
        tab = 0
        openPlaylist = null
        refresh()
        startDownload(s, n.isEmpty())
    }

    private fun startDownload(s: Song, useInfoTitle: Boolean) {
        s.status = Song.DOWNLOADING
        progress[s.id] = 0
        refresh()

        scope.launch {
            try {
                engineReady.await()
                withContext(Dispatchers.IO) {
                    // 1) 제목, 썸네일 정보
                    val infoReq = YoutubeDLRequest(s.url)
                    infoReq.addOption("--no-playlist")
                    val info = YoutubeDL.getInstance().getInfo(infoReq)
                    val t = info.title
                    if (useInfoTitle && !t.isNullOrBlank()) s.title = t
                    val thumbUrl = info.thumbnail
                    if (!thumbUrl.isNullOrEmpty()) {
                        try {
                            URL(thumbUrl).openStream().use { inp ->
                                thumbFile(s).outputStream().use { out -> inp.copyTo(out) }
                            }
                            s.thumb = thumbFile(s).absolutePath
                        } catch (ignored: Exception) {
                        }
                    }

                    // 2) MP3 다운로드
                    val req = YoutubeDLRequest(s.url)
                    req.addOption("--no-playlist")
                    req.addOption("-x")
                    req.addOption("--audio-format", "mp3")
                    req.addOption("--audio-quality", "0")
                    req.addOption("-o", File(musicDir, s.id + ".%(ext)s").absolutePath)
                    YoutubeDL.getInstance().execute(req, s.id) { p, _, _ ->
                        ui.post {
                            progress[s.id] = p.toInt()
                            listAdapter.notifyDataSetChanged()
                        }
                    }
                }
                if (!audioFile(s).exists()) throw IllegalStateException("MP3 파일이 만들어지지 않았어요")
                thumbCache.remove(s.id)
                s.status = Song.READY
                toast("저장 완료: ${s.title}")
            } catch (e: Exception) {
                s.status = Song.FAILED
                toast("다운로드 실패: ${e.message}")
            }
            progress.remove(s.id)
            save()
            refresh()
        }
    }

    // =====================================================
    // 재생
    // =====================================================

    private fun connectPlayer() {
        val token = SessionToken(this, ComponentName(this, PlaybackService::class.java))
        scope.launch {
            val c = MediaController.Builder(this@MainActivity, token).buildAsync().await()
            c.addListener(playerListener)
            controller = c
            refresh()
        }
    }

    private fun toItem(s: Song): MediaItem {
        val meta = MediaMetadata.Builder().setTitle(s.title)
        val tf = thumbFile(s)
        if (tf.exists()) meta.setArtworkUri(Uri.fromFile(tf))
        return MediaItem.Builder()
            .setMediaId(s.id)
            .setUri(Uri.fromFile(audioFile(s)))
            .setMediaMetadata(meta.build())
            .build()
    }

    private fun playList(list: List<Song>, start: Song?) {
        val ready = list.filter { it.status == Song.READY && audioFile(it).exists() }
        if (ready.isEmpty()) {
            toast("재생할 곡이 없어요")
            return
        }
        val c = controller
        if (c == null) {
            toast("플레이어 연결 중이에요. 잠시 후 다시 눌러 주세요")
            return
        }
        val idx = if (start == null) 0 else ready.indexOfFirst { it.id == start.id }.coerceAtLeast(0)
        c.setMediaItems(ready.map { toItem(it) }, idx, 0L)
        c.prepare()
        c.play()
    }

    private fun togglePlay() {
        val c = controller ?: return
        if (c.mediaItemCount == 0) {
            playList(songs, null)
            return
        }
        if (c.isPlaying) {
            c.pause()
        } else {
            if (c.playbackState == Player.STATE_ENDED) c.seekToDefaultPosition(0)
            c.play()
        }
    }

    private fun toggleShuffle() {
        val c = controller ?: return
        c.shuffleModeEnabled = !c.shuffleModeEnabled
    }

    private fun cycleRepeat() {
        val c = controller ?: return
        c.repeatMode = when (c.repeatMode) {
            Player.REPEAT_MODE_OFF -> Player.REPEAT_MODE_ALL
            Player.REPEAT_MODE_ALL -> Player.REPEAT_MODE_ONE
            else -> Player.REPEAT_MODE_OFF
        }
    }

    private fun cycleSpeed() {
        val c = controller ?: return
        val cur = c.playbackParameters.speed
        val idx = speeds.indexOfFirst { abs(it - cur) < 0.01f }
        c.setPlaybackSpeed(speeds[(idx + 1) % speeds.size])
    }

    private fun showSleepMenu() {
        val opts = listOf(0, 15, 30, 45, 60)
        AlertDialog.Builder(this)
            .setTitle("취침 예약")
            .setItems(opts.map { if (it == 0) "끄기" else "${it}분 뒤 정지" }.toTypedArray()) { _, which ->
                sleepRunnable?.let { ui.removeCallbacks(it) }
                sleepRunnable = null
                val m = opts[which]
                if (m > 0) {
                    val r = Runnable {
                        controller?.pause()
                        sleepRunnable = null
                        updatePlayerInfo()
                        toast("취침 예약으로 재생을 멈췄어요")
                    }
                    sleepRunnable = r
                    ui.postDelayed(r, m * 60_000L)
                    toast("${m}분 뒤에 멈춰요")
                }
                updatePlayerInfo()
            }
            .show()
    }

    // =====================================================
    // 플레이어 UI 갱신
    // =====================================================

    private fun fmt(ms: Long): String {
        val total = ms / 1000
        return String.format("%d:%02d", total / 60, total % 60)
    }

    private fun updateProgress() {
        val c = controller ?: return
        val dur = if (c.duration == C.TIME_UNSET) 0L else c.duration
        val pos = c.currentPosition
        if (!seeking) {
            seekBar.max = dur.toInt()
            seekBar.progress = pos.toInt()
            timeNow.text = fmt(pos)
        }
        timeTotal.text = fmt(dur)
    }

    private fun updatePlayerInfo() {
        val c = controller
        val playing = c?.isPlaying == true
        val id = c?.currentMediaItem?.mediaId
        val song = songs.firstOrNull { it.id == id }

        playerTitle.text = song?.title ?: "재생 중인 곡 없음"
        playerSub.text = when {
            song == null -> "곡을 선택하세요"
            playing -> "재생 중"
            else -> "일시정지"
        }
        val bmp = song?.let { thumb(it) }
        playerArt.setImageBitmap(bmp)

        playBtn.text = if (playing) "⏸" else "▶"
        shuffleBtn.setTextColor(if (c?.shuffleModeEnabled == true) accent else textSub)
        when (c?.repeatMode) {
            Player.REPEAT_MODE_ALL -> {
                repeatBtn.text = "🔁"
                repeatBtn.setTextColor(accent)
            }
            Player.REPEAT_MODE_ONE -> {
                repeatBtn.text = "🔂"
                repeatBtn.setTextColor(accent)
            }
            else -> {
                repeatBtn.text = "🔁"
                repeatBtn.setTextColor(textSub)
            }
        }
        speedBtn.text = "${c?.playbackParameters?.speed ?: 1f}x"
        sleepBtn.text = if (sleepRunnable != null) "⏲ 예약 중" else "⏲ 취침예약"
        listAdapter.notifyDataSetChanged()
    }

    // =====================================================
    // 저장 / 불러오기
    // =====================================================

    private fun save() {
        val sa = JSONArray()
        for (s in songs) {
            sa.put(
                JSONObject()
                    .put("id", s.id)
                    .put("title", s.title)
                    .put("url", s.url)
                    .put("thumb", s.thumb)
                    .put("fav", s.fav)
                    .put("status", s.status)
            )
        }
        val pl = JSONObject()
        for ((n, ids) in playlists) pl.put(n, JSONArray(ids))
        prefs.edit()
            .putString("songs", sa.toString())
            .putString("playlists", pl.toString())
            .apply()
    }

    private fun load() {
        val sa = JSONArray(prefs.getString("songs", "[]"))
        for (k in 0 until sa.length()) {
            val o = sa.getJSONObject(k)
            val s = Song(
                id = o.getString("id"),
                title = o.getString("title"),
                url = o.getString("url"),
                thumb = o.optString("thumb", ""),
                fav = o.optBoolean("fav", false),
                status = o.optInt("status", Song.READY)
            )
            if (s.status == Song.DOWNLOADING || (s.status == Song.READY && !audioFile(s).exists())) {
                s.status = Song.FAILED
            }
            songs.add(s)
        }
        val pl = JSONObject(prefs.getString("playlists", "{}"))
        val keys = pl.keys()
        while (keys.hasNext()) {
            val name = keys.next()
            val arr = pl.getJSONArray(name)
            val ids = mutableListOf<String>()
            for (i in 0 until arr.length()) ids.add(arr.getString(i))
            playlists[name] = ids
        }
    }

    // 유튜브 앱에서 "공유 → YT Player"로 보내면 링크 자동 입력
    private fun handleIntent(i: Intent?) {
        if (i?.action != Intent.ACTION_SEND) return
        val text = i.getStringExtra(Intent.EXTRA_TEXT) ?: return
        val link = Regex("https?://\\S+").find(text)?.value ?: text
        form.visibility = View.VISIBLE
        linkInput.setText(link)
        val subject = i.getStringExtra(Intent.EXTRA_SUBJECT)
        if (!subject.isNullOrBlank() && nameInput.text.isBlank()) nameInput.setText(subject)
        toast("링크를 채웠어요. 이름을 확인하고 저장하세요")
    }

    private fun toast(msg: String) = Toast.makeText(this, msg, Toast.LENGTH_SHORT).show()
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

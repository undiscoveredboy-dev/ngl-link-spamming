import random


class MessageGenerator:
    def __init__(self):
        self.generic_messages = [
            "Hey there! Just wanted to drop a quick message to say hi and see how you're doing. Hope you're having a great day! 😊",
            "Hi friend! Sending some positive vibes your way. Hope you're doing well!",
            "Hey buddy! Remember, you're awesome and capable of achieving anything you set your mind to! 💪",
            "Hello! Just checking in to see how you're doing. Let me know if there's anything I can do to support you!",
            "Hi! Wishing you a fantastic day filled with joy and laughter. Keep shining bright! ✨",
            "Hey! Hope your day is as amazing as you are! 😄",
            "Hi there! Just wanted to remind you that you're appreciated and valued. Keep being awesome!",
            "Hey friend! Just dropping by to say hello and spread some positivity your way. Have a wonderful day!",
            "Hello! Sending you lots of love and good vibes. You've got this!",
            "Hi! Remember, every challenge you face is an opportunity to grow stronger. Keep pushing forward!",
            "Hey there! Just wanted to send a quick virtual hug your way. You're not alone, and I'm here for you!",
            "Hi friend! Hope your day is filled with laughter, love, and all the good things in life. You deserve it!"
        ]
        
        self.messages_hacker = [
            "Initiating secure connection. Your digital presence is attracting attention. Stay vigilant. - ShadowCipher",
            "Warning: Unusual activity detected in your online behavior. Exercise caution. - DarkNetOp",
            "Cipher protocol activated. Your online actions have drawn scrutiny. Maintain discretion. - GhostHacker",
            "Alert: Anomaly detected in network traffic. You may be under surveillance. - StealthByte",
            "Security breach alert: Your digital footprint is being monitored. Take evasive action. - PhantomByte",
            "Caution: Digital surveillance detected. Your activities are being watched closely. - CyberPhantom",
            "Intrusion warning: Your online presence is under scrutiny. Stay under the radar. - CryptoGhost",
            "Encryption compromised. Your digital identity may be at risk. Take precautions. - ShadowCipher",
            "Attention: Suspicious network activity detected. Exercise heightened security measures. - DarkNetOp",
            "Security protocol breached. Your digital security may have been compromised. - GhostHacker",
            "Warning: Abnormal data flow detected in your network. Stay alert. - StealthByte",
            "Code red: Unauthorized access detected. Your online security is under threat. - PhantomByte",
            "Initiating secure transmission. Your digital activities have attracted attention. Stay covert. - CyberPhantom",
            "Caution: Anomalies detected in network traffic. Proceed with caution. - CryptoGhost",
            "Alert: Cipher protocol engaged. Your online presence may be compromised. - ShadowCipher",
            "Security breach detected. Your digital identity is vulnerable. Take action. - DarkNetOp",
            "Warning: Digital surveillance in progress. Maintain operational security. - GhostHacker",
            "Attention: Unusual patterns detected in your online behavior. Stay under the radar. - StealthByte",
            "Intrusion alert: Your online activities are being monitored. Stay low-key. - PhantomByte",
            "Encryption compromised. Your digital security may be compromised. Take evasive action. - CyberPhantom",
            "Alert: Suspicious network activity detected. Exercise caution in your online interactions. - CryptoGhost",
            "Security protocol breached. Your digital footprint is attracting unwanted attention. - ShadowCipher",
            "Code red: Unauthorized access detected. Take measures to protect your online security. - DarkNetOp",
            "Initiating secure communication. Your digital presence is under scrutiny. Maintain discretion. - GhostHacker",
            "Caution: Abnormal data flow detected. Your online activities may be compromised. - StealthByte",
            "Alert: Cipher protocol activated. Your digital security is at risk. Take precautions. - PhantomByte",
            "Security breach detected. Your digital privacy may be compromised. Take evasive action. - CyberPhantom",
            "Warning: Digital surveillance detected. Exercise caution in your online interactions. - CryptoGhost",
            "Attention: Unusual activity detected in your network. Stay alert. - ShadowCipher",
            "Intrusion warning: Your digital footprint has been noticed. Stay under the radar. - DarkNetOp",
            "Encryption compromised. Your online security may be compromised. Take action. - GhostHacker",
            "Alert: Suspicious network activity detected. Proceed with caution in your online activities. - StealthByte",
            "Security protocol breached. Your digital identity is vulnerable. Take evasive action. - PhantomByte",
            "Code red: Unauthorized access detected. Exercise caution in your digital interactions. - CyberPhantom",
            "Initiating secure transmission. Your digital presence is under surveillance. Stay covert. - CryptoGhost",
            "Caution: Anomalies detected in network traffic. Maintain operational security. - ShadowCipher",
            "Alert: Cipher protocol engaged. Your digital privacy may be compromised. - DarkNetOp",
            "Security breach detected. Your online activities are being monitored. Take action. - GhostHacker",
            "Warning: Digital surveillance in progress. Stay low-key in your online interactions. - StealthByte",
            "Attention: Unusual patterns detected in your online behavior. Exercise caution. - PhantomByte",
            "Intrusion alert: Your digital security may be compromised. Stay vigilant. - CyberPhantom",
            "Warning: Data integrity at risk. Immediate attention required to safeguard digital assets. - CyberSentinel",
            "Caution: Encryption anomaly detected. Verify security protocols immediately. - NetShield",
            "Alert: Unauthorized data access suspected. Increase security measures now. - GuardByte",
            "Notice: Potential compromise in system integrity. Review all network activity. - SecurePath",
            "Urgent: Suspicious encryption behavior observed. Tighten security controls. - CryptoWatch",
            "Warning: Network perimeter breach detected. Activate enhanced defensive measures. - FirewallGuard",
            "Alert: Possible phishing attempt in progress. Do not disclose personal information. - PhishNet",
            "Security Notice: Irregular access patterns observed. Confirm user identities. - IdentityShield",
            "Critical: Vulnerable software detected. Update systems to prevent potential breaches. - PatchMaster",
            "Attention: Elevated risk of cyber intrusion detected. Secure all digital communications. - NetSecure",
            "Warning: Malicious code detected in network stream. Initiate malware scans. - VirusSweeper",
            "Alert: System integrity compromised. Initiate recovery protocols immediately. - RecoveryOps",
            "Security Update: Anomaly in authentication logs. Review all recent sessions. - AccessGuard",
            "Notice: Increased risk of data exfiltration detected. Monitor all outbound traffic. - DataWatch",
            "Urgent: Threat to digital infrastructure imminent. Prioritize cybersecurity measures. - CyberDefender",
            "Warning: Abnormal network behavior detected. Assess potential security threats. - ThreatAnalyzer",
            "Alert: High-risk vulnerability found. Patch systems immediately to avoid exploitation. - SecurePatch",
            "Security Advisory: Unauthorized attempts to access secure files detected. Enhance file security. - FileGuard",
            "Critical Warning: Network infrastructure under attack. Deploy countermeasures. - NetworkDefender",
            "Alert: Disruption in encryption channels observed. Assess for potential data breaches. - EncryptGuard",
            "Caution: Irregular data transmissions detected. Assess for potential interception. - SignalCrypt",
            "Warning: Unusual login attempts from unrecognized locations. Verify account security. - LoginMonitor",
            "Alert: Network defense parameters altered. Revert to secure configurations. - DefenseGuard",
            "Security Notice: Suspicious registry modifications detected. Conduct system audits. - SystemCheck",
            "Urgent: Elevated activity in admin panels observed. Confirm authenticity of sessions. - AdminWatch",
            "Notice: Possible intrusion in secure zones. Initiate lockdown procedures. - ZoneDefender",
            "Alert: High-risk IP addresses connected to network. Block suspicious connections. - IPBlocker",
            "Caution: Data leakage suspected. Secure confidential information immediately. - LeakPrevent",
            "Warning: External devices attempting unauthorized connections. Monitor and control access. - DeviceShield",
            "Critical: Unusual outbound traffic patterns observed. Investigate for data theft. - TrafficGuard",
            "Security Advisory: Multiple failed attempts to access secure data detected. Increase alertness. - FailSafe",
            "Alert: Encryption keys potentially compromised. Reissue new keys promptly. - KeyMaster",
            "Notice: Cloud storage irregularities reported. Verify integrity of stored data. - CloudSecure",
            "Urgent: Anomalies in system performance detected. Check for hidden processes. - PerformanceCheck",
            "Warning: Unauthorized changes to firewall settings detected. Restore to known safe state. - FirewallRestore",
            "Security Update: Suspicious API calls observed. Validate against external threats. - APIMonitor",
            "Critical Alert: Possible zero-day vulnerability exploited. Apply emergency patches. - ZeroDayDefense",
            "Alert: Increased DNS requests suggest possible DDoS attack. Prepare defenses. - DNSProtect",
            "Warning: Unverified scripts running on system. Investigate origin and purpose. - ScriptScanner",
            "Caution: Network access points open to vulnerabilities. Conduct comprehensive security sweep. - AccessPointCheck"
        ]

    def generate_message(self):
        if random.random() < 1:
            return random.choice(self.messages_hacker)
        else:
            return random.choice(self.generic_messages)
        

class GameSlugGenerator:
    def __init__(self):
        self.game_slugs = [
            "",  
            "confessions",  
            "3words",  
            "tbh",  
            "shipme",  
            "yourcrush",  
            "cancelled",  
            "dealbreaker"  
        ]
        
    def generate_game_slug(self):
        return random.choice(self.game_slugs)
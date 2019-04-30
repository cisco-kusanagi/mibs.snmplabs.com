#
# PySNMP MIB module ARUBA-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARUBA-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Integer32, Counter32, Unsigned32, ObjectIdentity, NotificationType, Bits, ModuleIdentity, TimeTicks, ObjectSyntax, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Integer32", "Counter32", "Unsigned32", "ObjectIdentity", "NotificationType", "Bits", "ModuleIdentity", "TimeTicks", "ObjectSyntax", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class ArubaEnableValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class ArubaFrameType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("associateRequest", 0), ("associateResponse", 1), ("reassociateRequest", 2), ("reassociateResponse", 3), ("probeRequest", 4), ("probeResponse", 5), ("beacon", 8), ("atim", 9), ("disassociate", 10), ("auth", 11), ("deauth", 12))

class ArubaPhyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("dot11a", 1), ("dot11b", 2), ("dot11g", 3), ("dot11ag", 4), ("wired", 5))

class ArubaHTMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("none", 1), ("ht20", 2), ("ht40", 3), ("vht20", 4), ("vht40", 5), ("vht80", 6), ("vht160", 7), ("vht80plus80", 8))

class ArubaHTExtChannel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("above", 2), ("below", 3), ("eighty", 4), ("onesixty", 5))

class ArubaMonEncryptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("open", 0), ("wep", 1), ("wpa", 2), ("wpa2", 3))

class ArubaMonEncryptionCipher(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("wep40", 1), ("wep104", 2), ("tkip", 3), ("aesccmp", 4), ("other", 5))

class ArubaMonAuthAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("psk", 1), ("dot1x", 2), ("other", 3))

class ArubaSwitchRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("master", 1), ("local", 2), ("backupmaster", 3))

class ArubaSupportStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unsupported", 1), ("supported", 2))

class ArubaActiveState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

class ArubaACLDomain(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("alias", 1), ("any", 2), ("user", 3), ("host", 4), ("network", 5))

class ArubaACLNetworkServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("alias", 1), ("any", 2), ("tcp", 3), ("udp", 4), ("protocol", 5))

class ArubaACLAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("deny", 1), ("permit", 2), ("srcNAT", 3), ("dstNAT", 4), ("redirect", 5))

class ArubaDaysOfWeek(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("sun", 1), ("mon", 2), ("tue", 3), ("wed", 4), ("thu", 5), ("fri", 6), ("sat", 7))

class ArubaAuthenticationMethods(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 7, 15, 16, 17, 28, 255))
    namedValues = NamedValues(("none", 0), ("web", 1), ("mac", 2), ("vpn", 3), ("dot1x", 4), ("kerberos", 5), ("secureId", 7), ("pubcookie", 15), ("xSec", 16), ("xSecMachine", 17), ("via-vpn", 28), ("other", 255))

class ArubaSubAuthenticationMethods(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("authPAP", 1), ("authCHAP", 2), ("authMSCHAP", 3), ("authMSCHAPv2", 4), ("eapTLS", 5), ("eapTTLS", 6), ("eapLEAP", 7), ("eapMD5", 8), ("eapPEAP", 9))

class ArubaEncryptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("none", 0), ("static-wep", 1), ("dynamic-wep", 2), ("wpa-psk-tkip", 3), ("wpa-tkip", 4), ("wpa-psk-aes", 5), ("wpa-aes", 6), ("wpa2-psk-tkip", 7), ("wpa2-tkip", 8), ("wpa2-psk-aes", 9), ("wpa2-aes", 10), ("xSec", 11), ("bSec-128", 12), ("bSec-256", 13), ("aes-128-cmac", 14), ("unknown", 15))

class ArubaUserForwardMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("tunnel-encrypted", 0), ("bridge", 1), ("tunnel-decrypted", 2), ("split-tunnel", 3))

class ArubaRogueApType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("valid", 1), ("interfering", 2), ("unsecure", 3), ("dos", 4), ("unknown", 5), ("knownInterfering", 6), ("suspectedUnsecure", 7))

class ArubaAPMatchType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("unknown", 0), ("configuredWiredMac", 1), ("ethernetWiredMac", 2), ("apWiredMac", 3), ("externalWiredMac", 4), ("manual", 5), ("baseBSSIDOverride", 6), ("mms", 7), ("ethernetGatewayWiredMac", 8), ("classificationDisabled", 9), ("apBSSID", 10), ("propagatedEthernetWiredMac", 11), ("apRule", 12), ("systemWiredMac", 13), ("systemGatewayMac", 14))

class ArubaAPMatchMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notApplicable", 0), ("exactMatch", 1), ("plusOneMatch", 2), ("minusOneMatch", 3), ("ouiMatch", 4))

class ArubaStationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("valid", 1), ("interfering", 2), ("dos", 3))

class ArubaEncryptionMethods(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("disabled", 0), ("static-wep", 1), ("dynamic-wep", 2), ("static-wpa", 3), ("dynamic-wpa", 4), ("wpa2-psk-aes", 5), ("wpa2-8021x-aes", 6), ("wpa2PreAuth", 7), ("xsec", 8), ("wpa-psk-aes", 9), ("wpa-aes", 10), ("wpa2-psk-tkip", 11), ("wpa2-8021x-tkip", 12))

class ArubaHashAlgorithms(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("md5", 1), ("sha", 2))

class ArubaVlanValidRange(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4095)

class ArubaPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("access", 1), ("dot1q", 2))

class ArubaDot1dState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("disabled", 1), ("blocked", 2), ("listening", 3), ("learning", 4), ("forwarding", 5))

class ArubaAPDot1dState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("notAvailable", 1), ("off", 2), ("disabled", 3), ("listening", 4), ("learning", 5), ("forwarding", 6), ("blocking", 7))

class ArubaPoeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2), ("enabledCisco", 3), ("notAvailable", 4))

class ArubaCardType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))
    namedValues = NamedValues(("lc1", 1), ("lc2", 2), ("sc1", 3), ("sc2", 4), ("sw2400", 5), ("sw800", 6), ("sw200", 7), ("m3mk1", 8), ("sw3200", 9), ("sw3400", 10), ("sw3600", 11), ("sw650", 12), ("sw651", 13), ("reserved1", 14), ("reserved2", 15), ("sw620", 16), ("sw7210", 17), ("sw7220", 18), ("sw7240", 19), ("sw3500", 20), ("sw2500", 21), ("sw1500", 22), ("sw7010", 23), ("sw7005", 24), ("sw7030", 25), ("sw7205", 26), ("sw7024", 27), ("sw7240xm", 28), ("sw7008", 29))

class ArubaESIServerMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("bridged", 1), ("routed", 2), ("nat", 3))

class ArubaESIServerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class ArubaIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("port", 1), ("vlan", 2), ("tunnel", 3), ("loopback", 4))

class ArubaVoipProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 9, 11, 13, 15))
    namedValues = NamedValues(("sccp", 1), ("svp", 2), ("vocera", 3), ("sip", 9), ("ua", 11), ("h323", 13), ("unknown", 15))

class ArubaAccessPointMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("airMonitor", 1), ("accessPoint", 2), ("accessPointAndMonitor", 3), ("meshPortal", 4), ("meshPoint", 5), ("rfprotectSensor", 6), ("spectrumSensor", 7))

class ArubaAuthServerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("internaldb", 1), ("radius", 2), ("ldap", 3), ("kerberos", 4), ("tacacs", 5))

class ArubaAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("srcAddress", 1), ("dstAddress", 2), ("bssid", 3))

class ArubaBlackListReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 100))
    namedValues = NamedValues(("userDefined", 1), ("mitmAttack", 2), ("authFailure", 3), ("pingFlood", 4), ("sessionFlood", 5), ("synFlood", 6), ("sessionBlacklist", 7), ("ipSpoofing", 8), ("esiBlacklist", 9), ("other", 100))

class ArubaDBType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mssql", 1), ("mysql", 2))

class ArubaVrrpState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("initialize", 1), ("backup", 2), ("master", 3))

class ArubaOperStateValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3))

class ArubaAntennaSetting(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notPresent", 1), ("enabled", 2), ("disabled", 3))

class ArubaAPStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class ArubaPortSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("speed10Mbps", 1), ("speed100Mbps", 2), ("speed1000Mbps", 3), ("speedAuto", 4), ("speed10Gbps", 5), ("speed2Gbps", 6), ("speed5Gbps", 7))

class ArubaPortDuplex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("half", 1), ("full", 2), ("auto", 3))

class ArubaPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("fastethernet", 1), ("gigabitethernet", 2), ("xgigabitethernet", 3), ("twogigabitethernet", 4), ("fivegigabitethernet", 5))

class ArubaEnet1Mode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("activeStandby", 1), ("tunnel", 2), ("bridge", 3), ("notApplicable", 4), ("split", 5))

class ArubaUnprovisionedStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("yes", 1), ("no", 2))

class ArubaMonitorMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("all", 1), ("none", 2), ("mixed", 3))

class ArubaConfigurationState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("success", 1), ("error", 2))

class ArubaConfigurationChangeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("create", 1), ("delete", 2), ("modify", 3))

class ArubaCallStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("idle", 0), ("initiated", 1), ("connecting", 2), ("delivered", 3), ("connected", 4), ("offered", 5), ("alerting", 6), ("releasing", 7), ("cancelling", 8), ("challenging", 9), ("transient", 10), ("blockwait", 11), ("succ", 12), ("fail", 13), ("aborted", 14), ("blocked", 15))

class ArubaVoipProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 9, 11, 13))
    namedValues = NamedValues(("sccp", 1), ("svp", 2), ("vocera", 3), ("sip", 9), ("ua", 11), ("h323", 13))

class ArubaVoipRegState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("registering", 1), ("unregistering", 2), ("challenge", 3), ("registered", 4), ("unregistered", 5))

class ArubaVoiceCdrDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("og", 0), ("ic", 1))

class ArubaVoiceCacBit(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("cacActiveLoadBalancing", 0), ("cacHighCapThresholdReached", 1), ("cacHandRsrvThresholdReached", 2), ("cacPeakCapacityReached", 3))

class ArubaMeshRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("nonmesh", 0), ("point", 1), ("portal", 2))

class ArubaHTRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34))
    namedValues = NamedValues(("unknown", 0), ("ht6dot5", 1), ("ht13", 2), ("ht13dot5", 3), ("ht15", 4), ("ht19dot5", 5), ("ht26", 6), ("ht27", 7), ("ht30", 8), ("ht39", 9), ("ht40dot5", 10), ("ht45", 11), ("ht52", 12), ("ht54", 13), ("ht58dot5", 14), ("ht60", 15), ("ht65", 16), ("ht78", 17), ("ht81", 18), ("ht90", 19), ("ht104", 20), ("ht108", 21), ("ht117", 22), ("ht120", 23), ("ht121dot5", 24), ("ht130", 25), ("ht135", 26), ("ht150", 27), ("ht162", 28), ("ht180", 29), ("ht216", 30), ("ht240", 31), ("ht243", 32), ("ht270", 33), ("ht300", 34))

class ArubaARMChangeReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))
    namedValues = NamedValues(("radarDetected", 1), ("radarCleared", 2), ("txHang", 3), ("txHangClear", 4), ("fortyMhzIntol", 5), ("cancel40mhzIntol", 6), ("fortyMhzAlign", 7), ("armInterference", 8), ("armInvalidCh", 9), ("armErrorThresh", 10), ("armNoiseThresh", 11), ("armEmptyCh", 12), ("armRogueCont", 13), ("armDecreasePower", 14), ("armIncreasePower", 15), ("armTurnOffRadio", 16), ("armTurnOnRadio", 17), ("armChannelQualityThresh", 18), ("armDynamicBW", 19), ("armInterferenceCCA", 20), ("airmatchNoise", 21), ("airmatchSolver", 22), ("airmatchFreeze", 23), ("airmatchUnfreeze", 24), ("random", 25), ("airmatchInit", 26), ("unknown", 27), ("airmatchNoiseCleared", 28), ("airmatchRogueCont", 29))

class ArubaAPMasterStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("move", 3))

class ArubaDot3azStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("disabled", 0), ("unsupported", 1), ("eee100BaseTX", 2), ("eee1000BaseT", 3), ("eee10GBaseT", 4), ("eee1000BaseKX", 5), ("eee10GBaseKX4", 6), ("eee10GBaseKR", 7))

class ArubaThresholdResourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("dataPathCpu", 0), ("controlPathCpu", 1), ("controlPathMemory", 2), ("totalTunnelCapacity", 3), ("userCapacity", 4), ("noofAps", 5), ("noofLocals", 6))

class ArubaStackState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("primary", 1), ("secondary", 2), ("linecard", 3), ("away", 4))

class ArubaStackChangeEvent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("primarySlotChanged", 2), ("secondarySlotChanged", 3), ("lineCardSlotChanged", 4), ("roleChanged", 5), ("priorityChanged", 6), ("versionMismatch", 7), ("slotExceeded", 8))

class ArubaStackIfTopoJoined(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("connected", 1), ("disconnected", 2))

class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ArubaIfState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("linkUp", 1), ("linkDown", 2))

class ArubaIfStateChangeReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("admin", 1), ("loopProtect", 2), ("macLimit", 3), ("raGuard", 4), ("bpduGuard", 5))

class ArubaAPUplinkType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ethernet", 1), ("usb", 2), ("pppoe", 3), ("wifi", 4))

class ArubaAPUplinkChangeReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("linkFailure", 1), ("vpnFailure", 2), ("preemption", 3))

class ArubaPortalServerDownReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("connectFail", 1))

class ArubaHaRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("dual", 0), ("active", 1), ("standby", 2), ("disabled", 3))

class ArubaHaConnectivityStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("haSuccess", 0), ("haNetUnreach", 1), ("haCpUnreach", 2), ("haImageMissMatch", 3), ("haApDenied", 4), ("haHbtFailure", 5), ("haInvalidHelloResponse", 6), ("haStandbyTunnelDown", 7))

class ArubaFlexRadioMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("single2GHzBand", 0), ("single5GHzBand", 1), ("dual2GHzplus5GHzBand", 2), ("unknown", 3), ("notApplicable", 4))

mibBuilder.exportSymbols("ARUBA-TC", ArubaPhyType=ArubaPhyType, ArubaACLAction=ArubaACLAction, ArubaVlanValidRange=ArubaVlanValidRange, ArubaMonEncryptionType=ArubaMonEncryptionType, ArubaACLDomain=ArubaACLDomain, ArubaVrrpState=ArubaVrrpState, ArubaDaysOfWeek=ArubaDaysOfWeek, ArubaAPMatchType=ArubaAPMatchType, ArubaAPDot1dState=ArubaAPDot1dState, ArubaUnprovisionedStatus=ArubaUnprovisionedStatus, ArubaPortSpeed=ArubaPortSpeed, ArubaVoiceCdrDirection=ArubaVoiceCdrDirection, ArubaVoipProtocolType=ArubaVoipProtocolType, ArubaPoeState=ArubaPoeState, ArubaPortalServerDownReason=ArubaPortalServerDownReason, ArubaHaConnectivityStatus=ArubaHaConnectivityStatus, ArubaDBType=ArubaDBType, ArubaEnableValue=ArubaEnableValue, ArubaAuthServerType=ArubaAuthServerType, ArubaIfType=ArubaIfType, ArubaAddressType=ArubaAddressType, ArubaAuthenticationMethods=ArubaAuthenticationMethods, ArubaAPUplinkType=ArubaAPUplinkType, ArubaUserForwardMode=ArubaUserForwardMode, ArubaStackState=ArubaStackState, ArubaHaRole=ArubaHaRole, ArubaIfStateChangeReason=ArubaIfStateChangeReason, ArubaConfigurationState=ArubaConfigurationState, ArubaHTMode=ArubaHTMode, ArubaStationType=ArubaStationType, ArubaBlackListReason=ArubaBlackListReason, ArubaMonitorMode=ArubaMonitorMode, ArubaIfState=ArubaIfState, ArubaFlexRadioMode=ArubaFlexRadioMode, ArubaAPMatchMethod=ArubaAPMatchMethod, ArubaVoiceCacBit=ArubaVoiceCacBit, ArubaSwitchRole=ArubaSwitchRole, ArubaMonEncryptionCipher=ArubaMonEncryptionCipher, ArubaAPStatus=ArubaAPStatus, ArubaAPMasterStatus=ArubaAPMasterStatus, ArubaVoipRegState=ArubaVoipRegState, ArubaEnet1Mode=ArubaEnet1Mode, ArubaAPUplinkChangeReason=ArubaAPUplinkChangeReason, ArubaMonAuthAlgorithm=ArubaMonAuthAlgorithm, ArubaConfigurationChangeType=ArubaConfigurationChangeType, ArubaPortDuplex=ArubaPortDuplex, ArubaVoipProtocol=ArubaVoipProtocol, ArubaActiveState=ArubaActiveState, ArubaStackIfTopoJoined=ArubaStackIfTopoJoined, ArubaOperStateValue=ArubaOperStateValue, ArubaThresholdResourceType=ArubaThresholdResourceType, ArubaESIServerMode=ArubaESIServerMode, ArubaPortType=ArubaPortType, ArubaCardType=ArubaCardType, ArubaMeshRole=ArubaMeshRole, ArubaESIServerStatus=ArubaESIServerStatus, ArubaHTRate=ArubaHTRate, ArubaCallStates=ArubaCallStates, InterfaceIndex=InterfaceIndex, ArubaSupportStatus=ArubaSupportStatus, ArubaAntennaSetting=ArubaAntennaSetting, ArubaHTExtChannel=ArubaHTExtChannel, ArubaRogueApType=ArubaRogueApType, ArubaAccessPointMode=ArubaAccessPointMode, ArubaARMChangeReason=ArubaARMChangeReason, ArubaDot3azStatus=ArubaDot3azStatus, ArubaEncryptionMethods=ArubaEncryptionMethods, ArubaFrameType=ArubaFrameType, ArubaPortMode=ArubaPortMode, ArubaDot1dState=ArubaDot1dState, ArubaStackChangeEvent=ArubaStackChangeEvent, ArubaACLNetworkServiceType=ArubaACLNetworkServiceType, ArubaHashAlgorithms=ArubaHashAlgorithms, ArubaSubAuthenticationMethods=ArubaSubAuthenticationMethods, ArubaEncryptionType=ArubaEncryptionType)

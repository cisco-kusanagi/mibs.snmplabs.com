#
# PySNMP MIB module RUCKUS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:58:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ruckusCommonTCModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonTCModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, NotificationType, Gauge32, Integer32, Unsigned32, iso, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "NotificationType", "Gauge32", "Integer32", "Unsigned32", "iso", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ruckusTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1))
if mibBuilder.loadTexts: ruckusTCMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusTCMIB.setOrganization('Ruckus Wireless, Inc.')
if mibBuilder.loadTexts: ruckusTCMIB.setContactInfo('Ruckus Wireless, Inc. Postal: 880 W Maude Ave Sunnyvale, CA 94085 USA EMail: support@ruckuswireless.com Phone: +1-650-265-4200')
if mibBuilder.loadTexts: ruckusTCMIB.setDescription('This is the mib module for defining all the textual conventions.')
class RuckusRadioMode(TextualConvention, Integer32):
    description = 'Specifies the physical type of the radio.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ieee802dot11b", 1), ("ieee802dot11g", 2), ("ieee802dot11Mixed", 3), ("ieee802dot11a", 4), ("ieee802dot11ng", 5), ("ieee802dot11na", 6))

class RuckusWEPKey(TextualConvention, OctetString):
    description = 'Specifies the WEP key.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(5, 5), ValueSizeConstraint(13, 13), ValueSizeConstraint(10, 10), ValueSizeConstraint(26, 26), )
class RuckusAdminStatus(TextualConvention, Integer32):
    description = 'Administrative status for ruckus managed object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class RuckusCountryCode(TextualConvention, OctetString):
    description = 'Specifies the country code. Each country represented as a two character. Here is the lsit: ALBANIA -> AL ALGERIA -> DZ ARGENTINA -> AR ARMENIA -> AM AUSTRALIA -> AU AUSTRIA -> AT AZERBAIJAN -> AZ BAHRAIN -> BH BELARUS -> BY BELGIUM -> BE BELIZE -> BZ BOLIVIA -> BO BRAZIL -> BR BRUNEI_DARUSSALAM -> BN BULGARIA -> BG CANADA -> CA CHILE -> CL CHINA -> CN COLOMBIA -> CO COSTA_RICA -> CR CROATIA -> HR CYPRUS -> CY CZECH -> CZ DENMARK -> DK DOMINICAN_REPUBLIC -> DO ECUADOR -> EC EGYPT -> EG EL_SALVADOR -> SV ESTONIA -> EE FINLAND -> FI FRANCE -> FR FRANCE2 -> F2 GEORGIA -> GE GERMANY -> DE GREECE -> GR GUATEMALA -> GT HONDURAS -> HN HONG_KONG -> HK HUNGARY -> HU ICELAND -> IS INDIA -> IN INDONESIA -> ID IRAN -> IR IRELAND -> IE ISRAEL -> IL ITALY -> IT JAPAN -> JP JAPAN1 -> J1 JAPAN2 -> J2 JAPAN3 -> J3 JAPAN4 -> J4 JAPAN5 -> J5 JAPAN6 -> J6 JAPAN7 -> JP JAPAN8 -> JP JAPAN9 -> JP JAPAN10 -> JP JAPAN11 -> JP JAPAN12 -> JP JAPAN13 -> JP JAPAN14 -> JP JAPAN15 -> JP JAPAN16 -> JP JAPAN17 -> JP JAPAN18 -> JP JAPAN19 -> JP JAPAN20 -> JP JAPAN21 -> JP JAPAN22 -> JP JAPAN23 -> JP JAPAN24 -> JP JORDAN -> JO KAZAKHSTAN -> KZ KOREA_NORTH -> KP KOREA_ROC -> KR KOREA_ROC2 -> K2 KUWAIT -> KW LATVIA -> LV LEBANON -> LB LIECHTENSTEIN -> LI LITHUANIA -> LT LUXEMBOURG -> LU MACAU -> MO MACEDONIA -> MK MALAYSIA -> MY MEXICO -> MX MONACO -> MC MOROCCO -> MA NETHERLANDS -> NL NEW_ZEALAND -> NZ NORWAY -> NO OMAN -> OM PAKISTAN -> PK PANAMA -> PA PERU -> PE PHILIPPINES -> PH POLAND -> PL PORTUGAL -> PT PUERTO_RICO -> PR QATAR -> QA ROMANIA -> RO RUSSIA -> RU SAUDI_ARABIA -> SA SINGAPORE -> SG SLOVAKIA -> SK SLOVENIA -> SI SOUTH_AFRICA -> ZA SPAIN -> ES SWEDEN -> SE SWITZERLAND -> CH SYRIA -> SY TAIWAN -> TW THAILAND -> TH TRINIDAD_Y_TOBAGO -> TT TUNISIA -> TN TURKEY -> TR UKRAINE -> UA UAE -> AE UNITED_KINGDOM -> GB UNITED_STATES -> US UNITED_STATES_FCC49 -> US URUGUAY -> UY UZBEKISTAN -> UZ VENEZUELA -> VE VIET_NAM -> VN YEMEN -> YE ZIMBABWE -> ZW'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class RuckusFequency(TextualConvention, Integer32):
    description = 'This data type represents the frequency value that are expressed in MHz. Units are in thousands of a MHz. 2412 - 5805 MHz For example: 2.412 GHz would be represented as 2412 MHz'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(2412, 5805)

class RuckusWPAPassPhrase(TextualConvention, OctetString):
    description = 'Specifies the WPA PSK (Wi-Fi Protected Access Pre Shared key). If the key length is 64 then all 64 characters should be in hex, otherwise the key assumed to be ascii.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 63), ValueSizeConstraint(64, 64), )
class RuckusSSID(TextualConvention, OctetString):
    description = 'Ruckus service set identifier.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 32)

class RuckusRate(TextualConvention, OctetString):
    description = 'This attribute shall specify the set of data rates at which the station may transmit data. Each octet contains a value representing a rate. Each rate shall be within the range from 2 to 127, corresponding to data rates in increments of 500 kb/s from 1 Mb/s to 63.5 Mb/s, and shall be supported (as indicated in the supported rates table) for receiving data. This value is reported in transmitted Beacon, Probe Request, Probe Response, Association Request, Association Response, Reassociation Request, and Reassociation Response frames, and is used to determine whether a BSS with which the station desires to synchronize is suitable. It is also used when starting a BSS, as specified in 10.3.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 126)

class RuckusdB(TextualConvention, Integer32):
    description = 'Used to express values of type dB.'
    status = 'current'

class RuckusRateLimiting(TextualConvention, Integer32):
    description = 'Used to express values of Rate limiting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("disable", 0), ("rate100Kbps", 1), ("rate250Kbps", 2), ("rate500Kbps", 3), ("rate1Mbps", 4), ("rate2Mbps", 5), ("rate5Mbps", 6), ("rate10Mbps", 7), ("rate20Mbps", 8), ("rate50Mbps", 9))

class RuckusWLANServiceType(TextualConvention, Integer32):
    description = 'The WLAN Service types supported on Ruckus Wireless systems.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("standardUsage", 1), ("guestAccess", 2), ("hotSpotService", 3))

class RuckusAuthenticationType(TextualConvention, Integer32):
    description = 'The Authentication types supported on Ruckus Wireless systems.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("open", 1), ("shared", 2), ("eap", 3), ("mac-address", 4), ("eap-mac-mix", 5))

class RuckusEncryptionType(TextualConvention, Integer32):
    description = 'The Encryption types supported on Ruckus Wireless systems.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("wpa", 1), ("wpa2", 2), ("wpa-Mixed", 3), ("wep-64", 4), ("wep-128", 5), ("none-enc", 6))

class RuckusWPACipherType(TextualConvention, Integer32):
    description = 'The WPA Encryption Cipher methods supported on Ruckus Wireless systems.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("tkip", 1), ("aes", 2), ("auto", 3), ("none", 4))

class RuckusWLANServicePriority(TextualConvention, Integer32):
    description = 'The LAN QoS Service levels supported on Ruckus Wireless systems.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("high", 1), ("low", 2))

class RuckusSysLogLevel(TextualConvention, Integer32):
    description = 'The sysLog reporting levels supported on Ruckus Wireless systems.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("more", 1), ("warning-and-critical", 2), ("critical-only", 3))

class RuckusSNMPv3AuthenticationType(TextualConvention, Integer32):
    description = 'The SNMP v3 authentication type supported on Ruckus Wireless systems.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("md5", 1), ("sha", 2))

class RuckusSNMPv3EncryptionType(TextualConvention, Integer32):
    description = 'The SNMP v3 encryption type supported on Ruckus Wireless systems.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("des", 1), ("aes", 2))

class RuckusSNMPVersionType(TextualConvention, Integer32):
    description = 'The SNMP Version type supported on Ruckus Wireless systems.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("v2", 1), ("v3", 2))

class RuckusNameString(TextualConvention, OctetString):
    description = 'The general (128 characters) Name String defined on Ruckus Wireless systems.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class RuckusPassPhrase(TextualConvention, OctetString):
    description = 'The general (64 characters) passphrase defined on Ruckus Wireless systems.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 64)

class RuckusAAAServiceType(TextualConvention, Integer32):
    description = 'The Ruckus AAA Server Service type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active-directory", 1), ("ldap-directory", 2), ("aaa-authentication", 3), ("aaa-accounting", 4))

class RuckusAPIpAddressSettingMode(TextualConvention, Integer32):
    description = 'The AP IP address setting mode, admin-by-zd : ZD configure the AP IP address, admin-by-dhcp : DHCP server configure the AP IP address, admin-by-ap : AP configure its IP address locally.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("admin-by-zd", 1), ("admin-by-dhcp", 2), ("admin-by-ap", 3))

class RuckusAPRadioType(TextualConvention, Integer32):
    description = 'The Ruckus AP unit wireless Radio type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ieee80211bg", 1), ("ieee80211na", 2), ("ieee80211a", 3), ("ieee80211n", 4))

class RuckusAPRadioType24(TextualConvention, Integer32):
    description = 'The Ruckus AP unit wireless Radio type 2.4G.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ieee80211b", 1), ("ieee80211g", 2), ("ieee80211bg", 3), ("ieee80211ng", 4))

class RuckusAPRadioType5(TextualConvention, Integer32):
    description = 'The Ruckus AP unit wireless Radio type 5G.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ieee80211a", 1), ("ieee80211n", 2), ("ieee80211nag", 3))

class RuckusAPRadioTxPowerLevel(TextualConvention, Integer32):
    description = 'The Ruckus AP unit wireless Radio Tx Power level setting.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("auto", 1), ("full", 2), ("half-full", 3), ("quarter-full", 4), ("one-eighth-full", 5), ("one-tenth-full", 6))

class RuckusAPWirelessChannel(TextualConvention, Integer32):
    description = 'The AP radio channel, selectable 0, 1-11, 0 : auto channel selection, 1-11 : specific channel selection.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 11)

class RuckusAPMeshConfigurationMode(TextualConvention, Integer32):
    description = 'The Ruckus AP unit Mesh wireless configuration mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("auto", 1), ("root-ap", 2), ("mesh-ap", 3), ("disabled", 4))

class RuckusAPUplinkSelectionMode(TextualConvention, Integer32):
    description = 'The Ruckus AP unit wireless uplink selection mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("smart", 1), ("manual", 2))

class RuckusAPApproveMode(TextualConvention, Integer32):
    description = 'ZD managed AP approve mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("approved", 1), ("not-approved", 2))

class RuckusZDAPManagementAdminControl(TextualConvention, Integer32):
    description = 'The ZD management control of an AP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("delete", 1), ("associated", 2))

ruckusTCObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 1))
ruckusTCEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 2))
ruckusTCConf = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 3))
ruckusTCGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 3, 1))
ruckusTCCompls = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 3, 2))
mibBuilder.exportSymbols("RUCKUS-TC-MIB", RuckusPassPhrase=RuckusPassPhrase, RuckusAuthenticationType=RuckusAuthenticationType, RuckusWLANServicePriority=RuckusWLANServicePriority, RuckusAPMeshConfigurationMode=RuckusAPMeshConfigurationMode, RuckusAPRadioTxPowerLevel=RuckusAPRadioTxPowerLevel, RuckusAAAServiceType=RuckusAAAServiceType, RuckusWPACipherType=RuckusWPACipherType, RuckusAPRadioType5=RuckusAPRadioType5, RuckusSNMPv3AuthenticationType=RuckusSNMPv3AuthenticationType, RuckusRadioMode=RuckusRadioMode, RuckusAPIpAddressSettingMode=RuckusAPIpAddressSettingMode, RuckusAPRadioType24=RuckusAPRadioType24, RuckusdB=RuckusdB, RuckusZDAPManagementAdminControl=RuckusZDAPManagementAdminControl, ruckusTCConf=ruckusTCConf, RuckusEncryptionType=RuckusEncryptionType, PYSNMP_MODULE_ID=ruckusTCMIB, RuckusFequency=RuckusFequency, RuckusNameString=RuckusNameString, RuckusCountryCode=RuckusCountryCode, RuckusRateLimiting=RuckusRateLimiting, RuckusSNMPVersionType=RuckusSNMPVersionType, RuckusAPUplinkSelectionMode=RuckusAPUplinkSelectionMode, ruckusTCObjects=ruckusTCObjects, RuckusAPApproveMode=RuckusAPApproveMode, ruckusTCGroups=ruckusTCGroups, ruckusTCCompls=ruckusTCCompls, RuckusRate=RuckusRate, RuckusWEPKey=RuckusWEPKey, RuckusSNMPv3EncryptionType=RuckusSNMPv3EncryptionType, ruckusTCMIB=ruckusTCMIB, RuckusAdminStatus=RuckusAdminStatus, RuckusSysLogLevel=RuckusSysLogLevel, RuckusSSID=RuckusSSID, RuckusWLANServiceType=RuckusWLANServiceType, RuckusAPWirelessChannel=RuckusAPWirelessChannel, RuckusAPRadioType=RuckusAPRadioType, ruckusTCEvents=ruckusTCEvents, RuckusWPAPassPhrase=RuckusWPAPassPhrase)

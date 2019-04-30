#
# PySNMP MIB module RUCKUS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:50:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ruckusCommonTCModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonTCModule")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, ObjectIdentity, Integer32, ModuleIdentity, Counter64, IpAddress, Bits, iso, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "ObjectIdentity", "Integer32", "ModuleIdentity", "Counter64", "IpAddress", "Bits", "iso", "Counter32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ruckusTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1))
if mibBuilder.loadTexts: ruckusTCMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusTCMIB.setOrganization('Ruckus Wireless, Inc.')
class RuckusRadioMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ieee802dot11b", 1), ("ieee802dot11g", 2), ("ieee802dot11Mixed", 3), ("ieee802dot11a", 4), ("ieee802dot11ng", 5), ("ieee802dot11na", 6))

class RuckusWEPKey(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(5, 5), ValueSizeConstraint(13, 13), ValueSizeConstraint(10, 10), ValueSizeConstraint(26, 26), )
class RuckusAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class RuckusCountryCode(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class RuckusFequency(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(2412, 5805)

class RuckusWPAPassPhrase(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 63), ValueSizeConstraint(64, 64), )
class RuckusSSID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 32)

class RuckusRate(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 126)

class RuckusdB(TextualConvention, Integer32):
    status = 'current'

class RuckusRateLimiting(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("disable", 0), ("rate100Kbps", 1), ("rate250Kbps", 2), ("rate500Kbps", 3), ("rate1Mbps", 4), ("rate2Mbps", 5), ("rate5Mbps", 6), ("rate10Mbps", 7), ("rate20Mbps", 8), ("rate50Mbps", 9))

class RuckusWLANServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("standardUsage", 1), ("guestAccess", 2), ("hotSpotService", 3))

class RuckusAuthenticationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("open", 1), ("shared", 2), ("eap", 3), ("mac-address", 4), ("eap-mac-mix", 5))

class RuckusEncryptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("wpa", 1), ("wpa2", 2), ("wpa-Mixed", 3), ("wep-64", 4), ("wep-128", 5), ("none-enc", 6))

class RuckusWPACipherType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("tkip", 1), ("aes", 2), ("auto", 3), ("none", 4))

class RuckusWLANServicePriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("high", 1), ("low", 2))

class RuckusSysLogLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("more", 1), ("warning-and-critical", 2), ("critical-only", 3))

class RuckusSNMPv3AuthenticationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("md5", 1), ("sha", 2))

class RuckusSNMPv3EncryptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("des", 1), ("aes", 2))

class RuckusSNMPVersionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("v2", 1), ("v3", 2))

class RuckusNameString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class RuckusPassPhrase(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 64)

class RuckusAAAServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active-directory", 1), ("ldap-directory", 2), ("aaa-authentication", 3), ("aaa-accounting", 4))

class RuckusAPIpAddressSettingMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("admin-by-zd", 1), ("admin-by-dhcp", 2), ("admin-by-ap", 3))

class RuckusAPRadioType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ieee80211bg", 1), ("ieee80211na", 2), ("ieee80211a", 3), ("ieee80211n", 4))

class RuckusAPRadioType24(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ieee80211b", 1), ("ieee80211g", 2), ("ieee80211bg", 3), ("ieee80211ng", 4))

class RuckusAPRadioType5(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ieee80211a", 1), ("ieee80211n", 2), ("ieee80211nag", 3))

class RuckusAPRadioTxPowerLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("auto", 1), ("full", 2), ("half-full", 3), ("quarter-full", 4), ("one-eighth-full", 5), ("one-tenth-full", 6))

class RuckusAPWirelessChannel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 11)

class RuckusAPMeshConfigurationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("auto", 1), ("root-ap", 2), ("mesh-ap", 3), ("disabled", 4))

class RuckusAPUplinkSelectionMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("smart", 1), ("manual", 2))

class RuckusAPApproveMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("approved", 1), ("not-approved", 2))

class RuckusZDAPManagementAdminControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("delete", 1), ("associated", 2))

ruckusTCObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 1))
ruckusTCEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 2))
ruckusTCConf = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 3))
ruckusTCGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 3, 1))
ruckusTCCompls = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 3, 2))
mibBuilder.exportSymbols("RUCKUS-TC-MIB", RuckusSysLogLevel=RuckusSysLogLevel, RuckusAPRadioType24=RuckusAPRadioType24, RuckusAPRadioType=RuckusAPRadioType, RuckusWPAPassPhrase=RuckusWPAPassPhrase, RuckusSNMPv3EncryptionType=RuckusSNMPv3EncryptionType, RuckusAuthenticationType=RuckusAuthenticationType, RuckusNameString=RuckusNameString, RuckusAdminStatus=RuckusAdminStatus, RuckusAPUplinkSelectionMode=RuckusAPUplinkSelectionMode, ruckusTCGroups=ruckusTCGroups, RuckusWEPKey=RuckusWEPKey, RuckusSSID=RuckusSSID, RuckusdB=RuckusdB, RuckusAPApproveMode=RuckusAPApproveMode, PYSNMP_MODULE_ID=ruckusTCMIB, RuckusCountryCode=RuckusCountryCode, RuckusAPRadioType5=RuckusAPRadioType5, RuckusWLANServiceType=RuckusWLANServiceType, RuckusAPWirelessChannel=RuckusAPWirelessChannel, RuckusRadioMode=RuckusRadioMode, RuckusSNMPVersionType=RuckusSNMPVersionType, RuckusAAAServiceType=RuckusAAAServiceType, RuckusPassPhrase=RuckusPassPhrase, RuckusAPRadioTxPowerLevel=RuckusAPRadioTxPowerLevel, RuckusAPMeshConfigurationMode=RuckusAPMeshConfigurationMode, RuckusZDAPManagementAdminControl=RuckusZDAPManagementAdminControl, ruckusTCEvents=ruckusTCEvents, RuckusWPACipherType=RuckusWPACipherType, ruckusTCObjects=ruckusTCObjects, RuckusWLANServicePriority=RuckusWLANServicePriority, ruckusTCCompls=ruckusTCCompls, RuckusSNMPv3AuthenticationType=RuckusSNMPv3AuthenticationType, ruckusTCConf=ruckusTCConf, ruckusTCMIB=ruckusTCMIB, RuckusRateLimiting=RuckusRateLimiting, RuckusAPIpAddressSettingMode=RuckusAPIpAddressSettingMode, RuckusFequency=RuckusFequency, RuckusRate=RuckusRate, RuckusEncryptionType=RuckusEncryptionType)

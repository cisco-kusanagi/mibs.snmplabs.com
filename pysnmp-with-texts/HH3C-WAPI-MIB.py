#
# PySNMP MIB module HH3C-WAPI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-WAPI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:30:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, ModuleIdentity, ObjectIdentity, IpAddress, Unsigned32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Bits, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Unsigned32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Bits", "Gauge32", "Counter64")
TextualConvention, MacAddress, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString", "TruthValue")
hh3cwapiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 77))
if mibBuilder.loadTexts: hh3cwapiMIB.setLastUpdated('201012011757Z')
if mibBuilder.loadTexts: hh3cwapiMIB.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cwapiMIB.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cwapiMIB.setDescription('HH3C-WAPI-MIB is an extension of MIB in WAPI protocol. This MIB contains objects to manage configuration and monitor running state for WAPI feature.')
hh3cwapiMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 77, 1))
hh3cwapiMIBStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 77, 2))
hh3cwapiMIBTableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3))
hh3cwapiTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 77, 4))
hh3cwapiModeEnabled = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiModeEnabled.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiModeEnabled.setDescription('When this object is set to TRUE, it shall indicate that WAPI is enabled. Otherwise, it shall indicate that WAPI is disabled.')
hh3cwapiASIPAddressType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiASIPAddressType.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiASIPAddressType.setDescription('This object is used to set global IP addresses type (IPv4 or IPv6) of AS.')
hh3cwapiASIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiASIPAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiASIPAddress.setDescription('This object is used to set the global IP address of AS.')
hh3cwapiCertificateInstalled = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiCertificateInstalled.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiCertificateInstalled.setDescription("This object indicates whether the entity has installed certificate. When the value is TURE, it shall indicate that the entity has installed certificate. Otherwise, it shall indicate that the entity hasn't installed certificate.")
hh3cwapiStatsWAISignatureErrors = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiStatsWAISignatureErrors.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiStatsWAISignatureErrors.setDescription('This counter increases when the received packet of WAI signature is wrong.')
hh3cwapiStatsWAIHMACErrors = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiStatsWAIHMACErrors.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiStatsWAIHMACErrors.setDescription('This counter increases when the received packet of WAI message authentication key checking error occurs.')
hh3cwapiStatsWAIAuthRsltFailures = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiStatsWAIAuthRsltFailures.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiStatsWAIAuthRsltFailures.setDescription('This counter increases when the WAI authentication result is unsuccessful.')
hh3cwapiStatsWAIDiscardCounters = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiStatsWAIDiscardCounters.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiStatsWAIDiscardCounters.setDescription('This counter increases when the received packet of WAI are discarded.')
hh3cwapiStatsWAITimeoutCounters = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiStatsWAITimeoutCounters.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiStatsWAITimeoutCounters.setDescription('This counter increases when the packet of WAI overtime are detected.')
hh3cwapiStatsWAIFormatErrors = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiStatsWAIFormatErrors.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiStatsWAIFormatErrors.setDescription('This counter increases when the WAI packet of WAI format error is detected.')
hh3cwapiStatsWAICtfHskFailures = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiStatsWAICtfHskFailures.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiStatsWAICtfHskFailures.setDescription('This counter increases when the WAI certificate authenticates unsuccessfully.')
hh3cwapiStatsWAIUniHskFailures = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiStatsWAIUniHskFailures.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiStatsWAIUniHskFailures.setDescription('This counter increases when the WAI unicast cipher key negotiates unsuccessfully.')
hh3cwapiStatsWAIMulHskFailures = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiStatsWAIMulHskFailures.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiStatsWAIMulHskFailures.setDescription('This counter increases when the WAI multicast cipher key announces unsuccessfully.')
hh3cwapiConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1), )
if mibBuilder.loadTexts: hh3cwapiConfigTable.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigTable.setDescription('The table containing WAPI configuration objects.')
hh3cwapiConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cwapiConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigEntry.setDescription('An entry in the hh3cwapiConfigTable.')
hh3cwapiConfigASIPAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiConfigASIPAddressType.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigASIPAddressType.setDescription('This object is used to set IP addresses type of AS.')
hh3cwapiConfigASIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiConfigASIPAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigASIPAddress.setDescription('This object is used to set the IP address of AS.')
hh3cwapiConfigAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("certificate", 1), ("psk", 2), ("certificatePsk", 3))).clone('certificate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiConfigAuthMethod.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigAuthMethod.setDescription('This object selects a mechanism for WAPI authentication method. The default is certificate.')
hh3cwapiConfigAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("radiusExtension", 2))).clone('standard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiConfigAuthMode.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigAuthMode.setDescription('This object selects a mechanism for WAPI authentication mode. When the value is standard, it shall indicate that the entity acts accord with the official definition. Otherwise, it shall indicate that the entity finishs authentication by means of RADIUS. The default is standard.')
hh3cwapiConfigISPDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiConfigISPDomain.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigISPDomain.setDescription('The ISP domain name.')
hh3cwapiConfigCertificateDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiConfigCertificateDomain.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigCertificateDomain.setDescription('The PKI domain name.')
hh3cwapiConfigASName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiConfigASName.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigASName.setDescription('The name of AS.')
hh3cwapiConfigBKRekeyEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiConfigBKRekeyEnabled.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigBKRekeyEnabled.setDescription('This object indicates whether the BK rekey function is supported. When the value is TURE, it shall indicate that the BK rekey function is supported. Otherwise, it shall indicate that the BK rekey function is not supported.')
hh3cwapiConfigExtTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2), )
if mibBuilder.loadTexts: hh3cwapiConfigExtTable.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigExtTable.setDescription('The table containing WAPI configuration objects for SSID.')
hh3cwapiConfigExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1), ).setIndexNames((0, "HH3C-WAPI-MIB", "hh3cwapiConfigServicePolicyID"))
if mibBuilder.loadTexts: hh3cwapiConfigExtEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigExtEntry.setDescription('An extend entry in the hh3cwapiConfigExtTable.')
hh3cwapiConfigServicePolicyID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cwapiConfigServicePolicyID.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigServicePolicyID.setDescription('Represents the ID of each service policy.')
hh3cwapiConfigUnicastCipherEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiConfigUnicastCipherEnabled.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigUnicastCipherEnabled.setDescription('This object enables or disables the unicast cipher.')
hh3cwapiConfigUnicastCipherSize = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiConfigUnicastCipherSize.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigUnicastCipherSize.setDescription('This object indicates the length in bits of the unicast cipher key. This should be 256 for SMS4, first 128 bits for encrypting, last 128 bits for integrity checking.')
hh3cwapiConfigAuthenticationSuiteEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiConfigAuthenticationSuiteEnabled.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigAuthenticationSuiteEnabled.setDescription('This variable indicates the corresponding AKM suite is enabled or disabled.')
hh3cwapiConfigAuthenticationSuite = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiConfigAuthenticationSuite.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiConfigAuthenticationSuite.setDescription('The selector of an AKM suite. It consists of an OUI (the first 3 octets) and a cipher suite identifier (the last octet).')
hh3cwapiCfgExtASIPAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 6), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiCfgExtASIPAddressType.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiCfgExtASIPAddressType.setDescription('This object is used to set IP addresses type of AS.')
hh3cwapiCfgExtASIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 7), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiCfgExtASIPAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiCfgExtASIPAddress.setDescription('This object is used to set the IP address of AS.')
hh3cwapiCfgExtASName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiCfgExtASName.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiCfgExtASName.setDescription('This object is used to set the name of AS.')
hh3cwapiCfgExtCertDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cwapiCfgExtCertDomain.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiCfgExtCertDomain.setDescription('This object is used to set the PKI domain name.')
hh3cwapiCfgExtCertInstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cwapiCfgExtCertInstalled.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiCfgExtCertInstalled.setDescription("This object indicates whether the entity has installed certificate. When the value is TURE, it shall indicate that the SSID has installed certificate. Otherwise, it shall indicate that the SSID hasn't installed certificate.")
hh3cwapiTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0))
hh3cwapiUserwithInvalidCertificate = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"))
if mibBuilder.loadTexts: hh3cwapiUserwithInvalidCertificate.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiUserwithInvalidCertificate.setDescription('This trap is sent when a user intrudes upon network with invalid certificate.')
hh3cwapiStationReplayAttack = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"))
if mibBuilder.loadTexts: hh3cwapiStationReplayAttack.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiStationReplayAttack.setDescription('This trap is sent when an attacker records and replays network transactions.')
hh3cwapiTamperAttack = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"))
if mibBuilder.loadTexts: hh3cwapiTamperAttack.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiTamperAttack.setDescription('This trap is sent when an attacker monitors network traffic and maliciously changes data in transit(for example, an attacker may modify the contents of a WAI message).')
hh3cwapiLowSafeLevelAttack = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"))
if mibBuilder.loadTexts: hh3cwapiLowSafeLevelAttack.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiLowSafeLevelAttack.setDescription('This trap is sent when a station associates AP(Access Point), creates packet of Unicast Key Negotiation Response with wrong WIE(WAPI Information Element) of ASUE(Authentication Supplicant Entity).')
hh3cwapiAddressRedirectionAttack = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 5)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"), ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"))
if mibBuilder.loadTexts: hh3cwapiAddressRedirectionAttack.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiAddressRedirectionAttack.setDescription('This trap is sent when an attacker maliciously changes destination MAC address of WPI(WLAN Privacy Infrastructure) frame.')
hh3cwapiTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1))
hh3cwapiTrapInfoMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cwapiTrapInfoMacAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiTrapInfoMacAddr.setDescription('The MAC address of the WAPI user.')
hh3cwapiTrapInfoAPId = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cwapiTrapInfoAPId.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiTrapInfoAPId.setDescription('To uniquely identify each AP.')
hh3cwapiTrapInfoRadioId = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cwapiTrapInfoRadioId.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiTrapInfoRadioId.setDescription('Represents each radio.')
hh3cwapiTrapInfoBSSId = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 4), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cwapiTrapInfoBSSId.setStatus('current')
if mibBuilder.loadTexts: hh3cwapiTrapInfoBSSId.setDescription('As MAC Address format, it is to identify BSS.')
mibBuilder.exportSymbols("HH3C-WAPI-MIB", hh3cwapiConfigAuthMode=hh3cwapiConfigAuthMode, hh3cwapiMIBStatsObjects=hh3cwapiMIBStatsObjects, hh3cwapiTrapPrefix=hh3cwapiTrapPrefix, hh3cwapiTrapInfoMacAddr=hh3cwapiTrapInfoMacAddr, hh3cwapiStatsWAIMulHskFailures=hh3cwapiStatsWAIMulHskFailures, hh3cwapiTrapInfoBSSId=hh3cwapiTrapInfoBSSId, hh3cwapiConfigASName=hh3cwapiConfigASName, hh3cwapiModeEnabled=hh3cwapiModeEnabled, hh3cwapiConfigExtEntry=hh3cwapiConfigExtEntry, hh3cwapiTrap=hh3cwapiTrap, hh3cwapiMIB=hh3cwapiMIB, hh3cwapiConfigServicePolicyID=hh3cwapiConfigServicePolicyID, hh3cwapiUserwithInvalidCertificate=hh3cwapiUserwithInvalidCertificate, hh3cwapiAddressRedirectionAttack=hh3cwapiAddressRedirectionAttack, hh3cwapiStationReplayAttack=hh3cwapiStationReplayAttack, hh3cwapiTrapInfoAPId=hh3cwapiTrapInfoAPId, hh3cwapiConfigExtTable=hh3cwapiConfigExtTable, hh3cwapiTamperAttack=hh3cwapiTamperAttack, hh3cwapiASIPAddressType=hh3cwapiASIPAddressType, hh3cwapiCfgExtASName=hh3cwapiCfgExtASName, PYSNMP_MODULE_ID=hh3cwapiMIB, hh3cwapiTrapInfo=hh3cwapiTrapInfo, hh3cwapiMIBObjects=hh3cwapiMIBObjects, hh3cwapiASIPAddress=hh3cwapiASIPAddress, hh3cwapiStatsWAICtfHskFailures=hh3cwapiStatsWAICtfHskFailures, hh3cwapiCfgExtCertInstalled=hh3cwapiCfgExtCertInstalled, hh3cwapiStatsWAIHMACErrors=hh3cwapiStatsWAIHMACErrors, hh3cwapiTrapInfoRadioId=hh3cwapiTrapInfoRadioId, hh3cwapiStatsWAIUniHskFailures=hh3cwapiStatsWAIUniHskFailures, hh3cwapiConfigUnicastCipherSize=hh3cwapiConfigUnicastCipherSize, hh3cwapiCfgExtCertDomain=hh3cwapiCfgExtCertDomain, hh3cwapiStatsWAISignatureErrors=hh3cwapiStatsWAISignatureErrors, hh3cwapiConfigASIPAddressType=hh3cwapiConfigASIPAddressType, hh3cwapiConfigUnicastCipherEnabled=hh3cwapiConfigUnicastCipherEnabled, hh3cwapiConfigAuthenticationSuite=hh3cwapiConfigAuthenticationSuite, hh3cwapiLowSafeLevelAttack=hh3cwapiLowSafeLevelAttack, hh3cwapiStatsWAIAuthRsltFailures=hh3cwapiStatsWAIAuthRsltFailures, hh3cwapiConfigTable=hh3cwapiConfigTable, hh3cwapiCfgExtASIPAddress=hh3cwapiCfgExtASIPAddress, hh3cwapiConfigBKRekeyEnabled=hh3cwapiConfigBKRekeyEnabled, hh3cwapiCfgExtASIPAddressType=hh3cwapiCfgExtASIPAddressType, hh3cwapiMIBTableObjects=hh3cwapiMIBTableObjects, hh3cwapiConfigCertificateDomain=hh3cwapiConfigCertificateDomain, hh3cwapiConfigASIPAddress=hh3cwapiConfigASIPAddress, hh3cwapiConfigEntry=hh3cwapiConfigEntry, hh3cwapiConfigAuthenticationSuiteEnabled=hh3cwapiConfigAuthenticationSuiteEnabled, hh3cwapiConfigISPDomain=hh3cwapiConfigISPDomain, hh3cwapiStatsWAITimeoutCounters=hh3cwapiStatsWAITimeoutCounters, hh3cwapiStatsWAIFormatErrors=hh3cwapiStatsWAIFormatErrors, hh3cwapiStatsWAIDiscardCounters=hh3cwapiStatsWAIDiscardCounters, hh3cwapiCertificateInstalled=hh3cwapiCertificateInstalled, hh3cwapiConfigAuthMethod=hh3cwapiConfigAuthMethod)
